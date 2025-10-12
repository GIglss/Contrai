from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemEnrichmentTransactionHash")


@_attrs_define
class ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemEnrichmentTransactionHash:
    """
    Attributes:
        hash_ (Union[Unset, str]):
    """

    hash_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hash_ = self.hash_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hash_ is not UNSET:
            field_dict["hash"] = hash_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hash_ = d.pop("hash", UNSET)

        api_response_of_get_categorised_transactions_request_data_transactions_item_enrichment_transaction_hash = cls(
            hash_=hash_,
        )

        api_response_of_get_categorised_transactions_request_data_transactions_item_enrichment_transaction_hash.additional_properties = d
        return api_response_of_get_categorised_transactions_request_data_transactions_item_enrichment_transaction_hash

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
