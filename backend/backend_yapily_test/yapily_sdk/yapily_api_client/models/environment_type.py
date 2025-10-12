from enum import Enum


class EnvironmentType(str, Enum):
    LIVE = "LIVE"
    MOCK = "MOCK"
    SANDBOX = "SANDBOX"

    def __str__(self) -> str:
        return str(self.value)
