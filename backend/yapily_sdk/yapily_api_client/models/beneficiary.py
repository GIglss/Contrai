from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.beneficiary_payee import BeneficiaryPayee


T = TypeVar("T", bound="Beneficiary")


@_attrs_define
class Beneficiary:
    """Account information belonging to the target beneficiary (person/ business).

    Attributes:
        id (Union[Unset, str]): Unique identifier of the `beneficiary`.
        reference (Union[Unset, str]): A creditor reference that is requested to be used for all payment instructions to
            this beneficiary.
        payee (Union[Unset, BeneficiaryPayee]): __Mandatory__. Account details belonging to the `Beneficiary Payee`
            (person/ business). You must define this in your payment request along with all of the nested mandatory
            properties.
        trusted (Union[Unset, bool]): Indicates whether the account owner has stated that this beneficiary should be
            trusted. This often results in reduced authentication and authorisation requirements on payments to the
            beneficiary.
    """

    id: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    payee: Union[Unset, "BeneficiaryPayee"] = UNSET
    trusted: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        reference = self.reference

        payee: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payee, Unset):
            payee = self.payee.to_dict()

        trusted = self.trusted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if reference is not UNSET:
            field_dict["reference"] = reference
        if payee is not UNSET:
            field_dict["payee"] = payee
        if trusted is not UNSET:
            field_dict["trusted"] = trusted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.beneficiary_payee import BeneficiaryPayee

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        reference = d.pop("reference", UNSET)

        _payee = d.pop("payee", UNSET)
        payee: Union[Unset, BeneficiaryPayee]
        if isinstance(_payee, Unset):
            payee = UNSET
        else:
            payee = BeneficiaryPayee.from_dict(_payee)

        trusted = d.pop("trusted", UNSET)

        beneficiary = cls(
            id=id,
            reference=reference,
            payee=payee,
            trusted=trusted,
        )

        beneficiary.additional_properties = d
        return beneficiary

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
