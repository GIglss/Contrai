from enum import Enum


class ChargeBearerType(str, Enum):
    CRED = "CRED"
    DEBT = "DEBT"
    SHAR = "SHAR"
    SLEV = "SLEV"

    def __str__(self) -> str:
        return str(self.value)
