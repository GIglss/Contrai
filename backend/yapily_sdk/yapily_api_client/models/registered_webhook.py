from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.registered_webhook_callback_url import RegisteredWebhookCallbackUrl
    from ..models.webhook_metadata import WebhookMetadata


T = TypeVar("T", bound="RegisteredWebhook")


@_attrs_define
class RegisteredWebhook:
    """
    Attributes:
        id (Union[Unset, UUID]): This webhook's ID, used to update or remove the webhook
        application_id (Union[Unset, UUID]):
        categories (Union[Unset, list[str]]):
        callback_url (Union[Unset, RegisteredWebhookCallbackUrl]): Callback URLs where events will be sent
        metadata (Union[Unset, WebhookMetadata]): Any data (under 10kB total) that should be associated with the
            Webhook. A copy of this data will be returned on every Webhook trigger.
    """

    id: Union[Unset, UUID] = UNSET
    application_id: Union[Unset, UUID] = UNSET
    categories: Union[Unset, list[str]] = UNSET
    callback_url: Union[Unset, "RegisteredWebhookCallbackUrl"] = UNSET
    metadata: Union[Unset, "WebhookMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        application_id: Union[Unset, str] = UNSET
        if not isinstance(self.application_id, Unset):
            application_id = str(self.application_id)

        categories: Union[Unset, list[str]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories

        callback_url: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.callback_url, Unset):
            callback_url = self.callback_url.to_dict()

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if categories is not UNSET:
            field_dict["categories"] = categories
        if callback_url is not UNSET:
            field_dict["callbackUrl"] = callback_url
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.registered_webhook_callback_url import RegisteredWebhookCallbackUrl
        from ..models.webhook_metadata import WebhookMetadata

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _application_id = d.pop("applicationId", UNSET)
        application_id: Union[Unset, UUID]
        if isinstance(_application_id, Unset):
            application_id = UNSET
        else:
            application_id = UUID(_application_id)

        categories = cast(list[str], d.pop("categories", UNSET))

        _callback_url = d.pop("callbackUrl", UNSET)
        callback_url: Union[Unset, RegisteredWebhookCallbackUrl]
        if isinstance(_callback_url, Unset):
            callback_url = UNSET
        else:
            callback_url = RegisteredWebhookCallbackUrl.from_dict(_callback_url)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, WebhookMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = WebhookMetadata.from_dict(_metadata)

        registered_webhook = cls(
            id=id,
            application_id=application_id,
            categories=categories,
            callback_url=callback_url,
            metadata=metadata,
        )

        registered_webhook.additional_properties = d
        return registered_webhook

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
