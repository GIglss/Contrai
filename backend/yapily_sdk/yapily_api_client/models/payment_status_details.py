import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.payment_status import PaymentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multi_authorisation import MultiAuthorisation
    from ..models.payment_iso_status import PaymentIsoStatus


T = TypeVar("T", bound="PaymentStatusDetails")


@_attrs_define
class PaymentStatusDetails:
    """
    Attributes:
        status (Union[Unset, PaymentStatus]): The status of the Payment. <br><br>For more information, see [Payment
            Status](/guides/payments/payment-status/)
        status_reason (Union[Unset, str]):
        status_reason_description (Union[Unset, str]):
        status_update_date (Union[Unset, datetime.datetime]):
        multi_authorisation_status (Union[Unset, MultiAuthorisation]): Details the additional levels of authorisation
            which are required from, and being managed by, the `Institution`.
        iso_status (Union[Unset, PaymentIsoStatus]): The payment status code, as denoted by a 3-letter ISO 20022 code.
    """

    status: Union[Unset, PaymentStatus] = UNSET
    status_reason: Union[Unset, str] = UNSET
    status_reason_description: Union[Unset, str] = UNSET
    status_update_date: Union[Unset, datetime.datetime] = UNSET
    multi_authorisation_status: Union[Unset, "MultiAuthorisation"] = UNSET
    iso_status: Union[Unset, "PaymentIsoStatus"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_reason = self.status_reason

        status_reason_description = self.status_reason_description

        status_update_date: Union[Unset, str] = UNSET
        if not isinstance(self.status_update_date, Unset):
            status_update_date = self.status_update_date.isoformat()

        multi_authorisation_status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.multi_authorisation_status, Unset):
            multi_authorisation_status = self.multi_authorisation_status.to_dict()

        iso_status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.iso_status, Unset):
            iso_status = self.iso_status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if status_reason is not UNSET:
            field_dict["statusReason"] = status_reason
        if status_reason_description is not UNSET:
            field_dict["statusReasonDescription"] = status_reason_description
        if status_update_date is not UNSET:
            field_dict["statusUpdateDate"] = status_update_date
        if multi_authorisation_status is not UNSET:
            field_dict["multiAuthorisationStatus"] = multi_authorisation_status
        if iso_status is not UNSET:
            field_dict["isoStatus"] = iso_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.multi_authorisation import MultiAuthorisation
        from ..models.payment_iso_status import PaymentIsoStatus

        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: Union[Unset, PaymentStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PaymentStatus(_status)

        status_reason = d.pop("statusReason", UNSET)

        status_reason_description = d.pop("statusReasonDescription", UNSET)

        _status_update_date = d.pop("statusUpdateDate", UNSET)
        status_update_date: Union[Unset, datetime.datetime]
        if isinstance(_status_update_date, Unset):
            status_update_date = UNSET
        else:
            status_update_date = isoparse(_status_update_date)

        _multi_authorisation_status = d.pop("multiAuthorisationStatus", UNSET)
        multi_authorisation_status: Union[Unset, MultiAuthorisation]
        if isinstance(_multi_authorisation_status, Unset):
            multi_authorisation_status = UNSET
        else:
            multi_authorisation_status = MultiAuthorisation.from_dict(_multi_authorisation_status)

        _iso_status = d.pop("isoStatus", UNSET)
        iso_status: Union[Unset, PaymentIsoStatus]
        if isinstance(_iso_status, Unset):
            iso_status = UNSET
        else:
            iso_status = PaymentIsoStatus.from_dict(_iso_status)

        payment_status_details = cls(
            status=status,
            status_reason=status_reason,
            status_reason_description=status_reason_description,
            status_update_date=status_update_date,
            multi_authorisation_status=multi_authorisation_status,
            iso_status=iso_status,
        )

        payment_status_details.additional_properties = d
        return payment_status_details

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
