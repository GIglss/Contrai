from enum import Enum


class Type(str, Enum):
    CHIP_OTP = "CHIP_OTP"
    PHOTO_OTP = "PHOTO_OTP"
    PUSH_OTP = "PUSH_OTP"
    SMS_OTP = "SMS_OTP"

    def __str__(self) -> str:
        return str(self.value)
