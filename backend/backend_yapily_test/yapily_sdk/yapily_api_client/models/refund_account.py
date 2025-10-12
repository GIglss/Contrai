from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_identifications import AccountIdentifications


T = TypeVar("T", bound="RefundAccount")


@_attrs_define
class RefundAccount:
    """The account to which funds should be returned if the payment is to be later refunded.

    Attributes:
        name (Union[Unset, str]):
        account_identifications (Union[Unset, list['AccountIdentifications']]):
    """

    name: Union[Unset, str] = UNSET
    account_identifications: Union[Unset, list["AccountIdentifications"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        account_identifications: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.account_identifications, Unset):
            account_identifications = []
            for account_identifications_item_data in self.account_identifications:
                account_identifications_item = account_identifications_item_data.to_dict()
                account_identifications.append(account_identifications_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if account_identifications is not UNSET:
            field_dict["accountIdentifications"] = account_identifications

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_identifications import AccountIdentifications

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        account_identifications = []
        _account_identifications = d.pop("accountIdentifications", UNSET)
        for account_identifications_item_data in _account_identifications or []:
            account_identifications_item = AccountIdentifications.from_dict(account_identifications_item_data)

            account_identifications.append(account_identifications_item)

        refund_account = cls(
            name=name,
            account_identifications=account_identifications,
        )

        refund_account.additional_properties = d
        return refund_account

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
