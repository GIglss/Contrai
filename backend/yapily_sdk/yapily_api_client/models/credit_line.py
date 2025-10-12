from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.credit_line_type import CreditLineType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amount_details import AmountDetails


T = TypeVar("T", bound="CreditLine")


@_attrs_define
class CreditLine:
    """__Mandatory__. Details whether the account has access to a credit line from an `Institution`.

    Attributes:
        type_ (Union[Unset, CreditLineType]): __Mandatory__. The type of credit that has been provided.
        credit_line_amount (Union[Unset, AmountDetails]): __Mandatory__. Monetary Amount.
    """

    type_: Union[Unset, CreditLineType] = UNSET
    credit_line_amount: Union[Unset, "AmountDetails"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        credit_line_amount: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.credit_line_amount, Unset):
            credit_line_amount = self.credit_line_amount.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if credit_line_amount is not UNSET:
            field_dict["creditLineAmount"] = credit_line_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amount_details import AmountDetails

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, CreditLineType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CreditLineType(_type_)

        _credit_line_amount = d.pop("creditLineAmount", UNSET)
        credit_line_amount: Union[Unset, AmountDetails]
        if isinstance(_credit_line_amount, Unset):
            credit_line_amount = UNSET
        else:
            credit_line_amount = AmountDetails.from_dict(_credit_line_amount)

        credit_line = cls(
            type_=type_,
            credit_line_amount=credit_line_amount,
        )

        credit_line.additional_properties = d
        return credit_line

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
