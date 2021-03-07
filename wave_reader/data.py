from enum import Enum


class WaveProduct(Enum):
    WAVE = "290"
    WAVE2 = "295"
    WAVEPLUS = "293"
    WAVEMINI = "292"
    UNKNOWN = ""
    # WAVEMIST = "294"
    # HUB = ["281", "282"]


# Company Identifier registered with the Bluetooth SIG
# Officially registered as "Corentium AS".
AIRTHINGS_ID = 820

# Model and serial number.
MANUFACTURER_DATA_FORMAT = "<LH"

SENSOR_VER_SUPPORTED = 1
DEVICE = {
    WaveProduct.WAVEPLUS: {
        "NAME": "Wave+",
        "UUID": ("b42e2a68-ade7-11e4-89d3-123b93f75cba",),
        "BUFFER": "<BBBBHHHHHHHH",
        "DATA_FORMAT": (
            lambda d: {
                "humidity": d[1] / 2.0 if d[1] else 0,
                "radon_sta": d[4],
                "radon_lta": d[5],
                "temperature": d[6] / 100.0 if d[6] else 0,
                "pressure": d[7] / 50.0 if d[7] else 0,
                "co2": d[8] * 1.0,
                "voc": d[9] * 1.0,
            }
        ),
    },
    WaveProduct.WAVE: {
        "NAME": "Wave",
        "UUID": (
            "00000000-0000-0000-0000-000000002a6f",  # Humidity
            "00000000-0000-0000-0000-000000002a6e",  # Temperature
            "b42e01aa-ade7-11e4-89d3-123b93f75cba",  # Radon STA
            "b42e0a4c-ade7-11e4-89d3-123b93f75cba",  # Radon LTA
        ),
        "BUFFER": "<H5B4H",
        "DATA_FORMAT": (
            lambda d: {
                "humidity": d[6] / 100.0 if d[6] else 0,
                "temperature": d[7] / 100.0 if d[7] else 0,
                "radon_sta": d[8],
                "radon_lta": d[9],
            }
        ),
    },
    WaveProduct.WAVE2: {
        "NAME": "Wave (2nd Gen)",
        "UUID": ("b42e4dcc-ade7-11e4-89d3-123b93f75cba",),
        "BUFFER": "<4B8H",
        "DATA_FORMAT": (
            lambda d: {
                "humidity": d[1] / 2.0 if d[1] else 0,
                "radon_sta": d[4],
                "radon_lta": d[5],
                "temperature": d[6] / 100.0 if d[6] else 0,
            }
        ),
    },
    WaveProduct.WAVEMINI: {
        "NAME": "Wave Mini",
        "UUID": ("b42e3b98-ade7-11e4-89d3-123b93f75cba",),
        "BUFFER": "<HHHHHHLL",
        "DATA_FORMAT": (
            lambda d: {
                "temperature": round(d[1] / 100.0 - 273.15 if d[1] else 0, 2),
                "humidity": d[3] / 100.0 if d[3] else 0,
                "voc": d[4],
            }
        ),
    },
    WaveProduct.UNKNOWN: {
        "NAME": "Unknown",
        "UUID": tuple(),
        "BUFFER": "",
        "DATA_FORMAT": lambda _: _,
    },
}
