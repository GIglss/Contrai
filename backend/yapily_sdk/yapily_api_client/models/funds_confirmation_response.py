from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amount_details import AmountDetails
    from ..models.funds_available import FundsAvailable


T = TypeVar("T", bound="FundsConfirmationResponse")


@_attrs_define
class FundsConfirmationResponse:
    """
    Attributes:
        payment_amount (AmountDetails): __Mandatory__. Monetary Amount.
        funds_available (FundsAvailable):
        id (Union[Unset, str]):
        reference (Union[Unset, str]): The payment reference or description. Limited to a maximum of 18 characters long.
            Example: Own Account Sweeping.
    """

    payment_amount: "AmountDetails"
    funds_available: "FundsAvailable"
    id: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payment_amount = self.payment_amount.to_dict()

        funds_available = self.funds_available.to_dict()

        id = self.id

        reference = self.reference

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "paymentAmount": payment_amount,
                "fundsAvailable": funds_available,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if reference is not UNSET:
            field_dict["reference"] = reference

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amount_details import AmountDetails
        from ..models.funds_available import FundsAvailable

        d = dict(src_dict)
        payment_amount = AmountDetails.from_dict(d.pop("paymentAmount"))

        funds_available = FundsAvailable.from_dict(d.pop("fundsAvailable"))

        id = d.pop("id", UNSET)

        reference = d.pop("reference", UNSET)

        funds_confirmation_response = cls(
            payment_amount=payment_amount,
            funds_available=funds_available,
            id=id,
            reference=reference,
        )

        funds_confirmation_response.additional_properties = d
        return funds_confirmation_response

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
