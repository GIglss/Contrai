from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_identifications import AccountIdentifications
    from ..models.address_details import AddressDetails


T = TypeVar("T", bound="BeneficiaryPayee")


@_attrs_define
class BeneficiaryPayee:
    """__Mandatory__. Account details belonging to the `Beneficiary Payee` (person/ business). You must define this in your
    payment request along with all of the nested mandatory properties.

        Attributes:
            account_identifications (list['AccountIdentifications']): __Mandatory__. The account identifications that
                identify the `BeneficiaryPayee` bank account. Example: [{'identification': '401016', 'type': 'SORT_CODE'},
                {'identification': '71518920', 'type': 'ACCOUNT_NUMBER'}].
            name (Union[Unset, str]): The account holder name of the beneficiary. Example: Jane Doe.
            address (Union[Unset, AddressDetails]): __Conditional__. The address of the `Payee` or
                `Payer`.<ul><li>`payee.address` is mandatory when the `paymentType` is an `INTERNATIONAL` payment</li><li>An
                `Institution` may require you to specify the `country` when used in the context of the `Payee` to be able to
                make a payment.</li></ul> Example: {'country': 'GB'}.
    """

    account_identifications: list["AccountIdentifications"]
    name: Union[Unset, str] = UNSET
    address: Union[Unset, "AddressDetails"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_identifications = []
        for account_identifications_item_data in self.account_identifications:
            account_identifications_item = account_identifications_item_data.to_dict()
            account_identifications.append(account_identifications_item)

        name = self.name

        address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountIdentifications": account_identifications,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_identifications import AccountIdentifications
        from ..models.address_details import AddressDetails

        d = dict(src_dict)
        account_identifications = []
        _account_identifications = d.pop("accountIdentifications")
        for account_identifications_item_data in _account_identifications:
            account_identifications_item = AccountIdentifications.from_dict(account_identifications_item_data)

            account_identifications.append(account_identifications_item)

        name = d.pop("name", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, AddressDetails]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = AddressDetails.from_dict(_address)

        beneficiary_payee = cls(
            account_identifications=account_identifications,
            name=name,
            address=address,
        )

        beneficiary_payee.additional_properties = d
        return beneficiary_payee

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
