import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MultiAuthorisation")


@_attrs_define
class MultiAuthorisation:
    """Details the additional levels of authorisation which are required from, and being managed by, the `Institution`.

    Attributes:
        status (Union[Unset, str]): __Mandatory__. Specifies the current status of the multi-authorisation flow.
        number_of_authorisation_required (Union[Unset, int]): __Mandatory__. Total number of authorisations required.
        number_of_authorisation_received (Union[Unset, int]): __Mandatory__. The total number of authorisations that
            have been received.
        last_updated_date_time (Union[Unset, datetime.datetime]): __Mandatory__. Date and time of when the authorisation
            was last updated.
        expiration_date_time (Union[Unset, datetime.datetime]): __Mandatory__. Date and time by when the authorisation
            flow must be completed before it expires and the authorisation request is terminated.
    """

    status: Union[Unset, str] = UNSET
    number_of_authorisation_required: Union[Unset, int] = UNSET
    number_of_authorisation_received: Union[Unset, int] = UNSET
    last_updated_date_time: Union[Unset, datetime.datetime] = UNSET
    expiration_date_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        number_of_authorisation_required = self.number_of_authorisation_required

        number_of_authorisation_received = self.number_of_authorisation_received

        last_updated_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_date_time, Unset):
            last_updated_date_time = self.last_updated_date_time.isoformat()

        expiration_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.expiration_date_time, Unset):
            expiration_date_time = self.expiration_date_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if number_of_authorisation_required is not UNSET:
            field_dict["numberOfAuthorisationRequired"] = number_of_authorisation_required
        if number_of_authorisation_received is not UNSET:
            field_dict["numberOfAuthorisationReceived"] = number_of_authorisation_received
        if last_updated_date_time is not UNSET:
            field_dict["lastUpdatedDateTime"] = last_updated_date_time
        if expiration_date_time is not UNSET:
            field_dict["expirationDateTime"] = expiration_date_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status", UNSET)

        number_of_authorisation_required = d.pop("numberOfAuthorisationRequired", UNSET)

        number_of_authorisation_received = d.pop("numberOfAuthorisationReceived", UNSET)

        _last_updated_date_time = d.pop("lastUpdatedDateTime", UNSET)
        last_updated_date_time: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_date_time, Unset):
            last_updated_date_time = UNSET
        else:
            last_updated_date_time = isoparse(_last_updated_date_time)

        _expiration_date_time = d.pop("expirationDateTime", UNSET)
        expiration_date_time: Union[Unset, datetime.datetime]
        if isinstance(_expiration_date_time, Unset):
            expiration_date_time = UNSET
        else:
            expiration_date_time = isoparse(_expiration_date_time)

        multi_authorisation = cls(
            status=status,
            number_of_authorisation_required=number_of_authorisation_required,
            number_of_authorisation_received=number_of_authorisation_received,
            last_updated_date_time=last_updated_date_time,
            expiration_date_time=expiration_date_time,
        )

        multi_authorisation.additional_properties = d
        return multi_authorisation

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
