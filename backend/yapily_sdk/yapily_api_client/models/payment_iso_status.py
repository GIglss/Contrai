from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.payment_iso_status_code_enum import PaymentIsoStatusCodeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentIsoStatus")


@_attrs_define
class PaymentIsoStatus:
    """The payment status code, as denoted by a 3-letter ISO 20022 code.

    Attributes:
        code (Union[Unset, PaymentIsoStatusCodeEnum]): The ISO 20022 `PaymentStatusCode`. Example: ACCC.
        name (Union[Unset, str]): The full name of the ISO 20022 `PaymentStatusCode`. Example:
            AcceptedCreditSettlementCompleted.
    """

    code: Union[Unset, PaymentIsoStatusCodeEnum] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code: Union[Unset, str] = UNSET
        if not isinstance(self.code, Unset):
            code = self.code.value

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _code = d.pop("code", UNSET)
        code: Union[Unset, PaymentIsoStatusCodeEnum]
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = PaymentIsoStatusCodeEnum(_code)

        name = d.pop("name", UNSET)

        payment_iso_status = cls(
            code=code,
            name=name,
        )

        payment_iso_status.additional_properties = d
        return payment_iso_status

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
