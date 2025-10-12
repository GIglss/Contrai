from enum import Enum


class BeneficiaryMatchStatus(str, Enum):
    CLOSE_MATCH = "CLOSE_MATCH"
    EXEMPTED = "EXEMPTED"
    FULL_MATCH = "FULL_MATCH"
    NO_MATCH = "NO_MATCH"
    VERIFICATION_CHECK_NOT_POSSIBLE = "VERIFICATION_CHECK_NOT_POSSIBLE"

    def __str__(self) -> str:
        return str(self.value)
