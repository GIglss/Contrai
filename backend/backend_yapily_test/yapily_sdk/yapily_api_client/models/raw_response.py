from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.raw_request import RawRequest
    from ..models.raw_response_headers import RawResponseHeaders
    from ..models.raw_response_result import RawResponseResult


T = TypeVar("T", bound="RawResponse")


@_attrs_define
class RawResponse:
    """[DEPRECATED] Interaction (raw request and response) that occurred with the `Institution` in order to fulfil a
    request.

        Attributes:
            request (Union[Unset, RawRequest]):
            duration (Union[Unset, str]):
            headers (Union[Unset, RawResponseHeaders]):
            result_code (Union[Unset, int]):
            result (Union[Unset, RawResponseResult]):
    """

    request: Union[Unset, "RawRequest"] = UNSET
    duration: Union[Unset, str] = UNSET
    headers: Union[Unset, "RawResponseHeaders"] = UNSET
    result_code: Union[Unset, int] = UNSET
    result: Union[Unset, "RawResponseResult"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        request: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.request, Unset):
            request = self.request.to_dict()

        duration = self.duration

        headers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        result_code = self.result_code

        result: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request is not UNSET:
            field_dict["request"] = request
        if duration is not UNSET:
            field_dict["duration"] = duration
        if headers is not UNSET:
            field_dict["headers"] = headers
        if result_code is not UNSET:
            field_dict["resultCode"] = result_code
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.raw_request import RawRequest
        from ..models.raw_response_headers import RawResponseHeaders
        from ..models.raw_response_result import RawResponseResult

        d = dict(src_dict)
        _request = d.pop("request", UNSET)
        request: Union[Unset, RawRequest]
        if isinstance(_request, Unset):
            request = UNSET
        else:
            request = RawRequest.from_dict(_request)

        duration = d.pop("duration", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, RawResponseHeaders]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = RawResponseHeaders.from_dict(_headers)

        result_code = d.pop("resultCode", UNSET)

        _result = d.pop("result", UNSET)
        result: Union[Unset, RawResponseResult]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = RawResponseResult.from_dict(_result)

        raw_response = cls(
            request=request,
            duration=duration,
            headers=headers,
            result_code=result_code,
            result=result,
        )

        raw_response.additional_properties = d
        return raw_response

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
