from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_error import EnumError

T = TypeVar("T", bound="ValidationError")


@_attrs_define
class ValidationError:
    """
    Attributes:
        field_name (str): name of the field with error
        error (EnumError):
    """

    field_name: str
    error: EnumError
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_name = self.field_name

        error = self.error.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fieldName": field_name,
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_name = d.pop("fieldName")

        error = EnumError(d.pop("error"))

        validation_error = cls(
            field_name=field_name,
            error=error,
        )

        validation_error.additional_properties = d
        return validation_error

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
