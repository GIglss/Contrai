from enum import Enum


class FrequencyEnumExtended(str, Enum):
    ANNUAL = "ANNUAL"
    CALENDAR_DAY = "CALENDAR_DAY"
    DAILY = "DAILY"
    EVERY_TWO_MONTHS = "EVERY_TWO_MONTHS"
    EVERY_TWO_WEEKS = "EVERY_TWO_WEEKS"
    EVERY_WORKING_DAY = "EVERY_WORKING_DAY"
    MONTHLY = "MONTHLY"
    QUARTERLY = "QUARTERLY"
    SEMIANNUAL = "SEMIANNUAL"
    WEEKLY = "WEEKLY"

    def __str__(self) -> str:
        return str(self.value)
