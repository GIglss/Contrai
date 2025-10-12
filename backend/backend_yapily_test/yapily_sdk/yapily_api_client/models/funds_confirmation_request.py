from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amount_details import AmountDetails


T = TypeVar("T", bound="FundsConfirmationRequest")


@_attrs_define
class FundsConfirmationRequest:
    """The fund confirmation object defining the details of the account and funds to be checked under the Variable
    Recurring Payment consent.

        Attributes:
            payment_amount (AmountDetails): __Mandatory__. Monetary Amount.
            reference (Union[Unset, str]): __Optional__. The payment reference or description. Limited to a maximum of 18
                characters long. Example: Own Account Sweeping.
    """

    payment_amount: "AmountDetails"
    reference: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payment_amount = self.payment_amount.to_dict()

        reference = self.reference

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "paymentAmount": payment_amount,
            }
        )
        if reference is not UNSET:
            field_dict["reference"] = reference

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amount_details import AmountDetails

        d = dict(src_dict)
        payment_amount = AmountDetails.from_dict(d.pop("paymentAmount"))

        reference = d.pop("reference", UNSET)

        funds_confirmation_request = cls(
            payment_amount=payment_amount,
            reference=reference,
        )

        funds_confirmation_request.additional_properties = d
        return funds_confirmation_request

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
