from enum import Enum


class TransactionStatusEnum(str, Enum):
    BOOKED = "BOOKED"
    PENDING = "PENDING"

    def __str__(self) -> str:
        return str(self.value)
