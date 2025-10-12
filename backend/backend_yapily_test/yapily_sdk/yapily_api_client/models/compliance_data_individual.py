import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ComplianceDataIndividual")


@_attrs_define
class ComplianceDataIndividual:
    """__Conditional__. Mandatory if the type is INDIVIDUAL.

    Attributes:
        name (str): This is the first and last name of your end user. Example: John Doe.
        birth_date (datetime.date): This is the date of birth of your end user. Example: 2000-08-12.
    """

    name: str
    birth_date: datetime.date
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        birth_date = self.birth_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "birthDate": birth_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        birth_date = isoparse(d.pop("birthDate")).date()

        compliance_data_individual = cls(
            name=name,
            birth_date=birth_date,
        )

        compliance_data_individual.additional_properties = d
        return compliance_data_individual

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
