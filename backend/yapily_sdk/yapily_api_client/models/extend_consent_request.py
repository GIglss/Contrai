import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ExtendConsentRequest")


@_attrs_define
class ExtendConsentRequest:
    """
    Attributes:
        last_confirmed_at (datetime.datetime): __Mandatory__. The time that the user confirmed access to their account
            information Example: 2022-08-16T10:59:53.288Z.
    """

    last_confirmed_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_confirmed_at = self.last_confirmed_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lastConfirmedAt": last_confirmed_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        last_confirmed_at = isoparse(d.pop("lastConfirmedAt"))

        extend_consent_request = cls(
            last_confirmed_at=last_confirmed_at,
        )

        extend_consent_request.additional_properties = d
        return extend_consent_request

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
