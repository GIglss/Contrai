from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CurrencyExchange")


@_attrs_define
class CurrencyExchange:
    """Provides details on the currrency exchange.

    Attributes:
        source_currency (Union[Unset, str]): Currency from which an amount is to be converted.
        target_currency (Union[Unset, str]): Currency to which an amount is to be converted.
        unit_currency (Union[Unset, str]): The currency in which the rate of exchange is expressed in a currency
            exchange. In the example 1GBP = xxxCUR, the unit currency is GBP.
        exchange_rate (Union[Unset, float]): The factor used for conversion of an amount from one currency to another.
            This reflects the price at which one currency was bought with another currency.
    """

    source_currency: Union[Unset, str] = UNSET
    target_currency: Union[Unset, str] = UNSET
    unit_currency: Union[Unset, str] = UNSET
    exchange_rate: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_currency = self.source_currency

        target_currency = self.target_currency

        unit_currency = self.unit_currency

        exchange_rate = self.exchange_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_currency is not UNSET:
            field_dict["sourceCurrency"] = source_currency
        if target_currency is not UNSET:
            field_dict["targetCurrency"] = target_currency
        if unit_currency is not UNSET:
            field_dict["unitCurrency"] = unit_currency
        if exchange_rate is not UNSET:
            field_dict["exchangeRate"] = exchange_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_currency = d.pop("sourceCurrency", UNSET)

        target_currency = d.pop("targetCurrency", UNSET)

        unit_currency = d.pop("unitCurrency", UNSET)

        exchange_rate = d.pop("exchangeRate", UNSET)

        currency_exchange = cls(
            source_currency=source_currency,
            target_currency=target_currency,
            unit_currency=unit_currency,
            exchange_rate=exchange_rate,
        )

        currency_exchange.additional_properties = d
        return currency_exchange

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
