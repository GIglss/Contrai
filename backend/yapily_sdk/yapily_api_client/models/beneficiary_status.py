from enum import Enum


class BeneficiaryStatus(str, Enum):
    PENDING = "PENDING"
    REJECTED = "REJECTED"
    VERIFIED = "VERIFIED"

    def __str__(self) -> str:
        return str(self.value)
