import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.institution_consent import InstitutionConsent


T = TypeVar("T", bound="ApplicationUser")


@_attrs_define
class ApplicationUser:
    """Information about a user of an application.

    Attributes:
        uuid (Union[Unset, UUID]): A unique identifier for the 'User' assigned by Yapily.
        application_uuid (Union[Unset, UUID]): Unique identifier of the application the user is associated with.
        application_user_id (Union[Unset, str]): __Conditional__. The user-friendly reference to the `User`.
        reference_id (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]): Date and time of when the user was created.
        institution_consents (Union[Unset, list['InstitutionConsent']]):
        vop_opt_out (Union[Unset, bool]): __Optional__. A flag to indicate whether the user has opted out of VOP.
            Default: False.
    """

    uuid: Union[Unset, UUID] = UNSET
    application_uuid: Union[Unset, UUID] = UNSET
    application_user_id: Union[Unset, str] = UNSET
    reference_id: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    institution_consents: Union[Unset, list["InstitutionConsent"]] = UNSET
    vop_opt_out: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid: Union[Unset, str] = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        application_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.application_uuid, Unset):
            application_uuid = str(self.application_uuid)

        application_user_id = self.application_user_id

        reference_id = self.reference_id

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        institution_consents: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.institution_consents, Unset):
            institution_consents = []
            for institution_consents_item_data in self.institution_consents:
                institution_consents_item = institution_consents_item_data.to_dict()
                institution_consents.append(institution_consents_item)

        vop_opt_out = self.vop_opt_out

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if application_uuid is not UNSET:
            field_dict["applicationUuid"] = application_uuid
        if application_user_id is not UNSET:
            field_dict["applicationUserId"] = application_user_id
        if reference_id is not UNSET:
            field_dict["referenceId"] = reference_id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if institution_consents is not UNSET:
            field_dict["institutionConsents"] = institution_consents
        if vop_opt_out is not UNSET:
            field_dict["vopOptOut"] = vop_opt_out

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.institution_consent import InstitutionConsent

        d = dict(src_dict)
        _uuid = d.pop("uuid", UNSET)
        uuid: Union[Unset, UUID]
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        _application_uuid = d.pop("applicationUuid", UNSET)
        application_uuid: Union[Unset, UUID]
        if isinstance(_application_uuid, Unset):
            application_uuid = UNSET
        else:
            application_uuid = UUID(_application_uuid)

        application_user_id = d.pop("applicationUserId", UNSET)

        reference_id = d.pop("referenceId", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        institution_consents = []
        _institution_consents = d.pop("institutionConsents", UNSET)
        for institution_consents_item_data in _institution_consents or []:
            institution_consents_item = InstitutionConsent.from_dict(institution_consents_item_data)

            institution_consents.append(institution_consents_item)

        vop_opt_out = d.pop("vopOptOut", UNSET)

        application_user = cls(
            uuid=uuid,
            application_uuid=application_uuid,
            application_user_id=application_user_id,
            reference_id=reference_id,
            created_at=created_at,
            institution_consents=institution_consents,
            vop_opt_out=vop_opt_out,
        )

        application_user.additional_properties = d
        return application_user

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
