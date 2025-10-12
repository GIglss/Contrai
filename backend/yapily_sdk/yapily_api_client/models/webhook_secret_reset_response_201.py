from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata import Metadata
    from ..models.webhook_secret_reset_response_201_data import WebhookSecretResetResponse201Data


T = TypeVar("T", bound="WebhookSecretResetResponse201")


@_attrs_define
class WebhookSecretResetResponse201:
    """
    Attributes:
        metadata (Union[Unset, Metadata]):
        data (Union[Unset, WebhookSecretResetResponse201Data]):
    """

    metadata: Union[Unset, "Metadata"] = UNSET
    data: Union[Unset, "WebhookSecretResetResponse201Data"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata import Metadata
        from ..models.webhook_secret_reset_response_201_data import WebhookSecretResetResponse201Data

        d = dict(src_dict)
        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = Metadata.from_dict(_metadata)

        _data = d.pop("data", UNSET)
        data: Union[Unset, WebhookSecretResetResponse201Data]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = WebhookSecretResetResponse201Data.from_dict(_data)

        webhook_secret_reset_response_201 = cls(
            metadata=metadata,
            data=data,
        )

        webhook_secret_reset_response_201.additional_properties = d
        return webhook_secret_reset_response_201

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
