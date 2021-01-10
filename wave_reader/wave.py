import struct
from dataclasses import asdict, dataclass, fields
from typing import Any, Dict, List, Optional, Union

from bleak import BleakClient, discover
from bleak.backends.bluezdbus.client import BleakClientBlueZDBus
from bleak.backends.device import BLEDevice

from wave_reader.data import (
    DEVICE, IDENTITY, SERIAL_NUMBER_BUFFER, WaveProduct,
)


class UnknownDevice(Exception):
    """Exception class to indicate invalid Wave device detected."""

    def __init__(self, message: str = "Invalid Wave device."):
        self.message = message
        super().__init__(self.message)


class UnsupportedVersion(Exception):
    """Exception class to indicate unsupported version detected."""

    def __init__(self, message: str):
        self.message = f"Unsupported version detected. {message}"
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
    :type device: Union[BLEDevice, Any]
    :type serial_number: int
    """

    sensor_version: Optional[int] = None
    sensors: Optional[DeviceSensors] = None
    client: Optional[BleakClientBlueZDBus] = None
    raw_values: Optional[bytearray] = None

    def __init__(self, device: Union[BLEDevice, Any], serial_number: int):
        self.name: str = device.name
        self.address: str = device.address  # UUID in Mac, or MAC in Linux and Win
        self.rssi: int = device.rssi
        self.metadata: Dict[str, Union[List, Dict]] = device.metadata
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
            data = struct.unpack(DEVICE[self.product]["BUFFER"], self.raw_values)
        except struct.error as message:
            raise UnsupportedVersion(message)

        self.sensor_version = data[0]
        if self.sensor_version != 1:
            raise UnsupportedVersion(
                f"Sensor version: Got ({self.sensor_version}) Expected (1)"
            )
        self.sensors = DeviceSensors.from_bytes(data, self.product)
        return self.sensors

    async def get_sensor_values(self):
        async with BleakClient(self.address) as client:
            self.client: BleakClientBlueZDBus = client
            if self.client and await self.client.is_connected():
                self.raw_values = await client.read_gatt_char(
                    DEVICE[self.product]["UUID"]
                )
                return self._map_sensor_values()

    @staticmethod
    def parse_serial_number(manufacturer_data: Dict[int, int]) -> int:
        """Converts manufacturer data and returns a serial number for the
        Airthings Wave devices.

        :param manufacturer_data: Manufacturer data
        :type manufacturer_data: dict
        :rtype: int
        """
        if not (isinstance(manufacturer_data, dict) and manufacturer_data):
            raise UnknownDevice("Invalid manufacturer data.")

        identity, data = list(manufacturer_data.items())[0]
        try:
            (serial_number, _) = struct.unpack(SERIAL_NUMBER_BUFFER, bytes(data))
        except (struct.error, TypeError):
            raise UnknownDevice("Buffer size is not valid for a Wave device.")
        else:
            if identity == IDENTITY:
                return serial_number
            else:
                raise UnknownDevice(f"Invalid identity: {identity}")


async def discover_devices() -> List[WaveDevice]:
    """Discovers all valid, accessible Airthings Wave devices.

    :rtype: List[WaveDevice]
    """
    wave_devices = []
    device: BLEDevice  # Typing annotation
    for device in await discover():
        try:
            serial_number = WaveDevice.parse_serial_number(
                device.metadata.get("manufacturer_data")
            )
        except UnknownDevice:
            continue
        wave_devices.append(WaveDevice(device, serial_number))
    return wave_devices
