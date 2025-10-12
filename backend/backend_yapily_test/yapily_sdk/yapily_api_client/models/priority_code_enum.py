from enum import Enum


class PriorityCodeEnum(str, Enum):
    NORMAL = "NORMAL"
    URGENT = "URGENT"

    def __str__(self) -> str:
        return str(self.value)
