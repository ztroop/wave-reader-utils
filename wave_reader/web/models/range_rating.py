from enum import Enum


class RangeRating(str, Enum):
    POOR = "POOR"
    FAIR = "FAIR"
    GOOD = "GOOD"

    def __str__(self) -> str:
        return str(self.value)
