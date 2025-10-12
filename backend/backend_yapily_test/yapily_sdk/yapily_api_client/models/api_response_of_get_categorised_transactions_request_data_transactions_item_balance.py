from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_response_of_get_categorised_transactions_request_data_transactions_item_balance_balance_amount import (
        ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemBalanceBalanceAmount,
    )


T = TypeVar("T", bound="ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemBalance")


@_attrs_define
class ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemBalance:
    """
    Attributes:
        type_ (Union[Unset, str]):
        balance_amount (Union[Unset,
            ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemBalanceBalanceAmount]):
    """

    type_: Union[Unset, str] = UNSET
    balance_amount: Union[
        Unset, "ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemBalanceBalanceAmount"
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

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
        from ..models.api_response_of_get_categorised_transactions_request_data_transactions_item_balance_balance_amount import (
            ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemBalanceBalanceAmount,
        )

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        _balance_amount = d.pop("balanceAmount", UNSET)
        balance_amount: Union[
            Unset, ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemBalanceBalanceAmount
        ]
        if isinstance(_balance_amount, Unset):
            balance_amount = UNSET
        else:
            balance_amount = (
                ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemBalanceBalanceAmount.from_dict(
                    _balance_amount
                )
            )

        api_response_of_get_categorised_transactions_request_data_transactions_item_balance = cls(
            type_=type_,
            balance_amount=balance_amount,
        )

        api_response_of_get_categorised_transactions_request_data_transactions_item_balance.additional_properties = d
        return api_response_of_get_categorised_transactions_request_data_transactions_item_balance

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
