import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.payment_status import PaymentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.initiation_details import InitiationDetails
    from ..models.payer_details import PayerDetails
    from ..models.payment_status_details import PaymentStatusDetails
    from ..models.refund_account import RefundAccount
    from ..models.submission_details import SubmissionDetails


T = TypeVar("T", bound="SubmissionResponse")


@_attrs_define
class SubmissionResponse:
    """
    Attributes:
        initiation_details (InitiationDetails): __Mandatory__. The payment initiation object defining the details of the
            payment under the Variable Recurring Payment consent.
        submission_details (SubmissionDetails): __Mandatory__. The payment submission object defining the details of the
            payment instruction to be executed under the Variable Recurring Payment.
        id (Union[Unset, str]):
        payment_idempotency_id (Union[Unset, str]):
        payment_lifecycle_id (Union[Unset, str]):
        institution_consent_id (Union[Unset, str]):
        status (Union[Unset, PaymentStatus]): The status of the Payment. <br><br>For more information, see [Payment
            Status](/guides/payments/payment-status/)
        status_details (Union[Unset, PaymentStatusDetails]):
        payer (Union[Unset, PayerDetails]): __Conditional__. Details of the benefactor [person or business].
        refund_account (Union[Unset, RefundAccount]): The account to which funds should be returned if the payment is to
            be later refunded.
        expected_execution_time (Union[Unset, datetime.datetime]):
        expected_settlement_time (Union[Unset, datetime.datetime]):
    """

    initiation_details: "InitiationDetails"
    submission_details: "SubmissionDetails"
    id: Union[Unset, str] = UNSET
    payment_idempotency_id: Union[Unset, str] = UNSET
    payment_lifecycle_id: Union[Unset, str] = UNSET
    institution_consent_id: Union[Unset, str] = UNSET
    status: Union[Unset, PaymentStatus] = UNSET
    status_details: Union[Unset, "PaymentStatusDetails"] = UNSET
    payer: Union[Unset, "PayerDetails"] = UNSET
    refund_account: Union[Unset, "RefundAccount"] = UNSET
    expected_execution_time: Union[Unset, datetime.datetime] = UNSET
    expected_settlement_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        initiation_details = self.initiation_details.to_dict()

        submission_details = self.submission_details.to_dict()

        id = self.id

        payment_idempotency_id = self.payment_idempotency_id

        payment_lifecycle_id = self.payment_lifecycle_id

        institution_consent_id = self.institution_consent_id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status_details, Unset):
            status_details = self.status_details.to_dict()

        payer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payer, Unset):
            payer = self.payer.to_dict()

        refund_account: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.refund_account, Unset):
            refund_account = self.refund_account.to_dict()

        expected_execution_time: Union[Unset, str] = UNSET
        if not isinstance(self.expected_execution_time, Unset):
            expected_execution_time = self.expected_execution_time.isoformat()

        expected_settlement_time: Union[Unset, str] = UNSET
        if not isinstance(self.expected_settlement_time, Unset):
            expected_settlement_time = self.expected_settlement_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "initiationDetails": initiation_details,
                "submissionDetails": submission_details,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if payment_idempotency_id is not UNSET:
            field_dict["paymentIdempotencyId"] = payment_idempotency_id
        if payment_lifecycle_id is not UNSET:
            field_dict["paymentLifecycleId"] = payment_lifecycle_id
        if institution_consent_id is not UNSET:
            field_dict["institutionConsentId"] = institution_consent_id
        if status is not UNSET:
            field_dict["status"] = status
        if status_details is not UNSET:
            field_dict["statusDetails"] = status_details
        if payer is not UNSET:
            field_dict["payer"] = payer
        if refund_account is not UNSET:
            field_dict["refundAccount"] = refund_account
        if expected_execution_time is not UNSET:
            field_dict["expectedExecutionTime"] = expected_execution_time
        if expected_settlement_time is not UNSET:
            field_dict["expectedSettlementTime"] = expected_settlement_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.initiation_details import InitiationDetails
        from ..models.payer_details import PayerDetails
        from ..models.payment_status_details import PaymentStatusDetails
        from ..models.refund_account import RefundAccount
        from ..models.submission_details import SubmissionDetails

        d = dict(src_dict)
        initiation_details = InitiationDetails.from_dict(d.pop("initiationDetails"))

        submission_details = SubmissionDetails.from_dict(d.pop("submissionDetails"))

        id = d.pop("id", UNSET)

        payment_idempotency_id = d.pop("paymentIdempotencyId", UNSET)

        payment_lifecycle_id = d.pop("paymentLifecycleId", UNSET)

        institution_consent_id = d.pop("institutionConsentId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, PaymentStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PaymentStatus(_status)

        _status_details = d.pop("statusDetails", UNSET)
        status_details: Union[Unset, PaymentStatusDetails]
        if isinstance(_status_details, Unset):
            status_details = UNSET
        else:
            status_details = PaymentStatusDetails.from_dict(_status_details)

        _payer = d.pop("payer", UNSET)
        payer: Union[Unset, PayerDetails]
        if isinstance(_payer, Unset):
            payer = UNSET
        else:
            payer = PayerDetails.from_dict(_payer)

        _refund_account = d.pop("refundAccount", UNSET)
        refund_account: Union[Unset, RefundAccount]
        if isinstance(_refund_account, Unset):
            refund_account = UNSET
        else:
            refund_account = RefundAccount.from_dict(_refund_account)

        _expected_execution_time = d.pop("expectedExecutionTime", UNSET)
        expected_execution_time: Union[Unset, datetime.datetime]
        if isinstance(_expected_execution_time, Unset):
            expected_execution_time = UNSET
        else:
            expected_execution_time = isoparse(_expected_execution_time)

        _expected_settlement_time = d.pop("expectedSettlementTime", UNSET)
        expected_settlement_time: Union[Unset, datetime.datetime]
        if isinstance(_expected_settlement_time, Unset):
            expected_settlement_time = UNSET
        else:
            expected_settlement_time = isoparse(_expected_settlement_time)

        submission_response = cls(
            initiation_details=initiation_details,
            submission_details=submission_details,
            id=id,
            payment_idempotency_id=payment_idempotency_id,
            payment_lifecycle_id=payment_lifecycle_id,
            institution_consent_id=institution_consent_id,
            status=status,
            status_details=status_details,
            payer=payer,
            refund_account=refund_account,
            expected_execution_time=expected_execution_time,
            expected_settlement_time=expected_settlement_time,
        )

        submission_response.additional_properties = d
        return submission_response

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
