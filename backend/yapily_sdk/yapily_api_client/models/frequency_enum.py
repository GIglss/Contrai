from enum import Enum


class FrequencyEnum(str, Enum):
    MONTHLY = "MONTHLY"

    def __str__(self) -> str:
        return str(self.value)
