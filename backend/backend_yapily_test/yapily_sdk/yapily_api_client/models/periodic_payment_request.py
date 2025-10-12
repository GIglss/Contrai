import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amount_details import AmountDetails
    from ..models.frequency_request import FrequencyRequest


T = TypeVar("T", bound="PeriodicPaymentRequest")


@_attrs_define
class PeriodicPaymentRequest:
    """__Conditional__. Used to specify properties to define a periodic payment. <br><br>Must be specified when the payment
    `type` is one of the following:<ul>     <li><code>DOMESTIC_PERIODIC_PAYMENT</code></li>
    <li><code>INTERNATIONAL_PERIODIC_PAYMENT</code></li></ul>

        Attributes:
            frequency (FrequencyRequest): __Mandatory__. Defines the intervals at which payment should be made.
            number_of_payments (Union[Unset, int]): __Conditional__. Defines the total number of payments to be
                made.<br><br>This is required if `finalPaymentDateTime` is not specified and it is intended for the periodic
                payment have a fixed amount of payments. Example: 5.
            next_payment_date_time (Union[Unset, datetime.datetime]): __Conditional__. Defines when to start the recurring
                payment date and time. Specify this if you want the first payment to start on a different day than what the
                frequency object defines. Example: 2018-01-10T00:00:00Z.
            next_payment_amount (Union[Unset, AmountDetails]): __Mandatory__. Monetary Amount.
            final_payment_date_time (Union[Unset, datetime.datetime]): __Conditional__. Defines the final payment date and
                time. To create an open-ended periodic payment, do not specify this property. Example: 2030-01-10T00:00:00Z.
            final_payment_amount (Union[Unset, AmountDetails]): __Mandatory__. Monetary Amount.
    """

    frequency: "FrequencyRequest"
    number_of_payments: Union[Unset, int] = UNSET
    next_payment_date_time: Union[Unset, datetime.datetime] = UNSET
    next_payment_amount: Union[Unset, "AmountDetails"] = UNSET
    final_payment_date_time: Union[Unset, datetime.datetime] = UNSET
    final_payment_amount: Union[Unset, "AmountDetails"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        frequency = self.frequency.to_dict()

        number_of_payments = self.number_of_payments

        next_payment_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.next_payment_date_time, Unset):
            next_payment_date_time = self.next_payment_date_time.isoformat()

        next_payment_amount: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.next_payment_amount, Unset):
            next_payment_amount = self.next_payment_amount.to_dict()

        final_payment_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.final_payment_date_time, Unset):
            final_payment_date_time = self.final_payment_date_time.isoformat()

        final_payment_amount: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.final_payment_amount, Unset):
            final_payment_amount = self.final_payment_amount.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "frequency": frequency,
            }
        )
        if number_of_payments is not UNSET:
            field_dict["numberOfPayments"] = number_of_payments
        if next_payment_date_time is not UNSET:
            field_dict["nextPaymentDateTime"] = next_payment_date_time
        if next_payment_amount is not UNSET:
            field_dict["nextPaymentAmount"] = next_payment_amount
        if final_payment_date_time is not UNSET:
            field_dict["finalPaymentDateTime"] = final_payment_date_time
        if final_payment_amount is not UNSET:
            field_dict["finalPaymentAmount"] = final_payment_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amount_details import AmountDetails
        from ..models.frequency_request import FrequencyRequest

        d = dict(src_dict)
        frequency = FrequencyRequest.from_dict(d.pop("frequency"))

        number_of_payments = d.pop("numberOfPayments", UNSET)

        _next_payment_date_time = d.pop("nextPaymentDateTime", UNSET)
        next_payment_date_time: Union[Unset, datetime.datetime]
        if isinstance(_next_payment_date_time, Unset):
            next_payment_date_time = UNSET
        else:
            next_payment_date_time = isoparse(_next_payment_date_time)

        _next_payment_amount = d.pop("nextPaymentAmount", UNSET)
        next_payment_amount: Union[Unset, AmountDetails]
        if isinstance(_next_payment_amount, Unset):
            next_payment_amount = UNSET
        else:
            next_payment_amount = AmountDetails.from_dict(_next_payment_amount)

        _final_payment_date_time = d.pop("finalPaymentDateTime", UNSET)
        final_payment_date_time: Union[Unset, datetime.datetime]
        if isinstance(_final_payment_date_time, Unset):
            final_payment_date_time = UNSET
        else:
            final_payment_date_time = isoparse(_final_payment_date_time)

        _final_payment_amount = d.pop("finalPaymentAmount", UNSET)
        final_payment_amount: Union[Unset, AmountDetails]
        if isinstance(_final_payment_amount, Unset):
            final_payment_amount = UNSET
        else:
            final_payment_amount = AmountDetails.from_dict(_final_payment_amount)

        periodic_payment_request = cls(
            frequency=frequency,
            number_of_payments=number_of_payments,
            next_payment_date_time=next_payment_date_time,
            next_payment_amount=next_payment_amount,
            final_payment_date_time=final_payment_date_time,
            final_payment_amount=final_payment_amount,
        )

        periodic_payment_request.additional_properties = d
        return periodic_payment_request

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
