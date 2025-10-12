from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_balance import AccountBalance
    from ..models.amount_details import AmountDetails


T = TypeVar("T", bound="Balances")


@_attrs_define
class Balances:
    """
    Attributes:
        main_balance_amount (Union[Unset, AmountDetails]): __Mandatory__. Monetary Amount.
        balances (Union[Unset, list['AccountBalance']]):
    """

    main_balance_amount: Union[Unset, "AmountDetails"] = UNSET
    balances: Union[Unset, list["AccountBalance"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        main_balance_amount: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.main_balance_amount, Unset):
            main_balance_amount = self.main_balance_amount.to_dict()

        balances: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.balances, Unset):
            balances = []
            for balances_item_data in self.balances:
                balances_item = balances_item_data.to_dict()
                balances.append(balances_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if main_balance_amount is not UNSET:
            field_dict["mainBalanceAmount"] = main_balance_amount
        if balances is not UNSET:
            field_dict["balances"] = balances

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_balance import AccountBalance
        from ..models.amount_details import AmountDetails

        d = dict(src_dict)
        _main_balance_amount = d.pop("mainBalanceAmount", UNSET)
        main_balance_amount: Union[Unset, AmountDetails]
        if isinstance(_main_balance_amount, Unset):
            main_balance_amount = UNSET
        else:
            main_balance_amount = AmountDetails.from_dict(_main_balance_amount)

        balances = []
        _balances = d.pop("balances", UNSET)
        for balances_item_data in _balances or []:
            balances_item = AccountBalance.from_dict(balances_item_data)

            balances.append(balances_item)

        balances = cls(
            main_balance_amount=main_balance_amount,
            balances=balances,
        )

        balances.additional_properties = d
        return balances

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
