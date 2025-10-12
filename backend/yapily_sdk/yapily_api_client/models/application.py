import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.institution import Institution
    from ..models.media import Media


T = TypeVar("T", bound="Application")


@_attrs_define
class Application:
    """Information about the application.

    Attributes:
        uuid (Union[Unset, UUID]): Unique identification for the `Application` as assigned by Yapily.
        name (Union[Unset, str]): The individual name of the `Application`.
        active (Union[Unset, bool]): States whether an `Application` is active.
        auth_callbacks (Union[Unset, list[str]]):
        institutions (Union[Unset, list['Institution']]):
        media (Union[Unset, list['Media']]):
        created (Union[Unset, datetime.datetime]): Date and time of when the application was created.
        updated (Union[Unset, datetime.datetime]): Date and time of when the application was last updated.
    """

    uuid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    active: Union[Unset, bool] = UNSET
    auth_callbacks: Union[Unset, list[str]] = UNSET
    institutions: Union[Unset, list["Institution"]] = UNSET
    media: Union[Unset, list["Media"]] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid: Union[Unset, str] = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        name = self.name

        active = self.active

        auth_callbacks: Union[Unset, list[str]] = UNSET
        if not isinstance(self.auth_callbacks, Unset):
            auth_callbacks = self.auth_callbacks

        institutions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.institutions, Unset):
            institutions = []
            for institutions_item_data in self.institutions:
                institutions_item = institutions_item_data.to_dict()
                institutions.append(institutions_item)

        media: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.media, Unset):
            media = []
            for media_item_data in self.media:
                media_item = media_item_data.to_dict()
                media.append(media_item)

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if active is not UNSET:
            field_dict["active"] = active
        if auth_callbacks is not UNSET:
            field_dict["authCallbacks"] = auth_callbacks
        if institutions is not UNSET:
            field_dict["institutions"] = institutions
        if media is not UNSET:
            field_dict["media"] = media
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.institution import Institution
        from ..models.media import Media

        d = dict(src_dict)
        _uuid = d.pop("uuid", UNSET)
        uuid: Union[Unset, UUID]
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        name = d.pop("name", UNSET)

        active = d.pop("active", UNSET)

        auth_callbacks = cast(list[str], d.pop("authCallbacks", UNSET))

        institutions = []
        _institutions = d.pop("institutions", UNSET)
        for institutions_item_data in _institutions or []:
            institutions_item = Institution.from_dict(institutions_item_data)

            institutions.append(institutions_item)

        media = []
        _media = d.pop("media", UNSET)
        for media_item_data in _media or []:
            media_item = Media.from_dict(media_item_data)

            media.append(media_item)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, datetime.datetime]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        application = cls(
            uuid=uuid,
            name=name,
            active=active,
            auth_callbacks=auth_callbacks,
            institutions=institutions,
            media=media,
            created=created,
            updated=updated,
        )

        application.additional_properties = d
        return application

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
