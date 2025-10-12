import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="FundsAvailable")


@_attrs_define
class FundsAvailable:
    """
    Attributes:
        funds_available (bool): __Mandatory__. Indicates whether funds are available or not.
        funds_available_at (datetime.datetime): __Mandatory__. Date and Time when the funds availability is checked.
    """

    funds_available: bool
    funds_available_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        funds_available = self.funds_available

        funds_available_at = self.funds_available_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fundsAvailable": funds_available,
                "fundsAvailableAt": funds_available_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        funds_available = d.pop("fundsAvailable")

        funds_available_at = isoparse(d.pop("fundsAvailableAt"))

        funds_available = cls(
            funds_available=funds_available,
            funds_available_at=funds_available_at,
        )

        funds_available.additional_properties = d
        return funds_available

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
