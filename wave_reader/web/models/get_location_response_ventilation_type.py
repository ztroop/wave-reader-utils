from enum import Enum


class GetLocationResponseVentilationType(str, Enum):
    NATURAL = "NATURAL"
    MECHANICAL = "MECHANICAL"
    BALANCED = "BALANCED"

    def __str__(self) -> str:
        return str(self.value)
