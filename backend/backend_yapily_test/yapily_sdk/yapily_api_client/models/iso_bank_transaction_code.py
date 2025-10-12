from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.iso_code_details import IsoCodeDetails


T = TypeVar("T", bound="IsoBankTransactionCode")


@_attrs_define
class IsoBankTransactionCode:
    """Defines the underlying transaction type (e.g. Card or Debit Transactions, Loans or Mortages). <br><br> Conforms to
    `ISO` standards - ISO 20022.

        Attributes:
            domain_code (Union[Unset, IsoCodeDetails]): __Mandatory__. Details the identification of the ISO code.
            family_code (Union[Unset, IsoCodeDetails]): __Mandatory__. Details the identification of the ISO code.
            sub_family_code (Union[Unset, IsoCodeDetails]): __Mandatory__. Details the identification of the ISO code.
    """

    domain_code: Union[Unset, "IsoCodeDetails"] = UNSET
    family_code: Union[Unset, "IsoCodeDetails"] = UNSET
    sub_family_code: Union[Unset, "IsoCodeDetails"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_code: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.domain_code, Unset):
            domain_code = self.domain_code.to_dict()

        family_code: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.family_code, Unset):
            family_code = self.family_code.to_dict()

        sub_family_code: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sub_family_code, Unset):
            sub_family_code = self.sub_family_code.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain_code is not UNSET:
            field_dict["domainCode"] = domain_code
        if family_code is not UNSET:
            field_dict["familyCode"] = family_code
        if sub_family_code is not UNSET:
            field_dict["subFamilyCode"] = sub_family_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.iso_code_details import IsoCodeDetails

        d = dict(src_dict)
        _domain_code = d.pop("domainCode", UNSET)
        domain_code: Union[Unset, IsoCodeDetails]
        if isinstance(_domain_code, Unset):
            domain_code = UNSET
        else:
            domain_code = IsoCodeDetails.from_dict(_domain_code)

        _family_code = d.pop("familyCode", UNSET)
        family_code: Union[Unset, IsoCodeDetails]
        if isinstance(_family_code, Unset):
            family_code = UNSET
        else:
            family_code = IsoCodeDetails.from_dict(_family_code)

        _sub_family_code = d.pop("subFamilyCode", UNSET)
        sub_family_code: Union[Unset, IsoCodeDetails]
        if isinstance(_sub_family_code, Unset):
            sub_family_code = UNSET
        else:
            sub_family_code = IsoCodeDetails.from_dict(_sub_family_code)

        iso_bank_transaction_code = cls(
            domain_code=domain_code,
            family_code=family_code,
            sub_family_code=sub_family_code,
        )

        iso_bank_transaction_code.additional_properties = d
        return iso_bank_transaction_code

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
