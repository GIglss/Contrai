import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="HostedVRPPhase")


@_attrs_define
class HostedVRPPhase:
    """The phase of the VRP Consent Request.

    Attributes:
        phase_name (Union[Unset, str]): The name of the hosted VRP consent process phase. Allowed values are : <ul> <li>
            INITIATED - Process initiated </li><li> DECLINED - Process failed and will not proceed further </li><li>
            INSTITUTION_SUBMITTED - Consent institution submitted </li><li> INPUT_CAPTURED - Additional input captured to
            process the Consent </li><li> IBAN_VALIDATED - Payer IBAN successfully validated </li><li> AUTHORISATION_CREATED
            - Consent authorisation request created with Institution, awaiting authorisation completion </li><li>
            AUTHORISATION_REJECTED - Consent Authorisation request rejected by Institution and will not proceed further
            </li><li> AUTHORISED - Consent authorisation completed </li><li> AUTHORISATION_FAILED - Consent authorisation
            failed and will not proceed further</li><li> SUBMITTED - Consent execution created and submitted to Institution
            </li><li> ACCEPTED - Consent execution accepted by Institution and awaiting settlement </li><li> REJECTED -
            Consent execution request rejected by Institution and will not proceed further </li><li> STATUS_POLLING_STARTED
            - Consent status polling started </li><li> STATUS_POLLING_ENDED - Consent status polling ended </li><li>
            MERCHANT_ACKNOWLEDGED - Consent acknowledgement received from merchant </li><li> FINISHED - Consent process
            completed </li> <li> REVOKED - Consent process completed </li>  </ul>
        phase_created_at (Union[Unset, datetime.datetime]): The date and time at which the phase of the hosted Consent
            was created.
    """

    phase_name: Union[Unset, str] = UNSET
    phase_created_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phase_name = self.phase_name

        phase_created_at: Union[Unset, str] = UNSET
        if not isinstance(self.phase_created_at, Unset):
            phase_created_at = self.phase_created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if phase_name is not UNSET:
            field_dict["phaseName"] = phase_name
        if phase_created_at is not UNSET:
            field_dict["phaseCreatedAt"] = phase_created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        phase_name = d.pop("phaseName", UNSET)

        _phase_created_at = d.pop("phaseCreatedAt", UNSET)
        phase_created_at: Union[Unset, datetime.datetime]
        if isinstance(_phase_created_at, Unset):
            phase_created_at = UNSET
        else:
            phase_created_at = isoparse(_phase_created_at)

        hosted_vrp_phase = cls(
            phase_name=phase_name,
            phase_created_at=phase_created_at,
        )

        hosted_vrp_phase.additional_properties = d
        return hosted_vrp_phase

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
