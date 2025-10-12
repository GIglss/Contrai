from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.address_type import AddressType
from ..types import UNSET, Unset

T = TypeVar("T", bound="IdentityAddress")


@_attrs_define
class IdentityAddress:
    """
    Attributes:
        address_lines (Union[Unset, list[str]]):
        city (Union[Unset, str]):
        postal_code (Union[Unset, str]):
        country (Union[Unset, str]):
        street_name (Union[Unset, str]):
        building_number (Union[Unset, str]):
        type_ (Union[Unset, AddressType]): __Optional__. The type of address
        county (Union[Unset, str]):
    """

    address_lines: Union[Unset, list[str]] = UNSET
    city: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    street_name: Union[Unset, str] = UNSET
    building_number: Union[Unset, str] = UNSET
    type_: Union[Unset, AddressType] = UNSET
    county: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_lines: Union[Unset, list[str]] = UNSET
        if not isinstance(self.address_lines, Unset):
            address_lines = self.address_lines

        city = self.city

        postal_code = self.postal_code

        country = self.country

        street_name = self.street_name

        building_number = self.building_number

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        county = self.county

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_lines is not UNSET:
            field_dict["addressLines"] = address_lines
        if city is not UNSET:
            field_dict["city"] = city
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if country is not UNSET:
            field_dict["country"] = country
        if street_name is not UNSET:
            field_dict["streetName"] = street_name
        if building_number is not UNSET:
            field_dict["buildingNumber"] = building_number
        if type_ is not UNSET:
            field_dict["type"] = type_
        if county is not UNSET:
            field_dict["county"] = county

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address_lines = cast(list[str], d.pop("addressLines", UNSET))

        city = d.pop("city", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        country = d.pop("country", UNSET)

        street_name = d.pop("streetName", UNSET)

        building_number = d.pop("buildingNumber", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, AddressType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AddressType(_type_)

        county = d.pop("county", UNSET)

        identity_address = cls(
            address_lines=address_lines,
            city=city,
            postal_code=postal_code,
            country=country,
            street_name=street_name,
            building_number=building_number,
            type_=type_,
            county=county,
        )

        identity_address.additional_properties = d
        return identity_address

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
