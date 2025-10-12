from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compliance_data import ComplianceData
    from ..models.initiation_details import InitiationDetails
    from ..models.redirect_request import RedirectRequest
    from ..models.sweeping_control_parameters import SweepingControlParameters


T = TypeVar("T", bound="SweepingAuthorisationRequest")


@_attrs_define
class SweepingAuthorisationRequest:
    """
    Attributes:
        institution_id (str): __Mandatory__. The reference to the `Institution` which identifies which institution the
            authorisation request is sent to. Example: yapily-mock.
        control_parameters (SweepingControlParameters): Define the restrictions and limits for payment orders as part of
            Sweeping VRP consent
        initiation_details (InitiationDetails): __Mandatory__. The payment initiation object defining the details of the
            payment under the Variable Recurring Payment consent.
        user_id (Union[Unset, UUID]): This is the Yapily user identifier for the user returned by the create user step
            POST ../users
        application_user_id (Union[Unset, str]): A client's own user reference. If the client wants to work with their
            own unique references for individual PSUs then they can use the applicationUserId property to provide that
            value. Where Yapily does not already have a Yapily userId that matches the supplied applicationUserId, then a
            new Yapily userId is created automatically and linked to the applicationUserId value.  Clients can then use
            either their own applicationUserId or the Yapily userId to reference the same user in future calls.
        forward_parameters (Union[Unset, list[str]]): Extra parameters the TPP may want to get forwarded in the callback
            request after the PSU redirect.
        callback (Union[Unset, str]): __Optional__. The server to redirect the user to after the user complete the
            authorisation at the `Institution`. <br><br>See [Using a callback
            (Optional)](https://docs.yapily.com/knowledge/callback_url/#using-a-callback-optional) for more information.
            Example: https://display-parameters.com.
        redirect (Union[Unset, RedirectRequest]): __Optional__. The server to redirect the user to after the user
            complete the authorisation at the `Institution`.
        one_time_token (Union[Unset, bool]): __Conditional__. Used to receive a `oneTimeToken` rather than a
            `consentToken` at the `callback` for additional security. This can only be used when the `callback` is set.
            <br><br>See [Using a callback with an OTT (Optional)](https://docs.yapily.com/knowledge/callback_url/#using-a-
            callback-with-an-ott-optional) for more information.
        compliance_data (Union[Unset, ComplianceData]): __Conditional__. Information needed to complete compliance
            checks. Mandatory for Yapily Connect customers.
    """

    institution_id: str
    control_parameters: "SweepingControlParameters"
    initiation_details: "InitiationDetails"
    user_id: Union[Unset, UUID] = UNSET
    application_user_id: Union[Unset, str] = UNSET
    forward_parameters: Union[Unset, list[str]] = UNSET
    callback: Union[Unset, str] = UNSET
    redirect: Union[Unset, "RedirectRequest"] = UNSET
    one_time_token: Union[Unset, bool] = UNSET
    compliance_data: Union[Unset, "ComplianceData"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        institution_id = self.institution_id

        control_parameters = self.control_parameters.to_dict()

        initiation_details = self.initiation_details.to_dict()

        user_id: Union[Unset, str] = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        application_user_id = self.application_user_id

        forward_parameters: Union[Unset, list[str]] = UNSET
        if not isinstance(self.forward_parameters, Unset):
            forward_parameters = self.forward_parameters

        callback = self.callback

        redirect: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.redirect, Unset):
            redirect = self.redirect.to_dict()

        one_time_token = self.one_time_token

        compliance_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.compliance_data, Unset):
            compliance_data = self.compliance_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "institutionId": institution_id,
                "controlParameters": control_parameters,
                "initiationDetails": initiation_details,
            }
        )
        if user_id is not UNSET:
            field_dict["userId"] = user_id
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
        if compliance_data is not UNSET:
            field_dict["complianceData"] = compliance_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compliance_data import ComplianceData
        from ..models.initiation_details import InitiationDetails
        from ..models.redirect_request import RedirectRequest
        from ..models.sweeping_control_parameters import SweepingControlParameters

        d = dict(src_dict)
        institution_id = d.pop("institutionId")

        control_parameters = SweepingControlParameters.from_dict(d.pop("controlParameters"))

        initiation_details = InitiationDetails.from_dict(d.pop("initiationDetails"))

        _user_id = d.pop("userId", UNSET)
        user_id: Union[Unset, UUID]
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

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

        _compliance_data = d.pop("complianceData", UNSET)
        compliance_data: Union[Unset, ComplianceData]
        if isinstance(_compliance_data, Unset):
            compliance_data = UNSET
        else:
            compliance_data = ComplianceData.from_dict(_compliance_data)

        sweeping_authorisation_request = cls(
            institution_id=institution_id,
            control_parameters=control_parameters,
            initiation_details=initiation_details,
            user_id=user_id,
            application_user_id=application_user_id,
            forward_parameters=forward_parameters,
            callback=callback,
            redirect=redirect,
            one_time_token=one_time_token,
            compliance_data=compliance_data,
        )

        sweeping_authorisation_request.additional_properties = d
        return sweeping_authorisation_request

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
