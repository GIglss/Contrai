from enum import Enum


class AddressType(str, Enum):
    BUSINESS = "BUSINESS"
    CORRESPONDENCE = "CORRESPONDENCE"
    DELIVERY_TO = "DELIVERY_TO"
    MAIL_TO = "MAIL_TO"
    POSTAL = "POSTAL"
    PO_BOX = "PO_BOX"
    RESIDENTIAL = "RESIDENTIAL"
    STATEMENT = "STATEMENT"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
