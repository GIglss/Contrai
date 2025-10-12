from enum import Enum


class AccountIdentifierType(str, Enum):
    IBAN = "IBAN"

    def __str__(self) -> str:
        return str(self.value)
