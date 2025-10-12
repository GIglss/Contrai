from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_transactions_categorisation_body_transactions_item import (
        PostTransactionsCategorisationBodyTransactionsItem,
    )


T = TypeVar("T", bound="PostTransactionsCategorisationBody")


@_attrs_define
class PostTransactionsCategorisationBody:
    """
    Attributes:
        country_code (str): __Mandatory__. Two-letter country code in ISO 3166-1 alpha-2 format (e.g. GB)
        categorisation_type (str): __Mandatory__. Allowed values are `consumer` and `business`.
        transactions (list['PostTransactionsCategorisationBodyTransactionsItem']):
    """

    country_code: str
    categorisation_type: str
    transactions: list["PostTransactionsCategorisationBodyTransactionsItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country_code = self.country_code

        categorisation_type = self.categorisation_type

        transactions = []
        for transactions_item_data in self.transactions:
            transactions_item = transactions_item_data.to_dict()
            transactions.append(transactions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "countryCode": country_code,
                "categorisationType": categorisation_type,
                "transactions": transactions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_transactions_categorisation_body_transactions_item import (
            PostTransactionsCategorisationBodyTransactionsItem,
        )

        d = dict(src_dict)
        country_code = d.pop("countryCode")

        categorisation_type = d.pop("categorisationType")

        transactions = []
        _transactions = d.pop("transactions")
        for transactions_item_data in _transactions:
            transactions_item = PostTransactionsCategorisationBodyTransactionsItem.from_dict(transactions_item_data)

            transactions.append(transactions_item)

        post_transactions_categorisation_body = cls(
            country_code=country_code,
            categorisation_type=categorisation_type,
            transactions=transactions,
        )

        post_transactions_categorisation_body.additional_properties = d
        return post_transactions_categorisation_body

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
