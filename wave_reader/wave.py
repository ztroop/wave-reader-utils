import logging
import struct
from collections import namedtuple
from dataclasses import dataclass, field, fields
from math import log
from typing import Any, Dict, List, Optional, Union

from bleak import BleakClient, discover
from bleak.backends.bluezdbus.client import BleakClientBlueZDBus
from bleak.backends.device import BLEDevice

from wave_reader.data import (
    AIRTHINGS_ID, DEVICE, MANUFACTURER_DATA_FORMAT, SENSOR_VER_SUPPORTED,
    WaveProduct,
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
    :param dew_pont: Dew point approximation using the Magnus formula (degC)
    """

    humidity: Optional[float] = None
    radon_sta: Optional[int] = None
    radon_lta: Optional[int] = None
    temperature: Optional[float] = None
    pressure: Optional[float] = None
    co2: Optional[float] = None
    voc: Optional[float] = None
    dew_point: Optional[float] = field(init=False)

    def __post_init__(self):
        T, RH = self.temperature, self.humidity
        self.dew_point = round(
            (243.12 * (log(RH / 100) + ((17.62 * T) / (243.12 + T))))
            / (17.62 - (log(RH / 100) + ((17.62 * T) / (243.12 + T)))),  # noqa: W503
            2,
        )

    def __str__(self):
        return f'DeviceSensors ({", ".join(f"{k}: {v}" for k, v in self.as_dict().items())})'

    def as_dict(self) -> Dict[str, Union[int, float]]:
        """Returns a dictionary of populated dataclass fields."""

        data = {}
        for i in fields(self):
            v = getattr(self, i.name)
            if v:
                data[i.name] = v
        return data

    def as_tuple(self) -> tuple:
        """Return a tuple of all dataclass fields."""

        return fields(self)

    @classmethod
    def from_bytes(cls, data: List[int], product: WaveProduct):
        """Instantiate the class with raw sensor values and the ``WaveProduct``
        selection. Each product can have different sensors or may require the
        raw data to be handled differently.
        """

        return cls(**DEVICE[product]["SENSOR_FORMAT"](data))  # type: ignore


class WaveDevice:
    """An object that represents a Airthings Wave device. The
    ``discover_devices`` returns a list of ``BLEDevice`` objects
    that are used in the first parameter.

    If you want to instantiate a WaveDevice manually without using
    discovery, you can create a generic object with the following
    properties: ``name``, ``address`` and optionally ``rssi``, ``metadata``.

    :param device: Device information from Bleak's discover function
    :param serial: Parsed serial number from manufacturer data
    """

    _client: Optional[BleakClientBlueZDBus] = None
    sensor_readings: Optional[DeviceSensors] = None

    def __init__(self, device: Union[BLEDevice, Any], serial: str):
        self.name: Optional[str] = getattr(device, "name", None)
        self.rssi: Optional[int] = getattr(device, "rssi", None)
        self.metadata: Optional[Dict[str, Union[List, Dict]]] = getattr(
            device, "metadata", None
        )

        self.address: str = device.address  # UUID in MacOS, or MAC in Linux and Windows
        self.serial: str = serial
        self.model = self.serial[:4]
        self.product: WaveProduct = WaveProduct(self.model)

    def __eq__(self, other):
        for prop in ("name", "address", "serial"):
            if getattr(self, prop) != getattr(other, prop):
                return False
        return True

    def __str__(self):
        return f"WaveDevice ({self.serial})"

    def _map_sensor_values(self, raw_gatt_data):
        """Extract binary data and load sensor values from bytes."""

        try:
            data = struct.unpack(DEVICE[self.product]["BUFFER"], raw_gatt_data)
        except struct.error as err:
            raise UnsupportedError(err, self.name, self.address)

        sensor_version = data[0]
        if sensor_version != SENSOR_VER_SUPPORTED:
            raise UnsupportedError(
                f"Sensor version ({sensor_version}) != ({SENSOR_VER_SUPPORTED})",
                self.name,
                self.address,
            )
        self.sensor_readings = DeviceSensors.from_bytes(data, self.product)
        return True

    async def get_sensor_values(self) -> Optional[DeviceSensors]:
        """Connect to Wave device and retrieve Generic Attribute Profile
        (GATT) data. The binary data is handled and mapped to a dataclass.
        """

        async with BleakClient(self.address) as client:
            self._client: BleakClientBlueZDBus = client
            if self._client and await self._client.is_connected():
                raw_gatt_data = await client.read_gatt_char(
                    DEVICE[self.product]["UUID"]
                )
                self._map_sensor_values(raw_gatt_data)
                return self.sensor_readings
            else:
                return None

    @staticmethod
    def parse_manufacturer_data(manufacturer_data: Dict[int, int]) -> Optional[str]:
        """Converts manufacturer data and returns a serial number for the
        Airthings Wave devices.

        :param manufacturer_data: The device manufacturer data
        """

        if not (isinstance(manufacturer_data, dict) and manufacturer_data):
            return None

        identity, data = list(manufacturer_data.items())[0]
        try:
            (serial, _) = struct.unpack(MANUFACTURER_DATA_FORMAT, bytes(data))
        except (struct.error, TypeError):
            return None
        else:
            return str(serial) if identity == AIRTHINGS_ID else None

    @classmethod
    def create(cls, address: str, serial: str):
        """Create a WaveDevice instance with three distinct arguments.

        :param address: The device UUID in MacOS, or MAC in Linux and Windows.
        :param serial: The serial number for the device.
        """

        device = namedtuple("device", ["address"])
        return cls(device(address), serial)


async def discover_devices() -> List[WaveDevice]:
    """Discovers all valid, accessible Airthings Wave devices."""

    wave_devices = []
    device: BLEDevice  # Typing annotation
    for device in await discover():
        serial = WaveDevice.parse_manufacturer_data(
            device.metadata.get("manufacturer_data")
        )
        if not serial:
            _logger.debug(
                f"Device: {device.name} ({device.address}) is not a valid Wave device."
            )
            continue
        try:
            wave_device = WaveDevice(device, serial)
            wave_devices.append(wave_device)
            _logger.debug(
                f"Device: {device.name} ({device.address}) identified as a Wave device model {wave_device.model}."
            )
        except ValueError:
            _logger.warning(
                f"Device: {device.name} ({device.address}) is a valid Wave device, but unsupported."
            )
            continue
    return wave_devices
