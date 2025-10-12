import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_response_of_get_categorised_transactions_request_data_transactions_item_balance import (
        ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemBalance,
    )
    from ..models.api_response_of_get_categorised_transactions_request_data_transactions_item_enrichment import (
        ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemEnrichment,
    )
    from ..models.api_response_of_get_categorised_transactions_request_data_transactions_item_iso_bank_transaction_code import (
        ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemIsoBankTransactionCode,
    )
    from ..models.api_response_of_get_categorised_transactions_request_data_transactions_item_proprietary_bank_transaction_code import (
        ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemProprietaryBankTransactionCode,
    )
    from ..models.api_response_of_get_categorised_transactions_request_data_transactions_item_transaction_amount import (
        ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemTransactionAmount,
    )


T = TypeVar("T", bound="ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItem")


@_attrs_define
class ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItem:
    """
    Attributes:
        id (Union[Unset, str]):
        date (Union[Unset, str]):
        booking_date_time (Union[Unset, datetime.datetime]):
        value_date_time (Union[Unset, datetime.datetime]):
        status (Union[Unset, str]):
        amount (Union[Unset, int]):
        currency (Union[Unset, str]):
        transaction_amount (Union[Unset,
            ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemTransactionAmount]):
        reference (Union[Unset, str]):
        description (Union[Unset, str]):
        transaction_information (Union[Unset, list[str]]):
        proprietary_bank_transaction_code (Union[Unset,
            ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemProprietaryBankTransactionCode]):
        iso_bank_transaction_code (Union[Unset,
            ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemIsoBankTransactionCode]):
        balance (Union[Unset, ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemBalance]):
        enrichment (Union[Unset, ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemEnrichment]):
        hash_ (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    date: Union[Unset, str] = UNSET
    booking_date_time: Union[Unset, datetime.datetime] = UNSET
    value_date_time: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, str] = UNSET
    amount: Union[Unset, int] = UNSET
    currency: Union[Unset, str] = UNSET
    transaction_amount: Union[
        Unset, "ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemTransactionAmount"
    ] = UNSET
    reference: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    transaction_information: Union[Unset, list[str]] = UNSET
    proprietary_bank_transaction_code: Union[
        Unset, "ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemProprietaryBankTransactionCode"
    ] = UNSET
    iso_bank_transaction_code: Union[
        Unset, "ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemIsoBankTransactionCode"
    ] = UNSET
    balance: Union[Unset, "ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemBalance"] = UNSET
    enrichment: Union[Unset, "ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemEnrichment"] = UNSET
    hash_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        date = self.date

        booking_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.booking_date_time, Unset):
            booking_date_time = self.booking_date_time.isoformat()

        value_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.value_date_time, Unset):
            value_date_time = self.value_date_time.isoformat()

        status = self.status

        amount = self.amount

        currency = self.currency

        transaction_amount: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.transaction_amount, Unset):
            transaction_amount = self.transaction_amount.to_dict()

        reference = self.reference

        description = self.description

        transaction_information: Union[Unset, list[str]] = UNSET
        if not isinstance(self.transaction_information, Unset):
            transaction_information = self.transaction_information

        proprietary_bank_transaction_code: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.proprietary_bank_transaction_code, Unset):
            proprietary_bank_transaction_code = self.proprietary_bank_transaction_code.to_dict()

        iso_bank_transaction_code: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.iso_bank_transaction_code, Unset):
            iso_bank_transaction_code = self.iso_bank_transaction_code.to_dict()

        balance: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.balance, Unset):
            balance = self.balance.to_dict()

        enrichment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.enrichment, Unset):
            enrichment = self.enrichment.to_dict()

        hash_ = self.hash_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if date is not UNSET:
            field_dict["date"] = date
        if booking_date_time is not UNSET:
            field_dict["bookingDateTime"] = booking_date_time
        if value_date_time is not UNSET:
            field_dict["valueDateTime"] = value_date_time
        if status is not UNSET:
            field_dict["status"] = status
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if transaction_amount is not UNSET:
            field_dict["transactionAmount"] = transaction_amount
        if reference is not UNSET:
            field_dict["reference"] = reference
        if description is not UNSET:
            field_dict["description"] = description
        if transaction_information is not UNSET:
            field_dict["transactionInformation"] = transaction_information
        if proprietary_bank_transaction_code is not UNSET:
            field_dict["proprietaryBankTransactionCode"] = proprietary_bank_transaction_code
        if iso_bank_transaction_code is not UNSET:
            field_dict["isoBankTransactionCode"] = iso_bank_transaction_code
        if balance is not UNSET:
            field_dict["balance"] = balance
        if enrichment is not UNSET:
            field_dict["enrichment"] = enrichment
        if hash_ is not UNSET:
            field_dict["hash"] = hash_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_response_of_get_categorised_transactions_request_data_transactions_item_balance import (
            ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemBalance,
        )
        from ..models.api_response_of_get_categorised_transactions_request_data_transactions_item_enrichment import (
            ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemEnrichment,
        )
        from ..models.api_response_of_get_categorised_transactions_request_data_transactions_item_iso_bank_transaction_code import (
            ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemIsoBankTransactionCode,
        )
        from ..models.api_response_of_get_categorised_transactions_request_data_transactions_item_proprietary_bank_transaction_code import (
            ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemProprietaryBankTransactionCode,
        )
        from ..models.api_response_of_get_categorised_transactions_request_data_transactions_item_transaction_amount import (
            ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemTransactionAmount,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        date = d.pop("date", UNSET)

        _booking_date_time = d.pop("bookingDateTime", UNSET)
        booking_date_time: Union[Unset, datetime.datetime]
        if isinstance(_booking_date_time, Unset):
            booking_date_time = UNSET
        else:
            booking_date_time = isoparse(_booking_date_time)

        _value_date_time = d.pop("valueDateTime", UNSET)
        value_date_time: Union[Unset, datetime.datetime]
        if isinstance(_value_date_time, Unset):
            value_date_time = UNSET
        else:
            value_date_time = isoparse(_value_date_time)

        status = d.pop("status", UNSET)

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        _transaction_amount = d.pop("transactionAmount", UNSET)
        transaction_amount: Union[
            Unset, ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemTransactionAmount
        ]
        if isinstance(_transaction_amount, Unset):
            transaction_amount = UNSET
        else:
            transaction_amount = (
                ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemTransactionAmount.from_dict(
                    _transaction_amount
                )
            )

        reference = d.pop("reference", UNSET)

        description = d.pop("description", UNSET)

        transaction_information = cast(list[str], d.pop("transactionInformation", UNSET))

        _proprietary_bank_transaction_code = d.pop("proprietaryBankTransactionCode", UNSET)
        proprietary_bank_transaction_code: Union[
            Unset, ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemProprietaryBankTransactionCode
        ]
        if isinstance(_proprietary_bank_transaction_code, Unset):
            proprietary_bank_transaction_code = UNSET
        else:
            proprietary_bank_transaction_code = ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemProprietaryBankTransactionCode.from_dict(
                _proprietary_bank_transaction_code
            )

        _iso_bank_transaction_code = d.pop("isoBankTransactionCode", UNSET)
        iso_bank_transaction_code: Union[
            Unset, ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemIsoBankTransactionCode
        ]
        if isinstance(_iso_bank_transaction_code, Unset):
            iso_bank_transaction_code = UNSET
        else:
            iso_bank_transaction_code = (
                ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemIsoBankTransactionCode.from_dict(
                    _iso_bank_transaction_code
                )
            )

        _balance = d.pop("balance", UNSET)
        balance: Union[Unset, ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemBalance]
        if isinstance(_balance, Unset):
            balance = UNSET
        else:
            balance = ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemBalance.from_dict(_balance)

        _enrichment = d.pop("enrichment", UNSET)
        enrichment: Union[Unset, ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemEnrichment]
        if isinstance(_enrichment, Unset):
            enrichment = UNSET
        else:
            enrichment = ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemEnrichment.from_dict(
                _enrichment
            )

        hash_ = d.pop("hash", UNSET)

        api_response_of_get_categorised_transactions_request_data_transactions_item = cls(
            id=id,
            date=date,
            booking_date_time=booking_date_time,
            value_date_time=value_date_time,
            status=status,
            amount=amount,
            currency=currency,
            transaction_amount=transaction_amount,
            reference=reference,
            description=description,
            transaction_information=transaction_information,
            proprietary_bank_transaction_code=proprietary_bank_transaction_code,
            iso_bank_transaction_code=iso_bank_transaction_code,
            balance=balance,
            enrichment=enrichment,
            hash_=hash_,
        )

        api_response_of_get_categorised_transactions_request_data_transactions_item.additional_properties = d
        return api_response_of_get_categorised_transactions_request_data_transactions_item

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
