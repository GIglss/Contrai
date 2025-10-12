import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hosted_account_request_details_response import HostedAccountRequestDetailsResponse
    from ..models.institution_identifiers_response import InstitutionIdentifiersResponse
    from ..models.user_settings import UserSettings


T = TypeVar("T", bound="HostedConsentRequestResponse")


@_attrs_define
class HostedConsentRequestResponse:
    """
    Attributes:
        consent_request_id (Union[Unset, UUID]): Unique Id of the consent request.
        user_id (Union[Unset, UUID]): Unique Id for the `User` assigned by Yapily.
        application_user_id (Union[Unset, str]): Your reference to the `User`.
        application_id (Union[Unset, UUID]): Unique Id of the `Application` the user is associated with.
        institution_identifiers (Union[Unset, InstitutionIdentifiersResponse]): Specifies the institution selected for
            making the payment.
        user_settings (Union[Unset, UserSettings]): Specifies the language and location preferences of the user.
        redirect_url (Union[Unset, str]): URL of consent server to redirect the user after completion of the consent
            flow. Example: https://tpp-application.com.
        account_request_details (Union[Unset, HostedAccountRequestDetailsResponse]): Details of the Account Request.
        hosted_url (Union[Unset, str]): The URL of Hosted UI page for the applicationId which initiates the user journey
            for the consent. <br> URL would be appended with authToken, applicationId and userSettings.
        created_at (Union[Unset, datetime.datetime]): The date and time at which the consent was created.
        authorisation_expires_at (Union[Unset, datetime.datetime]): The date and time at which the auth Token will
            expire.
    """

    consent_request_id: Union[Unset, UUID] = UNSET
    user_id: Union[Unset, UUID] = UNSET
    application_user_id: Union[Unset, str] = UNSET
    application_id: Union[Unset, UUID] = UNSET
    institution_identifiers: Union[Unset, "InstitutionIdentifiersResponse"] = UNSET
    user_settings: Union[Unset, "UserSettings"] = UNSET
    redirect_url: Union[Unset, str] = UNSET
    account_request_details: Union[Unset, "HostedAccountRequestDetailsResponse"] = UNSET
    hosted_url: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    authorisation_expires_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        consent_request_id: Union[Unset, str] = UNSET
        if not isinstance(self.consent_request_id, Unset):
            consent_request_id = str(self.consent_request_id)

        user_id: Union[Unset, str] = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        application_user_id = self.application_user_id

        application_id: Union[Unset, str] = UNSET
        if not isinstance(self.application_id, Unset):
            application_id = str(self.application_id)

        institution_identifiers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.institution_identifiers, Unset):
            institution_identifiers = self.institution_identifiers.to_dict()

        user_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user_settings, Unset):
            user_settings = self.user_settings.to_dict()

        redirect_url = self.redirect_url

        account_request_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.account_request_details, Unset):
            account_request_details = self.account_request_details.to_dict()

        hosted_url = self.hosted_url

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        authorisation_expires_at: Union[Unset, str] = UNSET
        if not isinstance(self.authorisation_expires_at, Unset):
            authorisation_expires_at = self.authorisation_expires_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if consent_request_id is not UNSET:
            field_dict["consentRequestId"] = consent_request_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if application_user_id is not UNSET:
            field_dict["applicationUserId"] = application_user_id
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if institution_identifiers is not UNSET:
            field_dict["institutionIdentifiers"] = institution_identifiers
        if user_settings is not UNSET:
            field_dict["userSettings"] = user_settings
        if redirect_url is not UNSET:
            field_dict["redirectUrl"] = redirect_url
        if account_request_details is not UNSET:
            field_dict["accountRequestDetails"] = account_request_details
        if hosted_url is not UNSET:
            field_dict["hostedUrl"] = hosted_url
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if authorisation_expires_at is not UNSET:
            field_dict["authorisationExpiresAt"] = authorisation_expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hosted_account_request_details_response import HostedAccountRequestDetailsResponse
        from ..models.institution_identifiers_response import InstitutionIdentifiersResponse
        from ..models.user_settings import UserSettings

        d = dict(src_dict)
        _consent_request_id = d.pop("consentRequestId", UNSET)
        consent_request_id: Union[Unset, UUID]
        if isinstance(_consent_request_id, Unset):
            consent_request_id = UNSET
        else:
            consent_request_id = UUID(_consent_request_id)

        _user_id = d.pop("userId", UNSET)
        user_id: Union[Unset, UUID]
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        application_user_id = d.pop("applicationUserId", UNSET)

        _application_id = d.pop("applicationId", UNSET)
        application_id: Union[Unset, UUID]
        if isinstance(_application_id, Unset):
            application_id = UNSET
        else:
            application_id = UUID(_application_id)

        _institution_identifiers = d.pop("institutionIdentifiers", UNSET)
        institution_identifiers: Union[Unset, InstitutionIdentifiersResponse]
        if isinstance(_institution_identifiers, Unset):
            institution_identifiers = UNSET
        else:
            institution_identifiers = InstitutionIdentifiersResponse.from_dict(_institution_identifiers)

        _user_settings = d.pop("userSettings", UNSET)
        user_settings: Union[Unset, UserSettings]
        if isinstance(_user_settings, Unset):
            user_settings = UNSET
        else:
            user_settings = UserSettings.from_dict(_user_settings)

        redirect_url = d.pop("redirectUrl", UNSET)

        _account_request_details = d.pop("accountRequestDetails", UNSET)
        account_request_details: Union[Unset, HostedAccountRequestDetailsResponse]
        if isinstance(_account_request_details, Unset):
            account_request_details = UNSET
        else:
            account_request_details = HostedAccountRequestDetailsResponse.from_dict(_account_request_details)

        hosted_url = d.pop("hostedUrl", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _authorisation_expires_at = d.pop("authorisationExpiresAt", UNSET)
        authorisation_expires_at: Union[Unset, datetime.datetime]
        if isinstance(_authorisation_expires_at, Unset):
            authorisation_expires_at = UNSET
        else:
            authorisation_expires_at = isoparse(_authorisation_expires_at)

        hosted_consent_request_response = cls(
            consent_request_id=consent_request_id,
            user_id=user_id,
            application_user_id=application_user_id,
            application_id=application_id,
            institution_identifiers=institution_identifiers,
            user_settings=user_settings,
            redirect_url=redirect_url,
            account_request_details=account_request_details,
            hosted_url=hosted_url,
            created_at=created_at,
            authorisation_expires_at=authorisation_expires_at,
        )

        hosted_consent_request_response.additional_properties = d
        return hosted_consent_request_response

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
