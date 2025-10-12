from enum import Enum


class CreditLineType(str, Enum):
    AVAILABLE = "AVAILABLE"
    CREDIT = "CREDIT"
    EMERGENCY = "EMERGENCY"
    OTHER = "OTHER"
    PRE_AGREED = "PRE_AGREED"
    TEMPORARY = "TEMPORARY"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
