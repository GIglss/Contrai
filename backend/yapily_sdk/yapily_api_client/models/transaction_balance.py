from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_balance_type import AccountBalanceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amount_details import AmountDetails


T = TypeVar("T", bound="TransactionBalance")


@_attrs_define
class TransactionBalance:
    """
    Attributes:
        type_ (Union[Unset, AccountBalanceType]): Specifies the type of the stated account balance.
        balance_amount (Union[Unset, AmountDetails]): __Mandatory__. Monetary Amount.
    """

    type_: Union[Unset, AccountBalanceType] = UNSET
    balance_amount: Union[Unset, "AmountDetails"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        balance_amount: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.balance_amount, Unset):
            balance_amount = self.balance_amount.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if balance_amount is not UNSET:
            field_dict["balanceAmount"] = balance_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amount_details import AmountDetails

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, AccountBalanceType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AccountBalanceType(_type_)

        _balance_amount = d.pop("balanceAmount", UNSET)
        balance_amount: Union[Unset, AmountDetails]
        if isinstance(_balance_amount, Unset):
            balance_amount = UNSET
        else:
            balance_amount = AmountDetails.from_dict(_balance_amount)

        transaction_balance = cls(
            type_=type_,
            balance_amount=balance_amount,
        )

        transaction_balance.additional_properties = d
        return transaction_balance

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
