from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.institution_identifiers import InstitutionIdentifiers
    from ..models.user_settings import UserSettings
    from ..models.vrp_setup_request import VRPSetupRequest


T = TypeVar("T", bound="CreateHostedVRPConsentRequest")


@_attrs_define
class CreateHostedVRPConsentRequest:
    """
    Attributes:
        institution_identifiers (InstitutionIdentifiers): Specifies the institution requirements for making the payment.
            Skips the bank selection screen in payment flow if the `institutionId` and `institutionCountryCode` are
            provided.
        redirect_url (str): URL of client's server to redirect the PSU after completion of the consent authorisation.
            Example: https://tpp-application.com.
        vrp_setup (VRPSetupRequest):
        user_id (Union[Unset, UUID]): __Conditional__. Yapily Identifier for the `User` returned by the create user step
            POST /users. Clients must either provide userId or applicationUserId.
        application_user_id (Union[Unset, str]): __Conditional__. Client's own `User` reference. If the client wants to
            work with their own unique references for individual PSUs then they can use the applicationUserId property to
            provide that value. Where Yapily does not already have a Yapily userId that matches the supplied
            applicationUserId, then a new Yapily userId is created automatically and linked to the applicationUserId value.
            Clients must either provide userId or applicationUserId.
        user_settings (Union[Unset, UserSettings]): Specifies the language and location preferences of the user.
        one_time_token (Union[Unset, bool]): Used to receive a oneTimeToken rather than a consentToken at the
            redirectUrl for additional security. This can only be used when the redirectUrl is set. Example: false.
    """

    institution_identifiers: "InstitutionIdentifiers"
    redirect_url: str
    vrp_setup: "VRPSetupRequest"
    user_id: Union[Unset, UUID] = UNSET
    application_user_id: Union[Unset, str] = UNSET
    user_settings: Union[Unset, "UserSettings"] = UNSET
    one_time_token: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        institution_identifiers = self.institution_identifiers.to_dict()

        redirect_url = self.redirect_url

        vrp_setup = self.vrp_setup.to_dict()

        user_id: Union[Unset, str] = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        application_user_id = self.application_user_id

        user_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user_settings, Unset):
            user_settings = self.user_settings.to_dict()

        one_time_token = self.one_time_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "institutionIdentifiers": institution_identifiers,
                "redirectUrl": redirect_url,
                "vrpSetup": vrp_setup,
            }
        )
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if application_user_id is not UNSET:
            field_dict["applicationUserId"] = application_user_id
        if user_settings is not UNSET:
            field_dict["userSettings"] = user_settings
        if one_time_token is not UNSET:
            field_dict["oneTimeToken"] = one_time_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.institution_identifiers import InstitutionIdentifiers
        from ..models.user_settings import UserSettings
        from ..models.vrp_setup_request import VRPSetupRequest

        d = dict(src_dict)
        institution_identifiers = InstitutionIdentifiers.from_dict(d.pop("institutionIdentifiers"))

        redirect_url = d.pop("redirectUrl")

        vrp_setup = VRPSetupRequest.from_dict(d.pop("vrpSetup"))

        _user_id = d.pop("userId", UNSET)
        user_id: Union[Unset, UUID]
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        application_user_id = d.pop("applicationUserId", UNSET)

        _user_settings = d.pop("userSettings", UNSET)
        user_settings: Union[Unset, UserSettings]
        if isinstance(_user_settings, Unset):
            user_settings = UNSET
        else:
            user_settings = UserSettings.from_dict(_user_settings)

        one_time_token = d.pop("oneTimeToken", UNSET)

        create_hosted_vrp_consent_request = cls(
            institution_identifiers=institution_identifiers,
            redirect_url=redirect_url,
            vrp_setup=vrp_setup,
            user_id=user_id,
            application_user_id=application_user_id,
            user_settings=user_settings,
            one_time_token=one_time_token,
        )

        create_hosted_vrp_consent_request.additional_properties = d
        return create_hosted_vrp_consent_request

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
