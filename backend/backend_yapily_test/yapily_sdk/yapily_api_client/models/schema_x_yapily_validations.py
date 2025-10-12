from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SchemaXYapilyValidations")


@_attrs_define
class SchemaXYapilyValidations:
    """
    Attributes:
        max_duration_from_now (Union[Unset, str]):
    """

    max_duration_from_now: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_duration_from_now = self.max_duration_from_now

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_duration_from_now is not UNSET:
            field_dict["maxDurationFromNow"] = max_duration_from_now

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_duration_from_now = d.pop("maxDurationFromNow", UNSET)

        schema_x_yapily_validations = cls(
            max_duration_from_now=max_duration_from_now,
        )

        schema_x_yapily_validations.additional_properties = d
        return schema_x_yapily_validations

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
