from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.amount_details import AmountDetails


T = TypeVar("T", bound="SubmissionRequest")


@_attrs_define
class SubmissionRequest:
    """__Mandatory__. The payment request object defining the details of the payment for execution under the Variable
    Recurring Payment consent.

        Attributes:
            payment_idempotency_id (str): __Mandatory__. A unique identifier that you must provide to identify the payment.
                This can be any alpha-numeric string but is limited to a maximum of 35 characters. Example:
                04ab4536gaerfc0e1f93c4f4.
            psu_authentication_method (str): __Mandatory__. Chosen authentication method for submission step. Allowed values
                are [SCA_REQUIRED, SCA_NOT_REQUIRED].
            payment_amount (AmountDetails): __Mandatory__. Monetary Amount.
    """

    payment_idempotency_id: str
    psu_authentication_method: str
    payment_amount: "AmountDetails"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payment_idempotency_id = self.payment_idempotency_id

        psu_authentication_method = self.psu_authentication_method

        payment_amount = self.payment_amount.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "paymentIdempotencyId": payment_idempotency_id,
                "psuAuthenticationMethod": psu_authentication_method,
                "paymentAmount": payment_amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amount_details import AmountDetails

        d = dict(src_dict)
        payment_idempotency_id = d.pop("paymentIdempotencyId")

        psu_authentication_method = d.pop("psuAuthenticationMethod")

        payment_amount = AmountDetails.from_dict(d.pop("paymentAmount"))

        submission_request = cls(
            payment_idempotency_id=payment_idempotency_id,
            psu_authentication_method=psu_authentication_method,
            payment_amount=payment_amount,
        )

        submission_request.additional_properties = d
        return submission_request

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
