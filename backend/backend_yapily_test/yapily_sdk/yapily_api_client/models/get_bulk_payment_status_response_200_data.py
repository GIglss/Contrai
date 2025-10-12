import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_bulk_payment_status_response_200_data_status_details import (
        GetBulkPaymentStatusResponse200DataStatusDetails,
    )


T = TypeVar("T", bound="GetBulkPaymentStatusResponse200Data")


@_attrs_define
class GetBulkPaymentStatusResponse200Data:
    """
    Attributes:
        id (Union[Unset, str]): Unique identifier of the Bulk Payment
        consent_id (Union[Unset, str]): Identification of the consent.
        status_details (Union[Unset, GetBulkPaymentStatusResponse200DataStatusDetails]):
        created_at (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, str] = UNSET
    consent_id: Union[Unset, str] = UNSET
    status_details: Union[Unset, "GetBulkPaymentStatusResponse200DataStatusDetails"] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        consent_id = self.consent_id

        status_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status_details, Unset):
            status_details = self.status_details.to_dict()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if consent_id is not UNSET:
            field_dict["consentId"] = consent_id
        if status_details is not UNSET:
            field_dict["statusDetails"] = status_details
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_bulk_payment_status_response_200_data_status_details import (
            GetBulkPaymentStatusResponse200DataStatusDetails,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        consent_id = d.pop("consentId", UNSET)

        _status_details = d.pop("statusDetails", UNSET)
        status_details: Union[Unset, GetBulkPaymentStatusResponse200DataStatusDetails]
        if isinstance(_status_details, Unset):
            status_details = UNSET
        else:
            status_details = GetBulkPaymentStatusResponse200DataStatusDetails.from_dict(_status_details)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        get_bulk_payment_status_response_200_data = cls(
            id=id,
            consent_id=consent_id,
            status_details=status_details,
            created_at=created_at,
        )

        get_bulk_payment_status_response_200_data.additional_properties = d
        return get_bulk_payment_status_response_200_data

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
