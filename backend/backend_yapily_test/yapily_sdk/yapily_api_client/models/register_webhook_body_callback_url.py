from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.register_webhook_body_callback_url_backup import RegisterWebhookBodyCallbackUrlBackup
    from ..models.register_webhook_body_callback_url_main import RegisterWebhookBodyCallbackUrlMain


T = TypeVar("T", bound="RegisterWebhookBodyCallbackUrl")


@_attrs_define
class RegisterWebhookBodyCallbackUrl:
    """Callback URLs where events will be sent. These must not contain any query parameters.

    Attributes:
        main (RegisterWebhookBodyCallbackUrlMain): Primary URL where events will be sent. It must not contain any query
            parameters.
        backup (Union[Unset, RegisterWebhookBodyCallbackUrlBackup]): Secondary URL where events will be sent whenever
            the primary URL is not responding. It must not contain any query parameters.
    """

    main: "RegisterWebhookBodyCallbackUrlMain"
    backup: Union[Unset, "RegisterWebhookBodyCallbackUrlBackup"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        main = self.main.to_dict()

        backup: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.backup, Unset):
            backup = self.backup.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "main": main,
            }
        )
        if backup is not UNSET:
            field_dict["backup"] = backup

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.register_webhook_body_callback_url_backup import RegisterWebhookBodyCallbackUrlBackup
        from ..models.register_webhook_body_callback_url_main import RegisterWebhookBodyCallbackUrlMain

        d = dict(src_dict)
        main = RegisterWebhookBodyCallbackUrlMain.from_dict(d.pop("main"))

        _backup = d.pop("backup", UNSET)
        backup: Union[Unset, RegisterWebhookBodyCallbackUrlBackup]
        if isinstance(_backup, Unset):
            backup = UNSET
        else:
            backup = RegisterWebhookBodyCallbackUrlBackup.from_dict(_backup)

        register_webhook_body_callback_url = cls(
            main=main,
            backup=backup,
        )

        register_webhook_body_callback_url.additional_properties = d
        return register_webhook_body_callback_url

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
