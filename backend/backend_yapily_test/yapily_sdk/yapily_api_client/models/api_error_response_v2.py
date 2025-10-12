from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_error_response_v2_error import ApiErrorResponseV2Error


T = TypeVar("T", bound="ApiErrorResponseV2")


@_attrs_define
class ApiErrorResponseV2:
    """API Error Response

    Attributes:
        error (Union[Unset, ApiErrorResponseV2Error]):
    """

    error: Union[Unset, "ApiErrorResponseV2Error"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_error_response_v2_error import ApiErrorResponseV2Error

        d = dict(src_dict)
        _error = d.pop("error", UNSET)
        error: Union[Unset, ApiErrorResponseV2Error]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = ApiErrorResponseV2Error.from_dict(_error)

        api_error_response_v2 = cls(
            error=error,
        )

        api_error_response_v2.additional_properties = d
        return api_error_response_v2

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
