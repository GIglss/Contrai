import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amount_details import AmountDetails
    from ..models.direct_debit_payee import DirectDebitPayee
    from ..models.payment_status_details import PaymentStatusDetails


T = TypeVar("T", bound="DirectDebitResponse")


@_attrs_define
class DirectDebitResponse:
    """
    Attributes:
        id (Union[Unset, str]):
        status_details (Union[Unset, PaymentStatusDetails]):
        payee_details (Union[Unset, DirectDebitPayee]):
        reference (Union[Unset, str]):
        previous_payment_amount (Union[Unset, AmountDetails]): __Mandatory__. Monetary Amount.
        previous_payment_date_time (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, str] = UNSET
    status_details: Union[Unset, "PaymentStatusDetails"] = UNSET
    payee_details: Union[Unset, "DirectDebitPayee"] = UNSET
    reference: Union[Unset, str] = UNSET
    previous_payment_amount: Union[Unset, "AmountDetails"] = UNSET
    previous_payment_date_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status_details, Unset):
            status_details = self.status_details.to_dict()

        payee_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payee_details, Unset):
            payee_details = self.payee_details.to_dict()

        reference = self.reference

        previous_payment_amount: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.previous_payment_amount, Unset):
            previous_payment_amount = self.previous_payment_amount.to_dict()

        previous_payment_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.previous_payment_date_time, Unset):
            previous_payment_date_time = self.previous_payment_date_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if status_details is not UNSET:
            field_dict["statusDetails"] = status_details
        if payee_details is not UNSET:
            field_dict["payeeDetails"] = payee_details
        if reference is not UNSET:
            field_dict["reference"] = reference
        if previous_payment_amount is not UNSET:
            field_dict["previousPaymentAmount"] = previous_payment_amount
        if previous_payment_date_time is not UNSET:
            field_dict["previousPaymentDateTime"] = previous_payment_date_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amount_details import AmountDetails
        from ..models.direct_debit_payee import DirectDebitPayee
        from ..models.payment_status_details import PaymentStatusDetails

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _status_details = d.pop("statusDetails", UNSET)
        status_details: Union[Unset, PaymentStatusDetails]
        if isinstance(_status_details, Unset):
            status_details = UNSET
        else:
            status_details = PaymentStatusDetails.from_dict(_status_details)

        _payee_details = d.pop("payeeDetails", UNSET)
        payee_details: Union[Unset, DirectDebitPayee]
        if isinstance(_payee_details, Unset):
            payee_details = UNSET
        else:
            payee_details = DirectDebitPayee.from_dict(_payee_details)

        reference = d.pop("reference", UNSET)

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

        direct_debit_response = cls(
            id=id,
            status_details=status_details,
            payee_details=payee_details,
            reference=reference,
            previous_payment_amount=previous_payment_amount,
            previous_payment_date_time=previous_payment_date_time,
        )

        direct_debit_response.additional_properties = d
        return direct_debit_response

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
