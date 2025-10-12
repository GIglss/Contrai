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
    from ..models.amount_details import AmountDetails
    from ..models.international_payment_request import InternationalPaymentRequest
    from ..models.payee_details import PayeeDetails
    from ..models.payer_details import PayerDetails
    from ..models.periodic_payment_request import PeriodicPaymentRequest


T = TypeVar("T", bound="PaymentRequest")


@_attrs_define
class PaymentRequest:
    """__Mandatory__. The payment request object defining the details of the payment.

    Attributes:
        payment_idempotency_id (str): __Mandatory__. A unique identifier that you must provide to identify the payment.
            This can be any alpha-numeric string but is limited to a maximum of 35 characters. Example:
            04ab4536gaerfc0e1f93c4f4.
        type_ (PaymentType): __Mandatory__. Used to specify which of the [payment
            types](https://docs.yapily.com/pages/key-concepts/payments/payment-execution/intro-to-payment-
            execution/#payment-types) to execute.<br><br>See [European
            Payments](https://docs.yapily.com/pages/knowledge/open-banking/european_payments/) to verify whether the `type`
            should be `DOMESTIC` or `INTERNATIONAL`.
        payee (PayeeDetails): __Mandatory__. Details of the beneficiary [person or business].
        amount (AmountDetails): __Mandatory__. Monetary Amount.
        payer (Union[Unset, PayerDetails]): __Conditional__. Details of the benefactor [person or business].
        reference (Union[Unset, str]): __Optional__. The payment reference or description. Limited to a maximum of 18
            characters long. Example: Bill payment.
        context_type (Union[Unset, PaymentCode]): __Optional__. The payment context code. This defaults to `OTHER` if
            not specified.
        purpose_code (Union[Unset, str]): __Optional__. The payment purpose code. <br><br>Allowed values: INTP, DEPT,
            BEXP, LICF, SERV, SUPP, TRAD, SUBS, GDSV, ROYA, COMT, CHAR, ECPR, CLPR, INTE, LOAN, LOAR, INPC, INPR, INSC,
            INSU, LIFI, PPTI, HLRP, HLST, PDEP, IVPT, REBT, REFU, CDBL, CPKC, EDUC, FEES, GAMB, LOTT, GIFT, INSM, REOD,
            GOVT, TCSC, BLDM, RENT, DIVD, INVS, SAVG, HLTI, DNTS, LTCF, MDCS, VIEW, BECH, BENE, SSBE, PEFC, PENS, ADCS,
            BONU, COMM, SALA, ESTX, HSTX, INTX, PTXP, RDTX, TAXS, VATX, WHLD, TAXR, CBTV, ELEC, GASB, PHON, UBIL, WTER .
            <br><br>See [Payment Purpose code](https://docs.yapily.com/pages/payments/payments-resources/tri-pilot/) to see
            the definition of each code
        periodic_payment (Union[Unset, PeriodicPaymentRequest]): __Conditional__. Used to specify properties to define a
            periodic payment. <br><br>Must be specified when the payment `type` is one of the following:<ul>
            <li><code>DOMESTIC_PERIODIC_PAYMENT</code></li>     <li><code>INTERNATIONAL_PERIODIC_PAYMENT</code></li></ul>
        international_payment (Union[Unset, InternationalPaymentRequest]): __Conditional__. Used to specify properties
            to define an international payment. <br><br>Must be specified when the payment `type` is one of the
            following:<ul>     <li><code>INTERNATIONAL_SINGLE_PAYMENT</code></li>
            <li><code>INTERNATIONAL_SCHEDULED_PAYMENT</code></li>
            <li><code>INTERNATIONAL_PERIODIC_PAYMENT</code></li></ul>
        payment_date_time (Union[Unset, datetime.datetime]): __Conditional__. Used to specify the date of the payment
            when the payment type is one of the following:<ul>    <li><code>DOMESTIC_SCHEDULED_PAYMENT</code></li>
            <li><code>DOMESTIC_PERIODIC_PAYMENT</code></li>    <li><code>INTERNATIONAL_SCHEDULED_PAYMENT</code></li>
            <li><code>INTERNATIONAL_PERIODIC_PAYMENT</code></li></ul> Example: 2021-07-21T17:32:28Z.
        read_refund_account (Union[Unset, bool]): __Optional__. Used to request the payer details in the payment
            response when the `Institution` provides the feature `READ_DOMESTIC_SINGLE_REFUND`.<br><br>See [Reverse
            Payments](https://docs.yapily.com/pages/knowledge/open-banking/reverse_payments/) for more information.
    """

    payment_idempotency_id: str
    type_: PaymentType
    payee: "PayeeDetails"
    amount: "AmountDetails"
    payer: Union[Unset, "PayerDetails"] = UNSET
    reference: Union[Unset, str] = UNSET
    context_type: Union[Unset, PaymentCode] = UNSET
    purpose_code: Union[Unset, str] = UNSET
    periodic_payment: Union[Unset, "PeriodicPaymentRequest"] = UNSET
    international_payment: Union[Unset, "InternationalPaymentRequest"] = UNSET
    payment_date_time: Union[Unset, datetime.datetime] = UNSET
    read_refund_account: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payment_idempotency_id = self.payment_idempotency_id

        type_ = self.type_.value

        payee = self.payee.to_dict()

        amount = self.amount.to_dict()

        payer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payer, Unset):
            payer = self.payer.to_dict()

        reference = self.reference

        context_type: Union[Unset, str] = UNSET
        if not isinstance(self.context_type, Unset):
            context_type = self.context_type.value

        purpose_code = self.purpose_code

        periodic_payment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.periodic_payment, Unset):
            periodic_payment = self.periodic_payment.to_dict()

        international_payment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.international_payment, Unset):
            international_payment = self.international_payment.to_dict()

        payment_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.payment_date_time, Unset):
            payment_date_time = self.payment_date_time.isoformat()

        read_refund_account = self.read_refund_account

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "paymentIdempotencyId": payment_idempotency_id,
                "type": type_,
                "payee": payee,
                "amount": amount,
            }
        )
        if payer is not UNSET:
            field_dict["payer"] = payer
        if reference is not UNSET:
            field_dict["reference"] = reference
        if context_type is not UNSET:
            field_dict["contextType"] = context_type
        if purpose_code is not UNSET:
            field_dict["purposeCode"] = purpose_code
        if periodic_payment is not UNSET:
            field_dict["periodicPayment"] = periodic_payment
        if international_payment is not UNSET:
            field_dict["internationalPayment"] = international_payment
        if payment_date_time is not UNSET:
            field_dict["paymentDateTime"] = payment_date_time
        if read_refund_account is not UNSET:
            field_dict["readRefundAccount"] = read_refund_account

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amount_details import AmountDetails
        from ..models.international_payment_request import InternationalPaymentRequest
        from ..models.payee_details import PayeeDetails
        from ..models.payer_details import PayerDetails
        from ..models.periodic_payment_request import PeriodicPaymentRequest

        d = dict(src_dict)
        payment_idempotency_id = d.pop("paymentIdempotencyId")

        type_ = PaymentType(d.pop("type"))

        payee = PayeeDetails.from_dict(d.pop("payee"))

        amount = AmountDetails.from_dict(d.pop("amount"))

        _payer = d.pop("payer", UNSET)
        payer: Union[Unset, PayerDetails]
        if isinstance(_payer, Unset):
            payer = UNSET
        else:
            payer = PayerDetails.from_dict(_payer)

        reference = d.pop("reference", UNSET)

        _context_type = d.pop("contextType", UNSET)
        context_type: Union[Unset, PaymentCode]
        if isinstance(_context_type, Unset):
            context_type = UNSET
        else:
            context_type = PaymentCode(_context_type)

        purpose_code = d.pop("purposeCode", UNSET)

        _periodic_payment = d.pop("periodicPayment", UNSET)
        periodic_payment: Union[Unset, PeriodicPaymentRequest]
        if isinstance(_periodic_payment, Unset):
            periodic_payment = UNSET
        else:
            periodic_payment = PeriodicPaymentRequest.from_dict(_periodic_payment)

        _international_payment = d.pop("internationalPayment", UNSET)
        international_payment: Union[Unset, InternationalPaymentRequest]
        if isinstance(_international_payment, Unset):
            international_payment = UNSET
        else:
            international_payment = InternationalPaymentRequest.from_dict(_international_payment)

        _payment_date_time = d.pop("paymentDateTime", UNSET)
        payment_date_time: Union[Unset, datetime.datetime]
        if isinstance(_payment_date_time, Unset):
            payment_date_time = UNSET
        else:
            payment_date_time = isoparse(_payment_date_time)

        read_refund_account = d.pop("readRefundAccount", UNSET)

        payment_request = cls(
            payment_idempotency_id=payment_idempotency_id,
            type_=type_,
            payee=payee,
            amount=amount,
            payer=payer,
            reference=reference,
            context_type=context_type,
            purpose_code=purpose_code,
            periodic_payment=periodic_payment,
            international_payment=international_payment,
            payment_date_time=payment_date_time,
            read_refund_account=read_refund_account,
        )

        payment_request.additional_properties = d
        return payment_request

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
