from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alignment_enum import AlignmentEnum
from ..models.frequency_enum import FrequencyEnum

if TYPE_CHECKING:
    from ..models.amount_details import AmountDetails


T = TypeVar("T", bound="VrpPeriodicLimit")


@_attrs_define
class VrpPeriodicLimit:
    """
    Attributes:
        maximum_amount (AmountDetails): __Mandatory__. Monetary Amount.
        frequency (FrequencyEnum): __Mandatory__. Frequency for which the payment limits are enforced. Allowed values
            are [MONTHLY].
        alignment (AlignmentEnum): __Mandatory__. Period alignment for which the payment limits are enforced. Allowed
            values are [CONSENT, CALENDAR]. If CONSENT, then period starts on consent creation date. If CALENDAR, then
            period lines up with the frequency e.g. WEEKLY period will begin at start of the week in question.
    """

    maximum_amount: "AmountDetails"
    frequency: FrequencyEnum
    alignment: AlignmentEnum
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        maximum_amount = self.maximum_amount.to_dict()

        frequency = self.frequency.value

        alignment = self.alignment.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "maximumAmount": maximum_amount,
                "frequency": frequency,
                "alignment": alignment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amount_details import AmountDetails

        d = dict(src_dict)
        maximum_amount = AmountDetails.from_dict(d.pop("maximumAmount"))

        frequency = FrequencyEnum(d.pop("frequency"))

        alignment = AlignmentEnum(d.pop("alignment"))

        vrp_periodic_limit = cls(
            maximum_amount=maximum_amount,
            frequency=frequency,
            alignment=alignment,
        )

        vrp_periodic_limit.additional_properties = d
        return vrp_periodic_limit

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
