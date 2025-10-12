import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnrichedTransaction")


@_attrs_define
class EnrichedTransaction:
    """Details of the transaction, identified by Yapily data services.

    Attributes:
        transaction_id (Union[Unset, str]): Unique identifier of the transaction Example:
            c51e3bee-36fb-4c0a-8441-d6ba2056fe87.
        transaction_information (Union[Unset, str]): Information for the transaction Example: Amazon Marketplace.
        amount (Union[Unset, float]): Monetary amount. Example: 21.99.
        institution (Union[Unset, str]): The `Institution` that the transaction is sent to. Example: starling.
        booking_date_time (Union[Unset, datetime.datetime]): Date and time of when a transaction entry occured and was
            posted to the account servicer's books. Example: 2020-04-24T00:30:19.951Z.
    """

    transaction_id: Union[Unset, str] = UNSET
    transaction_information: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    institution: Union[Unset, str] = UNSET
    booking_date_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transaction_id = self.transaction_id

        transaction_information = self.transaction_information

        amount = self.amount

        institution = self.institution

        booking_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.booking_date_time, Unset):
            booking_date_time = self.booking_date_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id
        if transaction_information is not UNSET:
            field_dict["transactionInformation"] = transaction_information
        if amount is not UNSET:
            field_dict["amount"] = amount
        if institution is not UNSET:
            field_dict["institution"] = institution
        if booking_date_time is not UNSET:
            field_dict["bookingDateTime"] = booking_date_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        transaction_id = d.pop("transactionId", UNSET)

        transaction_information = d.pop("transactionInformation", UNSET)

        amount = d.pop("amount", UNSET)

        institution = d.pop("institution", UNSET)

        _booking_date_time = d.pop("bookingDateTime", UNSET)
        booking_date_time: Union[Unset, datetime.datetime]
        if isinstance(_booking_date_time, Unset):
            booking_date_time = UNSET
        else:
            booking_date_time = isoparse(_booking_date_time)

        enriched_transaction = cls(
            transaction_id=transaction_id,
            transaction_information=transaction_information,
            amount=amount,
            institution=institution,
            booking_date_time=booking_date_time,
        )

        enriched_transaction.additional_properties = d
        return enriched_transaction

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
