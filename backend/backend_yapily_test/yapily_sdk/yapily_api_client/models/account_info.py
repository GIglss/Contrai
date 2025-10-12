from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_identifications import AccountIdentifications


T = TypeVar("T", bound="AccountInfo")


@_attrs_define
class AccountInfo:
    """__Conditional__. Used to create a request for the balance of the account specified. Once the user authorises the
    request, only the balance can be obtained by executing [GET Account Balances](./#get-account-balances).<br><br> This
    can be specified in conjunction with `accountIdentifiersForTransaction` to generate a `Consent` that can both access
    the accounts balance and transactions.

        Attributes:
            account_identification (AccountIdentifications):
            account_id (Union[Unset, str]): __Conditional__. Unique identifier of the account. Example:
                500000000000000000000001.
    """

    account_identification: "AccountIdentifications"
    account_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_identification = self.account_identification.to_dict()

        account_id = self.account_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountIdentification": account_identification,
            }
        )
        if account_id is not UNSET:
            field_dict["accountId"] = account_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_identifications import AccountIdentifications

        d = dict(src_dict)
        account_identification = AccountIdentifications.from_dict(d.pop("accountIdentification"))

        account_id = d.pop("accountId", UNSET)

        account_info = cls(
            account_identification=account_identification,
            account_id=account_id,
        )

        account_info.additional_properties = d
        return account_info

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
