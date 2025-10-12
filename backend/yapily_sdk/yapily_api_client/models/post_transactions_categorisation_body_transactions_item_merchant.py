from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostTransactionsCategorisationBodyTransactionsItemMerchant")


@_attrs_define
class PostTransactionsCategorisationBodyTransactionsItemMerchant:
    """
    Attributes:
        mcc (Union[Unset, str]): __Optional__. Merchant Category Code (MCC) according to ISO 18245
    """

    mcc: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mcc = self.mcc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mcc is not UNSET:
            field_dict["mcc"] = mcc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mcc = d.pop("mcc", UNSET)

        post_transactions_categorisation_body_transactions_item_merchant = cls(
            mcc=mcc,
        )

        post_transactions_categorisation_body_transactions_item_merchant.additional_properties = d
        return post_transactions_categorisation_body_transactions_item_merchant

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
