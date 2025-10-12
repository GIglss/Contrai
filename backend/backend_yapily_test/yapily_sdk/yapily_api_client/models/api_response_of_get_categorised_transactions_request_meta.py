from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiResponseOfGetCategorisedTransactionsRequestMeta")


@_attrs_define
class ApiResponseOfGetCategorisedTransactionsRequestMeta:
    """
    Attributes:
        tracing_id (Union[Unset, str]):
        count (Union[Unset, int]): Total number of categorised transactions available
        page_count (Union[Unset, int]): Total number of pages available, calculated based on the limit per page sent in
            the request.
    """

    tracing_id: Union[Unset, str] = UNSET
    count: Union[Unset, int] = UNSET
    page_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tracing_id = self.tracing_id

        count = self.count

        page_count = self.page_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tracing_id is not UNSET:
            field_dict["tracingId"] = tracing_id
        if count is not UNSET:
            field_dict["count"] = count
        if page_count is not UNSET:
            field_dict["pageCount"] = page_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tracing_id = d.pop("tracingId", UNSET)

        count = d.pop("count", UNSET)

        page_count = d.pop("pageCount", UNSET)

        api_response_of_get_categorised_transactions_request_meta = cls(
            tracing_id=tracing_id,
            count=count,
            page_count=page_count,
        )

        api_response_of_get_categorised_transactions_request_meta.additional_properties = d
        return api_response_of_get_categorised_transactions_request_meta

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
