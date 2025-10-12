from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.notification import Notification


T = TypeVar("T", bound="ResponseOnSuccessfulCreationOfEventSubscription")


@_attrs_define
class ResponseOnSuccessfulCreationOfEventSubscription:
    """
    Attributes:
        event_type_id (str): Unique identifier of the event type (for which notifications will be sent) Example:
            payment.status.completed.
        application_id (UUID): Application related to event subscription. Example: 2698db90-6635-4f76-b673-5ce8e2aeda0e.
        created (str): Creation date of event subscription. Example: 28-07-2021 15:47:03.
        notification (Notification): Subscription details for how and where to receive notifications.
    """

    event_type_id: str
    application_id: UUID
    created: str
    notification: "Notification"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type_id = self.event_type_id

        application_id = str(self.application_id)

        created = self.created

        notification = self.notification.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventTypeId": event_type_id,
                "applicationId": application_id,
                "created": created,
                "notification": notification,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification import Notification

        d = dict(src_dict)
        event_type_id = d.pop("eventTypeId")

        application_id = UUID(d.pop("applicationId"))

        created = d.pop("created")

        notification = Notification.from_dict(d.pop("notification"))

        response_on_successful_creation_of_event_subscription = cls(
            event_type_id=event_type_id,
            application_id=application_id,
            created=created,
            notification=notification,
        )

        response_on_successful_creation_of_event_subscription.additional_properties = d
        return response_on_successful_creation_of_event_subscription

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
