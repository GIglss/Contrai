from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compliance_data_address import ComplianceDataAddress


T = TypeVar("T", bound="ComplianceDataBusiness")


@_attrs_define
class ComplianceDataBusiness:
    """__Conditional__. Mandatory if the type is BUSINESS.

    Attributes:
        name (str): This is the registered company name of your end user. Example: Company LTD.
        registration_number (str): This is the registered company number of the business. Example: COM123NO.
        registered_address (ComplianceDataAddress): This is the registered company or trading address of your end user.
        trading_address (Union[Unset, ComplianceDataAddress]): This is the registered company or trading address of your
            end user.
    """

    name: str
    registration_number: str
    registered_address: "ComplianceDataAddress"
    trading_address: Union[Unset, "ComplianceDataAddress"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        registration_number = self.registration_number

        registered_address = self.registered_address.to_dict()

        trading_address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.trading_address, Unset):
            trading_address = self.trading_address.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "registrationNumber": registration_number,
                "registeredAddress": registered_address,
            }
        )
        if trading_address is not UNSET:
            field_dict["tradingAddress"] = trading_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compliance_data_address import ComplianceDataAddress

        d = dict(src_dict)
        name = d.pop("name")

        registration_number = d.pop("registrationNumber")

        registered_address = ComplianceDataAddress.from_dict(d.pop("registeredAddress"))

        _trading_address = d.pop("tradingAddress", UNSET)
        trading_address: Union[Unset, ComplianceDataAddress]
        if isinstance(_trading_address, Unset):
            trading_address = UNSET
        else:
            trading_address = ComplianceDataAddress.from_dict(_trading_address)

        compliance_data_business = cls(
            name=name,
            registration_number=registration_number,
            registered_address=registered_address,
            trading_address=trading_address,
        )

        compliance_data_business.additional_properties = d
        return compliance_data_business

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
