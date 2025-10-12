import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.authorisation_status import AuthorisationStatus
from ..models.feature_enum import FeatureEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.initiation_details import InitiationDetails
    from ..models.payer_details import PayerDetails
    from ..models.sweeping_control_parameters import SweepingControlParameters


T = TypeVar("T", bound="SweepingAuthorisationResponse")


@_attrs_define
class SweepingAuthorisationResponse:
    """
    Attributes:
        id (Union[Unset, UUID]):
        user_id (Union[Unset, UUID]): This is the Yapily user identifier for the user returned by the create user step
            POST ../users
        application_user_id (Union[Unset, str]): A client's own user reference. If the client wants to work with their
            own unique references for individual PSUs then they can use the applicationUserId property to provide that
            value. Where Yapily does not already have a Yapily userId that matches the supplied applicationUserId, then a
            new Yapily userId is created automatically and linked to the applicationUserId value.  Clients can then use
            either their own applicationUserId or the Yapily userId to reference the same user in future calls.
        institution_id (Union[Unset, str]): The reference to the Institution which identifies which institution the
            authorisation request is sent to.
        status (Union[Unset, AuthorisationStatus]): Current status of the embedded authorisation request in code form.
        created_at (Union[Unset, datetime.datetime]):
        feature_scope (Union[Unset, list[FeatureEnum]]): __Optional__. Used to granularly specify the set of features
            that the user will give their consent for when requesting access to their account information. Depending on the
            `Institution`, this may also populate a consent screen which list these scopes before the user
            authorises.<br><br>This endpoint accepts allow all [Financial Data Features](/guides/financial-
            data/features/#feature-list) that the `Institution` supports.To find out which scopes an `Institution` supports,
            check [GET Institution](./#get-institution).
        consent_token (Union[Unset, str]): The `consent-token` containing the user's authorisation to make the payment
            request.
        state (Union[Unset, str]):
        authorized_at (Union[Unset, datetime.datetime]):
        institution_consent_id (Union[Unset, str]): Identification of the consent at the Institution.
        authorisation_url (Union[Unset, str]):
        qr_code_url (Union[Unset, str]):
        control_parameters (Union[Unset, SweepingControlParameters]): Define the restrictions and limits for payment
            orders as part of Sweeping VRP consent
        payer (Union[Unset, PayerDetails]): __Conditional__. Details of the benefactor [person or business].
        initiation_details (Union[Unset, InitiationDetails]): __Mandatory__. The payment initiation object defining the
            details of the payment under the Variable Recurring Payment consent.
    """

    id: Union[Unset, UUID] = UNSET
    user_id: Union[Unset, UUID] = UNSET
    application_user_id: Union[Unset, str] = UNSET
    institution_id: Union[Unset, str] = UNSET
    status: Union[Unset, AuthorisationStatus] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    feature_scope: Union[Unset, list[FeatureEnum]] = UNSET
    consent_token: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    authorized_at: Union[Unset, datetime.datetime] = UNSET
    institution_consent_id: Union[Unset, str] = UNSET
    authorisation_url: Union[Unset, str] = UNSET
    qr_code_url: Union[Unset, str] = UNSET
    control_parameters: Union[Unset, "SweepingControlParameters"] = UNSET
    payer: Union[Unset, "PayerDetails"] = UNSET
    initiation_details: Union[Unset, "InitiationDetails"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        user_id: Union[Unset, str] = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        application_user_id = self.application_user_id

        institution_id = self.institution_id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        feature_scope: Union[Unset, list[str]] = UNSET
        if not isinstance(self.feature_scope, Unset):
            feature_scope = []
            for feature_scope_item_data in self.feature_scope:
                feature_scope_item = feature_scope_item_data.value
                feature_scope.append(feature_scope_item)

        consent_token = self.consent_token

        state = self.state

        authorized_at: Union[Unset, str] = UNSET
        if not isinstance(self.authorized_at, Unset):
            authorized_at = self.authorized_at.isoformat()

        institution_consent_id = self.institution_consent_id

        authorisation_url = self.authorisation_url

        qr_code_url = self.qr_code_url

        control_parameters: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.control_parameters, Unset):
            control_parameters = self.control_parameters.to_dict()

        payer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payer, Unset):
            payer = self.payer.to_dict()

        initiation_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.initiation_details, Unset):
            initiation_details = self.initiation_details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if application_user_id is not UNSET:
            field_dict["applicationUserId"] = application_user_id
        if institution_id is not UNSET:
            field_dict["institutionId"] = institution_id
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if feature_scope is not UNSET:
            field_dict["featureScope"] = feature_scope
        if consent_token is not UNSET:
            field_dict["consentToken"] = consent_token
        if state is not UNSET:
            field_dict["state"] = state
        if authorized_at is not UNSET:
            field_dict["authorizedAt"] = authorized_at
        if institution_consent_id is not UNSET:
            field_dict["institutionConsentId"] = institution_consent_id
        if authorisation_url is not UNSET:
            field_dict["authorisationUrl"] = authorisation_url
        if qr_code_url is not UNSET:
            field_dict["qrCodeUrl"] = qr_code_url
        if control_parameters is not UNSET:
            field_dict["controlParameters"] = control_parameters
        if payer is not UNSET:
            field_dict["payer"] = payer
        if initiation_details is not UNSET:
            field_dict["initiationDetails"] = initiation_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.initiation_details import InitiationDetails
        from ..models.payer_details import PayerDetails
        from ..models.sweeping_control_parameters import SweepingControlParameters

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _user_id = d.pop("userId", UNSET)
        user_id: Union[Unset, UUID]
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        application_user_id = d.pop("applicationUserId", UNSET)

        institution_id = d.pop("institutionId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, AuthorisationStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AuthorisationStatus(_status)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        feature_scope = []
        _feature_scope = d.pop("featureScope", UNSET)
        for feature_scope_item_data in _feature_scope or []:
            feature_scope_item = FeatureEnum(feature_scope_item_data)

            feature_scope.append(feature_scope_item)

        consent_token = d.pop("consentToken", UNSET)

        state = d.pop("state", UNSET)

        _authorized_at = d.pop("authorizedAt", UNSET)
        authorized_at: Union[Unset, datetime.datetime]
        if isinstance(_authorized_at, Unset):
            authorized_at = UNSET
        else:
            authorized_at = isoparse(_authorized_at)

        institution_consent_id = d.pop("institutionConsentId", UNSET)

        authorisation_url = d.pop("authorisationUrl", UNSET)

        qr_code_url = d.pop("qrCodeUrl", UNSET)

        _control_parameters = d.pop("controlParameters", UNSET)
        control_parameters: Union[Unset, SweepingControlParameters]
        if isinstance(_control_parameters, Unset):
            control_parameters = UNSET
        else:
            control_parameters = SweepingControlParameters.from_dict(_control_parameters)

        _payer = d.pop("payer", UNSET)
        payer: Union[Unset, PayerDetails]
        if isinstance(_payer, Unset):
            payer = UNSET
        else:
            payer = PayerDetails.from_dict(_payer)

        _initiation_details = d.pop("initiationDetails", UNSET)
        initiation_details: Union[Unset, InitiationDetails]
        if isinstance(_initiation_details, Unset):
            initiation_details = UNSET
        else:
            initiation_details = InitiationDetails.from_dict(_initiation_details)

        sweeping_authorisation_response = cls(
            id=id,
            user_id=user_id,
            application_user_id=application_user_id,
            institution_id=institution_id,
            status=status,
            created_at=created_at,
            feature_scope=feature_scope,
            consent_token=consent_token,
            state=state,
            authorized_at=authorized_at,
            institution_consent_id=institution_consent_id,
            authorisation_url=authorisation_url,
            qr_code_url=qr_code_url,
            control_parameters=control_parameters,
            payer=payer,
            initiation_details=initiation_details,
        )

        sweeping_authorisation_response.additional_properties = d
        return sweeping_authorisation_response

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
