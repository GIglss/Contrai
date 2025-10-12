from enum import Enum


class SortEnum(str, Enum):
    DATE = "date"
    VALUE_1 = "-date"

    def __str__(self) -> str:
        return str(self.value)
