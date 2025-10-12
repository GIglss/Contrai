from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.response_forwarded_data_headers import ResponseForwardedDataHeaders


T = TypeVar("T", bound="ResponseForwardedData")


@_attrs_define
class ResponseForwardedData:
    """
    Attributes:
        headers (Union[Unset, ResponseForwardedDataHeaders]):
        url (Union[Unset, str]):
    """

    headers: Union[Unset, "ResponseForwardedDataHeaders"] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        headers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if headers is not UNSET:
            field_dict["headers"] = headers
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.response_forwarded_data_headers import ResponseForwardedDataHeaders

        d = dict(src_dict)
        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, ResponseForwardedDataHeaders]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = ResponseForwardedDataHeaders.from_dict(_headers)

        url = d.pop("url", UNSET)

        response_forwarded_data = cls(
            headers=headers,
            url=url,
        )

        response_forwarded_data.additional_properties = d
        return response_forwarded_data

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
