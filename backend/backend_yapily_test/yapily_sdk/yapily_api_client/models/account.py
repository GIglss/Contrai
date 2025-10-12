from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_type import AccountType
from ..models.usage_type import UsageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_balance import AccountBalance
    from ..models.account_identifications import AccountIdentifications
    from ..models.account_name import AccountName
    from ..models.consolidated_account_information import ConsolidatedAccountInformation


T = TypeVar("T", bound="Account")


@_attrs_define
class Account:
    """
    Attributes:
        id (Union[Unset, str]): Unique identifier of the account.
        type_ (Union[Unset, str]): Specifies the type of account e.g. (BUSINESS_CURRENT).
        description (Union[Unset, str]): Product name as defined by the financial institution for this account
        balance (Union[Unset, float]): Main / headline balance for the account. <br><br> Use of this field is
            recommended as fallback only. Instead, use of the typed balances (accountBalances) is recommended.
        currency (Union[Unset, str]): Currency the bank account balance is denoted in. <br><br> Specified as a 3-letter
            ISO 4217 currency code
        usage_type (Union[Unset, UsageType]): The customer segment of the account.
        account_type (Union[Unset, AccountType]): The type of account e.g. (Credit Card, Savings).
        nickname (Union[Unset, str]): Nickname of the account that was provided by the account owner. <br><br> May be
            used to aid identification of the account.
        details (Union[Unset, str]): Supplementary specifications that might be provided by the Bank. These provide
            further characteristics about the account.
        account_names (Union[Unset, list['AccountName']]):
        account_identifications (Union[Unset, list['AccountIdentifications']]):
        account_balances (Union[Unset, list['AccountBalance']]):
        consolidated_account_information (Union[Unset, ConsolidatedAccountInformation]): Summary information regarding
            account balances of the overall account provided by the bank
    """

    id: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    balance: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    usage_type: Union[Unset, UsageType] = UNSET
    account_type: Union[Unset, AccountType] = UNSET
    nickname: Union[Unset, str] = UNSET
    details: Union[Unset, str] = UNSET
    account_names: Union[Unset, list["AccountName"]] = UNSET
    account_identifications: Union[Unset, list["AccountIdentifications"]] = UNSET
    account_balances: Union[Unset, list["AccountBalance"]] = UNSET
    consolidated_account_information: Union[Unset, "ConsolidatedAccountInformation"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        description = self.description

        balance = self.balance

        currency = self.currency

        usage_type: Union[Unset, str] = UNSET
        if not isinstance(self.usage_type, Unset):
            usage_type = self.usage_type.value

        account_type: Union[Unset, str] = UNSET
        if not isinstance(self.account_type, Unset):
            account_type = self.account_type.value

        nickname = self.nickname

        details = self.details

        account_names: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.account_names, Unset):
            account_names = []
            for account_names_item_data in self.account_names:
                account_names_item = account_names_item_data.to_dict()
                account_names.append(account_names_item)

        account_identifications: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.account_identifications, Unset):
            account_identifications = []
            for account_identifications_item_data in self.account_identifications:
                account_identifications_item = account_identifications_item_data.to_dict()
                account_identifications.append(account_identifications_item)

        account_balances: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.account_balances, Unset):
            account_balances = []
            for account_balances_item_data in self.account_balances:
                account_balances_item = account_balances_item_data.to_dict()
                account_balances.append(account_balances_item)

        consolidated_account_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.consolidated_account_information, Unset):
            consolidated_account_information = self.consolidated_account_information.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if description is not UNSET:
            field_dict["description"] = description
        if balance is not UNSET:
            field_dict["balance"] = balance
        if currency is not UNSET:
            field_dict["currency"] = currency
        if usage_type is not UNSET:
            field_dict["usageType"] = usage_type
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if details is not UNSET:
            field_dict["details"] = details
        if account_names is not UNSET:
            field_dict["accountNames"] = account_names
        if account_identifications is not UNSET:
            field_dict["accountIdentifications"] = account_identifications
        if account_balances is not UNSET:
            field_dict["accountBalances"] = account_balances
        if consolidated_account_information is not UNSET:
            field_dict["consolidatedAccountInformation"] = consolidated_account_information

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_balance import AccountBalance
        from ..models.account_identifications import AccountIdentifications
        from ..models.account_name import AccountName
        from ..models.consolidated_account_information import ConsolidatedAccountInformation

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        description = d.pop("description", UNSET)

        balance = d.pop("balance", UNSET)

        currency = d.pop("currency", UNSET)

        _usage_type = d.pop("usageType", UNSET)
        usage_type: Union[Unset, UsageType]
        if isinstance(_usage_type, Unset):
            usage_type = UNSET
        else:
            usage_type = UsageType(_usage_type)

        _account_type = d.pop("accountType", UNSET)
        account_type: Union[Unset, AccountType]
        if isinstance(_account_type, Unset):
            account_type = UNSET
        else:
            account_type = AccountType(_account_type)

        nickname = d.pop("nickname", UNSET)

        details = d.pop("details", UNSET)

        account_names = []
        _account_names = d.pop("accountNames", UNSET)
        for account_names_item_data in _account_names or []:
            account_names_item = AccountName.from_dict(account_names_item_data)

            account_names.append(account_names_item)

        account_identifications = []
        _account_identifications = d.pop("accountIdentifications", UNSET)
        for account_identifications_item_data in _account_identifications or []:
            account_identifications_item = AccountIdentifications.from_dict(account_identifications_item_data)

            account_identifications.append(account_identifications_item)

        account_balances = []
        _account_balances = d.pop("accountBalances", UNSET)
        for account_balances_item_data in _account_balances or []:
            account_balances_item = AccountBalance.from_dict(account_balances_item_data)

            account_balances.append(account_balances_item)

        _consolidated_account_information = d.pop("consolidatedAccountInformation", UNSET)
        consolidated_account_information: Union[Unset, ConsolidatedAccountInformation]
        if isinstance(_consolidated_account_information, Unset):
            consolidated_account_information = UNSET
        else:
            consolidated_account_information = ConsolidatedAccountInformation.from_dict(
                _consolidated_account_information
            )

        account = cls(
            id=id,
            type_=type_,
            description=description,
            balance=balance,
            currency=currency,
            usage_type=usage_type,
            account_type=account_type,
            nickname=nickname,
            details=details,
            account_names=account_names,
            account_identifications=account_identifications,
            account_balances=account_balances,
            consolidated_account_information=consolidated_account_information,
        )

        account.additional_properties = d
        return account

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
