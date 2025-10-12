from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amount_details import AmountDetails


T = TypeVar("T", bound="PaymentChargeDetails")


@_attrs_define
class PaymentChargeDetails:
    """Details the charges that will apply to the payment.

    Attributes:
        charge_amount (Union[Unset, AmountDetails]): __Mandatory__. Monetary Amount.
        charge_type (Union[Unset, str]): __Mandatory__. Specifies the nature of the transaction charge e.g. (Bank
            transfer fees).
        charge_to (Union[Unset, str]): __Mandatory__. States which party of the payment bears the charges.
    """

    charge_amount: Union[Unset, "AmountDetails"] = UNSET
    charge_type: Union[Unset, str] = UNSET
    charge_to: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge_amount: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.charge_amount, Unset):
            charge_amount = self.charge_amount.to_dict()

        charge_type = self.charge_type

        charge_to = self.charge_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if charge_amount is not UNSET:
            field_dict["chargeAmount"] = charge_amount
        if charge_type is not UNSET:
            field_dict["chargeType"] = charge_type
        if charge_to is not UNSET:
            field_dict["chargeTo"] = charge_to

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

        charge_type = d.pop("chargeType", UNSET)

        charge_to = d.pop("chargeTo", UNSET)

        payment_charge_details = cls(
            charge_amount=charge_amount,
            charge_type=charge_type,
            charge_to=charge_to,
        )

        payment_charge_details.additional_properties = d
        return payment_charge_details

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
