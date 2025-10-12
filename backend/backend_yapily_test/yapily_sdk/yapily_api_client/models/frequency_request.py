from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.frequency_enum_extended import FrequencyEnumExtended
from ..types import UNSET, Unset

T = TypeVar("T", bound="FrequencyRequest")


@_attrs_define
class FrequencyRequest:
    """__Mandatory__. Defines the intervals at which payment should be made.

    Attributes:
        type_ (FrequencyEnumExtended): __Mandatory__. See [payment frequency](/guides/payments/payment-
            execution/periodic-payments/#payment-frequency) for more information
        interval_week (Union[Unset, int]): __Conditional__. See [payment frequency](/guides/payments/payment-
            execution/periodic-payments/#payment-frequency) for more information Example: 1.
        interval_month (Union[Unset, int]): __Conditional__. See [payment frequency](/guides/payments/payment-
            execution/periodic-payments/#payment-frequency) for more information Example: 1.
        execution_day (Union[Unset, int]): __Conditional__. See [payment frequency](/guides/payments/payment-
            execution/periodic-payments/#payment-frequency) for more information Example: 1.
    """

    type_: FrequencyEnumExtended
    interval_week: Union[Unset, int] = UNSET
    interval_month: Union[Unset, int] = UNSET
    execution_day: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        interval_week = self.interval_week

        interval_month = self.interval_month

        execution_day = self.execution_day

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if interval_week is not UNSET:
            field_dict["intervalWeek"] = interval_week
        if interval_month is not UNSET:
            field_dict["intervalMonth"] = interval_month
        if execution_day is not UNSET:
            field_dict["executionDay"] = execution_day

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = FrequencyEnumExtended(d.pop("type"))

        interval_week = d.pop("intervalWeek", UNSET)

        interval_month = d.pop("intervalMonth", UNSET)

        execution_day = d.pop("executionDay", UNSET)

        frequency_request = cls(
            type_=type_,
            interval_week=interval_week,
            interval_month=interval_month,
            execution_day=execution_day,
        )

        frequency_request.additional_properties = d
        return frequency_request

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
