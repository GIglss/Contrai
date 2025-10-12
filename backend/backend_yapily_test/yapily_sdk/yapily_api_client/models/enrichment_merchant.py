from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnrichmentMerchant")


@_attrs_define
class EnrichmentMerchant:
    """Details of the merchant, identified by Yapily data services.

    Attributes:
        merchant_name (Union[Unset, str]): The name of the indivdual merchant involved in the transaction e.g. (TESCO
            Petrol).
        parent_group (Union[Unset, str]): The parent organisation that the merchant belongs to e.g. (TESCO).
    """

    merchant_name: Union[Unset, str] = UNSET
    parent_group: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        merchant_name = self.merchant_name

        parent_group = self.parent_group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if merchant_name is not UNSET:
            field_dict["merchantName"] = merchant_name
        if parent_group is not UNSET:
            field_dict["parentGroup"] = parent_group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        merchant_name = d.pop("merchantName", UNSET)

        parent_group = d.pop("parentGroup", UNSET)

        enrichment_merchant = cls(
            merchant_name=merchant_name,
            parent_group=parent_group,
        )

        enrichment_merchant.additional_properties = d
        return enrichment_merchant

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
