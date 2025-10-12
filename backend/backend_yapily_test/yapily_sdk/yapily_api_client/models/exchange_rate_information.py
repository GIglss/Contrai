from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rate_type_enum import RateTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExchangeRateInformation")


@_attrs_define
class ExchangeRateInformation:
    """__Optional__. Used to provide details on the currency exchange rate and contract.

    Attributes:
        unit_currency (str): __Mandatory__. The currency in which the rate of exchange is expressed in a currency
            exchange. In the example 1GBP = xxxCUR, the unit currency is `GBP`.
        rate_type (RateTypeEnum): __Mandatory__. The type used to complete the currency exchange.
        rate (Union[Unset, float]): __Optional__. The factor used for conversion of an amount from one currency to
            another. This reflects the price at which one currency was bought with another currency.
        foreign_exchange_contract_reference (Union[Unset, str]): __Optional__. The unique and unambiguous reference to
            the foreign exchange contract agreed between the initiating party/creditor and the debtor agent.
    """

    unit_currency: str
    rate_type: RateTypeEnum
    rate: Union[Unset, float] = UNSET
    foreign_exchange_contract_reference: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unit_currency = self.unit_currency

        rate_type = self.rate_type.value

        rate = self.rate

        foreign_exchange_contract_reference = self.foreign_exchange_contract_reference

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unitCurrency": unit_currency,
                "rateType": rate_type,
            }
        )
        if rate is not UNSET:
            field_dict["rate"] = rate
        if foreign_exchange_contract_reference is not UNSET:
            field_dict["foreignExchangeContractReference"] = foreign_exchange_contract_reference

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        unit_currency = d.pop("unitCurrency")

        rate_type = RateTypeEnum(d.pop("rateType"))

        rate = d.pop("rate", UNSET)

        foreign_exchange_contract_reference = d.pop("foreignExchangeContractReference", UNSET)

        exchange_rate_information = cls(
            unit_currency=unit_currency,
            rate_type=rate_type,
            rate=rate,
            foreign_exchange_contract_reference=foreign_exchange_contract_reference,
        )

        exchange_rate_information.additional_properties = d
        return exchange_rate_information

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
