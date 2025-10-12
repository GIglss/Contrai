import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amount_details import AmountDetails
    from ..models.sweeping_periodic_limits import SweepingPeriodicLimits


T = TypeVar("T", bound="SweepingControlParameters")


@_attrs_define
class SweepingControlParameters:
    """Define the restrictions and limits for payment orders as part of Sweeping VRP consent

    Attributes:
        psu_authentication_methods (list[str]): __Mandatory__. Defines the authentication method(s) allowed in payment
            submission step. Allowed values are [SCA_REQUIRED, SCA_NOT_REQUIRED].
        periodic_limits (list['SweepingPeriodicLimits']):
        max_amount_per_payment (AmountDetails): __Mandatory__. Monetary Amount.
        valid_from (Union[Unset, datetime.datetime]): __Optional__. Start date when the consent becomes valid.
        valid_to (Union[Unset, datetime.datetime]): __Optional__. End date when the consent expires and becomes invalid.
    """

    psu_authentication_methods: list[str]
    periodic_limits: list["SweepingPeriodicLimits"]
    max_amount_per_payment: "AmountDetails"
    valid_from: Union[Unset, datetime.datetime] = UNSET
    valid_to: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        psu_authentication_methods = self.psu_authentication_methods

        periodic_limits = []
        for periodic_limits_item_data in self.periodic_limits:
            periodic_limits_item = periodic_limits_item_data.to_dict()
            periodic_limits.append(periodic_limits_item)

        max_amount_per_payment = self.max_amount_per_payment.to_dict()

        valid_from: Union[Unset, str] = UNSET
        if not isinstance(self.valid_from, Unset):
            valid_from = self.valid_from.isoformat()

        valid_to: Union[Unset, str] = UNSET
        if not isinstance(self.valid_to, Unset):
            valid_to = self.valid_to.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "psuAuthenticationMethods": psu_authentication_methods,
                "periodicLimits": periodic_limits,
                "maxAmountPerPayment": max_amount_per_payment,
            }
        )
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amount_details import AmountDetails
        from ..models.sweeping_periodic_limits import SweepingPeriodicLimits

        d = dict(src_dict)
        psu_authentication_methods = cast(list[str], d.pop("psuAuthenticationMethods"))

        periodic_limits = []
        _periodic_limits = d.pop("periodicLimits")
        for periodic_limits_item_data in _periodic_limits:
            periodic_limits_item = SweepingPeriodicLimits.from_dict(periodic_limits_item_data)

            periodic_limits.append(periodic_limits_item)

        max_amount_per_payment = AmountDetails.from_dict(d.pop("maxAmountPerPayment"))

        _valid_from = d.pop("validFrom", UNSET)
        valid_from: Union[Unset, datetime.datetime]
        if isinstance(_valid_from, Unset):
            valid_from = UNSET
        else:
            valid_from = isoparse(_valid_from)

        _valid_to = d.pop("validTo", UNSET)
        valid_to: Union[Unset, datetime.datetime]
        if isinstance(_valid_to, Unset):
            valid_to = UNSET
        else:
            valid_to = isoparse(_valid_to)

        sweeping_control_parameters = cls(
            psu_authentication_methods=psu_authentication_methods,
            periodic_limits=periodic_limits,
            max_amount_per_payment=max_amount_per_payment,
            valid_from=valid_from,
            valid_to=valid_to,
        )

        sweeping_control_parameters.additional_properties = d
        return sweeping_control_parameters

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
