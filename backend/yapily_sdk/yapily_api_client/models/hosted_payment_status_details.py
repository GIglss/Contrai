import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.payment_status import PaymentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hosted_payment_iso_status import HostedPaymentIsoStatus


T = TypeVar("T", bound="HostedPaymentStatusDetails")


@_attrs_define
class HostedPaymentStatusDetails:
    """The status of the payment.

    Attributes:
        status (Union[Unset, PaymentStatus]): The status of the Payment. <br><br>For more information, see [Payment
            Status](/guides/payments/payment-status/)
        status_update_date (Union[Unset, datetime.datetime]): Date and time the status was updated.
        iso_status (Union[Unset, HostedPaymentIsoStatus]): The ISO status of the payment.
    """

    status: Union[Unset, PaymentStatus] = UNSET
    status_update_date: Union[Unset, datetime.datetime] = UNSET
    iso_status: Union[Unset, "HostedPaymentIsoStatus"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_update_date: Union[Unset, str] = UNSET
        if not isinstance(self.status_update_date, Unset):
            status_update_date = self.status_update_date.isoformat()

        iso_status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.iso_status, Unset):
            iso_status = self.iso_status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if status_update_date is not UNSET:
            field_dict["statusUpdateDate"] = status_update_date
        if iso_status is not UNSET:
            field_dict["isoStatus"] = iso_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hosted_payment_iso_status import HostedPaymentIsoStatus

        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: Union[Unset, PaymentStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PaymentStatus(_status)

        _status_update_date = d.pop("statusUpdateDate", UNSET)
        status_update_date: Union[Unset, datetime.datetime]
        if isinstance(_status_update_date, Unset):
            status_update_date = UNSET
        else:
            status_update_date = isoparse(_status_update_date)

        _iso_status = d.pop("isoStatus", UNSET)
        iso_status: Union[Unset, HostedPaymentIsoStatus]
        if isinstance(_iso_status, Unset):
            iso_status = UNSET
        else:
            iso_status = HostedPaymentIsoStatus.from_dict(_iso_status)

        hosted_payment_status_details = cls(
            status=status,
            status_update_date=status_update_date,
            iso_status=iso_status,
        )

        hosted_payment_status_details.additional_properties = d
        return hosted_payment_status_details

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
