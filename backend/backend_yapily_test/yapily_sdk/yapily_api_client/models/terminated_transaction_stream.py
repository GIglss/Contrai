import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.enriched_transaction import EnrichedTransaction
    from ..models.transaction_schedule import TransactionSchedule


T = TypeVar("T", bound="TerminatedTransactionStream")


@_attrs_define
class TerminatedTransactionStream:
    """Terminated transaction stream generated as part of the financial profile for a User.

    Attributes:
        name (Union[Unset, str]): The name of the TransactionStream Example: Amazon Marketplace.
        transactions (Union[Unset, list['EnrichedTransaction']]): A list of Transactions from the transaction stream.
        transaction_schedule (Union[Unset, TransactionSchedule]): The frequency at which transactions occurred.
        schedule_consistency_score (Union[Unset, float]): The consistency of the transaction.  This is a number between
            0 and 1 with 1 being the most consistent schedule. Example: 0.44.
        next_expected_transaction_date (Union[Unset, datetime.date]): When is the transaction expected to occur next.
            Example: 2019-10-04.
        earliest_transaction_date (Union[Unset, datetime.date]): When is the first recorded transaction date Example:
            2020-04-24.
        most_recent_transaction_date (Union[Unset, datetime.date]): When is the most recent transaction date Example:
            2019-10-03.
        amount_consistency_score (Union[Unset, float]): The consistency of the amount of the transaction.  This is a
            number between 0 and 1 with 1 being the most consistent amount. Example: 0.74.
        average_amount (Union[Unset, float]): The average amount of the transaction stream Example: 19.708.
        missed_transactions (Union[Unset, int]): Missed transactions of transaction stream Example: 3.
    """

    name: Union[Unset, str] = UNSET
    transactions: Union[Unset, list["EnrichedTransaction"]] = UNSET
    transaction_schedule: Union[Unset, "TransactionSchedule"] = UNSET
    schedule_consistency_score: Union[Unset, float] = UNSET
    next_expected_transaction_date: Union[Unset, datetime.date] = UNSET
    earliest_transaction_date: Union[Unset, datetime.date] = UNSET
    most_recent_transaction_date: Union[Unset, datetime.date] = UNSET
    amount_consistency_score: Union[Unset, float] = UNSET
    average_amount: Union[Unset, float] = UNSET
    missed_transactions: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        transactions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.transactions, Unset):
            transactions = []
            for transactions_item_data in self.transactions:
                transactions_item = transactions_item_data.to_dict()
                transactions.append(transactions_item)

        transaction_schedule: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.transaction_schedule, Unset):
            transaction_schedule = self.transaction_schedule.to_dict()

        schedule_consistency_score = self.schedule_consistency_score

        next_expected_transaction_date: Union[Unset, str] = UNSET
        if not isinstance(self.next_expected_transaction_date, Unset):
            next_expected_transaction_date = self.next_expected_transaction_date.isoformat()

        earliest_transaction_date: Union[Unset, str] = UNSET
        if not isinstance(self.earliest_transaction_date, Unset):
            earliest_transaction_date = self.earliest_transaction_date.isoformat()

        most_recent_transaction_date: Union[Unset, str] = UNSET
        if not isinstance(self.most_recent_transaction_date, Unset):
            most_recent_transaction_date = self.most_recent_transaction_date.isoformat()

        amount_consistency_score = self.amount_consistency_score

        average_amount = self.average_amount

        missed_transactions = self.missed_transactions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if transactions is not UNSET:
            field_dict["transactions"] = transactions
        if transaction_schedule is not UNSET:
            field_dict["transactionSchedule"] = transaction_schedule
        if schedule_consistency_score is not UNSET:
            field_dict["scheduleConsistencyScore"] = schedule_consistency_score
        if next_expected_transaction_date is not UNSET:
            field_dict["nextExpectedTransactionDate"] = next_expected_transaction_date
        if earliest_transaction_date is not UNSET:
            field_dict["earliestTransactionDate"] = earliest_transaction_date
        if most_recent_transaction_date is not UNSET:
            field_dict["mostRecentTransactionDate"] = most_recent_transaction_date
        if amount_consistency_score is not UNSET:
            field_dict["amountConsistencyScore"] = amount_consistency_score
        if average_amount is not UNSET:
            field_dict["averageAmount"] = average_amount
        if missed_transactions is not UNSET:
            field_dict["missedTransactions"] = missed_transactions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.enriched_transaction import EnrichedTransaction
        from ..models.transaction_schedule import TransactionSchedule

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        transactions = []
        _transactions = d.pop("transactions", UNSET)
        for transactions_item_data in _transactions or []:
            transactions_item = EnrichedTransaction.from_dict(transactions_item_data)

            transactions.append(transactions_item)

        _transaction_schedule = d.pop("transactionSchedule", UNSET)
        transaction_schedule: Union[Unset, TransactionSchedule]
        if isinstance(_transaction_schedule, Unset):
            transaction_schedule = UNSET
        else:
            transaction_schedule = TransactionSchedule.from_dict(_transaction_schedule)

        schedule_consistency_score = d.pop("scheduleConsistencyScore", UNSET)

        _next_expected_transaction_date = d.pop("nextExpectedTransactionDate", UNSET)
        next_expected_transaction_date: Union[Unset, datetime.date]
        if isinstance(_next_expected_transaction_date, Unset):
            next_expected_transaction_date = UNSET
        else:
            next_expected_transaction_date = isoparse(_next_expected_transaction_date).date()

        _earliest_transaction_date = d.pop("earliestTransactionDate", UNSET)
        earliest_transaction_date: Union[Unset, datetime.date]
        if isinstance(_earliest_transaction_date, Unset):
            earliest_transaction_date = UNSET
        else:
            earliest_transaction_date = isoparse(_earliest_transaction_date).date()

        _most_recent_transaction_date = d.pop("mostRecentTransactionDate", UNSET)
        most_recent_transaction_date: Union[Unset, datetime.date]
        if isinstance(_most_recent_transaction_date, Unset):
            most_recent_transaction_date = UNSET
        else:
            most_recent_transaction_date = isoparse(_most_recent_transaction_date).date()

        amount_consistency_score = d.pop("amountConsistencyScore", UNSET)

        average_amount = d.pop("averageAmount", UNSET)

        missed_transactions = d.pop("missedTransactions", UNSET)

        terminated_transaction_stream = cls(
            name=name,
            transactions=transactions,
            transaction_schedule=transaction_schedule,
            schedule_consistency_score=schedule_consistency_score,
            next_expected_transaction_date=next_expected_transaction_date,
            earliest_transaction_date=earliest_transaction_date,
            most_recent_transaction_date=most_recent_transaction_date,
            amount_consistency_score=amount_consistency_score,
            average_amount=average_amount,
            missed_transactions=missed_transactions,
        )

        terminated_transaction_stream.additional_properties = d
        return terminated_transaction_stream

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
