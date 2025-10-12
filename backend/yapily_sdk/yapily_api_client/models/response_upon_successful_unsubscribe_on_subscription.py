import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.delete_status_enum import DeleteStatusEnum

T = TypeVar("T", bound="ResponseUponSuccessfulUnsubscribeOnSubscription")


@_attrs_define
class ResponseUponSuccessfulUnsubscribeOnSubscription:
    """
    Attributes:
        event_type_id (str): Unique identifier of the event type (for which notifications will be sent) Example:
            payment.status.completed.
        application_id (UUID): Application related to event subscription. Example: 2698db90-6635-4f76-b673-5ce8e2aeda0e.
        created (datetime.datetime): Creation datetime of event subscription. Example: 28-07-2021 15:47:03.
        delete_status (DeleteStatusEnum): Indicates the outcome of the delete request.
    """

    event_type_id: str
    application_id: UUID
    created: datetime.datetime
    delete_status: DeleteStatusEnum
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type_id = self.event_type_id

        application_id = str(self.application_id)

        created = self.created.isoformat()

        delete_status = self.delete_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventTypeId": event_type_id,
                "applicationId": application_id,
                "created": created,
                "deleteStatus": delete_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_type_id = d.pop("eventTypeId")

        application_id = UUID(d.pop("applicationId"))

        created = isoparse(d.pop("created"))

        delete_status = DeleteStatusEnum(d.pop("deleteStatus"))

        response_upon_successful_unsubscribe_on_subscription = cls(
            event_type_id=event_type_id,
            application_id=application_id,
            created=created,
            delete_status=delete_status,
        )

        response_upon_successful_unsubscribe_on_subscription.additional_properties = d
        return response_upon_successful_unsubscribe_on_subscription

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
