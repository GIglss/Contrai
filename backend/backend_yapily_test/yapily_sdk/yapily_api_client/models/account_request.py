import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.feature_enum import FeatureEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_info import AccountInfo


T = TypeVar("T", bound="AccountRequest")


@_attrs_define
class AccountRequest:
    """__Conditional__. Used to further specify details of the `Consent` to request <br><br>Conditions:<ol><li>Mandatory to
    specify the individual scopes to request from the user at the `Institution` for an account
    authorisation</li><li>Mandatory to specify an expiry time on the created `Consent` at which time will render it
    unusable</li><li>Mandatory to specify the date range that the created `Consent` will be able to access transactions
    for (given the range is support for the `Institution`)</li></ol>

        Attributes:
            transaction_from (Union[Unset, datetime.datetime]): __Optional__. Specifies the earliest date of the transaction
                records to be returned.<br><br> You must supply this field to retrieve transactions older than 90 days for banks
                accessed via the the [CBI Globe Gateway](https://docs.yapily.com/pages/data/financial-data-resources/data-
                restrictions/#cbi-globe-gateway). Example: 2020-01-01T00:00:00Z.
            transaction_to (Union[Unset, datetime.datetime]): __Optional__. Specifies the latest date of the transaction
                records to be returned. Example: 2021-01-01T00:00:00Z.
            expires_at (Union[Unset, datetime.datetime]): __Optional__. Used to set a hard date for when the user's
                associated `Consent` will expire.<br><br>**Note**: If this supported by the bank, specifying this is property is
                opting out of having a long-lived consent that can be perpetually re-authorised by the user. This will add an
                `expiresAt` field on the `Consent` object which will render it unusable after this date.<br><br>**Note**: This
                is not supported by every `Institution`. In such case, the request will not fail but the property will be
                ignored and the created `Consent` will not have an expiry date. Example: 2025-01-01T00:00:00Z.
            account_identifiers (Union[Unset, AccountInfo]): __Conditional__. Used to create a request for the balance of
                the account specified. Once the user authorises the request, only the balance can be obtained by executing [GET
                Account Balances](./#get-account-balances).<br><br> This can be specified in conjunction with
                `accountIdentifiersForTransaction` to generate a `Consent` that can both access the accounts balance and
                transactions.
            account_identifiers_for_transaction (Union[Unset, list['AccountInfo']]): __Conditional__. Used to create a
                request for the transactions of the account specified. Once the user authorises the request, only the
                transactions can be obtained by executing [GET Account Transactions](./#get-account-transactions). <br><br>This
                can be specified in conjunction with `accountIdentifiersForBalance` to generate a `Consent` that can both access
                the accounts balance and transactions.
            account_identifiers_for_balance (Union[Unset, list['AccountInfo']]): __Conditional__. Used to create a request
                for the balance of the account specified. Once the user authorises the request, only the balance can be obtained
                by executing [GET Account Balances](./#get-account-balances).<br><br> This can be specified in conjunction with
                `accountIdentifiersForTransaction` to generate a `Consent` that can both access the accounts balance and
                transactions.
            feature_scope (Union[Unset, list[FeatureEnum]]): __Optional__. Used to granularly specify the set of features
                that the user will give their consent for when requesting access to their account information. Depending on the
                `Institution`, this may also populate a consent screen which list these scopes before the user
                authorises.<br><br>This endpoint accepts allow all [Financial Data Features](/guides/financial-
                data/features/#feature-list) that the `Institution` supports.To find out which scopes an `Institution` supports,
                check [GET Institution](./#get-institution).
    """

    transaction_from: Union[Unset, datetime.datetime] = UNSET
    transaction_to: Union[Unset, datetime.datetime] = UNSET
    expires_at: Union[Unset, datetime.datetime] = UNSET
    account_identifiers: Union[Unset, "AccountInfo"] = UNSET
    account_identifiers_for_transaction: Union[Unset, list["AccountInfo"]] = UNSET
    account_identifiers_for_balance: Union[Unset, list["AccountInfo"]] = UNSET
    feature_scope: Union[Unset, list[FeatureEnum]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transaction_from: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_from, Unset):
            transaction_from = self.transaction_from.isoformat()

        transaction_to: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_to, Unset):
            transaction_to = self.transaction_to.isoformat()

        expires_at: Union[Unset, str] = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        account_identifiers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.account_identifiers, Unset):
            account_identifiers = self.account_identifiers.to_dict()

        account_identifiers_for_transaction: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.account_identifiers_for_transaction, Unset):
            account_identifiers_for_transaction = []
            for account_identifiers_for_transaction_item_data in self.account_identifiers_for_transaction:
                account_identifiers_for_transaction_item = account_identifiers_for_transaction_item_data.to_dict()
                account_identifiers_for_transaction.append(account_identifiers_for_transaction_item)

        account_identifiers_for_balance: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.account_identifiers_for_balance, Unset):
            account_identifiers_for_balance = []
            for account_identifiers_for_balance_item_data in self.account_identifiers_for_balance:
                account_identifiers_for_balance_item = account_identifiers_for_balance_item_data.to_dict()
                account_identifiers_for_balance.append(account_identifiers_for_balance_item)

        feature_scope: Union[Unset, list[str]] = UNSET
        if not isinstance(self.feature_scope, Unset):
            feature_scope = []
            for feature_scope_item_data in self.feature_scope:
                feature_scope_item = feature_scope_item_data.value
                feature_scope.append(feature_scope_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transaction_from is not UNSET:
            field_dict["transactionFrom"] = transaction_from
        if transaction_to is not UNSET:
            field_dict["transactionTo"] = transaction_to
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if account_identifiers is not UNSET:
            field_dict["accountIdentifiers"] = account_identifiers
        if account_identifiers_for_transaction is not UNSET:
            field_dict["accountIdentifiersForTransaction"] = account_identifiers_for_transaction
        if account_identifiers_for_balance is not UNSET:
            field_dict["accountIdentifiersForBalance"] = account_identifiers_for_balance
        if feature_scope is not UNSET:
            field_dict["featureScope"] = feature_scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_info import AccountInfo

        d = dict(src_dict)
        _transaction_from = d.pop("transactionFrom", UNSET)
        transaction_from: Union[Unset, datetime.datetime]
        if isinstance(_transaction_from, Unset):
            transaction_from = UNSET
        else:
            transaction_from = isoparse(_transaction_from)

        _transaction_to = d.pop("transactionTo", UNSET)
        transaction_to: Union[Unset, datetime.datetime]
        if isinstance(_transaction_to, Unset):
            transaction_to = UNSET
        else:
            transaction_to = isoparse(_transaction_to)

        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: Union[Unset, datetime.datetime]
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = isoparse(_expires_at)

        _account_identifiers = d.pop("accountIdentifiers", UNSET)
        account_identifiers: Union[Unset, AccountInfo]
        if isinstance(_account_identifiers, Unset):
            account_identifiers = UNSET
        else:
            account_identifiers = AccountInfo.from_dict(_account_identifiers)

        account_identifiers_for_transaction = []
        _account_identifiers_for_transaction = d.pop("accountIdentifiersForTransaction", UNSET)
        for account_identifiers_for_transaction_item_data in _account_identifiers_for_transaction or []:
            account_identifiers_for_transaction_item = AccountInfo.from_dict(
                account_identifiers_for_transaction_item_data
            )

            account_identifiers_for_transaction.append(account_identifiers_for_transaction_item)

        account_identifiers_for_balance = []
        _account_identifiers_for_balance = d.pop("accountIdentifiersForBalance", UNSET)
        for account_identifiers_for_balance_item_data in _account_identifiers_for_balance or []:
            account_identifiers_for_balance_item = AccountInfo.from_dict(account_identifiers_for_balance_item_data)

            account_identifiers_for_balance.append(account_identifiers_for_balance_item)

        feature_scope = []
        _feature_scope = d.pop("featureScope", UNSET)
        for feature_scope_item_data in _feature_scope or []:
            feature_scope_item = FeatureEnum(feature_scope_item_data)

            feature_scope.append(feature_scope_item)

        account_request = cls(
            transaction_from=transaction_from,
            transaction_to=transaction_to,
            expires_at=expires_at,
            account_identifiers=account_identifiers,
            account_identifiers_for_transaction=account_identifiers_for_transaction,
            account_identifiers_for_balance=account_identifiers_for_balance,
            feature_scope=feature_scope,
        )

        account_request.additional_properties = d
        return account_request

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
