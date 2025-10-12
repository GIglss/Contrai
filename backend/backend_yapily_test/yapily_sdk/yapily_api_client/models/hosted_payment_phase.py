import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="HostedPaymentPhase")


@_attrs_define
class HostedPaymentPhase:
    """The phase of the payment.

    Attributes:
        phase_name (Union[Unset, str]): The name of the hosted payment process phase. Allowed values are : <ul> <li>
            INITIATED - Payment process initiated</li><li>    DECLINED - Payment process failed and will not proceed
            further</li><li>    INSTITUTION_SUBMITTED - Payment institution submitted</li><li>
            EMBEDDED_CREDENTIAL_REQUESTED - For embedded banks, a UI element to collect user credentials was
            displayed</li><li>    CREDENTIALS_ERROR - embedded credentials refused by institution</li><li>
            AUTHORISATION_INITIATED - All details required for payment initiation have been collected</li><li>
            VALIDATION_COMPLETED - The payment payload was validated successfully</li><li>    VALIDATION_FAILED - The
            payment data provided failed validation</li><li>    AUTHORISATION_CREATED - Payment authorisation request
            created with Institution</li><li>    EMBEDDED_CODE_REQUESTED - For embedded banks, a UI element to collect SCA
            for initiated consent was displayed</li><li>    EMBEDDED_TYPE_REQUESTED - For embedded banks, a UI element to
            allow the user to select their preferred SCA method for this consent authorisation was displayed</li><li>
            DECOUPLED_AUTHORISATION - For embedded banks, decoupled authorisation was initiated by the bank</li><li>
            EMBEDDED_CODE_COLLECTED - For embedded banks, SCA code was collected for consent authorisation</li><li>
            EMBEDDED_TYPE_SELECTED - For embedded banks, preferred SCA method was selected for consent
            authorisation</li><li>    PRE_AUTHORISED - pre authorisation was initiated by bank</li><li>
            CONSENT_POLLING_STARTED - We start polling the bank for consent authorisation status</li><li>
            CONSENT_POLLING_ENDED - We finish polling the bank for consent authorisation status</li><li>    AUTHORISED -
            Payment authorisation completed</li><li>    AUTHORISATION_FAILED - Payment authorisation failed and will not
            proceed further</li><li>    AUTHORISATION_REJECTED - Payment authorisation rejected and will not proceed
            further</li><li>    SUBMITTED - Payment execution created and submitted to Institution</li><li>
            SUBMITTED_AUTO - Payment execution created and submitted to Institution</li><li>    ACCEPTED - Payment execution
            accepted by Institution and awaiting settlement</li><li>    REJECTED - Payment or Authorisation request rejected
            by Institution and will not proceed further</li><li>    SETTLEMENT_COMPLETED - Payment settlement
            completed</li><li>    STATUS_POLLING_STARTED - Payment status polling started</li><li>    STATUS_POLLING_ENDED -
            Payment status polling ended</li><li>    MERCHANT_ACKNOWLEDGED - Payment acknowledgement received from
            merchant</li><li>    FINISHED - Payment process completed</li></ul>
        phase_created_at (Union[Unset, datetime.datetime]): The date and time when phase of the hosted payment was
            inserted.
    """

    phase_name: Union[Unset, str] = UNSET
    phase_created_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phase_name = self.phase_name

        phase_created_at: Union[Unset, str] = UNSET
        if not isinstance(self.phase_created_at, Unset):
            phase_created_at = self.phase_created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if phase_name is not UNSET:
            field_dict["phaseName"] = phase_name
        if phase_created_at is not UNSET:
            field_dict["phaseCreatedAt"] = phase_created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        phase_name = d.pop("phaseName", UNSET)

        _phase_created_at = d.pop("phaseCreatedAt", UNSET)
        phase_created_at: Union[Unset, datetime.datetime]
        if isinstance(_phase_created_at, Unset):
            phase_created_at = UNSET
        else:
            phase_created_at = isoparse(_phase_created_at)

        hosted_payment_phase = cls(
            phase_name=phase_name,
            phase_created_at=phase_created_at,
        )

        hosted_payment_phase.additional_properties = d
        return hosted_payment_phase

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
