from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiErrorResponseV2ErrorIssuesItem")


@_attrs_define
class ApiErrorResponseV2ErrorIssuesItem:
    """Detailed information regarding the issue that was experienced during processing of the request

    Attributes:
        code (str): 5 digit Error Code that uniquely identifies the type of issue, for full list of error codes pelase
            check our documentation
        message (str): Human readable description of the issue that was experienced
        type_ (Union[Unset, str]): Category of the issue
    """

    code: str
    message: str
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message")

        type_ = d.pop("type", UNSET)

        api_error_response_v2_error_issues_item = cls(
            code=code,
            message=message,
            type_=type_,
        )

        api_error_response_v2_error_issues_item.additional_properties = d
        return api_error_response_v2_error_issues_item

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
