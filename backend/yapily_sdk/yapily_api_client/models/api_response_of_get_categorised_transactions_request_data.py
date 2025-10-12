from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_response_of_get_categorised_transactions_request_data_transactions_item import (
        ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItem,
    )


T = TypeVar("T", bound="ApiResponseOfGetCategorisedTransactionsRequestData")


@_attrs_define
class ApiResponseOfGetCategorisedTransactionsRequestData:
    """
    Attributes:
        transactions (Union[Unset, list['ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItem']]):
    """

    transactions: Union[Unset, list["ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transactions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.transactions, Unset):
            transactions = []
            for transactions_item_data in self.transactions:
                transactions_item = transactions_item_data.to_dict()
                transactions.append(transactions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transactions is not UNSET:
            field_dict["transactions"] = transactions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_response_of_get_categorised_transactions_request_data_transactions_item import (
            ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItem,
        )

        d = dict(src_dict)
        transactions = []
        _transactions = d.pop("transactions", UNSET)
        for transactions_item_data in _transactions or []:
            transactions_item = ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItem.from_dict(
                transactions_item_data
            )

            transactions.append(transactions_item)

        api_response_of_get_categorised_transactions_request_data = cls(
            transactions=transactions,
        )

        api_response_of_get_categorised_transactions_request_data.additional_properties = d
        return api_response_of_get_categorised_transactions_request_data

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
