from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IsoCodeDetails")


@_attrs_define
class IsoCodeDetails:
    """__Mandatory__. Details the identification of the ISO code.

    Attributes:
        code (Union[Unset, str]): __Mandatory__. Unique identifier of the ISO code. Default: 'UNKNOWN'.
        name (Union[Unset, str]): __Mandatory__. Name of the ISO Code. Default: 'UNKNOWN'.
    """

    code: Union[Unset, str] = "UNKNOWN"
    name: Union[Unset, str] = "UNKNOWN"
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

        iso_code_details = cls(
            code=code,
            name=name,
        )

        iso_code_details.additional_properties = d
        return iso_code_details

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
