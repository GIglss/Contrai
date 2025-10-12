from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProprietaryBankTransactionCode")


@_attrs_define
class ProprietaryBankTransactionCode:
    """Transaction code that is proprietary to the `Institution`.

    Attributes:
        code (Union[Unset, str]): __Mandatory__. Proprietary code used to identify the underlying transaction.
        issuer (Union[Unset, str]): __Mandatory__. Issuer of the proprietary code.
    """

    code: Union[Unset, str] = UNSET
    issuer: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        issuer = self.issuer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if issuer is not UNSET:
            field_dict["issuer"] = issuer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        issuer = d.pop("issuer", UNSET)

        proprietary_bank_transaction_code = cls(
            code=code,
            issuer=issuer,
        )

        proprietary_bank_transaction_code.additional_properties = d
        return proprietary_bank_transaction_code

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
