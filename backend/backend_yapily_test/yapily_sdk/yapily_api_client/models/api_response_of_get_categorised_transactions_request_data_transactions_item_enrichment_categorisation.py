from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemEnrichmentCategorisation")


@_attrs_define
class ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemEnrichmentCategorisation:
    """
    Attributes:
        categories (Union[Unset, list[str]]):
    """

    categories: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        categories: Union[Unset, list[str]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        categories = cast(list[str], d.pop("categories", UNSET))

        api_response_of_get_categorised_transactions_request_data_transactions_item_enrichment_categorisation = cls(
            categories=categories,
        )

        api_response_of_get_categorised_transactions_request_data_transactions_item_enrichment_categorisation.additional_properties = d
        return api_response_of_get_categorised_transactions_request_data_transactions_item_enrichment_categorisation

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
