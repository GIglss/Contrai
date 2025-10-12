from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payee_details import PayeeDetails
    from ..models.payer_details import PayerDetails


T = TypeVar("T", bound="InitiationDetails")


@_attrs_define
class InitiationDetails:
    """__Mandatory__. The payment initiation object defining the details of the payment under the Variable Recurring
    Payment consent.

        Attributes:
            reference (Union[Unset, str]): __Optional__. The payment reference or description. Limited to a maximum of 18
                characters long. Example: Own Account Sweeping.
            payer (Union[Unset, PayerDetails]): __Conditional__. Details of the benefactor [person or business].
            payee (Union[Unset, PayeeDetails]): __Mandatory__. Details of the beneficiary [person or business].
    """

    reference: Union[Unset, str] = UNSET
    payer: Union[Unset, "PayerDetails"] = UNSET
    payee: Union[Unset, "PayeeDetails"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reference = self.reference

        payer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payer, Unset):
            payer = self.payer.to_dict()

        payee: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payee, Unset):
            payee = self.payee.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference is not UNSET:
            field_dict["reference"] = reference
        if payer is not UNSET:
            field_dict["payer"] = payer
        if payee is not UNSET:
            field_dict["payee"] = payee

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payee_details import PayeeDetails
        from ..models.payer_details import PayerDetails

        d = dict(src_dict)
        reference = d.pop("reference", UNSET)

        _payer = d.pop("payer", UNSET)
        payer: Union[Unset, PayerDetails]
        if isinstance(_payer, Unset):
            payer = UNSET
        else:
            payer = PayerDetails.from_dict(_payer)

        _payee = d.pop("payee", UNSET)
        payee: Union[Unset, PayeeDetails]
        if isinstance(_payee, Unset):
            payee = UNSET
        else:
            payee = PayeeDetails.from_dict(_payee)

        initiation_details = cls(
            reference=reference,
            payer=payer,
            payee=payee,
        )

        initiation_details.additional_properties = d
        return initiation_details

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
