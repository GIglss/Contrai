import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.raw_request_body import RawRequestBody
    from ..models.raw_request_body_parameters import RawRequestBodyParameters
    from ..models.raw_request_headers import RawRequestHeaders


T = TypeVar("T", bound="RawRequest")


@_attrs_define
class RawRequest:
    """
    Attributes:
        method (Union[Unset, str]):
        url (Union[Unset, str]):
        request_instant (Union[Unset, datetime.datetime]):
        headers (Union[Unset, RawRequestHeaders]):
        body (Union[Unset, RawRequestBody]):
        body_parameters (Union[Unset, RawRequestBodyParameters]):
        start_time (Union[Unset, datetime.datetime]):
        started_at (Union[Unset, datetime.datetime]):
    """

    method: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    request_instant: Union[Unset, datetime.datetime] = UNSET
    headers: Union[Unset, "RawRequestHeaders"] = UNSET
    body: Union[Unset, "RawRequestBody"] = UNSET
    body_parameters: Union[Unset, "RawRequestBodyParameters"] = UNSET
    start_time: Union[Unset, datetime.datetime] = UNSET
    started_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method = self.method

        url = self.url

        request_instant: Union[Unset, str] = UNSET
        if not isinstance(self.request_instant, Unset):
            request_instant = self.request_instant.isoformat()

        headers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        body: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        body_parameters: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.body_parameters, Unset):
            body_parameters = self.body_parameters.to_dict()

        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        started_at: Union[Unset, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method is not UNSET:
            field_dict["method"] = method
        if url is not UNSET:
            field_dict["url"] = url
        if request_instant is not UNSET:
            field_dict["requestInstant"] = request_instant
        if headers is not UNSET:
            field_dict["headers"] = headers
        if body is not UNSET:
            field_dict["body"] = body
        if body_parameters is not UNSET:
            field_dict["bodyParameters"] = body_parameters
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.raw_request_body import RawRequestBody
        from ..models.raw_request_body_parameters import RawRequestBodyParameters
        from ..models.raw_request_headers import RawRequestHeaders

        d = dict(src_dict)
        method = d.pop("method", UNSET)

        url = d.pop("url", UNSET)

        _request_instant = d.pop("requestInstant", UNSET)
        request_instant: Union[Unset, datetime.datetime]
        if isinstance(_request_instant, Unset):
            request_instant = UNSET
        else:
            request_instant = isoparse(_request_instant)

        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, RawRequestHeaders]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = RawRequestHeaders.from_dict(_headers)

        _body = d.pop("body", UNSET)
        body: Union[Unset, RawRequestBody]
        if isinstance(_body, Unset):
            body = UNSET
        else:
            body = RawRequestBody.from_dict(_body)

        _body_parameters = d.pop("bodyParameters", UNSET)
        body_parameters: Union[Unset, RawRequestBodyParameters]
        if isinstance(_body_parameters, Unset):
            body_parameters = UNSET
        else:
            body_parameters = RawRequestBodyParameters.from_dict(_body_parameters)

        _start_time = d.pop("startTime", UNSET)
        start_time: Union[Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        _started_at = d.pop("startedAt", UNSET)
        started_at: Union[Unset, datetime.datetime]
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        raw_request = cls(
            method=method,
            url=url,
            request_instant=request_instant,
            headers=headers,
            body=body,
            body_parameters=body_parameters,
            start_time=start_time,
            started_at=started_at,
        )

        raw_request.additional_properties = d
        return raw_request

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
