from enum import Enum


class SensorUnit(str, Enum):
    C = "c"
    F = "f"
    MBAR = "mbar"
    PA = "pa"
    BQ = "bq"
    PCI = "pci"
    PCT = "pct"
    MV = "mv"
    PPM = "ppm"
    PPB = "ppb"
    DEG = "deg"
    MGPC = "mgpc"
    M = "m"
    KM = "km"
    KPH = "kph"
    KWH = "kWh"
    MPH = "mph"
    RISKINDEX = "riskIndex"
    CONTROLSIGNAL = "controlSignal"
    DBSPL = "dbspl"
    WEATHERCODE = "weatherCode"
    M3H = "m3h"
    CON = "con"
    BINARY = "binary"
    SECONDS = "seconds"
    INFO = "info"
    OCC = "occ"

    def __str__(self) -> str:
        return str(self.value)
