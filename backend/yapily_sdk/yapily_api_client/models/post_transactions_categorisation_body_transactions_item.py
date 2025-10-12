from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_transactions_categorisation_body_transactions_item_amount import (
        PostTransactionsCategorisationBodyTransactionsItemAmount,
    )
    from ..models.post_transactions_categorisation_body_transactions_item_merchant import (
        PostTransactionsCategorisationBodyTransactionsItemMerchant,
    )


T = TypeVar("T", bound="PostTransactionsCategorisationBodyTransactionsItem")


@_attrs_define
class PostTransactionsCategorisationBodyTransactionsItem:
    """
    Attributes:
        id (str): __Mandatory__. A globally unique transaction ID.
        date (str): __Mandatory__. Transaction date in ISO 8601 format (eg. 2025-01-01T12:59:59.999Z)
        amount (PostTransactionsCategorisationBodyTransactionsItemAmount):
        description (str): __Mandatory__. Transaction-specific description.
        country_code (str): __Mandatory__. Transaction-specific two-letter country code in ISO 3166-1 alpha-2 format
            (e.g. GB)
        merchant (Union[Unset, PostTransactionsCategorisationBodyTransactionsItemMerchant]):
    """

    id: str
    date: str
    amount: "PostTransactionsCategorisationBodyTransactionsItemAmount"
    description: str
    country_code: str
    merchant: Union[Unset, "PostTransactionsCategorisationBodyTransactionsItemMerchant"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        date = self.date

        amount = self.amount.to_dict()

        description = self.description

        country_code = self.country_code

        merchant: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "date": date,
                "amount": amount,
                "description": description,
                "countryCode": country_code,
            }
        )
        if merchant is not UNSET:
            field_dict["merchant"] = merchant

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_transactions_categorisation_body_transactions_item_amount import (
            PostTransactionsCategorisationBodyTransactionsItemAmount,
        )
        from ..models.post_transactions_categorisation_body_transactions_item_merchant import (
            PostTransactionsCategorisationBodyTransactionsItemMerchant,
        )

        d = dict(src_dict)
        id = d.pop("id")

        date = d.pop("date")

        amount = PostTransactionsCategorisationBodyTransactionsItemAmount.from_dict(d.pop("amount"))

        description = d.pop("description")

        country_code = d.pop("countryCode")

        _merchant = d.pop("merchant", UNSET)
        merchant: Union[Unset, PostTransactionsCategorisationBodyTransactionsItemMerchant]
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = PostTransactionsCategorisationBodyTransactionsItemMerchant.from_dict(_merchant)

        post_transactions_categorisation_body_transactions_item = cls(
            id=id,
            date=date,
            amount=amount,
            description=description,
            country_code=country_code,
            merchant=merchant,
        )

        post_transactions_categorisation_body_transactions_item.additional_properties = d
        return post_transactions_categorisation_body_transactions_item

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
