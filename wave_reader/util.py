import struct
from enum import Enum
from typing import Dict, List, TypedDict, Union


class WaveProduct(Enum):
    WAVEPLUS = "Airthings Wave+"
    WAVE = "Airthings Wave"
    WAVEMINI = "Airthings Wave Mini"


DEVICE = {
    WaveProduct.WAVEPLUS: {
        "UUID": "b42e2a68-ade7-11e4-89d3-123b93f75cba",
        "BUFFER": "<BBBBHHHHHHHH",
    },
    WaveProduct.WAVE: {
        "UUID": "b42e4dcc-ade7-11e4-89d3-123b93f75cba",
        "BUFFER": "<4B8H",
    },
    WaveProduct.WAVEMINI: {
        "UUID": "b42e3b98-ade7-11e4-89d3-123b93f75cba",
        "BUFFER": "<HHHHHHLL",
    },
}


class Metadata(TypedDict):
    """A typing object for type hinting purposes."""

    uuids: List[str]
    manufacturer_data: Dict[int, int]


class UnknownDevice(Exception):
    """Custom exception class to cover various instances of invalid
    BTLE devices.

    :param message: Custom message
    :type message: str
    """

    def __init__(self, message: str = "Invalid Wave Device."):
        self.message = message
        super().__init__(self.message)


class UnsupportedVersion(Exception):
    """Custom exception class to indicate unsupported version detected.

    :param message: The version or message context to indicate an
        unsupported version
    :type message: str
    """

    def __init__(self, message: str):
        self.message = f"Unsupported Version Detected. {message}"
        super().__init__(self.message)


def parse_serial_number(manufacturer_data: Dict[int, int]) -> Union[int, None]:
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
        (serial_number, _) = struct.unpack("<LH", bytes(data))
    except (struct.error, TypeError):
        raise UnknownDevice("Buffer size is not valid for a Wave device.")
    else:
        if identity == 820:
            return serial_number
        else:
            raise UnknownDevice(f"Invalid identity: {identity}")
