from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_request import AccountRequest
    from ..models.redirect_request import RedirectRequest


T = TypeVar("T", bound="AccountAuthorisationRequest")


@_attrs_define
class AccountAuthorisationRequest:
    """
    Attributes:
        institution_id (str): __Mandatory__. The reference to the `Institution` which identifies which institution the
            authorisation request is sent to. Example: yapily-mock.
        user_uuid (Union[Unset, UUID]): `User` for which the authorisation request was created.
        application_user_id (Union[Unset, str]): __Conditional__. User-friendly identifier of the `User` that provides
            authorisation. If a `User` with the specified `applicationUserId` exists, it will be used otherwise, a new
            `User` with the specified `applicationUserId` will be created and used. Either the `userUuid` or
            `applicationUserId` must be provided. Example: user-234562290.
        forward_parameters (Union[Unset, list[str]]): Extra parameters the TPP may want to get forwarded in the callback
            request after the PSU redirect.
        callback (Union[Unset, str]): __Optional__. The server to redirect the user to after the user completes the
            authorisation at the `Institution`. <br><br>See [Using a callback
            (Optional)](https://docs.yapily.com/pages/knowledge/yapily-concepts/callback_url/#using-a-callback-optional) for
            more information. Example: https://display-parameters.com.
        redirect (Union[Unset, RedirectRequest]): __Optional__. The server to redirect the user to after the user
            complete the authorisation at the `Institution`.
        one_time_token (Union[Unset, bool]): __Conditional__. Used to receive a `oneTimeToken` rather than a
            `consentToken` at the `callback` for additional security. This can only be used when the `callback` is set.
            <br><br>See [Using a callback with an OTT (Optional)](https://docs.yapily.com/pages/knowledge/yapily-
            concepts/callback_url/#using-a-callback-with-an-ott-optional) for more information.
        account_request (Union[Unset, AccountRequest]): __Conditional__. Used to further specify details of the
            `Consent` to request <br><br>Conditions:<ol><li>Mandatory to specify the individual scopes to request from the
            user at the `Institution` for an account authorisation</li><li>Mandatory to specify an expiry time on the
            created `Consent` at which time will render it unusable</li><li>Mandatory to specify the date range that the
            created `Consent` will be able to access transactions for (given the range is support for the
            `Institution`)</li></ol>
    """

    institution_id: str
    user_uuid: Union[Unset, UUID] = UNSET
    application_user_id: Union[Unset, str] = UNSET
    forward_parameters: Union[Unset, list[str]] = UNSET
    callback: Union[Unset, str] = UNSET
    redirect: Union[Unset, "RedirectRequest"] = UNSET
    one_time_token: Union[Unset, bool] = UNSET
    account_request: Union[Unset, "AccountRequest"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        institution_id = self.institution_id

        user_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.user_uuid, Unset):
            user_uuid = str(self.user_uuid)

        application_user_id = self.application_user_id

        forward_parameters: Union[Unset, list[str]] = UNSET
        if not isinstance(self.forward_parameters, Unset):
            forward_parameters = self.forward_parameters

        callback = self.callback

        redirect: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.redirect, Unset):
            redirect = self.redirect.to_dict()

        one_time_token = self.one_time_token

        account_request: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.account_request, Unset):
            account_request = self.account_request.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "institutionId": institution_id,
            }
        )
        if user_uuid is not UNSET:
            field_dict["userUuid"] = user_uuid
        if application_user_id is not UNSET:
            field_dict["applicationUserId"] = application_user_id
        if forward_parameters is not UNSET:
            field_dict["forwardParameters"] = forward_parameters
        if callback is not UNSET:
            field_dict["callback"] = callback
        if redirect is not UNSET:
            field_dict["redirect"] = redirect
        if one_time_token is not UNSET:
            field_dict["oneTimeToken"] = one_time_token
        if account_request is not UNSET:
            field_dict["accountRequest"] = account_request

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_request import AccountRequest
        from ..models.redirect_request import RedirectRequest

        d = dict(src_dict)
        institution_id = d.pop("institutionId")

        _user_uuid = d.pop("userUuid", UNSET)
        user_uuid: Union[Unset, UUID]
        if isinstance(_user_uuid, Unset):
            user_uuid = UNSET
        else:
            user_uuid = UUID(_user_uuid)

        application_user_id = d.pop("applicationUserId", UNSET)

        forward_parameters = cast(list[str], d.pop("forwardParameters", UNSET))

        callback = d.pop("callback", UNSET)

        _redirect = d.pop("redirect", UNSET)
        redirect: Union[Unset, RedirectRequest]
        if isinstance(_redirect, Unset):
            redirect = UNSET
        else:
            redirect = RedirectRequest.from_dict(_redirect)

        one_time_token = d.pop("oneTimeToken", UNSET)

        _account_request = d.pop("accountRequest", UNSET)
        account_request: Union[Unset, AccountRequest]
        if isinstance(_account_request, Unset):
            account_request = UNSET
        else:
            account_request = AccountRequest.from_dict(_account_request)

        account_authorisation_request = cls(
            institution_id=institution_id,
            user_uuid=user_uuid,
            application_user_id=application_user_id,
            forward_parameters=forward_parameters,
            callback=callback,
            redirect=redirect,
            one_time_token=one_time_token,
            account_request=account_request,
        )

        account_authorisation_request.additional_properties = d
        return account_authorisation_request

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
