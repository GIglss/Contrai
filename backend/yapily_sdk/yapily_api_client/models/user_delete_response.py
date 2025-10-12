import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.delete_status_enum import DeleteStatusEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.consent_delete_response import ConsentDeleteResponse


T = TypeVar("T", bound="UserDeleteResponse")


@_attrs_define
class UserDeleteResponse:
    """Deletion of the user. Includes the user profile and all associate consents.

    Attributes:
        id (Union[Unset, str]): Unique identifier of the user.
        delete_status (Union[Unset, DeleteStatusEnum]): Indicates the outcome of the delete request.
        creation_date (Union[Unset, datetime.datetime]): Date and time that the user was created.
        user_consents (Union[Unset, list['ConsentDeleteResponse']]):
    """

    id: Union[Unset, str] = UNSET
    delete_status: Union[Unset, DeleteStatusEnum] = UNSET
    creation_date: Union[Unset, datetime.datetime] = UNSET
    user_consents: Union[Unset, list["ConsentDeleteResponse"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        delete_status: Union[Unset, str] = UNSET
        if not isinstance(self.delete_status, Unset):
            delete_status = self.delete_status.value

        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        user_consents: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.user_consents, Unset):
            user_consents = []
            for user_consents_item_data in self.user_consents:
                user_consents_item = user_consents_item_data.to_dict()
                user_consents.append(user_consents_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if delete_status is not UNSET:
            field_dict["deleteStatus"] = delete_status
        if creation_date is not UNSET:
            field_dict["creationDate"] = creation_date
        if user_consents is not UNSET:
            field_dict["userConsents"] = user_consents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.consent_delete_response import ConsentDeleteResponse

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _delete_status = d.pop("deleteStatus", UNSET)
        delete_status: Union[Unset, DeleteStatusEnum]
        if isinstance(_delete_status, Unset):
            delete_status = UNSET
        else:
            delete_status = DeleteStatusEnum(_delete_status)

        _creation_date = d.pop("creationDate", UNSET)
        creation_date: Union[Unset, datetime.datetime]
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        user_consents = []
        _user_consents = d.pop("userConsents", UNSET)
        for user_consents_item_data in _user_consents or []:
            user_consents_item = ConsentDeleteResponse.from_dict(user_consents_item_data)

            user_consents.append(user_consents_item)

        user_delete_response = cls(
            id=id,
            delete_status=delete_status,
            creation_date=creation_date,
            user_consents=user_consents,
        )

        user_delete_response.additional_properties = d
        return user_delete_response

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
