from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Metadata")


@_attrs_define
class Metadata:
    """
    Attributes:
        tracing_id (Union[Unset, UUID]): yapily tracing id
    """

    tracing_id: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tracing_id: Union[Unset, str] = UNSET
        if not isinstance(self.tracing_id, Unset):
            tracing_id = str(self.tracing_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tracing_id is not UNSET:
            field_dict["tracingId"] = tracing_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _tracing_id = d.pop("tracingId", UNSET)
        tracing_id: Union[Unset, UUID]
        if isinstance(_tracing_id, Unset):
            tracing_id = UNSET
        else:
            tracing_id = UUID(_tracing_id)

        metadata = cls(
            tracing_id=tracing_id,
        )

        metadata.additional_properties = d
        return metadata

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
