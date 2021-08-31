from enum import Enum


class BatteryType(str, Enum):
    ALKALINE = "ALKALINE"
    LITHIUM = "LITHIUM"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
