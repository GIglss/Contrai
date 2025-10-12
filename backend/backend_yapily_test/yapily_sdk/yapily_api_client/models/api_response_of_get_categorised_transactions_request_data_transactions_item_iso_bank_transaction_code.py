from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_response_of_get_categorised_transactions_request_data_transactions_item_iso_bank_transaction_code_domain_code import (
        ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemIsoBankTransactionCodeDomainCode,
    )
    from ..models.api_response_of_get_categorised_transactions_request_data_transactions_item_iso_bank_transaction_code_family_code import (
        ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemIsoBankTransactionCodeFamilyCode,
    )
    from ..models.api_response_of_get_categorised_transactions_request_data_transactions_item_iso_bank_transaction_code_sub_family_code import (
        ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemIsoBankTransactionCodeSubFamilyCode,
    )


T = TypeVar("T", bound="ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemIsoBankTransactionCode")


@_attrs_define
class ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemIsoBankTransactionCode:
    """
    Attributes:
        domain_code (Union[Unset,
            ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemIsoBankTransactionCodeDomainCode]):
        family_code (Union[Unset,
            ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemIsoBankTransactionCodeFamilyCode]):
        sub_family_code (Union[Unset,
            ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemIsoBankTransactionCodeSubFamilyCode]):
    """

    domain_code: Union[
        Unset, "ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemIsoBankTransactionCodeDomainCode"
    ] = UNSET
    family_code: Union[
        Unset, "ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemIsoBankTransactionCodeFamilyCode"
    ] = UNSET
    sub_family_code: Union[
        Unset, "ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemIsoBankTransactionCodeSubFamilyCode"
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_code: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.domain_code, Unset):
            domain_code = self.domain_code.to_dict()

        family_code: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.family_code, Unset):
            family_code = self.family_code.to_dict()

        sub_family_code: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sub_family_code, Unset):
            sub_family_code = self.sub_family_code.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain_code is not UNSET:
            field_dict["domainCode"] = domain_code
        if family_code is not UNSET:
            field_dict["familyCode"] = family_code
        if sub_family_code is not UNSET:
            field_dict["subFamilyCode"] = sub_family_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_response_of_get_categorised_transactions_request_data_transactions_item_iso_bank_transaction_code_domain_code import (
            ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemIsoBankTransactionCodeDomainCode,
        )
        from ..models.api_response_of_get_categorised_transactions_request_data_transactions_item_iso_bank_transaction_code_family_code import (
            ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemIsoBankTransactionCodeFamilyCode,
        )
        from ..models.api_response_of_get_categorised_transactions_request_data_transactions_item_iso_bank_transaction_code_sub_family_code import (
            ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemIsoBankTransactionCodeSubFamilyCode,
        )

        d = dict(src_dict)
        _domain_code = d.pop("domainCode", UNSET)
        domain_code: Union[
            Unset, ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemIsoBankTransactionCodeDomainCode
        ]
        if isinstance(_domain_code, Unset):
            domain_code = UNSET
        else:
            domain_code = ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemIsoBankTransactionCodeDomainCode.from_dict(
                _domain_code
            )

        _family_code = d.pop("familyCode", UNSET)
        family_code: Union[
            Unset, ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemIsoBankTransactionCodeFamilyCode
        ]
        if isinstance(_family_code, Unset):
            family_code = UNSET
        else:
            family_code = ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemIsoBankTransactionCodeFamilyCode.from_dict(
                _family_code
            )

        _sub_family_code = d.pop("subFamilyCode", UNSET)
        sub_family_code: Union[
            Unset, ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemIsoBankTransactionCodeSubFamilyCode
        ]
        if isinstance(_sub_family_code, Unset):
            sub_family_code = UNSET
        else:
            sub_family_code = ApiResponseOfGetCategorisedTransactionsRequestDataTransactionsItemIsoBankTransactionCodeSubFamilyCode.from_dict(
                _sub_family_code
            )

        api_response_of_get_categorised_transactions_request_data_transactions_item_iso_bank_transaction_code = cls(
            domain_code=domain_code,
            family_code=family_code,
            sub_family_code=sub_family_code,
        )

        api_response_of_get_categorised_transactions_request_data_transactions_item_iso_bank_transaction_code.additional_properties = d
        return api_response_of_get_categorised_transactions_request_data_transactions_item_iso_bank_transaction_code

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
