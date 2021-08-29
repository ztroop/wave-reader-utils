from enum import Enum


class ThresholdLevel(str, Enum):
    HIGH = "high"
    LOW = "low"
    NORMAL = "normal"
    LOWWARN = "lowWarn"
    HIGHWARN = "highWarn"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
