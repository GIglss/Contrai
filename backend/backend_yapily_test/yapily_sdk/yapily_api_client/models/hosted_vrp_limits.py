from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amount_details import AmountDetails
    from ..models.hosted_non_sweeping_periodic_limits import HostedNonSweepingPeriodicLimits


T = TypeVar("T", bound="HostedVRPLimits")


@_attrs_define
class HostedVRPLimits:
    """The restrictions and limits for payments executed under the VRP consent

    Attributes:
        periodic_limits (Union[Unset, list['HostedNonSweepingPeriodicLimits']]):
        max_amount_per_payment (Union[Unset, AmountDetails]): __Mandatory__. Monetary Amount.
        max_cumulative_amount (Union[Unset, AmountDetails]): __Mandatory__. Monetary Amount.
        max_cumulative_number_of_payments (Union[Unset, int]): __Optional__. Max number of payments that can be
            submitted under this consent.
        edited_by_user (Union[Unset, bool]): Indicates if the user edited the control parameters during authorisation
    """

    periodic_limits: Union[Unset, list["HostedNonSweepingPeriodicLimits"]] = UNSET
    max_amount_per_payment: Union[Unset, "AmountDetails"] = UNSET
    max_cumulative_amount: Union[Unset, "AmountDetails"] = UNSET
    max_cumulative_number_of_payments: Union[Unset, int] = UNSET
    edited_by_user: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        periodic_limits: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.periodic_limits, Unset):
            periodic_limits = []
            for periodic_limits_item_data in self.periodic_limits:
                periodic_limits_item = periodic_limits_item_data.to_dict()
                periodic_limits.append(periodic_limits_item)

        max_amount_per_payment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.max_amount_per_payment, Unset):
            max_amount_per_payment = self.max_amount_per_payment.to_dict()

        max_cumulative_amount: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.max_cumulative_amount, Unset):
            max_cumulative_amount = self.max_cumulative_amount.to_dict()

        max_cumulative_number_of_payments = self.max_cumulative_number_of_payments

        edited_by_user = self.edited_by_user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if periodic_limits is not UNSET:
            field_dict["periodicLimits"] = periodic_limits
        if max_amount_per_payment is not UNSET:
            field_dict["maxAmountPerPayment"] = max_amount_per_payment
        if max_cumulative_amount is not UNSET:
            field_dict["maxCumulativeAmount"] = max_cumulative_amount
        if max_cumulative_number_of_payments is not UNSET:
            field_dict["maxCumulativeNumberOfPayments"] = max_cumulative_number_of_payments
        if edited_by_user is not UNSET:
            field_dict["editedByUser"] = edited_by_user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amount_details import AmountDetails
        from ..models.hosted_non_sweeping_periodic_limits import HostedNonSweepingPeriodicLimits

        d = dict(src_dict)
        periodic_limits = []
        _periodic_limits = d.pop("periodicLimits", UNSET)
        for periodic_limits_item_data in _periodic_limits or []:
            periodic_limits_item = HostedNonSweepingPeriodicLimits.from_dict(periodic_limits_item_data)

            periodic_limits.append(periodic_limits_item)

        _max_amount_per_payment = d.pop("maxAmountPerPayment", UNSET)
        max_amount_per_payment: Union[Unset, AmountDetails]
        if isinstance(_max_amount_per_payment, Unset):
            max_amount_per_payment = UNSET
        else:
            max_amount_per_payment = AmountDetails.from_dict(_max_amount_per_payment)

        _max_cumulative_amount = d.pop("maxCumulativeAmount", UNSET)
        max_cumulative_amount: Union[Unset, AmountDetails]
        if isinstance(_max_cumulative_amount, Unset):
            max_cumulative_amount = UNSET
        else:
            max_cumulative_amount = AmountDetails.from_dict(_max_cumulative_amount)

        max_cumulative_number_of_payments = d.pop("maxCumulativeNumberOfPayments", UNSET)

        edited_by_user = d.pop("editedByUser", UNSET)

        hosted_vrp_limits = cls(
            periodic_limits=periodic_limits,
            max_amount_per_payment=max_amount_per_payment,
            max_cumulative_amount=max_cumulative_amount,
            max_cumulative_number_of_payments=max_cumulative_number_of_payments,
            edited_by_user=edited_by_user,
        )

        hosted_vrp_limits.additional_properties = d
        return hosted_vrp_limits

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
