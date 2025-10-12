from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.amount_details import AmountDetails


T = TypeVar("T", bound="CreateHostedVRPPaymentRequest")


@_attrs_define
class CreateHostedVRPPaymentRequest:
    """__Mandatory__. The payment request object defining the details of the payment for execution under the Variable
    Recurring Payment consent.

        Attributes:
            payment_idempotency_id (str): __Mandatory__. A unique identifier that you must provide to identify the payment.
                This can be any alpha-numeric string but is limited to a maximum of 35 characters. Example:
                04ab4536gaerfc0e1f93c4f4.
            amount (AmountDetails): __Mandatory__. Monetary Amount.
    """

    payment_idempotency_id: str
    amount: "AmountDetails"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payment_idempotency_id = self.payment_idempotency_id

        amount = self.amount.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "paymentIdempotencyId": payment_idempotency_id,
                "amount": amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amount_details import AmountDetails

        d = dict(src_dict)
        payment_idempotency_id = d.pop("paymentIdempotencyId")

        amount = AmountDetails.from_dict(d.pop("amount"))

        create_hosted_vrp_payment_request = cls(
            payment_idempotency_id=payment_idempotency_id,
            amount=amount,
        )

        create_hosted_vrp_payment_request.additional_properties = d
        return create_hosted_vrp_payment_request

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
