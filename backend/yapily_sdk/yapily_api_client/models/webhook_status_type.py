from enum import Enum


class WebhookStatusType(str, Enum):
    ACTIVE = "active"
    PAUSED = "paused"

    def __str__(self) -> str:
        return str(self.value)
