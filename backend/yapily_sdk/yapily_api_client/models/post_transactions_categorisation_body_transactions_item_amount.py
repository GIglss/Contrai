from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostTransactionsCategorisationBodyTransactionsItemAmount")


@_attrs_define
class PostTransactionsCategorisationBodyTransactionsItemAmount:
    """
    Attributes:
        value (int): __Mandatory__. Transaction money amount in cents (or equivalent). Positive amount implies money in,
            negative amount implies money out.
        currency (str): __Mandatory__. Transaction currency.
    """

    value: int
    currency: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        currency = self.currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "currency": currency,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        currency = d.pop("currency")

        post_transactions_categorisation_body_transactions_item_amount = cls(
            value=value,
            currency=currency,
        )

        post_transactions_categorisation_body_transactions_item_amount.additional_properties = d
        return post_transactions_categorisation_body_transactions_item_amount

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
