from enum import Enum


class AccountIdentificationType(str, Enum):
    ABA = "ABA"
    ABA_ACH = "ABA_ACH"
    ABA_WIRE = "ABA_WIRE"
    ACCOUNT_NUMBER = "ACCOUNT_NUMBER"
    BBAN = "BBAN"
    BIC = "BIC"
    BLZ = "BLZ"
    BRANCH_CODE = "BRANCH_CODE"
    BSB = "BSB"
    CLABE = "CLABE"
    CTN = "CTN"
    EMAIL = "EMAIL"
    IBAN = "IBAN"
    IFS = "IFS"
    MASKED_PAN = "MASKED_PAN"
    MSISDN = "MSISDN"
    NCC = "NCC"
    PAN = "PAN"
    ROLL_NUMBER = "ROLL_NUMBER"
    SORT_CODE = "SORT_CODE"
    VIRTUAL_ACCOUNT_ID = "VIRTUAL_ACCOUNT_ID"

    def __str__(self) -> str:
        return str(self.value)
