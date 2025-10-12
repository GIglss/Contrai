import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.payment_status import PaymentStatus
from ..models.priority_code_enum import PriorityCodeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amount_details import AmountDetails
    from ..models.bulk_payment_status_details import BulkPaymentStatusDetails
    from ..models.exchange_rate_information_response import ExchangeRateInformationResponse
    from ..models.frequency_response import FrequencyResponse
    from ..models.payee_details import PayeeDetails
    from ..models.payer_details import PayerDetails
    from ..models.payment_charge_details import PaymentChargeDetails
    from ..models.refund_account import RefundAccount


T = TypeVar("T", bound="BulkPaymentResponse")


@_attrs_define
class BulkPaymentResponse:
    """
    Attributes:
        id (Union[Unset, str]): The unique ID for this Bulk Payment.
        institution_consent_id (Union[Unset, str]): The Institution's Consent ID used for this Bulk Payment.
        institution_interaction_id (Union[Unset, str]): The Financial API (FAPI) Interaction ID for this Bulk Payment.
        payment_idempotency_id (Union[Unset, str]): The unique ID provided by you to identify this Bulk Payment.
        payment_lifecycle_id (Union[Unset, str]):
        payment_scheme (Union[Unset, str]): The payment scheme (ie. payment rail, local instrument) used to carry out
            this Bulk Payment.
        status (Union[Unset, PaymentStatus]): The status of the Payment. <br><br>For more information, see [Payment
            Status](/guides/payments/payment-status/)
        status_details (Union[Unset, BulkPaymentStatusDetails]):
        payer (Union[Unset, PayerDetails]): __Conditional__. Details of the benefactor [person or business].
        payee_details (Union[Unset, PayeeDetails]): __Mandatory__. Details of the beneficiary [person or business].
        reference (Union[Unset, str]): The reference or description for this Bulk Payment.
        amount (Union[Unset, float]): The total monetary amount of this Bulk Payment.
        currency (Union[Unset, str]): The currency of the amount, specified as a 3-letter ISO 4217 code.
        amount_details (Union[Unset, AmountDetails]): __Mandatory__. Monetary Amount.
        created_at (Union[Unset, datetime.datetime]): Date and time of when the payment request was created.
        first_payment_amount (Union[Unset, AmountDetails]): __Mandatory__. Monetary Amount.
        first_payment_date_time (Union[Unset, datetime.datetime]): Date and time of when the first payment request is to
            be made.
        next_payment_amount (Union[Unset, AmountDetails]): __Mandatory__. Monetary Amount.
        next_payment_date_time (Union[Unset, datetime.datetime]): __Conditional__. Defines when the recurring payment is
            to be made.
        final_payment_amount (Union[Unset, AmountDetails]): __Mandatory__. Monetary Amount.
        final_payment_date_time (Union[Unset, datetime.datetime]): Date and time of when the final payment is to be
            made.
        number_of_payments (Union[Unset, int]): Number of recurring payment requests to be made as part of the
            instructed payment schedule.
        previous_payment_amount (Union[Unset, AmountDetails]): __Mandatory__. Monetary Amount.
        previous_payment_date_time (Union[Unset, datetime.datetime]): Date and time of when the previous payment request
            was posted.
        charge_details (Union[Unset, list['PaymentChargeDetails']]):
        scheduled_payment_type (Union[Unset, str]): Details the execution type and the payment date between the payer
            and the payee.
        scheduled_payment_date_time (Union[Unset, datetime.datetime]): Date and time of when the scheduled payment
            request will be made.
        frequency (Union[Unset, FrequencyResponse]): __Mandatory__. Defines the intervals at which payment should be
            made.
        currency_of_transfer (Union[Unset, str]): __Mandatory__. The currency to be transferred to the payee. This may
            differ from the currency the payment is denoted in and the currency of the payer's account. Specified as a
            3-letter code (ISO 4217).
        purpose (Union[Unset, str]): Specifies the external purpose code for the `Institution` - IS0 20022.
        priority (Union[Unset, PriorityCodeEnum]):
        exchange_rate (Union[Unset, ExchangeRateInformationResponse]):
        refund_account (Union[Unset, RefundAccount]): The account to which funds should be returned if the payment is to
            be later refunded.
        bulk_amount_sum (Union[Unset, float]):
    """

    id: Union[Unset, str] = UNSET
    institution_consent_id: Union[Unset, str] = UNSET
    institution_interaction_id: Union[Unset, str] = UNSET
    payment_idempotency_id: Union[Unset, str] = UNSET
    payment_lifecycle_id: Union[Unset, str] = UNSET
    payment_scheme: Union[Unset, str] = UNSET
    status: Union[Unset, PaymentStatus] = UNSET
    status_details: Union[Unset, "BulkPaymentStatusDetails"] = UNSET
    payer: Union[Unset, "PayerDetails"] = UNSET
    payee_details: Union[Unset, "PayeeDetails"] = UNSET
    reference: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    amount_details: Union[Unset, "AmountDetails"] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    first_payment_amount: Union[Unset, "AmountDetails"] = UNSET
    first_payment_date_time: Union[Unset, datetime.datetime] = UNSET
    next_payment_amount: Union[Unset, "AmountDetails"] = UNSET
    next_payment_date_time: Union[Unset, datetime.datetime] = UNSET
    final_payment_amount: Union[Unset, "AmountDetails"] = UNSET
    final_payment_date_time: Union[Unset, datetime.datetime] = UNSET
    number_of_payments: Union[Unset, int] = UNSET
    previous_payment_amount: Union[Unset, "AmountDetails"] = UNSET
    previous_payment_date_time: Union[Unset, datetime.datetime] = UNSET
    charge_details: Union[Unset, list["PaymentChargeDetails"]] = UNSET
    scheduled_payment_type: Union[Unset, str] = UNSET
    scheduled_payment_date_time: Union[Unset, datetime.datetime] = UNSET
    frequency: Union[Unset, "FrequencyResponse"] = UNSET
    currency_of_transfer: Union[Unset, str] = UNSET
    purpose: Union[Unset, str] = UNSET
    priority: Union[Unset, PriorityCodeEnum] = UNSET
    exchange_rate: Union[Unset, "ExchangeRateInformationResponse"] = UNSET
    refund_account: Union[Unset, "RefundAccount"] = UNSET
    bulk_amount_sum: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        institution_consent_id = self.institution_consent_id

        institution_interaction_id = self.institution_interaction_id

        payment_idempotency_id = self.payment_idempotency_id

        payment_lifecycle_id = self.payment_lifecycle_id

        payment_scheme = self.payment_scheme

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status_details, Unset):
            status_details = self.status_details.to_dict()

        payer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payer, Unset):
            payer = self.payer.to_dict()

        payee_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payee_details, Unset):
            payee_details = self.payee_details.to_dict()

        reference = self.reference

        amount = self.amount

        currency = self.currency

        amount_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.amount_details, Unset):
            amount_details = self.amount_details.to_dict()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        first_payment_amount: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.first_payment_amount, Unset):
            first_payment_amount = self.first_payment_amount.to_dict()

        first_payment_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.first_payment_date_time, Unset):
            first_payment_date_time = self.first_payment_date_time.isoformat()

        next_payment_amount: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.next_payment_amount, Unset):
            next_payment_amount = self.next_payment_amount.to_dict()

        next_payment_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.next_payment_date_time, Unset):
            next_payment_date_time = self.next_payment_date_time.isoformat()

        final_payment_amount: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.final_payment_amount, Unset):
            final_payment_amount = self.final_payment_amount.to_dict()

        final_payment_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.final_payment_date_time, Unset):
            final_payment_date_time = self.final_payment_date_time.isoformat()

        number_of_payments = self.number_of_payments

        previous_payment_amount: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.previous_payment_amount, Unset):
            previous_payment_amount = self.previous_payment_amount.to_dict()

        previous_payment_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.previous_payment_date_time, Unset):
            previous_payment_date_time = self.previous_payment_date_time.isoformat()

        charge_details: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.charge_details, Unset):
            charge_details = []
            for charge_details_item_data in self.charge_details:
                charge_details_item = charge_details_item_data.to_dict()
                charge_details.append(charge_details_item)

        scheduled_payment_type = self.scheduled_payment_type

        scheduled_payment_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.scheduled_payment_date_time, Unset):
            scheduled_payment_date_time = self.scheduled_payment_date_time.isoformat()

        frequency: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.frequency, Unset):
            frequency = self.frequency.to_dict()

        currency_of_transfer = self.currency_of_transfer

        purpose = self.purpose

        priority: Union[Unset, str] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        exchange_rate: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.exchange_rate, Unset):
            exchange_rate = self.exchange_rate.to_dict()

        refund_account: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.refund_account, Unset):
            refund_account = self.refund_account.to_dict()

        bulk_amount_sum = self.bulk_amount_sum

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if institution_consent_id is not UNSET:
            field_dict["institutionConsentId"] = institution_consent_id
        if institution_interaction_id is not UNSET:
            field_dict["institutionInteractionId"] = institution_interaction_id
        if payment_idempotency_id is not UNSET:
            field_dict["paymentIdempotencyId"] = payment_idempotency_id
        if payment_lifecycle_id is not UNSET:
            field_dict["paymentLifecycleId"] = payment_lifecycle_id
        if payment_scheme is not UNSET:
            field_dict["paymentScheme"] = payment_scheme
        if status is not UNSET:
            field_dict["status"] = status
        if status_details is not UNSET:
            field_dict["statusDetails"] = status_details
        if payer is not UNSET:
            field_dict["payer"] = payer
        if payee_details is not UNSET:
            field_dict["payeeDetails"] = payee_details
        if reference is not UNSET:
            field_dict["reference"] = reference
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if amount_details is not UNSET:
            field_dict["amountDetails"] = amount_details
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if first_payment_amount is not UNSET:
            field_dict["firstPaymentAmount"] = first_payment_amount
        if first_payment_date_time is not UNSET:
            field_dict["firstPaymentDateTime"] = first_payment_date_time
        if next_payment_amount is not UNSET:
            field_dict["nextPaymentAmount"] = next_payment_amount
        if next_payment_date_time is not UNSET:
            field_dict["nextPaymentDateTime"] = next_payment_date_time
        if final_payment_amount is not UNSET:
            field_dict["finalPaymentAmount"] = final_payment_amount
        if final_payment_date_time is not UNSET:
            field_dict["finalPaymentDateTime"] = final_payment_date_time
        if number_of_payments is not UNSET:
            field_dict["numberOfPayments"] = number_of_payments
        if previous_payment_amount is not UNSET:
            field_dict["previousPaymentAmount"] = previous_payment_amount
        if previous_payment_date_time is not UNSET:
            field_dict["previousPaymentDateTime"] = previous_payment_date_time
        if charge_details is not UNSET:
            field_dict["chargeDetails"] = charge_details
        if scheduled_payment_type is not UNSET:
            field_dict["scheduledPaymentType"] = scheduled_payment_type
        if scheduled_payment_date_time is not UNSET:
            field_dict["scheduledPaymentDateTime"] = scheduled_payment_date_time
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if currency_of_transfer is not UNSET:
            field_dict["currencyOfTransfer"] = currency_of_transfer
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if priority is not UNSET:
            field_dict["priority"] = priority
        if exchange_rate is not UNSET:
            field_dict["exchangeRate"] = exchange_rate
        if refund_account is not UNSET:
            field_dict["refundAccount"] = refund_account
        if bulk_amount_sum is not UNSET:
            field_dict["bulkAmountSum"] = bulk_amount_sum

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amount_details import AmountDetails
        from ..models.bulk_payment_status_details import BulkPaymentStatusDetails
        from ..models.exchange_rate_information_response import ExchangeRateInformationResponse
        from ..models.frequency_response import FrequencyResponse
        from ..models.payee_details import PayeeDetails
        from ..models.payer_details import PayerDetails
        from ..models.payment_charge_details import PaymentChargeDetails
        from ..models.refund_account import RefundAccount

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        institution_consent_id = d.pop("institutionConsentId", UNSET)

        institution_interaction_id = d.pop("institutionInteractionId", UNSET)

        payment_idempotency_id = d.pop("paymentIdempotencyId", UNSET)

        payment_lifecycle_id = d.pop("paymentLifecycleId", UNSET)

        payment_scheme = d.pop("paymentScheme", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, PaymentStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PaymentStatus(_status)

        _status_details = d.pop("statusDetails", UNSET)
        status_details: Union[Unset, BulkPaymentStatusDetails]
        if isinstance(_status_details, Unset):
            status_details = UNSET
        else:
            status_details = BulkPaymentStatusDetails.from_dict(_status_details)

        _payer = d.pop("payer", UNSET)
        payer: Union[Unset, PayerDetails]
        if isinstance(_payer, Unset):
            payer = UNSET
        else:
            payer = PayerDetails.from_dict(_payer)

        _payee_details = d.pop("payeeDetails", UNSET)
        payee_details: Union[Unset, PayeeDetails]
        if isinstance(_payee_details, Unset):
            payee_details = UNSET
        else:
            payee_details = PayeeDetails.from_dict(_payee_details)

        reference = d.pop("reference", UNSET)

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        _amount_details = d.pop("amountDetails", UNSET)
        amount_details: Union[Unset, AmountDetails]
        if isinstance(_amount_details, Unset):
            amount_details = UNSET
        else:
            amount_details = AmountDetails.from_dict(_amount_details)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _first_payment_amount = d.pop("firstPaymentAmount", UNSET)
        first_payment_amount: Union[Unset, AmountDetails]
        if isinstance(_first_payment_amount, Unset):
            first_payment_amount = UNSET
        else:
            first_payment_amount = AmountDetails.from_dict(_first_payment_amount)

        _first_payment_date_time = d.pop("firstPaymentDateTime", UNSET)
        first_payment_date_time: Union[Unset, datetime.datetime]
        if isinstance(_first_payment_date_time, Unset):
            first_payment_date_time = UNSET
        else:
            first_payment_date_time = isoparse(_first_payment_date_time)

        _next_payment_amount = d.pop("nextPaymentAmount", UNSET)
        next_payment_amount: Union[Unset, AmountDetails]
        if isinstance(_next_payment_amount, Unset):
            next_payment_amount = UNSET
        else:
            next_payment_amount = AmountDetails.from_dict(_next_payment_amount)

        _next_payment_date_time = d.pop("nextPaymentDateTime", UNSET)
        next_payment_date_time: Union[Unset, datetime.datetime]
        if isinstance(_next_payment_date_time, Unset):
            next_payment_date_time = UNSET
        else:
            next_payment_date_time = isoparse(_next_payment_date_time)

        _final_payment_amount = d.pop("finalPaymentAmount", UNSET)
        final_payment_amount: Union[Unset, AmountDetails]
        if isinstance(_final_payment_amount, Unset):
            final_payment_amount = UNSET
        else:
            final_payment_amount = AmountDetails.from_dict(_final_payment_amount)

        _final_payment_date_time = d.pop("finalPaymentDateTime", UNSET)
        final_payment_date_time: Union[Unset, datetime.datetime]
        if isinstance(_final_payment_date_time, Unset):
            final_payment_date_time = UNSET
        else:
            final_payment_date_time = isoparse(_final_payment_date_time)

        number_of_payments = d.pop("numberOfPayments", UNSET)

        _previous_payment_amount = d.pop("previousPaymentAmount", UNSET)
        previous_payment_amount: Union[Unset, AmountDetails]
        if isinstance(_previous_payment_amount, Unset):
            previous_payment_amount = UNSET
        else:
            previous_payment_amount = AmountDetails.from_dict(_previous_payment_amount)

        _previous_payment_date_time = d.pop("previousPaymentDateTime", UNSET)
        previous_payment_date_time: Union[Unset, datetime.datetime]
        if isinstance(_previous_payment_date_time, Unset):
            previous_payment_date_time = UNSET
        else:
            previous_payment_date_time = isoparse(_previous_payment_date_time)

        charge_details = []
        _charge_details = d.pop("chargeDetails", UNSET)
        for charge_details_item_data in _charge_details or []:
            charge_details_item = PaymentChargeDetails.from_dict(charge_details_item_data)

            charge_details.append(charge_details_item)

        scheduled_payment_type = d.pop("scheduledPaymentType", UNSET)

        _scheduled_payment_date_time = d.pop("scheduledPaymentDateTime", UNSET)
        scheduled_payment_date_time: Union[Unset, datetime.datetime]
        if isinstance(_scheduled_payment_date_time, Unset):
            scheduled_payment_date_time = UNSET
        else:
            scheduled_payment_date_time = isoparse(_scheduled_payment_date_time)

        _frequency = d.pop("frequency", UNSET)
        frequency: Union[Unset, FrequencyResponse]
        if isinstance(_frequency, Unset):
            frequency = UNSET
        else:
            frequency = FrequencyResponse.from_dict(_frequency)

        currency_of_transfer = d.pop("currencyOfTransfer", UNSET)

        purpose = d.pop("purpose", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, PriorityCodeEnum]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = PriorityCodeEnum(_priority)

        _exchange_rate = d.pop("exchangeRate", UNSET)
        exchange_rate: Union[Unset, ExchangeRateInformationResponse]
        if isinstance(_exchange_rate, Unset):
            exchange_rate = UNSET
        else:
            exchange_rate = ExchangeRateInformationResponse.from_dict(_exchange_rate)

        _refund_account = d.pop("refundAccount", UNSET)
        refund_account: Union[Unset, RefundAccount]
        if isinstance(_refund_account, Unset):
            refund_account = UNSET
        else:
            refund_account = RefundAccount.from_dict(_refund_account)

        bulk_amount_sum = d.pop("bulkAmountSum", UNSET)

        bulk_payment_response = cls(
            id=id,
            institution_consent_id=institution_consent_id,
            institution_interaction_id=institution_interaction_id,
            payment_idempotency_id=payment_idempotency_id,
            payment_lifecycle_id=payment_lifecycle_id,
            payment_scheme=payment_scheme,
            status=status,
            status_details=status_details,
            payer=payer,
            payee_details=payee_details,
            reference=reference,
            amount=amount,
            currency=currency,
            amount_details=amount_details,
            created_at=created_at,
            first_payment_amount=first_payment_amount,
            first_payment_date_time=first_payment_date_time,
            next_payment_amount=next_payment_amount,
            next_payment_date_time=next_payment_date_time,
            final_payment_amount=final_payment_amount,
            final_payment_date_time=final_payment_date_time,
            number_of_payments=number_of_payments,
            previous_payment_amount=previous_payment_amount,
            previous_payment_date_time=previous_payment_date_time,
            charge_details=charge_details,
            scheduled_payment_type=scheduled_payment_type,
            scheduled_payment_date_time=scheduled_payment_date_time,
            frequency=frequency,
            currency_of_transfer=currency_of_transfer,
            purpose=purpose,
            priority=priority,
            exchange_rate=exchange_rate,
            refund_account=refund_account,
            bulk_amount_sum=bulk_amount_sum,
        )

        bulk_payment_response.additional_properties = d
        return bulk_payment_response

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
