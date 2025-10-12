from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patch_operation import PatchOperation

T = TypeVar("T", bound="PatchUserBeneficiaryBodyItem")


@_attrs_define
class PatchUserBeneficiaryBodyItem:
    """Patch details to be applied to user.

    Attributes:
        op (PatchOperation): The operation to be performed
        path (str): The path to the target location
        value (str): The value to be added, replaced or tested
    """

    op: PatchOperation
    path: str
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        op = self.op.value

        path = self.path

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "op": op,
                "path": path,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        op = PatchOperation(d.pop("op"))

        path = d.pop("path")

        value = d.pop("value")

        patch_user_beneficiary_body_item = cls(
            op=op,
            path=path,
            value=value,
        )

        patch_user_beneficiary_body_item.additional_properties = d
        return patch_user_beneficiary_body_item

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
