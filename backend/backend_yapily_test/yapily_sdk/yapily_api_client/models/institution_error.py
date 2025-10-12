from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InstitutionError")


@_attrs_define
class InstitutionError:
    """Raw error details provided by the `Institution`, when it was the error source.

    Attributes:
        error_message (Union[Unset, str]): Textual description of the `Institution` error.
        http_status_code (Union[Unset, int]): Numeric HTTP status code associated with the `Institution` error.
    """

    error_message: Union[Unset, str] = UNSET
    http_status_code: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_message = self.error_message

        http_status_code = self.http_status_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if http_status_code is not UNSET:
            field_dict["httpStatusCode"] = http_status_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error_message = d.pop("errorMessage", UNSET)

        http_status_code = d.pop("httpStatusCode", UNSET)

        institution_error = cls(
            error_message=error_message,
            http_status_code=http_status_code,
        )

        institution_error.additional_properties = d
        return institution_error

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
