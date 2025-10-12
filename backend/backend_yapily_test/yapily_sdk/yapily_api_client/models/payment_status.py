from enum import Enum


class PaymentStatus(str, Enum):
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"
    COMPLETED_SETTLEMENT_IN_PROCESS = "COMPLETED_SETTLEMENT_IN_PROCESS"
    DECLINED = "DECLINED"
    EXPIRED = "EXPIRED"
    FAILED = "FAILED"
    INACTIVE = "INACTIVE"
    PENDING = "PENDING"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
