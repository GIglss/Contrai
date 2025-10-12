from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.terminated_transaction_stream import TerminatedTransactionStream
    from ..models.transaction_stream import TransactionStream


T = TypeVar("T", bound="EnrichedWrapper")


@_attrs_define
class EnrichedWrapper:
    """Details of income and expenditure streams, identified by Yapily data services.

    Attributes:
        income_streams (list['TransactionStream']): Lists all possible income streams identified for the `Application
            User`.
        expenditure_streams (list['TransactionStream']): Lists all possible expenditure streams identified for the
            `Application User`.
        recently_terminated_income_streams (list['TerminatedTransactionStream']): A list of terminated transaction
            income streams
        recently_terminated_expenditure_streams (list['TerminatedTransactionStream']): A list of terminated transaction
            expenditure streams
    """

    income_streams: list["TransactionStream"]
    expenditure_streams: list["TransactionStream"]
    recently_terminated_income_streams: list["TerminatedTransactionStream"]
    recently_terminated_expenditure_streams: list["TerminatedTransactionStream"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        income_streams = []
        for income_streams_item_data in self.income_streams:
            income_streams_item = income_streams_item_data.to_dict()
            income_streams.append(income_streams_item)

        expenditure_streams = []
        for expenditure_streams_item_data in self.expenditure_streams:
            expenditure_streams_item = expenditure_streams_item_data.to_dict()
            expenditure_streams.append(expenditure_streams_item)

        recently_terminated_income_streams = []
        for recently_terminated_income_streams_item_data in self.recently_terminated_income_streams:
            recently_terminated_income_streams_item = recently_terminated_income_streams_item_data.to_dict()
            recently_terminated_income_streams.append(recently_terminated_income_streams_item)

        recently_terminated_expenditure_streams = []
        for recently_terminated_expenditure_streams_item_data in self.recently_terminated_expenditure_streams:
            recently_terminated_expenditure_streams_item = recently_terminated_expenditure_streams_item_data.to_dict()
            recently_terminated_expenditure_streams.append(recently_terminated_expenditure_streams_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incomeStreams": income_streams,
                "expenditureStreams": expenditure_streams,
                "recentlyTerminatedIncomeStreams": recently_terminated_income_streams,
                "recentlyTerminatedExpenditureStreams": recently_terminated_expenditure_streams,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.terminated_transaction_stream import TerminatedTransactionStream
        from ..models.transaction_stream import TransactionStream

        d = dict(src_dict)
        income_streams = []
        _income_streams = d.pop("incomeStreams")
        for income_streams_item_data in _income_streams:
            income_streams_item = TransactionStream.from_dict(income_streams_item_data)

            income_streams.append(income_streams_item)

        expenditure_streams = []
        _expenditure_streams = d.pop("expenditureStreams")
        for expenditure_streams_item_data in _expenditure_streams:
            expenditure_streams_item = TransactionStream.from_dict(expenditure_streams_item_data)

            expenditure_streams.append(expenditure_streams_item)

        recently_terminated_income_streams = []
        _recently_terminated_income_streams = d.pop("recentlyTerminatedIncomeStreams")
        for recently_terminated_income_streams_item_data in _recently_terminated_income_streams:
            recently_terminated_income_streams_item = TerminatedTransactionStream.from_dict(
                recently_terminated_income_streams_item_data
            )

            recently_terminated_income_streams.append(recently_terminated_income_streams_item)

        recently_terminated_expenditure_streams = []
        _recently_terminated_expenditure_streams = d.pop("recentlyTerminatedExpenditureStreams")
        for recently_terminated_expenditure_streams_item_data in _recently_terminated_expenditure_streams:
            recently_terminated_expenditure_streams_item = TerminatedTransactionStream.from_dict(
                recently_terminated_expenditure_streams_item_data
            )

            recently_terminated_expenditure_streams.append(recently_terminated_expenditure_streams_item)

        enriched_wrapper = cls(
            income_streams=income_streams,
            expenditure_streams=expenditure_streams,
            recently_terminated_income_streams=recently_terminated_income_streams,
            recently_terminated_expenditure_streams=recently_terminated_expenditure_streams,
        )

        enriched_wrapper.additional_properties = d
        return enriched_wrapper

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
