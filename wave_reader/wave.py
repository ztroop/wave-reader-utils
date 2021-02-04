import logging
import struct
from collections import namedtuple
from dataclasses import asdict, dataclass, fields
from typing import Any, Dict, List, Optional, Union

from bleak import BleakClient, discover
from bleak.backends.bluezdbus.client import BleakClientBlueZDBus
from bleak.backends.device import BLEDevice

from wave_reader.data import (
    DEVICE, IDENTITY, SERIAL_NUMBER_BUFFER, WaveProduct,
)

_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())


class UnsupportedError(Exception):
    """Custom exception class for unsupported device errors.

    :param message: The error message
    :param name: The device name
    :param addr: The device address (UUID in MacOS, MAC in Linux/Windows)
    """

    def __init__(self, message: str, name: str, addr: str):
        self.message = f"Device: {name} ({addr}) -> {message}"
        _logger.error(self.message)
        super().__init__(self.message)


@dataclass
class DeviceSensors:
    """A dataclass to encapsulate sensor data.

    :param humidity: Relative humidity level (%rH)
    :param radon_sta: Short-term average for radon level (Bq/m3)
    :param radon_lta: Long-term average for radon level (Bq/m3)
    :param temperature: Ambient temperature (degC)
    :param pressure: Atmospheric pressure (hPa)
    :param co2: Carbon dioxide level (ppm)
    :param voc: Volatile organic compound level (ppb)
    """

    humidity: Optional[float]
    radon_sta: Optional[int]
    radon_lta: Optional[int]
    temperature: Optional[float]
    pressure: Optional[float]
    co2: Optional[float]
    voc: Optional[float]

    def __str__(self):
        r = {i.name: getattr(self, i.name) for i in fields(self)}
        return f'DeviceSensors ({", ".join(f"{k}: {v}" for k, v in r.items())})'

    def as_dict(self):
        return asdict(self)

    @classmethod
    def from_bytes(cls, data: List, product: WaveProduct):
        return cls(**DEVICE[product]["SENSOR_FORMAT"](data))  # type: ignore


class WaveDevice:
    """An object that represents a Airthings Wave device. The
    ``discover_devices`` returns a list of ``BLEDevice`` objects
    that are used in the first parameter.

    If you want to instantiate a WaveDevice manually without using
    discovery, you can create a generic object with the following
    properties: ``name``, ``address`` and optionally ``rssi``, ``metadata``.

    :param device: Device information from Bleak's discover function
    :param serial_number: Parsed serial number from manufacturer data
    """

    sensor_version: Optional[int] = None
    sensors: Optional[DeviceSensors] = None
    client: Optional[BleakClientBlueZDBus] = None
    _raw_gatt_values: Optional[bytearray] = None

    def __init__(self, device: Union[BLEDevice, Any], serial_number: int):
        self.name: str = device.name
        self.address: str = device.address  # UUID in MacOS, or MAC in Linux and Windows
        self.rssi: Optional[int] = getattr(device, "rssi", None)
        self.metadata: Optional[Dict[str, Union[List, Dict]]] = getattr(
            device, "metadata", None
        )
        self.product: WaveProduct = WaveProduct(self.name)
        self.serial_number: int = serial_number

    def __eq__(self, other):
        for prop in ("name", "address", "serial_number"):
            if getattr(self, prop) != getattr(other, prop):
                return False
        return True

    def __str__(self):
        return f"WaveDevice ({self.serial_number})"

    def _map_sensor_values(self):
        try:
            data = struct.unpack(DEVICE[self.product]["BUFFER"], self._raw_gatt_values)
        except struct.error as err:
            raise UnsupportedError(err, self.name, self.address)

        self.sensor_version = data[0]
        if self.sensor_version != 1:
            raise UnsupportedError(
                f"Sensor version ({self.sensor_version}) != (1)",
                self.name,
                self.address,
            )
        self.sensors = DeviceSensors.from_bytes(data, self.product)
        return self.sensors

    async def get_sensor_values(self):
        async with BleakClient(self.address) as client:
            self.client: BleakClientBlueZDBus = client
            if self.client and await self.client.is_connected():
                self._raw_gatt_values = await client.read_gatt_char(
                    DEVICE[self.product]["UUID"]
                )
                return self._map_sensor_values()

    @staticmethod
    def parse_serial_number(manufacturer_data: Dict[int, int]) -> Optional[int]:
        """Converts manufacturer data and returns a serial number for the
        Airthings Wave devices.

        :param manufacturer_data: The device manufacturer data
        """
        if not (isinstance(manufacturer_data, dict) and manufacturer_data):
            return None

        identity, data = list(manufacturer_data.items())[0]
        try:
            (serial_number, _) = struct.unpack(SERIAL_NUMBER_BUFFER, bytes(data))
        except (struct.error, TypeError):
            return None
        else:
            return serial_number if identity == IDENTITY else None

    @classmethod
    def create(cls, name: str, address: str, serial_number: int):
        """Create a WaveDevice instance with three distinct arguments.

        :param name: The device product name. See ``wave_reader.data.WaveProduct``
            for a full list of supported devices.
        :param address: The device UUID in MacOS, or MAC in Linux and Windows.
        :param serial_number: The serial number for the device.
        """
        device = namedtuple("device", ["name", "address"])
        return cls(device(name, address), serial_number)


async def discover_devices() -> List[WaveDevice]:
    """Discovers all valid, accessible Airthings Wave devices."""
    wave_devices = []
    device: BLEDevice  # Typing annotation
    for device in await discover():
        serial_number = WaveDevice.parse_serial_number(
            device.metadata.get("manufacturer_data")
        )
        if not serial_number:
            _logger.debug(
                f"Device: {device.name} ({device.address}) was not identified as a Wave device."
            )
            continue
        try:
            wave_devices.append(WaveDevice(device, serial_number))
        except ValueError:
            _logger.warning(
                f"Device: {device.name} ({device.address}) was identified, but unsupported."
            )
            continue
    return wave_devices
