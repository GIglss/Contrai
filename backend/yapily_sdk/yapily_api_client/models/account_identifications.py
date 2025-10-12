from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_identification_type import AccountIdentificationType

T = TypeVar("T", bound="AccountIdentifications")


@_attrs_define
class AccountIdentifications:
    """
    Attributes:
        type_ (AccountIdentificationType): __Mandatory__. Used to describe the format of the account.<br><br> See
            [Account Identification Combinations](https://docs.yapily.com/pages/key-concepts/payments/payment-
            execution/intro-to-payment-execution/#account-identifications-combinations) for more information on when to
            specify each type. Example: SORT_CODE.
        identification (str): __Mandatory__. The value associated with the account identification type.<br><br> See
            [Account Identification Combinations](https://docs.yapily.com/pages/key-concepts/payments/payment-
            execution/intro-to-payment-execution/#account-identifications-combinations) for more information on the format
            of the values. Example: 401016.
    """

    type_: AccountIdentificationType
    identification: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        identification = self.identification

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "identification": identification,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = AccountIdentificationType(d.pop("type"))

        identification = d.pop("identification")

        account_identifications = cls(
            type_=type_,
            identification=identification,
        )

        account_identifications.additional_properties = d
        return account_identifications

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
