from enum import Enum


class AlignmentEnum(str, Enum):
    CALENDAR = "CALENDAR"
    CONSENT = "CONSENT"

    def __str__(self) -> str:
        return str(self.value)
