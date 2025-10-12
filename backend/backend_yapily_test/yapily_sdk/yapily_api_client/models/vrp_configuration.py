from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amount_details import AmountDetails
    from ..models.vrp_periodic_limit import VrpPeriodicLimit


T = TypeVar("T", bound="VrpConfiguration")


@_attrs_define
class VrpConfiguration:
    """
    Attributes:
        maximum_individual_amount (Union[Unset, AmountDetails]): __Mandatory__. Monetary Amount.
        maximum_cumulative_amount (Union[Unset, AmountDetails]): __Mandatory__. Monetary Amount.
        maximum_cumulative_number_of_payments (Union[Unset, int]): Maximum cumulative number of payments
        periodic_limits (Union[Unset, list['VrpPeriodicLimit']]):
        recurring_payment_category (Union[Unset, str]): Payment Category with allowed values: ONGOING, SUBSCRIPTION
            Example: ONGOING.
    """

    maximum_individual_amount: Union[Unset, "AmountDetails"] = UNSET
    maximum_cumulative_amount: Union[Unset, "AmountDetails"] = UNSET
    maximum_cumulative_number_of_payments: Union[Unset, int] = UNSET
    periodic_limits: Union[Unset, list["VrpPeriodicLimit"]] = UNSET
    recurring_payment_category: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        maximum_individual_amount: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.maximum_individual_amount, Unset):
            maximum_individual_amount = self.maximum_individual_amount.to_dict()

        maximum_cumulative_amount: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.maximum_cumulative_amount, Unset):
            maximum_cumulative_amount = self.maximum_cumulative_amount.to_dict()

        maximum_cumulative_number_of_payments = self.maximum_cumulative_number_of_payments

        periodic_limits: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.periodic_limits, Unset):
            periodic_limits = []
            for periodic_limits_item_data in self.periodic_limits:
                periodic_limits_item = periodic_limits_item_data.to_dict()
                periodic_limits.append(periodic_limits_item)

        recurring_payment_category = self.recurring_payment_category

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if maximum_individual_amount is not UNSET:
            field_dict["maximumIndividualAmount"] = maximum_individual_amount
        if maximum_cumulative_amount is not UNSET:
            field_dict["maximumCumulativeAmount"] = maximum_cumulative_amount
        if maximum_cumulative_number_of_payments is not UNSET:
            field_dict["maximumCumulativeNumberOfPayments"] = maximum_cumulative_number_of_payments
        if periodic_limits is not UNSET:
            field_dict["periodicLimits"] = periodic_limits
        if recurring_payment_category is not UNSET:
            field_dict["recurringPaymentCategory"] = recurring_payment_category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amount_details import AmountDetails
        from ..models.vrp_periodic_limit import VrpPeriodicLimit

        d = dict(src_dict)
        _maximum_individual_amount = d.pop("maximumIndividualAmount", UNSET)
        maximum_individual_amount: Union[Unset, AmountDetails]
        if isinstance(_maximum_individual_amount, Unset):
            maximum_individual_amount = UNSET
        else:
            maximum_individual_amount = AmountDetails.from_dict(_maximum_individual_amount)

        _maximum_cumulative_amount = d.pop("maximumCumulativeAmount", UNSET)
        maximum_cumulative_amount: Union[Unset, AmountDetails]
        if isinstance(_maximum_cumulative_amount, Unset):
            maximum_cumulative_amount = UNSET
        else:
            maximum_cumulative_amount = AmountDetails.from_dict(_maximum_cumulative_amount)

        maximum_cumulative_number_of_payments = d.pop("maximumCumulativeNumberOfPayments", UNSET)

        periodic_limits = []
        _periodic_limits = d.pop("periodicLimits", UNSET)
        for periodic_limits_item_data in _periodic_limits or []:
            periodic_limits_item = VrpPeriodicLimit.from_dict(periodic_limits_item_data)

            periodic_limits.append(periodic_limits_item)

        recurring_payment_category = d.pop("recurringPaymentCategory", UNSET)

        vrp_configuration = cls(
            maximum_individual_amount=maximum_individual_amount,
            maximum_cumulative_amount=maximum_cumulative_amount,
            maximum_cumulative_number_of_payments=maximum_cumulative_number_of_payments,
            periodic_limits=periodic_limits,
            recurring_payment_category=recurring_payment_category,
        )

        vrp_configuration.additional_properties = d
        return vrp_configuration

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
