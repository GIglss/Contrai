from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.register_webhook_body_callback_url import RegisterWebhookBodyCallbackUrl
    from ..models.webhook_metadata import WebhookMetadata


T = TypeVar("T", bound="RegisterWebhookBody")


@_attrs_define
class RegisterWebhookBody:
    """
    Attributes:
        application_id (UUID):
        categories (list[str]): One or more event categories for which the webhook will be triggered
        callback_url (RegisterWebhookBodyCallbackUrl): Callback URLs where events will be sent. These must not contain
            any query parameters.
        metadata (Union[Unset, WebhookMetadata]): Any data (under 10kB total) that should be associated with the
            Webhook. A copy of this data will be returned on every Webhook trigger.
    """

    application_id: UUID
    categories: list[str]
    callback_url: "RegisterWebhookBodyCallbackUrl"
    metadata: Union[Unset, "WebhookMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_id = str(self.application_id)

        categories = self.categories

        callback_url = self.callback_url.to_dict()

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "applicationId": application_id,
                "categories": categories,
                "callbackUrl": callback_url,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.register_webhook_body_callback_url import RegisterWebhookBodyCallbackUrl
        from ..models.webhook_metadata import WebhookMetadata

        d = dict(src_dict)
        application_id = UUID(d.pop("applicationId"))

        categories = cast(list[str], d.pop("categories"))

        callback_url = RegisterWebhookBodyCallbackUrl.from_dict(d.pop("callbackUrl"))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, WebhookMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = WebhookMetadata.from_dict(_metadata)

        register_webhook_body = cls(
            application_id=application_id,
            categories=categories,
            callback_url=callback_url,
            metadata=metadata,
        )

        register_webhook_body.additional_properties = d
        return register_webhook_body

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
