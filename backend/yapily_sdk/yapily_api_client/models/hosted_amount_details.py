from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HostedAmountDetails")


@_attrs_define
class HostedAmountDetails:
    """The payment amount and currency

    Attributes:
        amount_to_pay (float): The payment amount Example: 10.5.
        currency (str): The [ISO 4217](https://www.xe.com/iso4217.php) currency code Example: GBP.
    """

    amount_to_pay: float
    currency: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_to_pay = self.amount_to_pay

        currency = self.currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amountToPay": amount_to_pay,
                "currency": currency,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount_to_pay = d.pop("amountToPay")

        currency = d.pop("currency")

        hosted_amount_details = cls(
            amount_to_pay=amount_to_pay,
            currency=currency,
        )

        hosted_amount_details.additional_properties = d
        return hosted_amount_details

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
