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
    from ..models.user_settings import UserSettings
    from ..models.vrp_setup_request import VRPSetupRequest


T = TypeVar("T", bound="HostedVRPConsentRequestResponse")


@_attrs_define
class HostedVRPConsentRequestResponse:
    """
    Attributes:
        id (UUID): Represents the Unique Id of the VRP consent request
        application_id (UUID): Represents the Unique Id of the `Application` the user is associated with.
        hosted_url (str): Represents the URL of Hosted UI page for the applicationId which initiates the user journey
            for the Consent. <br> URL would be appended with authToken, applicationId and userSettings.
        auth_token (str): Represents the JWT Token signed by the certificate-vault using Yapily's keys.
        created_at (datetime.datetime): Represents the date and time at which the Consent was created.
        user_id (Union[Unset, UUID]): Represents the Unique Id for the `User` assigned by Yapily.
        application_user_id (Union[Unset, str]): Represents the user-friendly reference to the `User`.
        institution_identifiers (Union[Unset, InstitutionIdentifiers]): Specifies the institution requirements for
            making the payment. Skips the bank selection screen in payment flow if the `institutionId` and
            `institutionCountryCode` are provided.
        user_settings (Union[Unset, UserSettings]): Specifies the language and location preferences of the user.
        redirect_url (Union[Unset, str]): URL of client's server to redirect the PSU after completion of the consent
            authorisation. Example: https://tpp-application.com.
        vrp_setup (Union[Unset, VRPSetupRequest]):
        authorisation_expires_at (Union[Unset, datetime.datetime]): Represents the date and time at which the auth Token
            will expire.
    """

    id: UUID
    application_id: UUID
    hosted_url: str
    auth_token: str
    created_at: datetime.datetime
    user_id: Union[Unset, UUID] = UNSET
    application_user_id: Union[Unset, str] = UNSET
    institution_identifiers: Union[Unset, "InstitutionIdentifiers"] = UNSET
    user_settings: Union[Unset, "UserSettings"] = UNSET
    redirect_url: Union[Unset, str] = UNSET
    vrp_setup: Union[Unset, "VRPSetupRequest"] = UNSET
    authorisation_expires_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        application_id = str(self.application_id)

        hosted_url = self.hosted_url

        auth_token = self.auth_token

        created_at = self.created_at.isoformat()

        user_id: Union[Unset, str] = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        application_user_id = self.application_user_id

        institution_identifiers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.institution_identifiers, Unset):
            institution_identifiers = self.institution_identifiers.to_dict()

        user_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user_settings, Unset):
            user_settings = self.user_settings.to_dict()

        redirect_url = self.redirect_url

        vrp_setup: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vrp_setup, Unset):
            vrp_setup = self.vrp_setup.to_dict()

        authorisation_expires_at: Union[Unset, str] = UNSET
        if not isinstance(self.authorisation_expires_at, Unset):
            authorisation_expires_at = self.authorisation_expires_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "applicationId": application_id,
                "hostedUrl": hosted_url,
                "authToken": auth_token,
                "createdAt": created_at,
            }
        )
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if application_user_id is not UNSET:
            field_dict["applicationUserId"] = application_user_id
        if institution_identifiers is not UNSET:
            field_dict["institutionIdentifiers"] = institution_identifiers
        if user_settings is not UNSET:
            field_dict["userSettings"] = user_settings
        if redirect_url is not UNSET:
            field_dict["redirectUrl"] = redirect_url
        if vrp_setup is not UNSET:
            field_dict["vrpSetup"] = vrp_setup
        if authorisation_expires_at is not UNSET:
            field_dict["authorisationExpiresAt"] = authorisation_expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.institution_identifiers import InstitutionIdentifiers
        from ..models.user_settings import UserSettings
        from ..models.vrp_setup_request import VRPSetupRequest

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        application_id = UUID(d.pop("applicationId"))

        hosted_url = d.pop("hostedUrl")

        auth_token = d.pop("authToken")

        created_at = isoparse(d.pop("createdAt"))

        _user_id = d.pop("userId", UNSET)
        user_id: Union[Unset, UUID]
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        application_user_id = d.pop("applicationUserId", UNSET)

        _institution_identifiers = d.pop("institutionIdentifiers", UNSET)
        institution_identifiers: Union[Unset, InstitutionIdentifiers]
        if isinstance(_institution_identifiers, Unset):
            institution_identifiers = UNSET
        else:
            institution_identifiers = InstitutionIdentifiers.from_dict(_institution_identifiers)

        _user_settings = d.pop("userSettings", UNSET)
        user_settings: Union[Unset, UserSettings]
        if isinstance(_user_settings, Unset):
            user_settings = UNSET
        else:
            user_settings = UserSettings.from_dict(_user_settings)

        redirect_url = d.pop("redirectUrl", UNSET)

        _vrp_setup = d.pop("vrpSetup", UNSET)
        vrp_setup: Union[Unset, VRPSetupRequest]
        if isinstance(_vrp_setup, Unset):
            vrp_setup = UNSET
        else:
            vrp_setup = VRPSetupRequest.from_dict(_vrp_setup)

        _authorisation_expires_at = d.pop("authorisationExpiresAt", UNSET)
        authorisation_expires_at: Union[Unset, datetime.datetime]
        if isinstance(_authorisation_expires_at, Unset):
            authorisation_expires_at = UNSET
        else:
            authorisation_expires_at = isoparse(_authorisation_expires_at)

        hosted_vrp_consent_request_response = cls(
            id=id,
            application_id=application_id,
            hosted_url=hosted_url,
            auth_token=auth_token,
            created_at=created_at,
            user_id=user_id,
            application_user_id=application_user_id,
            institution_identifiers=institution_identifiers,
            user_settings=user_settings,
            redirect_url=redirect_url,
            vrp_setup=vrp_setup,
            authorisation_expires_at=authorisation_expires_at,
        )

        hosted_vrp_consent_request_response.additional_properties = d
        return hosted_vrp_consent_request_response

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
