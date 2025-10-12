import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.authorisation_status import AuthorisationStatus
from ..models.feature_enum import FeatureEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountAuthorisationResponse")


@_attrs_define
class AccountAuthorisationResponse:
    """
    Attributes:
        id (Union[Unset, UUID]): Unique identifier for the account authorisation request.<br><br>The `consentID` used to
            [retrieve a consent](/api/reference/#operation/getConsentById).
        user_uuid (Union[Unset, UUID]): The `User` that the authorisation request was created for.
        application_user_id (Union[Unset, str]): The user-friendly reference to the `User` that the authorisation
            request was created for.
        reference_id (Union[Unset, str]):
        institution_id (Union[Unset, str]): The `Institution` the authorisation request was sent to.
        status (Union[Unset, AuthorisationStatus]): Current status of the embedded authorisation request in code form.
        created_at (Union[Unset, datetime.datetime]): Date and time the consent was created.
        transaction_from (Union[Unset, datetime.datetime]): When performing a transaction query using the consent, this
            is the earliest date of transaction records that can be retrieved.
        transaction_to (Union[Unset, datetime.datetime]): When performing a transaction query using the consent, this is
            the latest date of transaction records that can be retrieved.
        expires_at (Union[Unset, datetime.datetime]): Date and time the authorisation expires. Re-authorisation is
            needed to retain access.
        time_to_expire_in_millis (Union[Unset, int]):
        time_to_expire (Union[Unset, str]):
        feature_scope (Union[Unset, list[FeatureEnum]]): The set of features the consent provides access to.
        consent_token (Union[Unset, str]): Represents the authorisation to gain access to the requested features.
            Required to access account information.
        state (Union[Unset, str]): Correlation ID used with the `Institution` during the authorisation process.
        authorized_at (Union[Unset, datetime.datetime]): Date and time the request was authorised by the `Institution`.
        last_confirmed_at (Union[Unset, datetime.datetime]): The time the PSU last confirmed access to their account
            information, either through full authentication with the institution, or through reconfirmation with the TPP.
        reconfirm_by (Union[Unset, datetime.datetime]): The date and time the consent must be reconfirmed by to ensure
            continued access to the account information.
        institution_consent_id (Union[Unset, str]): Unique identifier of the consent assigned by the `Institution`.
        authorisation_url (Union[Unset, str]):
        qr_code_url (Union[Unset, str]): The URL link for the QR code that may be scanned via a mobile device to make an
            authorisation redirect to the bank (authURL encoded).
    """

    id: Union[Unset, UUID] = UNSET
    user_uuid: Union[Unset, UUID] = UNSET
    application_user_id: Union[Unset, str] = UNSET
    reference_id: Union[Unset, str] = UNSET
    institution_id: Union[Unset, str] = UNSET
    status: Union[Unset, AuthorisationStatus] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    transaction_from: Union[Unset, datetime.datetime] = UNSET
    transaction_to: Union[Unset, datetime.datetime] = UNSET
    expires_at: Union[Unset, datetime.datetime] = UNSET
    time_to_expire_in_millis: Union[Unset, int] = UNSET
    time_to_expire: Union[Unset, str] = UNSET
    feature_scope: Union[Unset, list[FeatureEnum]] = UNSET
    consent_token: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    authorized_at: Union[Unset, datetime.datetime] = UNSET
    last_confirmed_at: Union[Unset, datetime.datetime] = UNSET
    reconfirm_by: Union[Unset, datetime.datetime] = UNSET
    institution_consent_id: Union[Unset, str] = UNSET
    authorisation_url: Union[Unset, str] = UNSET
    qr_code_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        user_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.user_uuid, Unset):
            user_uuid = str(self.user_uuid)

        application_user_id = self.application_user_id

        reference_id = self.reference_id

        institution_id = self.institution_id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        transaction_from: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_from, Unset):
            transaction_from = self.transaction_from.isoformat()

        transaction_to: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_to, Unset):
            transaction_to = self.transaction_to.isoformat()

        expires_at: Union[Unset, str] = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        time_to_expire_in_millis = self.time_to_expire_in_millis

        time_to_expire = self.time_to_expire

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

        last_confirmed_at: Union[Unset, str] = UNSET
        if not isinstance(self.last_confirmed_at, Unset):
            last_confirmed_at = self.last_confirmed_at.isoformat()

        reconfirm_by: Union[Unset, str] = UNSET
        if not isinstance(self.reconfirm_by, Unset):
            reconfirm_by = self.reconfirm_by.isoformat()

        institution_consent_id = self.institution_consent_id

        authorisation_url = self.authorisation_url

        qr_code_url = self.qr_code_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if user_uuid is not UNSET:
            field_dict["userUuid"] = user_uuid
        if application_user_id is not UNSET:
            field_dict["applicationUserId"] = application_user_id
        if reference_id is not UNSET:
            field_dict["referenceId"] = reference_id
        if institution_id is not UNSET:
            field_dict["institutionId"] = institution_id
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if transaction_from is not UNSET:
            field_dict["transactionFrom"] = transaction_from
        if transaction_to is not UNSET:
            field_dict["transactionTo"] = transaction_to
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if time_to_expire_in_millis is not UNSET:
            field_dict["timeToExpireInMillis"] = time_to_expire_in_millis
        if time_to_expire is not UNSET:
            field_dict["timeToExpire"] = time_to_expire
        if feature_scope is not UNSET:
            field_dict["featureScope"] = feature_scope
        if consent_token is not UNSET:
            field_dict["consentToken"] = consent_token
        if state is not UNSET:
            field_dict["state"] = state
        if authorized_at is not UNSET:
            field_dict["authorizedAt"] = authorized_at
        if last_confirmed_at is not UNSET:
            field_dict["lastConfirmedAt"] = last_confirmed_at
        if reconfirm_by is not UNSET:
            field_dict["reconfirmBy"] = reconfirm_by
        if institution_consent_id is not UNSET:
            field_dict["institutionConsentId"] = institution_consent_id
        if authorisation_url is not UNSET:
            field_dict["authorisationUrl"] = authorisation_url
        if qr_code_url is not UNSET:
            field_dict["qrCodeUrl"] = qr_code_url

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

        _user_uuid = d.pop("userUuid", UNSET)
        user_uuid: Union[Unset, UUID]
        if isinstance(_user_uuid, Unset):
            user_uuid = UNSET
        else:
            user_uuid = UUID(_user_uuid)

        application_user_id = d.pop("applicationUserId", UNSET)

        reference_id = d.pop("referenceId", UNSET)

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

        _transaction_from = d.pop("transactionFrom", UNSET)
        transaction_from: Union[Unset, datetime.datetime]
        if isinstance(_transaction_from, Unset):
            transaction_from = UNSET
        else:
            transaction_from = isoparse(_transaction_from)

        _transaction_to = d.pop("transactionTo", UNSET)
        transaction_to: Union[Unset, datetime.datetime]
        if isinstance(_transaction_to, Unset):
            transaction_to = UNSET
        else:
            transaction_to = isoparse(_transaction_to)

        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: Union[Unset, datetime.datetime]
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = isoparse(_expires_at)

        time_to_expire_in_millis = d.pop("timeToExpireInMillis", UNSET)

        time_to_expire = d.pop("timeToExpire", UNSET)

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

        _last_confirmed_at = d.pop("lastConfirmedAt", UNSET)
        last_confirmed_at: Union[Unset, datetime.datetime]
        if isinstance(_last_confirmed_at, Unset):
            last_confirmed_at = UNSET
        else:
            last_confirmed_at = isoparse(_last_confirmed_at)

        _reconfirm_by = d.pop("reconfirmBy", UNSET)
        reconfirm_by: Union[Unset, datetime.datetime]
        if isinstance(_reconfirm_by, Unset):
            reconfirm_by = UNSET
        else:
            reconfirm_by = isoparse(_reconfirm_by)

        institution_consent_id = d.pop("institutionConsentId", UNSET)

        authorisation_url = d.pop("authorisationUrl", UNSET)

        qr_code_url = d.pop("qrCodeUrl", UNSET)

        account_authorisation_response = cls(
            id=id,
            user_uuid=user_uuid,
            application_user_id=application_user_id,
            reference_id=reference_id,
            institution_id=institution_id,
            status=status,
            created_at=created_at,
            transaction_from=transaction_from,
            transaction_to=transaction_to,
            expires_at=expires_at,
            time_to_expire_in_millis=time_to_expire_in_millis,
            time_to_expire=time_to_expire,
            feature_scope=feature_scope,
            consent_token=consent_token,
            state=state,
            authorized_at=authorized_at,
            last_confirmed_at=last_confirmed_at,
            reconfirm_by=reconfirm_by,
            institution_consent_id=institution_consent_id,
            authorisation_url=authorisation_url,
            qr_code_url=qr_code_url,
        )

        account_authorisation_response.additional_properties = d
        return account_authorisation_response

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
