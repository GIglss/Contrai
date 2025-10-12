from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amount_details import AmountDetails


T = TypeVar("T", bound="TransactionChargeDetails")


@_attrs_define
class TransactionChargeDetails:
    """Details the charges that will apply to the transaction.

    Attributes:
        charge_amount (Union[Unset, AmountDetails]): __Mandatory__. Monetary Amount.
    """

    charge_amount: Union[Unset, "AmountDetails"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge_amount: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.charge_amount, Unset):
            charge_amount = self.charge_amount.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if charge_amount is not UNSET:
            field_dict["chargeAmount"] = charge_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amount_details import AmountDetails

        d = dict(src_dict)
        _charge_amount = d.pop("chargeAmount", UNSET)
        charge_amount: Union[Unset, AmountDetails]
        if isinstance(_charge_amount, Unset):
            charge_amount = UNSET
        else:
            charge_amount = AmountDetails.from_dict(_charge_amount)

        transaction_charge_details = cls(
            charge_amount=charge_amount,
        )

        transaction_charge_details.additional_properties = d
        return transaction_charge_details

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
