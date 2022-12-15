from enum import Enum


class PatchOperationOp(str, Enum):
    ADD = "ADD"
    REMOVE = "REMOVE"

    def __str__(self) -> str:
        return str(self.value)
