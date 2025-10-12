from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.notification import Notification


T = TypeVar("T", bound="RequestToCreateASubscriptionForNotifications")


@_attrs_define
class RequestToCreateASubscriptionForNotifications:
    """
    Attributes:
        event_type_id (str): Unique identifier of the event type (for which notifications will be sent).<br><br>Allowed
            values: payment.status, payment.status.completed, payment.isoStatus  Example: payment.status.completed.
        notification (Notification): Subscription details for how and where to receive notifications.
    """

    event_type_id: str
    notification: "Notification"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type_id = self.event_type_id

        notification = self.notification.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventTypeId": event_type_id,
                "notification": notification,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification import Notification

        d = dict(src_dict)
        event_type_id = d.pop("eventTypeId")

        notification = Notification.from_dict(d.pop("notification"))

        request_to_create_a_subscription_for_notifications = cls(
            event_type_id=event_type_id,
            notification=notification,
        )

        request_to_create_a_subscription_for_notifications.additional_properties = d
        return request_to_create_a_subscription_for_notifications

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
