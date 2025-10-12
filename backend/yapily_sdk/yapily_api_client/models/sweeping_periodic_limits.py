from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.amount_details import AmountDetails


T = TypeVar("T", bound="SweepingPeriodicLimits")


@_attrs_define
class SweepingPeriodicLimits:
    """
    Attributes:
        total_max_amount (AmountDetails): __Mandatory__. Monetary Amount.
        frequency (str): __Mandatory__. Frequency for which the payment limits are enforced. Allowed values are [DAILY,
            WEEKLY, EVERY_TWO_WEEKS, MONTHLY, YEARLY].
        alignment (str): __Mandatory__. Period alignment for which the payment limits are enforced. Allowed values are
            [CONSENT, CALENDAR]. If CONSENT, then period starts on consent creation date. If CALENDAR, then period lines up
            with the frequency e.g. WEEKLY period will begin at start of the week in question.
    """

    total_max_amount: "AmountDetails"
    frequency: str
    alignment: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_max_amount = self.total_max_amount.to_dict()

        frequency = self.frequency

        alignment = self.alignment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalMaxAmount": total_max_amount,
                "frequency": frequency,
                "alignment": alignment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amount_details import AmountDetails

        d = dict(src_dict)
        total_max_amount = AmountDetails.from_dict(d.pop("totalMaxAmount"))

        frequency = d.pop("frequency")

        alignment = d.pop("alignment")

        sweeping_periodic_limits = cls(
            total_max_amount=total_max_amount,
            frequency=frequency,
            alignment=alignment,
        )

        sweeping_periodic_limits.additional_properties = d
        return sweeping_periodic_limits

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
