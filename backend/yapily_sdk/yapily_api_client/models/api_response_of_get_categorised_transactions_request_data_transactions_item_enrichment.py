from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_response_of_get_categorised_transactions_request_data_transactions_item_enrichment_categorisation import (
        ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemEnrichmentCategorisation,
    )
    from ..models.api_response_of_get_categorised_transactions_request_data_transactions_item_enrichment_merchant import (
        ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemEnrichmentMerchant,
    )
    from ..models.api_response_of_get_categorised_transactions_request_data_transactions_item_enrichment_transaction_hash import (
        ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemEnrichmentTransactionHash,
    )


T = TypeVar("T", bound="ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemEnrichment")


@_attrs_define
class ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemEnrichment:
    """
    Attributes:
        categorisation (Union[Unset,
            ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemEnrichmentCategorisation]):
        recurrence (Union[Unset, str]):
        transaction_hash (Union[Unset,
            ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemEnrichmentTransactionHash]):
        merchant (Union[Unset, ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemEnrichmentMerchant]):
        payment_processor (Union[Unset, str]):
    """

    categorisation: Union[
        Unset, "ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemEnrichmentCategorisation"
    ] = UNSET
    recurrence: Union[Unset, str] = UNSET
    transaction_hash: Union[
        Unset, "ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemEnrichmentTransactionHash"
    ] = UNSET
    merchant: Union[Unset, "ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemEnrichmentMerchant"] = (
        UNSET
    )
    payment_processor: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        categorisation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.categorisation, Unset):
            categorisation = self.categorisation.to_dict()

        recurrence = self.recurrence

        transaction_hash: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.transaction_hash, Unset):
            transaction_hash = self.transaction_hash.to_dict()

        merchant: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        payment_processor = self.payment_processor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if categorisation is not UNSET:
            field_dict["categorisation"] = categorisation
        if recurrence is not UNSET:
            field_dict["recurrence"] = recurrence
        if transaction_hash is not UNSET:
            field_dict["transactionHash"] = transaction_hash
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if payment_processor is not UNSET:
            field_dict["paymentProcessor"] = payment_processor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_response_of_get_categorised_transactions_request_data_transactions_item_enrichment_categorisation import (
            ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemEnrichmentCategorisation,
        )
        from ..models.api_response_of_get_categorised_transactions_request_data_transactions_item_enrichment_merchant import (
            ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemEnrichmentMerchant,
        )
        from ..models.api_response_of_get_categorised_transactions_request_data_transactions_item_enrichment_transaction_hash import (
            ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemEnrichmentTransactionHash,
        )

        d = dict(src_dict)
        _categorisation = d.pop("categorisation", UNSET)
        categorisation: Union[
            Unset, ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemEnrichmentCategorisation
        ]
        if isinstance(_categorisation, Unset):
            categorisation = UNSET
        else:
            categorisation = (
                ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemEnrichmentCategorisation.from_dict(
                    _categorisation
                )
            )

        recurrence = d.pop("recurrence", UNSET)

        _transaction_hash = d.pop("transactionHash", UNSET)
        transaction_hash: Union[
            Unset, ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemEnrichmentTransactionHash
        ]
        if isinstance(_transaction_hash, Unset):
            transaction_hash = UNSET
        else:
            transaction_hash = (
                ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemEnrichmentTransactionHash.from_dict(
                    _transaction_hash
                )
            )

        _merchant = d.pop("merchant", UNSET)
        merchant: Union[Unset, ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemEnrichmentMerchant]
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemEnrichmentMerchant.from_dict(
                _merchant
            )

        payment_processor = d.pop("paymentProcessor", UNSET)

        api_response_of_get_categorised_transactions_request_data_transactions_item_enrichment = cls(
            categorisation=categorisation,
            recurrence=recurrence,
            transaction_hash=transaction_hash,
            merchant=merchant,
            payment_processor=payment_processor,
        )

        api_response_of_get_categorised_transactions_request_data_transactions_item_enrichment.additional_properties = d
        return api_response_of_get_categorised_transactions_request_data_transactions_item_enrichment

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
