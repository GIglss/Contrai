from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_balance import AccountBalance


T = TypeVar("T", bound="ConsolidatedAccountInformation")


@_attrs_define
class ConsolidatedAccountInformation:
    """Summary information regarding account balances of the overall account provided by the bank

    Attributes:
        id (Union[Unset, str]): Identifier of the consolidated account. When used in Get Account Transactions calls, the
            transactions between the sub-accounts will not be reported
        account_balances (Union[Unset, list['AccountBalance']]):
    """

    id: Union[Unset, str] = UNSET
    account_balances: Union[Unset, list["AccountBalance"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        account_balances: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.account_balances, Unset):
            account_balances = []
            for account_balances_item_data in self.account_balances:
                account_balances_item = account_balances_item_data.to_dict()
                account_balances.append(account_balances_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if account_balances is not UNSET:
            field_dict["accountBalances"] = account_balances

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_balance import AccountBalance

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        account_balances = []
        _account_balances = d.pop("accountBalances", UNSET)
        for account_balances_item_data in _account_balances or []:
            account_balances_item = AccountBalance.from_dict(account_balances_item_data)

            account_balances.append(account_balances_item)

        consolidated_account_information = cls(
            id=id,
            account_balances=account_balances,
        )

        consolidated_account_information.additional_properties = d
        return consolidated_account_information

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
