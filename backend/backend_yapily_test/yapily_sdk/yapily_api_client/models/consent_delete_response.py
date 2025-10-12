import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.delete_status_enum import DeleteStatusEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConsentDeleteResponse")


@_attrs_define
class ConsentDeleteResponse:
    """
    Attributes:
        id (Union[Unset, UUID]): __Conditional__. User-friendly identifier of the `User` that provides authorisation. If
            a `User` with the specified `applicationUserId` exists, it will be used otherwise, a new `User` with the
            specified `applicationUserId` will be created and used. Either the `userUuid` or `applicationUserId` must be
            provided.
        delete_status (Union[Unset, DeleteStatusEnum]): Indicates the outcome of the delete request.
        institution_id (Union[Unset, str]): __Mandatory__. The `Institution` the authorisation request is sent to.
        institution_consent_id (Union[Unset, str]): Identification of the consent at the Institution.
        creation_date (Union[Unset, datetime.datetime]): Date and time of when the consent was authorised.
    """

    id: Union[Unset, UUID] = UNSET
    delete_status: Union[Unset, DeleteStatusEnum] = UNSET
    institution_id: Union[Unset, str] = UNSET
    institution_consent_id: Union[Unset, str] = UNSET
    creation_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        delete_status: Union[Unset, str] = UNSET
        if not isinstance(self.delete_status, Unset):
            delete_status = self.delete_status.value

        institution_id = self.institution_id

        institution_consent_id = self.institution_consent_id

        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if delete_status is not UNSET:
            field_dict["deleteStatus"] = delete_status
        if institution_id is not UNSET:
            field_dict["institutionId"] = institution_id
        if institution_consent_id is not UNSET:
            field_dict["institutionConsentId"] = institution_consent_id
        if creation_date is not UNSET:
            field_dict["creationDate"] = creation_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _delete_status = d.pop("deleteStatus", UNSET)
        delete_status: Union[Unset, DeleteStatusEnum]
        if isinstance(_delete_status, Unset):
            delete_status = UNSET
        else:
            delete_status = DeleteStatusEnum(_delete_status)

        institution_id = d.pop("institutionId", UNSET)

        institution_consent_id = d.pop("institutionConsentId", UNSET)

        _creation_date = d.pop("creationDate", UNSET)
        creation_date: Union[Unset, datetime.datetime]
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        consent_delete_response = cls(
            id=id,
            delete_status=delete_status,
            institution_id=institution_id,
            institution_consent_id=institution_consent_id,
            creation_date=creation_date,
        )

        consent_delete_response.additional_properties = d
        return consent_delete_response

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
