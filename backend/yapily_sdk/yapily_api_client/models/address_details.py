from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.address_type import AddressType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddressDetails")


@_attrs_define
class AddressDetails:
    """__Conditional__. The address of the `Payee` or `Payer`.<ul><li>`payee.address` is mandatory when the `paymentType`
    is an `INTERNATIONAL` payment</li><li>An `Institution` may require you to specify the `country` when used in the
    context of the `Payee` to be able to make a payment.</li></ul>

        Example:
            {'country': 'GB'}

        Attributes:
            address_lines (Union[Unset, list[str]]): __Optional__. The address line of the address Example: ['Ardenham
                Court'].
            street_name (Union[Unset, str]): __Optional__. The street name of the address Example: Oxford Road.
            building_number (Union[Unset, str]): __Optional__. The building number of the address Example: 45.
            post_code (Union[Unset, str]): __Optional__. The post code of the address Example: HP19 3EQ.
            town_name (Union[Unset, str]): __Optional__. The town name of the address Example: Aylesbury.
            county (Union[Unset, list[str]]): __Optional__. The list of counties for the address Example:
                ['Buckinghamshire'].
            country (Union[Unset, str]): __Conditional__. The 2-letter country code for the address. <br><br>An
                `Institution` may require you to specify the `country` when used in the context of the `Payee` to be able to
                make a payment Example: GB.
            department (Union[Unset, str]): __Optional__. The department for the address Example: Unit 2.
            sub_department (Union[Unset, str]): __Optional__. The sub-department for the address Example: Floor 3.
            address_type (Union[Unset, AddressType]): __Optional__. The type of address
    """

    address_lines: Union[Unset, list[str]] = UNSET
    street_name: Union[Unset, str] = UNSET
    building_number: Union[Unset, str] = UNSET
    post_code: Union[Unset, str] = UNSET
    town_name: Union[Unset, str] = UNSET
    county: Union[Unset, list[str]] = UNSET
    country: Union[Unset, str] = UNSET
    department: Union[Unset, str] = UNSET
    sub_department: Union[Unset, str] = UNSET
    address_type: Union[Unset, AddressType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_lines: Union[Unset, list[str]] = UNSET
        if not isinstance(self.address_lines, Unset):
            address_lines = self.address_lines

        street_name = self.street_name

        building_number = self.building_number

        post_code = self.post_code

        town_name = self.town_name

        county: Union[Unset, list[str]] = UNSET
        if not isinstance(self.county, Unset):
            county = self.county

        country = self.country

        department = self.department

        sub_department = self.sub_department

        address_type: Union[Unset, str] = UNSET
        if not isinstance(self.address_type, Unset):
            address_type = self.address_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_lines is not UNSET:
            field_dict["addressLines"] = address_lines
        if street_name is not UNSET:
            field_dict["streetName"] = street_name
        if building_number is not UNSET:
            field_dict["buildingNumber"] = building_number
        if post_code is not UNSET:
            field_dict["postCode"] = post_code
        if town_name is not UNSET:
            field_dict["townName"] = town_name
        if county is not UNSET:
            field_dict["county"] = county
        if country is not UNSET:
            field_dict["country"] = country
        if department is not UNSET:
            field_dict["department"] = department
        if sub_department is not UNSET:
            field_dict["subDepartment"] = sub_department
        if address_type is not UNSET:
            field_dict["addressType"] = address_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address_lines = cast(list[str], d.pop("addressLines", UNSET))

        street_name = d.pop("streetName", UNSET)

        building_number = d.pop("buildingNumber", UNSET)

        post_code = d.pop("postCode", UNSET)

        town_name = d.pop("townName", UNSET)

        county = cast(list[str], d.pop("county", UNSET))

        country = d.pop("country", UNSET)

        department = d.pop("department", UNSET)

        sub_department = d.pop("subDepartment", UNSET)

        _address_type = d.pop("addressType", UNSET)
        address_type: Union[Unset, AddressType]
        if isinstance(_address_type, Unset):
            address_type = UNSET
        else:
            address_type = AddressType(_address_type)

        address_details = cls(
            address_lines=address_lines,
            street_name=street_name,
            building_number=building_number,
            post_code=post_code,
            town_name=town_name,
            county=county,
            country=country,
            department=department,
            sub_department=sub_department,
            address_type=address_type,
        )

        address_details.additional_properties = d
        return address_details

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
