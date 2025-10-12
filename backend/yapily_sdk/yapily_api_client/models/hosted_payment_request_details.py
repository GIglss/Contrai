import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.payment_code import PaymentCode
from ..models.payment_type import PaymentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hosted_amount_details import HostedAmountDetails
    from ..models.payee_details import PayeeDetails
    from ..models.payer_details import PayerDetails


T = TypeVar("T", bound="HostedPaymentRequestDetails")


@_attrs_define
class HostedPaymentRequestDetails:
    """Details of the payment.

    Attributes:
        payment_idempotency_id (str): A unique identifier that you must provide to identify the payment. This can be any
            alpha-numeric string but is limited to a maximum of 35 characters. Example: 04ab4536gaerfc0e1f93c4f4.
        type_ (PaymentType): __Mandatory__. Used to specify which of the [payment
            types](https://docs.yapily.com/pages/key-concepts/payments/payment-execution/intro-to-payment-
            execution/#payment-types) to execute.<br><br>See [European
            Payments](https://docs.yapily.com/pages/knowledge/open-banking/european_payments/) to verify whether the `type`
            should be `DOMESTIC` or `INTERNATIONAL`.
        payee (PayeeDetails): __Mandatory__. Details of the beneficiary [person or business].
        amount_details (HostedAmountDetails): The payment amount and currency
        reference (Union[Unset, str]): The payment reference or description. Limited to a maximum of 18 characters for
            UK institutions. Example: Bill payment.
        context_type (Union[Unset, PaymentCode]): __Optional__. The payment context code. This defaults to `OTHER` if
            not specified.
        payer (Union[Unset, PayerDetails]): __Conditional__. Details of the benefactor [person or business].
        payment_due_date (Union[Unset, datetime.date]): The date that the payment is due. Displayed to the end user in
            the payment summary screen.
    """

    payment_idempotency_id: str
    type_: PaymentType
    payee: "PayeeDetails"
    amount_details: "HostedAmountDetails"
    reference: Union[Unset, str] = UNSET
    context_type: Union[Unset, PaymentCode] = UNSET
    payer: Union[Unset, "PayerDetails"] = UNSET
    payment_due_date: Union[Unset, datetime.date] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payment_idempotency_id = self.payment_idempotency_id

        type_ = self.type_.value

        payee = self.payee.to_dict()

        amount_details = self.amount_details.to_dict()

        reference = self.reference

        context_type: Union[Unset, str] = UNSET
        if not isinstance(self.context_type, Unset):
            context_type = self.context_type.value

        payer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payer, Unset):
            payer = self.payer.to_dict()

        payment_due_date: Union[Unset, str] = UNSET
        if not isinstance(self.payment_due_date, Unset):
            payment_due_date = self.payment_due_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "paymentIdempotencyId": payment_idempotency_id,
                "type": type_,
                "payee": payee,
                "amountDetails": amount_details,
            }
        )
        if reference is not UNSET:
            field_dict["reference"] = reference
        if context_type is not UNSET:
            field_dict["contextType"] = context_type
        if payer is not UNSET:
            field_dict["payer"] = payer
        if payment_due_date is not UNSET:
            field_dict["paymentDueDate"] = payment_due_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hosted_amount_details import HostedAmountDetails
        from ..models.payee_details import PayeeDetails
        from ..models.payer_details import PayerDetails

        d = dict(src_dict)
        payment_idempotency_id = d.pop("paymentIdempotencyId")

        type_ = PaymentType(d.pop("type"))

        payee = PayeeDetails.from_dict(d.pop("payee"))

        amount_details = HostedAmountDetails.from_dict(d.pop("amountDetails"))

        reference = d.pop("reference", UNSET)

        _context_type = d.pop("contextType", UNSET)
        context_type: Union[Unset, PaymentCode]
        if isinstance(_context_type, Unset):
            context_type = UNSET
        else:
            context_type = PaymentCode(_context_type)

        _payer = d.pop("payer", UNSET)
        payer: Union[Unset, PayerDetails]
        if isinstance(_payer, Unset):
            payer = UNSET
        else:
            payer = PayerDetails.from_dict(_payer)

        _payment_due_date = d.pop("paymentDueDate", UNSET)
        payment_due_date: Union[Unset, datetime.date]
        if isinstance(_payment_due_date, Unset):
            payment_due_date = UNSET
        else:
            payment_due_date = isoparse(_payment_due_date).date()

        hosted_payment_request_details = cls(
            payment_idempotency_id=payment_idempotency_id,
            type_=type_,
            payee=payee,
            amount_details=amount_details,
            reference=reference,
            context_type=context_type,
            payer=payer,
            payment_due_date=payment_due_date,
        )

        hosted_payment_request_details.additional_properties = d
        return hosted_payment_request_details

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
