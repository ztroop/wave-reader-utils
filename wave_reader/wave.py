import struct
from typing import Any, List, Union

from bleak import BleakClient, discover
from bleak.backends.bluezdbus.client import BleakClientBlueZDBus
from bleak.backends.device import BLEDevice

from wave_reader.util import (
    Metadata, UnknownDevice, UnsupportedVersion, parse_serial_number,
)

WAVEPLUS_UUID: str = "b42e2a68-ade7-11e4-89d3-123b93f75cba"
WAVE_UUID: str = "b42e4dcc-ade7-11e4-89d3-123b93f75cba"


class DeviceSensors:
    """A generic object to encapsulate sensor data.

    :param humidity: Relative humidity level (%rH)
    :param radon_sta: Short-term average for radon level (Bq/m3)
    :param radon_lta: Long-term average for radon level (Bq/m3)
    :param temperature: Ambient temperature (degC)
    :param pressure: Atmospheric pressure (hPa)
    :param co2: Carbon dioxide level (ppm)
    :param voc: Volatile organic compound level (ppb)
    """
    PROPS = ("humidity", "radon_sta", "radon_lta", "temperature",
             "pressure", "co2", "voc")

    def __init__(self, humidity, radon_sta, radon_lta, temp, pressure=None,
                 co2=None, voc=None):
        self.humidity: float = humidity
        self.radon_sta: int = radon_sta
        self.radon_lta: int = radon_lta
        self.temperature: float = temp
        self.pressure: Union[float, None] = pressure
        self.co2: Union[float, None] = co2
        self.voc: Union[float, None] = voc

    def __eq__(self, other):
        for prop in self.PROPS:
            if getattr(self, prop) != getattr(other, prop):
                return False
        return True

    def __str__(self):
        n = ", "
        r = {i: getattr(self, i) for i in self.PROPS}
        return f'DeviceSensors ({n.join(f"{k}: {v}" for k, v in r.items())})'

    @classmethod
    def from_bytes(cls, data: List, name: str):
        if "Airthings Wave+" in name:
            return cls(
                data[1] / 2.0,
                data[4],
                data[5],
                data[6] / 100.0,
                data[7] / 50.0,
                data[8] * 1.0,
                data[9] * 1.0,
            )
        else:
            return cls(data[1] / 2.0, data[4], data[5], data[6] / 100.0)


class WaveDevice:
    """An object that represents a Airthings Wave device. The
    ``discover_wave_devices`` returns a list of ``BLEDevice`` objects
    that are used in the first parameter.

    If you want to instantiate a WaveDevice manually without using
    discovery, you can create a generic object with the following
    properties: ``name``, ``address``, ``rssi``, ``metadata``.

    :param device: Device information from Bleak's discover function
    :param serial_number: Parsed serial number from manufacturer data
    :type device: Union[BLEDevice, Any]
    :type serial_number: int
    """

    def __init__(self, device: Union[BLEDevice, Any], serial_number: int):
        self.name: str = device.name
        self.address: str = device.address  # UUID in Mac, or MAC in Linux and Win
        self.rssi: int = device.rssi  # Received Signal Strength Indicator
        self.metadata: Metadata = device.metadata
        self.serial_number: int = serial_number
        self.sensor_version: Union[int, None] = None
        self.sensors: Union[DeviceSensors, None] = None
        self.client: Union[BleakClientBlueZDBus, None] = None
        self.raw_values: Union[bytearray, None] = None

    def __eq__(self, other):
        for prop in ("name", "address", "metadata", "serial_number"):
            if getattr(self, prop) != getattr(other, prop):
                return False
        return True

    def __str__(self):
        return "WaveDevice ({0})".format(self.serial_number)

    def map_sensor_values(self):
        try:
            if "Airthings Wave+" in self.name:
                data = struct.unpack("<BBBBHHHHHHHH", self.raw_values)
            else:
                data = struct.unpack("<4B8H", self.raw_values)
        except struct.error as message:
            raise UnsupportedVersion(message)
        try:
            self.sensors = DeviceSensors.from_bytes(data, self.name)
        except ZeroDivisionError:
            raise ValueError(
                "A sensor is reporting zero. Device may not be functioning correctly."
            )
        self.sensor_version = data[0]
        if self.sensor_version != 1:
            raise UnsupportedVersion(f"Got: {self.sensor_version}")

    async def get_raw_sensor_values(self):
        if self.client and await self.client.is_connected():
            self.raw_values = await self.client.read_gatt_char(
                WAVEPLUS_UUID if "Airthings Wave+" in self.name else WAVE_UUID
            )
            self.map_sensor_values()


async def fetch_readings_from_devices(devices: List[WaveDevice]) -> List[WaveDevice]:
    """Fetches sensor readings from devices. Sensors data is accessible
    through ``WaveDevice.sensors`` where the values are mapped to.

    :param devices: A list of ``WaveDevice`` objects, you can use your own
        ``WaveDevice``, or use the discovered devices from ``discover_wave_devices()``
    :rtype: List[WaveDevice]
    """
    device: WaveDevice  # Typing annotation
    for device in devices:
        async with BleakClient(device.address) as client:
            device.client: BleakClientBlueZDBus = client
            await device.get_raw_sensor_values()
    return devices


async def discover_wave_devices() -> List[WaveDevice]:
    """Discovers all valid, accessible Airthings Wave devices.

    :rtype: List[WaveDevice]
    """
    wave_devices = []
    device: BLEDevice  # Typing annotation
    for device in await discover():
        manufacturer_data = device.metadata.get("manufacturer_data")
        try:
            if not manufacturer_data:
                continue
            serial_number = parse_serial_number(manufacturer_data)
        except UnknownDevice:
            continue
        wave_devices.append(WaveDevice(device, serial_number))
    return wave_devices
