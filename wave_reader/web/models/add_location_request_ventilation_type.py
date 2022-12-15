from enum import Enum


class AddLocationRequestVentilationType(str, Enum):
    NATURAL = "NATURAL"
    MECHANICAL = "MECHANICAL"
    BALANCED = "BALANCED"

    def __str__(self) -> str:
        return str(self.value)
