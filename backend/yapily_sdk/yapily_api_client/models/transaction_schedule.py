from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransactionSchedule")


@_attrs_define
class TransactionSchedule:
    """The frequency at which transactions occurred.

    Attributes:
        frequency (Union[Unset, str]): How often the transaction happens.  Can be 'Monthly', 'Twice monthly', 'Every two
            weeks', 'Every four weeks', 'Daily', 'Weekly', 'Every weekday', 'Twice daily', 'Twice every weekday' Example:
            Daily.
        detailed_frequency (Union[Unset, str]): When in the cycle the transaction occurs.  Can be 'Daily', 'Twice
            daily', 'Twice every weekday', 'Every weekday', 'Weekly on day n', 'Every two weeks on day n', 'Monthly on
            working day before day n of month', 'Monthly on last working day of month', 'Twice a month on 15th and last
            working day of month', 'Every four weeks on day n' Example: Daily.
        detailed_frequency_parameter (Union[Unset, float]): The n in detailedFrequency where there is one - for week-
            based frequencies, an integer from 0 to 6 where 0 is Monday or for month-based frequencies, an integer from 0 to
            27 where 0 is the first day of the month Example: 1.
    """

    frequency: Union[Unset, str] = UNSET
    detailed_frequency: Union[Unset, str] = UNSET
    detailed_frequency_parameter: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        frequency = self.frequency

        detailed_frequency = self.detailed_frequency

        detailed_frequency_parameter = self.detailed_frequency_parameter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if detailed_frequency is not UNSET:
            field_dict["detailedFrequency"] = detailed_frequency
        if detailed_frequency_parameter is not UNSET:
            field_dict["detailedFrequencyParameter"] = detailed_frequency_parameter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        frequency = d.pop("frequency", UNSET)

        detailed_frequency = d.pop("detailedFrequency", UNSET)

        detailed_frequency_parameter = d.pop("detailedFrequencyParameter", UNSET)

        transaction_schedule = cls(
            frequency=frequency,
            detailed_frequency=detailed_frequency,
            detailed_frequency_parameter=detailed_frequency_parameter,
        )

        transaction_schedule.additional_properties = d
        return transaction_schedule

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
