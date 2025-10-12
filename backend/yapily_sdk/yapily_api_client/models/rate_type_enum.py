from enum import Enum


class RateTypeEnum(str, Enum):
    ACTUAL = "ACTUAL"
    AGREED = "AGREED"
    INDICATIVE = "INDICATIVE"

    def __str__(self) -> str:
        return str(self.value)
