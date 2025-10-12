from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.registered_webhook_callback_url_backup import RegisteredWebhookCallbackUrlBackup
    from ..models.registered_webhook_callback_url_main import RegisteredWebhookCallbackUrlMain


T = TypeVar("T", bound="RegisteredWebhookCallbackUrl")


@_attrs_define
class RegisteredWebhookCallbackUrl:
    """Callback URLs where events will be sent

    Attributes:
        main (Union[Unset, RegisteredWebhookCallbackUrlMain]): Primary URL where events will be sent
        backup (Union[Unset, RegisteredWebhookCallbackUrlBackup]): Secondary URL where events will be sent whenever the
            primary URL is not responding
    """

    main: Union[Unset, "RegisteredWebhookCallbackUrlMain"] = UNSET
    backup: Union[Unset, "RegisteredWebhookCallbackUrlBackup"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        main: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.main, Unset):
            main = self.main.to_dict()

        backup: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.backup, Unset):
            backup = self.backup.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if main is not UNSET:
            field_dict["main"] = main
        if backup is not UNSET:
            field_dict["backup"] = backup

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.registered_webhook_callback_url_backup import RegisteredWebhookCallbackUrlBackup
        from ..models.registered_webhook_callback_url_main import RegisteredWebhookCallbackUrlMain

        d = dict(src_dict)
        _main = d.pop("main", UNSET)
        main: Union[Unset, RegisteredWebhookCallbackUrlMain]
        if isinstance(_main, Unset):
            main = UNSET
        else:
            main = RegisteredWebhookCallbackUrlMain.from_dict(_main)

        _backup = d.pop("backup", UNSET)
        backup: Union[Unset, RegisteredWebhookCallbackUrlBackup]
        if isinstance(_backup, Unset):
            backup = UNSET
        else:
            backup = RegisteredWebhookCallbackUrlBackup.from_dict(_backup)

        registered_webhook_callback_url = cls(
            main=main,
            backup=backup,
        )

        registered_webhook_callback_url.additional_properties = d
        return registered_webhook_callback_url

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
