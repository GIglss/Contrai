from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Country")


@_attrs_define
class Country:
    """An array of `Country` denoting which regions the `Institution` provides coverage for

    Attributes:
        display_name (Union[Unset, str]): Country name.
        country_code_2 (Union[Unset, str]): Two character ISO 3166 country code.
    """

    display_name: Union[Unset, str] = UNSET
    country_code_2: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        country_code_2 = self.country_code_2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if country_code_2 is not UNSET:
            field_dict["countryCode2"] = country_code_2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("displayName", UNSET)

        country_code_2 = d.pop("countryCode2", UNSET)

        country = cls(
            display_name=display_name,
            country_code_2=country_code_2,
        )

        country.additional_properties = d
        return country

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
