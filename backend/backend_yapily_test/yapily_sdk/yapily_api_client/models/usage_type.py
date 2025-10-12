from enum import Enum


class UsageType(str, Enum):
    BUSINESS = "BUSINESS"
    OTHER = "OTHER"
    PERSONAL = "PERSONAL"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
