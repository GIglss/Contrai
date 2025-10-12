from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.institution_error import InstitutionError


T = TypeVar("T", bound="ErrorIssue")


@_attrs_define
class ErrorIssue:
    """Detailed information regarding the issue that was experienced during processing of the request

    Attributes:
        type_ (str): Category of the issue
        code (str): Code that uniquely identifies the type of issue
        parameter (Union[Unset, str]): Identifies the parameter / property within the request (headers, query parameters
            or body) that the issue relates to. For headers and query parameters, it refers to the parameter name. For the
            body, it refers to the JSONPath of the property
        message (Union[Unset, str]): Human readable description of the issue that was experienced
        institution_error (Union[Unset, InstitutionError]): Raw error details provided by the `Institution`, when it was
            the error source.
    """

    type_: str
    code: str
    parameter: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    institution_error: Union[Unset, "InstitutionError"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        code = self.code

        parameter = self.parameter

        message = self.message

        institution_error: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.institution_error, Unset):
            institution_error = self.institution_error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "code": code,
            }
        )
        if parameter is not UNSET:
            field_dict["parameter"] = parameter
        if message is not UNSET:
            field_dict["message"] = message
        if institution_error is not UNSET:
            field_dict["institutionError"] = institution_error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.institution_error import InstitutionError

        d = dict(src_dict)
        type_ = d.pop("type")

        code = d.pop("code")

        parameter = d.pop("parameter", UNSET)

        message = d.pop("message", UNSET)

        _institution_error = d.pop("institutionError", UNSET)
        institution_error: Union[Unset, InstitutionError]
        if isinstance(_institution_error, Unset):
            institution_error = UNSET
        else:
            institution_error = InstitutionError.from_dict(_institution_error)

        error_issue = cls(
            type_=type_,
            code=code,
            parameter=parameter,
            message=message,
            institution_error=institution_error,
        )

        error_issue.additional_properties = d
        return error_issue

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
