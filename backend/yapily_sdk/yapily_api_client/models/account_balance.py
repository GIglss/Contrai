import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.account_balance_type import AccountBalanceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amount_details import AmountDetails
    from ..models.credit_line import CreditLine


T = TypeVar("T", bound="AccountBalance")


@_attrs_define
class AccountBalance:
    """
    Attributes:
        type_ (Union[Unset, AccountBalanceType]): Specifies the type of the stated account balance.
        date_time (Union[Unset, datetime.datetime]): Date and time of the reported balance.
        balance_amount (Union[Unset, AmountDetails]): __Mandatory__. Monetary Amount.
        credit_line_included (Union[Unset, bool]): __Optional__. Indicates whether any credit lines are included in the
            balance.
        credit_lines (Union[Unset, list['CreditLine']]): __Optional__. Specifies the type of balance.
    """

    type_: Union[Unset, AccountBalanceType] = UNSET
    date_time: Union[Unset, datetime.datetime] = UNSET
    balance_amount: Union[Unset, "AmountDetails"] = UNSET
    credit_line_included: Union[Unset, bool] = UNSET
    credit_lines: Union[Unset, list["CreditLine"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        date_time: Union[Unset, str] = UNSET
        if not isinstance(self.date_time, Unset):
            date_time = self.date_time.isoformat()

        balance_amount: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.balance_amount, Unset):
            balance_amount = self.balance_amount.to_dict()

        credit_line_included = self.credit_line_included

        credit_lines: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.credit_lines, Unset):
            credit_lines = []
            for credit_lines_item_data in self.credit_lines:
                credit_lines_item = credit_lines_item_data.to_dict()
                credit_lines.append(credit_lines_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if date_time is not UNSET:
            field_dict["dateTime"] = date_time
        if balance_amount is not UNSET:
            field_dict["balanceAmount"] = balance_amount
        if credit_line_included is not UNSET:
            field_dict["creditLineIncluded"] = credit_line_included
        if credit_lines is not UNSET:
            field_dict["creditLines"] = credit_lines

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amount_details import AmountDetails
        from ..models.credit_line import CreditLine

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, AccountBalanceType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AccountBalanceType(_type_)

        _date_time = d.pop("dateTime", UNSET)
        date_time: Union[Unset, datetime.datetime]
        if isinstance(_date_time, Unset):
            date_time = UNSET
        else:
            date_time = isoparse(_date_time)

        _balance_amount = d.pop("balanceAmount", UNSET)
        balance_amount: Union[Unset, AmountDetails]
        if isinstance(_balance_amount, Unset):
            balance_amount = UNSET
        else:
            balance_amount = AmountDetails.from_dict(_balance_amount)

        credit_line_included = d.pop("creditLineIncluded", UNSET)

        credit_lines = []
        _credit_lines = d.pop("creditLines", UNSET)
        for credit_lines_item_data in _credit_lines or []:
            credit_lines_item = CreditLine.from_dict(credit_lines_item_data)

            credit_lines.append(credit_lines_item)

        account_balance = cls(
            type_=type_,
            date_time=date_time,
            balance_amount=balance_amount,
            credit_line_included=credit_line_included,
            credit_lines=credit_lines,
        )

        account_balance.additional_properties = d
        return account_balance

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
