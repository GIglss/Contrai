import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.institution_identifiers import InstitutionIdentifiers
    from ..models.vrp_setup_request import VRPSetupRequest


T = TypeVar("T", bound="GetHostedVRPConsentsResponseItem")


@_attrs_define
class GetHostedVRPConsentsResponseItem:
    """
    Attributes:
        id (UUID): Represents the Unique Id of the VRP consent request
        application_id (UUID): Represents the Unique Id of the `Application` the user is associated with.
        institution_identifiers (Union[Unset, InstitutionIdentifiers]): Specifies the institution requirements for
            making the payment. Skips the bank selection screen in payment flow if the `institutionId` and
            `institutionCountryCode` are provided.
        vrp_setup (Union[Unset, VRPSetupRequest]):
        updated_at (Union[Unset, datetime.datetime]): Represents the date and time at which the Consent was updated.
        consent_status (Union[Unset, str]): Current status of the authorisation. Can be one of [AWAITING_AUTHORIZATION,
            AUTHORIZED, REJECTED, REVOKED, FAILED, EXPIRED]
    """

    id: UUID
    application_id: UUID
    institution_identifiers: Union[Unset, "InstitutionIdentifiers"] = UNSET
    vrp_setup: Union[Unset, "VRPSetupRequest"] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    consent_status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        application_id = str(self.application_id)

        institution_identifiers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.institution_identifiers, Unset):
            institution_identifiers = self.institution_identifiers.to_dict()

        vrp_setup: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vrp_setup, Unset):
            vrp_setup = self.vrp_setup.to_dict()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        consent_status = self.consent_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "applicationId": application_id,
            }
        )
        if institution_identifiers is not UNSET:
            field_dict["institutionIdentifiers"] = institution_identifiers
        if vrp_setup is not UNSET:
            field_dict["vrpSetup"] = vrp_setup
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if consent_status is not UNSET:
            field_dict["consentStatus"] = consent_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.institution_identifiers import InstitutionIdentifiers
        from ..models.vrp_setup_request import VRPSetupRequest

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        application_id = UUID(d.pop("applicationId"))

        _institution_identifiers = d.pop("institutionIdentifiers", UNSET)
        institution_identifiers: Union[Unset, InstitutionIdentifiers]
        if isinstance(_institution_identifiers, Unset):
            institution_identifiers = UNSET
        else:
            institution_identifiers = InstitutionIdentifiers.from_dict(_institution_identifiers)

        _vrp_setup = d.pop("vrpSetup", UNSET)
        vrp_setup: Union[Unset, VRPSetupRequest]
        if isinstance(_vrp_setup, Unset):
            vrp_setup = UNSET
        else:
            vrp_setup = VRPSetupRequest.from_dict(_vrp_setup)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        consent_status = d.pop("consentStatus", UNSET)

        get_hosted_vrp_consents_response_item = cls(
            id=id,
            application_id=application_id,
            institution_identifiers=institution_identifiers,
            vrp_setup=vrp_setup,
            updated_at=updated_at,
            consent_status=consent_status,
        )

        get_hosted_vrp_consents_response_item.additional_properties = d
        return get_hosted_vrp_consents_response_item

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
