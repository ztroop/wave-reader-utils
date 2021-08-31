from enum import Enum


class MeasurementSystem(str, Enum):
    US = "US"
    METRIC = "METRIC"

    def __str__(self) -> str:
        return str(self.value)
