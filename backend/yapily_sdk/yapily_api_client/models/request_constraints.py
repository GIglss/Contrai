from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema import Schema


T = TypeVar("T", bound="RequestConstraints")


@_attrs_define
class RequestConstraints:
    """Object defining the constraints rules applicable for a given requests.

    Attributes:
        body (Schema):
        headers (Union[Unset, Schema]):
    """

    body: "Schema"
    headers: Union[Unset, "Schema"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body.to_dict()

        headers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
            }
        )
        if headers is not UNSET:
            field_dict["headers"] = headers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema import Schema

        d = dict(src_dict)
        body = Schema.from_dict(d.pop("body"))

        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, Schema]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = Schema.from_dict(_headers)

        request_constraints = cls(
            body=body,
            headers=headers,
        )

        request_constraints.additional_properties = d
        return request_constraints

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
