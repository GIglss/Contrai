from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResponseMetaWithCount")


@_attrs_define
class ResponseMetaWithCount:
    """
    Attributes:
        tracing_id (Union[Unset, str]):
        count (Union[Unset, int]):
    """

    tracing_id: Union[Unset, str] = UNSET
    count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tracing_id = self.tracing_id

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tracing_id is not UNSET:
            field_dict["tracingId"] = tracing_id
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tracing_id = d.pop("tracingId", UNSET)

        count = d.pop("count", UNSET)

        response_meta_with_count = cls(
            tracing_id=tracing_id,
            count=count,
        )

        response_meta_with_count.additional_properties = d
        return response_meta_with_count

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
