from enum import Enum


class PatchOperation(str, Enum):
    ADD = "add"
    REPLACE = "replace"

    def __str__(self) -> str:
        return str(self.value)
