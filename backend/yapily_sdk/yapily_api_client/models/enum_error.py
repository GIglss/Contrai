from enum import Enum


class EnumError(str, Enum):
    INVALID_FORMAT = "INVALID_FORMAT"
    MANDATORY = "MANDATORY"

    def __str__(self) -> str:
        return str(self.value)
