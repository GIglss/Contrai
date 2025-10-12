from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComplianceDataAddress")


@_attrs_define
class ComplianceDataAddress:
    """This is the registered company or trading address of your end user.

    Attributes:
        address_line_1 (str): __Mandatory__. AddressLine1 of the business. Example: 123 Queens Street.
        town_name (str): __Mandatory__. Town name of the business. Example: York.
        post_code (str): __Mandatory__. Post code of the business. Example: 12345.
        country (str): __Mandatory__. Country of the business. Example: GB.
        address_line_2 (Union[Unset, str]): __Optional__. AddressLine2 of the business. Example: Unit 13.
    """

    address_line_1: str
    town_name: str
    post_code: str
    country: str
    address_line_2: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_line_1 = self.address_line_1

        town_name = self.town_name

        post_code = self.post_code

        country = self.country

        address_line_2 = self.address_line_2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "addressLine1": address_line_1,
                "townName": town_name,
                "postCode": post_code,
                "country": country,
            }
        )
        if address_line_2 is not UNSET:
            field_dict["addressLine2"] = address_line_2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address_line_1 = d.pop("addressLine1")

        town_name = d.pop("townName")

        post_code = d.pop("postCode")

        country = d.pop("country")

        address_line_2 = d.pop("addressLine2", UNSET)

        compliance_data_address = cls(
            address_line_1=address_line_1,
            town_name=town_name,
            post_code=post_code,
            country=country,
            address_line_2=address_line_2,
        )

        compliance_data_address.additional_properties = d
        return compliance_data_address

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
