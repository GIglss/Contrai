from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.institution_error import InstitutionError


T = TypeVar("T", bound="ApiError")


@_attrs_define
class ApiError:
    """Provides details of the error that has occurred.

    Attributes:
        code (Union[Unset, int]): __Mandatory__. Numeric `HTTP` status code associated with the error.
        institution_error (Union[Unset, InstitutionError]): Raw error details provided by the `Institution`, when it was
            the error source.
        message (Union[Unset, str]): __Mandatory__. Description of the exact error that has been experienced.
        source (Union[Unset, str]):
        status (Union[Unset, str]): __Mandatory__. Textual description of the `HTTP` error status type.
        tracing_id (Union[Unset, str]): __Optional__.  A unique identifier assigned by Yapily for the request that can
            be used for support purposes.
    """

    code: Union[Unset, int] = UNSET
    institution_error: Union[Unset, "InstitutionError"] = UNSET
    message: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    tracing_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        institution_error: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.institution_error, Unset):
            institution_error = self.institution_error.to_dict()

        message = self.message

        source = self.source

        status = self.status

        tracing_id = self.tracing_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if institution_error is not UNSET:
            field_dict["institutionError"] = institution_error
        if message is not UNSET:
            field_dict["message"] = message
        if source is not UNSET:
            field_dict["source"] = source
        if status is not UNSET:
            field_dict["status"] = status
        if tracing_id is not UNSET:
            field_dict["tracingId"] = tracing_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.institution_error import InstitutionError

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        _institution_error = d.pop("institutionError", UNSET)
        institution_error: Union[Unset, InstitutionError]
        if isinstance(_institution_error, Unset):
            institution_error = UNSET
        else:
            institution_error = InstitutionError.from_dict(_institution_error)

        message = d.pop("message", UNSET)

        source = d.pop("source", UNSET)

        status = d.pop("status", UNSET)

        tracing_id = d.pop("tracingId", UNSET)

        api_error = cls(
            code=code,
            institution_error=institution_error,
            message=message,
            source=source,
            status=status,
            tracing_id=tracing_id,
        )

        api_error.additional_properties = d
        return api_error

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
