from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InstitutionIdentifiers")


@_attrs_define
class InstitutionIdentifiers:
    """Specifies the institution requirements for making the payment. Skips the bank selection screen in payment flow if
    the `institutionId` and `institutionCountryCode` are provided.

        Attributes:
            institution_country_code (str): 2 letter ISO Country code of the `Institution` the payment request is sent to.
                Example: GB.
            institution_id (Union[Unset, str]): Yapily identifier which identifies the `Institution` the payment request is
                sent to.
    """

    institution_country_code: str
    institution_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        institution_country_code = self.institution_country_code

        institution_id = self.institution_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "institutionCountryCode": institution_country_code,
            }
        )
        if institution_id is not UNSET:
            field_dict["institutionId"] = institution_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        institution_country_code = d.pop("institutionCountryCode")

        institution_id = d.pop("institutionId", UNSET)

        institution_identifiers = cls(
            institution_country_code=institution_country_code,
            institution_id=institution_id,
        )

        institution_identifiers.additional_properties = d
        return institution_identifiers

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
