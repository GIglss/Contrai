from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ConsentAuthCodeRequest")


@_attrs_define
class ConsentAuthCodeRequest:
    """The request body containing the `ConsentAuthCodeRequest` json payload

    Attributes:
        auth_code (str): __Mandatory__. The authorisation code Example: 6b965fbb-ff09-4afa-b897-90c34797cb8f.
        auth_state (str): __Mandatory__. The authorisation state Example: 1270cb2ffc4842b78953afa2228e0a87.
    """

    auth_code: str
    auth_state: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_code = self.auth_code

        auth_state = self.auth_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authCode": auth_code,
                "authState": auth_state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auth_code = d.pop("authCode")

        auth_state = d.pop("authState")

        consent_auth_code_request = cls(
            auth_code=auth_code,
            auth_state=auth_state,
        )

        consent_auth_code_request.additional_properties = d
        return consent_auth_code_request

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
