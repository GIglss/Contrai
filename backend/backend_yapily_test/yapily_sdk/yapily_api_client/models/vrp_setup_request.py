import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amount_details import AmountDetails
    from ..models.hosted_vrp_limits_request import HostedVRPLimitsRequest
    from ..models.payee_details import PayeeDetails
    from ..models.payer_details import PayerDetails
    from ..models.payment_risk import PaymentRisk


T = TypeVar("T", bound="VRPSetupRequest")


@_attrs_define
class VRPSetupRequest:
    """
    Attributes:
        payee (PayeeDetails): __Mandatory__. Details of the beneficiary [person or business].
        payer (Union[Unset, PayerDetails]): __Conditional__. Details of the benefactor [person or business].
        reference (Union[Unset, str]): __Optional__. The payment reference or description. Limited to a maximum of 18
            characters long. Example: Own Account Sweeping.
        limits (Union[Unset, HostedVRPLimitsRequest]): The restrictions and limits for payments executed under the VRP
            consent
        valid_from (Union[Unset, datetime.datetime]): __Optional__. Start date when the consent becomes valid.
        valid_to (Union[Unset, datetime.datetime]): __Optional__. End date when the consent expires and becomes invalid.
        recurring_payment_category (Union[Unset, str]): The use-case for the VRP consent supported by the bank. Allowed
            values: <br>`ONGOING` <br>`SUBSCRIPTION`
        initial_payment (Union[Unset, AmountDetails]): __Mandatory__. Monetary Amount.
        risk (Union[Unset, PaymentRisk]): Additional information about the payment that may be used for risk scoring
    """

    payee: "PayeeDetails"
    payer: Union[Unset, "PayerDetails"] = UNSET
    reference: Union[Unset, str] = UNSET
    limits: Union[Unset, "HostedVRPLimitsRequest"] = UNSET
    valid_from: Union[Unset, datetime.datetime] = UNSET
    valid_to: Union[Unset, datetime.datetime] = UNSET
    recurring_payment_category: Union[Unset, str] = UNSET
    initial_payment: Union[Unset, "AmountDetails"] = UNSET
    risk: Union[Unset, "PaymentRisk"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payee = self.payee.to_dict()

        payer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payer, Unset):
            payer = self.payer.to_dict()

        reference = self.reference

        limits: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.limits, Unset):
            limits = self.limits.to_dict()

        valid_from: Union[Unset, str] = UNSET
        if not isinstance(self.valid_from, Unset):
            valid_from = self.valid_from.isoformat()

        valid_to: Union[Unset, str] = UNSET
        if not isinstance(self.valid_to, Unset):
            valid_to = self.valid_to.isoformat()

        recurring_payment_category = self.recurring_payment_category

        initial_payment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.initial_payment, Unset):
            initial_payment = self.initial_payment.to_dict()

        risk: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.risk, Unset):
            risk = self.risk.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payee": payee,
            }
        )
        if payer is not UNSET:
            field_dict["payer"] = payer
        if reference is not UNSET:
            field_dict["reference"] = reference
        if limits is not UNSET:
            field_dict["limits"] = limits
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to
        if recurring_payment_category is not UNSET:
            field_dict["recurringPaymentCategory"] = recurring_payment_category
        if initial_payment is not UNSET:
            field_dict["initialPayment"] = initial_payment
        if risk is not UNSET:
            field_dict["risk"] = risk

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amount_details import AmountDetails
        from ..models.hosted_vrp_limits_request import HostedVRPLimitsRequest
        from ..models.payee_details import PayeeDetails
        from ..models.payer_details import PayerDetails
        from ..models.payment_risk import PaymentRisk

        d = dict(src_dict)
        payee = PayeeDetails.from_dict(d.pop("payee"))

        _payer = d.pop("payer", UNSET)
        payer: Union[Unset, PayerDetails]
        if isinstance(_payer, Unset):
            payer = UNSET
        else:
            payer = PayerDetails.from_dict(_payer)

        reference = d.pop("reference", UNSET)

        _limits = d.pop("limits", UNSET)
        limits: Union[Unset, HostedVRPLimitsRequest]
        if isinstance(_limits, Unset):
            limits = UNSET
        else:
            limits = HostedVRPLimitsRequest.from_dict(_limits)

        _valid_from = d.pop("validFrom", UNSET)
        valid_from: Union[Unset, datetime.datetime]
        if isinstance(_valid_from, Unset):
            valid_from = UNSET
        else:
            valid_from = isoparse(_valid_from)

        _valid_to = d.pop("validTo", UNSET)
        valid_to: Union[Unset, datetime.datetime]
        if isinstance(_valid_to, Unset):
            valid_to = UNSET
        else:
            valid_to = isoparse(_valid_to)

        recurring_payment_category = d.pop("recurringPaymentCategory", UNSET)

        _initial_payment = d.pop("initialPayment", UNSET)
        initial_payment: Union[Unset, AmountDetails]
        if isinstance(_initial_payment, Unset):
            initial_payment = UNSET
        else:
            initial_payment = AmountDetails.from_dict(_initial_payment)

        _risk = d.pop("risk", UNSET)
        risk: Union[Unset, PaymentRisk]
        if isinstance(_risk, Unset):
            risk = UNSET
        else:
            risk = PaymentRisk.from_dict(_risk)

        vrp_setup_request = cls(
            payee=payee,
            payer=payer,
            reference=reference,
            limits=limits,
            valid_from=valid_from,
            valid_to=valid_to,
            recurring_payment_category=recurring_payment_category,
            initial_payment=initial_payment,
            risk=risk,
        )

        vrp_setup_request.additional_properties = d
        return vrp_setup_request

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
