from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.account_identifier import AccountIdentifier


T = TypeVar("T", bound="ApplicationBeneficiaryDataDetails")


@_attrs_define
class ApplicationBeneficiaryDataDetails:
    """
    Attributes:
        name (str): name of the beneficiary Example: John Doe.
        account_identifier (AccountIdentifier): Account's details.
    """

    name: str
    account_identifier: "AccountIdentifier"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        account_identifier = self.account_identifier.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "accountIdentifier": account_identifier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_identifier import AccountIdentifier

        d = dict(src_dict)
        name = d.pop("name")

        account_identifier = AccountIdentifier.from_dict(d.pop("accountIdentifier"))

        application_beneficiary_data_details = cls(
            name=name,
            account_identifier=account_identifier,
        )

        application_beneficiary_data_details.additional_properties = d
        return application_beneficiary_data_details

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
