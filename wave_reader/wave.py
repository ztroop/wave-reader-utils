import asyncio
import logging
import struct
from collections import namedtuple
from dataclasses import dataclass, fields
from datetime import datetime
from math import log
from typing import Any, Dict, List, Optional, Union

from bleak import BleakClient, BleakScanner
from bleak.backends.client import BaseBleakClient
from bleak.backends.device import BLEDevice

from wave_reader.data import (
    AIRTHINGS_ID, DEVICE, MANUFACTURER_DATA_FORMAT, SENSOR_VER_SUPPORTED,
    WaveProduct,
)
from wave_reader.measure import (
    CO2, PM, VOC, Humidity, Pressure, Radon, Temperature,
)
from wave_reader.utils import UnsupportedError, requires_client

_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())


@dataclass
class DeviceSensors:
    """A dataclass to encapsulate sensor data.

    :param humidity: Relative humidity level (%rH)
    :param radon_sta: Short-term average for radon level (Bq/m3)
    :param radon_lta: Long-term average for radon level (Bq/m3)
    :param temperature: Ambient temperature (°C)
    :param pressure: Atmospheric pressure (hPa)
    :param co2: Carbon dioxide level (ppm)
    :param voc: Volatile organic compound level (ppb)
    :param pm: Particulate matter (ug/m3)
    """

    humidity: Optional[Humidity] = None
    radon_sta: Optional[Radon] = None
    radon_lta: Optional[Radon] = None
    temperature: Optional[Temperature] = None
    pressure: Optional[Pressure] = None
    co2: Optional[CO2] = None
    voc: Optional[VOC] = None
    pm: Optional[PM] = None

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

    @property
    def dew_point(self) -> Optional[float]:
        """Dew point approximation using the Magnus formula. (°C)"""

        if not self.temperature or not self.humidity:
            return None

        T, RH = self.temperature, self.humidity
        return round(
            (243.12 * (log(RH / 100) + ((17.62 * T) / (243.12 + T))))
            / (17.62 - (log(RH / 100) + ((17.62 * T) / (243.12 + T)))),  # noqa: W503
            2,
        )

    @classmethod
    def from_bytes(cls, data: List[int], product: WaveProduct):
        """Instantiate the class with raw sensor values and the ``WaveProduct``
        selection. Each product can have different sensors or may require the
        raw data to be handled differently.
        """

        return cls(**DEVICE[product]["DATA_FORMAT"](data))  # type: ignore


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

    _client: Optional[BaseBleakClient] = None
    _gatt_services = None
    sensor_readings: Optional[DeviceSensors] = None
    readings_updated: Optional[datetime] = None

    def __init__(self, device: Union[BLEDevice, Any], serial: str):
        self.name: Optional[str] = getattr(device, "name", None)
        self.rssi: Optional[int] = getattr(device, "rssi", None)
        self.metadata: Optional[Dict[str, Union[List, Dict]]] = getattr(
            device, "metadata", None
        )

        self.address: str = getattr(device, "address", "")  # UUID in MacOS, or MAC in Linux and Windows
        self.serial: str = serial
        try:
            self.product: WaveProduct = WaveProduct(self.serial[:3])
            _logger.debug(f"Device: ({self.address}) is a ({self.product}) device.")
        except (KeyError, ValueError):
            _logger.warning(f"Device: ({self.address}) is an unsupported Wave device.")
            self.product = WaveProduct.UNKNOWN

    def __eq__(self, other):
        for prop in ("name", "address", "serial"):
            if getattr(self, prop) != getattr(other, prop):
                return False
        return True

    def __str__(self):
        return f"WaveDevice ({self.serial})"

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, *_):
        await self.disconnect()

    def _map_sensor_values(self, gatt_data: bytearray) -> Optional[DeviceSensors]:
        """Extract binary data and load sensor values from bytes."""

        try:
            data: List[int] = struct.unpack(DEVICE[self.product]["BUFFER"], gatt_data)  # type: ignore
        except struct.error as err:
            raise UnsupportedError(str(err), self.address)

        if self.product != WaveProduct.WAVE and data[0] != SENSOR_VER_SUPPORTED:  # 💩
            raise UnsupportedError(
                f"Sensor version ({data[0]}) != ({SENSOR_VER_SUPPORTED})",
                self.address,
            )
        self.sensor_readings = DeviceSensors.from_bytes(data, self.product)
        self.readings_updated = datetime.utcnow()
        return self.sensor_readings

    async def connect(self) -> bool:
        """Method for initiating BLE connection."""

        self._client = BleakClient(self.address)  # type: ignore
        _logger.info(f"Device: ({self.address}) connecting BLE client.")
        return await self._client.connect() if self._client else False

    @requires_client
    async def is_connected(self) -> bool:
        """Method for determining the status of the BLE connection."""

        return await self._client.is_connected()  # type: ignore

    @requires_client
    async def disconnect(self) -> bool:
        """Method for closing BLE connection."""

        _logger.info(f"Device: ({self.address}) disconnecting BLE client.")
        return await self._client.disconnect() if self._client else False

    @requires_client
    async def read_gatt_descriptor(self, gatt_desc: str) -> Optional[bytearray]:
        """Read Generic Attribute Profile GATT descriptor data.

        :param handle: Specify a descriptor UUID string
        """

        if not self._gatt_services:
            await self.get_services()

        for k, v in getattr(self._gatt_services, "descriptors", {}).items():
            if getattr(v, "uuid") == gatt_desc:
                return await self._client.read_gatt_descriptor(k)  # type: ignore

        return None

    @requires_client
    async def read_gatt_characteristic(self, gatt_char: str) -> bytearray:
        """Read Generic Attribute Profile GATT characteristic data.

        :param gatt_char: Specify a characteristic UUID string
        """

        return await self._client.read_gatt_char(gatt_char)  # type: ignore

    @requires_client
    async def get_services(self) -> Dict:
        """Get available services, descriptors and characteristics for the device."""

        self._gatt_services = self._client.services  # type: ignore
        return getattr(self._gatt_services, "services")

    @requires_client
    async def get_sensor_values(self) -> Optional[DeviceSensors]:
        """Get sensor values from the specified Wave device."""

        characteristics = bytearray()
        uuid: str
        for uuid in DEVICE[self.product]["UUID"]:  # type: ignore
            characteristics += await self.read_gatt_characteristic(uuid)
        return self._map_sensor_values(characteristics)

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
        """Create a WaveDevice instance with arguments.

        :param address: The device UUID in MacOS, or MAC in Linux and Windows.
        :param serial: The serial number for the device.
        """

        device = namedtuple("device", ["address"])
        return cls(device(address), serial)


async def discover_devices(
    wave_devices: Optional[List[WaveDevice]] = None, timeout=5.0, **kwargs
) -> List[WaveDevice]:
    """Discovers all valid, accessible Airthings Wave devices.

    :param wave_devices: List to return devices from asyncio task
    :param timeout: Scanning timeout in seconds (Default: 5.0)
    """

    wave_devices = wave_devices if isinstance(wave_devices, list) else []
    device: BLEDevice  # Typing annotation
    for device in await BleakScanner.discover(timeout=timeout, **kwargs):
        serial = WaveDevice.parse_manufacturer_data(
            device.metadata.get("manufacturer_data")
        )
        if serial:
            wave_devices.append(WaveDevice(device, serial))
        else:
            _logger.debug(f"Device: ({device.address}) is not a valid Wave device.")
            continue

    return wave_devices


def scan(max_retries: int = 3, timeout=5.0, **kwargs) -> List[WaveDevice]:
    """Convenience function for discovering devices. This is particularly useful
    for users that are not as comfortable asynchronous programming.

    :param max_retries: Number of attempts for connecting to devices
    :param timeout: Scanning timeout in seconds (Default: 5.0)
    """

    retry_attempts = 0
    wave_devices: List[WaveDevice] = []

    def _scan():
        loop = asyncio.new_event_loop()
        task = loop.create_task(
            discover_devices(wave_devices, timeout=timeout, **kwargs)
        )
        tasks = asyncio.gather(task, return_exceptions=True)
        loop.run_until_complete(tasks)

    while retry_attempts < max_retries:
        try:
            _scan()
            break
        except Exception as err:
            _logger.debug(err)
            _logger.warning(
                f"Encountered an error. Retrying. {retry_attempts}/{max_retries}"
            )
            retry_attempts += 1
        if retry_attempts >= max_retries:
            _logger.error(f"Exceeded {max_retries} attempts. Aborting.")

    return wave_devices
