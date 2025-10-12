import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payment_request import PaymentRequest


T = TypeVar("T", bound="SubmitBulkPaymentRequest")


@_attrs_define
class SubmitBulkPaymentRequest:
    """The payment request object defining the details of the bulk payment

    Attributes:
        payments (list['PaymentRequest']): __Mandatory__. The array of `PaymentRequest` objects to initiate in the bulk
            payment.
        idempotency_id (Union[Unset, str]): __Optional__. An alphanumeric string (1-40 chars) used for idempotency.
            Unique per consent ID for 24 hours. Prevents duplicate bulk file payment submissions. Example:
            1cc3e60d-5500-42be-aaeb-3c5e2f5ed048.
        originator_identification_number (Union[Unset, str]): __Conditional__. The identification number of the
            originator.<ul><li>Mandatory for AIB bulk payments</li></ul>
        execution_date_time (Union[Unset, datetime.datetime]): __Optional__. Used to schedule the bulk payment to be
            executed at a future date if supported by the `Institution`.
    """

    payments: list["PaymentRequest"]
    idempotency_id: Union[Unset, str] = UNSET
    originator_identification_number: Union[Unset, str] = UNSET
    execution_date_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payments = []
        for payments_item_data in self.payments:
            payments_item = payments_item_data.to_dict()
            payments.append(payments_item)

        idempotency_id = self.idempotency_id

        originator_identification_number = self.originator_identification_number

        execution_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.execution_date_time, Unset):
            execution_date_time = self.execution_date_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payments": payments,
            }
        )
        if idempotency_id is not UNSET:
            field_dict["idempotencyId"] = idempotency_id
        if originator_identification_number is not UNSET:
            field_dict["originatorIdentificationNumber"] = originator_identification_number
        if execution_date_time is not UNSET:
            field_dict["executionDateTime"] = execution_date_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payment_request import PaymentRequest

        d = dict(src_dict)
        payments = []
        _payments = d.pop("payments")
        for payments_item_data in _payments:
            payments_item = PaymentRequest.from_dict(payments_item_data)

            payments.append(payments_item)

        idempotency_id = d.pop("idempotencyId", UNSET)

        originator_identification_number = d.pop("originatorIdentificationNumber", UNSET)

        _execution_date_time = d.pop("executionDateTime", UNSET)
        execution_date_time: Union[Unset, datetime.datetime]
        if isinstance(_execution_date_time, Unset):
            execution_date_time = UNSET
        else:
            execution_date_time = isoparse(_execution_date_time)

        submit_bulk_payment_request = cls(
            payments=payments,
            idempotency_id=idempotency_id,
            originator_identification_number=originator_identification_number,
            execution_date_time=execution_date_time,
        )

        submit_bulk_payment_request.additional_properties = d
        return submit_bulk_payment_request

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
