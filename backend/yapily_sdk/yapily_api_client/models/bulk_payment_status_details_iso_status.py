from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkPaymentStatusDetailsIsoStatus")


@_attrs_define
class BulkPaymentStatusDetailsIsoStatus:
    """The Institution's status for this Bulk Payment.

    Attributes:
        code (Union[Unset, str]): The Institution's status code for this Bulk Payment. It will often be a 3-letter ISO
            20022 status code, but it may also contain other values. Example: ACSP.
        name (Union[Unset, str]): The full name for the status code, provided only when it is a valid ISO 20022 status
            code. Example: AcceptedSettlementInProcess.
    """

    code: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

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
        code = d.pop("code", UNSET)

        name = d.pop("name", UNSET)

        bulk_payment_status_details_iso_status = cls(
            code=code,
            name=name,
        )

        bulk_payment_status_details_iso_status.additional_properties = d
        return bulk_payment_status_details_iso_status

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
