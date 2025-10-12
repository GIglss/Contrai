from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_payment_request import BulkPaymentRequest
    from ..models.redirect_request import RedirectRequest


T = TypeVar("T", bound="BulkPaymentAuthorisationRequest")


@_attrs_define
class BulkPaymentAuthorisationRequest:
    """
    Attributes:
        institution_id (str): __Mandatory__. The reference to the `Institution` which identifies which institution the
            authorisation request is sent to. Example: yapily-mock.
        user_uuid (Union[Unset, UUID]): __Conditional__. The reference to the `User` that will authorise the
            authorisation request using the Yapily generated UUID. Either the `userUuid` or `applicationUserId` must be
            provided. Example: e006a012-c306-4355-a6a1-99bf69ae5171.
        application_user_id (Union[Unset, str]): __Conditional__. The user-friendly reference to the `User` that will
            authorise the authorisation request. If a `User` with the specified `applicationUserId` exists, it will be used
            otherwise, a new `User` with the specified `applicationUserId` will be created and used. Either the `userUuid`
            or `applicationUserId` must be provided. Example: user-234562290.
        forward_parameters (Union[Unset, list[str]]): Extra parameters the TPP may want to get forwarded in the callback
            request after the PSU redirect.
        callback (Union[Unset, str]): __Optional__. The server to redirect the user to after the user complete the
            authorisation at the `Institution`. <br><br>See [Using a callback
            (Optional)](https://docs.yapily.com/pages/knowledge/yapily-concepts/callback_url/#using-a-callback-optional) for
            more information. Example: https://display-parameters.com.
        redirect (Union[Unset, RedirectRequest]): __Optional__. The server to redirect the user to after the user
            complete the authorisation at the `Institution`.
        one_time_token (Union[Unset, bool]): __Conditional__. Used to receive a `oneTimeToken` rather than a
            `consentToken` at the `callback` for additional security. This can only be used when the `callback` is set.
            <br><br>See [Using a callback with an OTT (Optional)](https://docs.yapily.com/pages/knowledge/yapily-
            concepts/callback_url/#using-a-callback-with-an-ott-optional) for more information.
        payment_request (Union[Unset, BulkPaymentRequest]): The payment request object defining the details of the bulk
            payment
    """

    institution_id: str
    user_uuid: Union[Unset, UUID] = UNSET
    application_user_id: Union[Unset, str] = UNSET
    forward_parameters: Union[Unset, list[str]] = UNSET
    callback: Union[Unset, str] = UNSET
    redirect: Union[Unset, "RedirectRequest"] = UNSET
    one_time_token: Union[Unset, bool] = UNSET
    payment_request: Union[Unset, "BulkPaymentRequest"] = UNSET
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

        payment_request: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payment_request, Unset):
            payment_request = self.payment_request.to_dict()

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
        if payment_request is not UNSET:
            field_dict["paymentRequest"] = payment_request

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_payment_request import BulkPaymentRequest
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

        _payment_request = d.pop("paymentRequest", UNSET)
        payment_request: Union[Unset, BulkPaymentRequest]
        if isinstance(_payment_request, Unset):
            payment_request = UNSET
        else:
            payment_request = BulkPaymentRequest.from_dict(_payment_request)

        bulk_payment_authorisation_request = cls(
            institution_id=institution_id,
            user_uuid=user_uuid,
            application_user_id=application_user_id,
            forward_parameters=forward_parameters,
            callback=callback,
            redirect=redirect,
            one_time_token=one_time_token,
            payment_request=payment_request,
        )

        bulk_payment_authorisation_request.additional_properties = d
        return bulk_payment_authorisation_request

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
