from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amount_details import AmountDetails
    from ..models.payee_details import PayeeDetails


T = TypeVar("T", bound="SubmissionDetails")


@_attrs_define
class SubmissionDetails:
    """__Mandatory__. The payment submission object defining the details of the payment instruction to be executed under
    the Variable Recurring Payment.

        Attributes:
            payee (PayeeDetails): __Mandatory__. Details of the beneficiary [person or business].
            payment_amount (AmountDetails): __Mandatory__. Monetary Amount.
            reference (Union[Unset, str]): __Optional__. The payment reference or description. Limited to a maximum of 18
                characters long. Example: Own Account Sweeping.
    """

    payee: "PayeeDetails"
    payment_amount: "AmountDetails"
    reference: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payee = self.payee.to_dict()

        payment_amount = self.payment_amount.to_dict()

        reference = self.reference

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payee": payee,
                "paymentAmount": payment_amount,
            }
        )
        if reference is not UNSET:
            field_dict["reference"] = reference

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amount_details import AmountDetails
        from ..models.payee_details import PayeeDetails

        d = dict(src_dict)
        payee = PayeeDetails.from_dict(d.pop("payee"))

        payment_amount = AmountDetails.from_dict(d.pop("paymentAmount"))

        reference = d.pop("reference", UNSET)

        submission_details = cls(
            payee=payee,
            payment_amount=payment_amount,
            reference=reference,
        )

        submission_details.additional_properties = d
        return submission_details

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
