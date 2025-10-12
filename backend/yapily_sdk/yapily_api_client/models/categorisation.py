from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Categorisation")


@_attrs_define
class Categorisation:
    """Income and Expense categorisation that the Yapily categorisation engine has determined for the transaction.

    Attributes:
        categories (Union[Unset, list[str]]):
        source (Union[Unset, str]):
    """

    categories: Union[Unset, list[str]] = UNSET
    source: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        categories: Union[Unset, list[str]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if categories is not UNSET:
            field_dict["categories"] = categories
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        categories = cast(list[str], d.pop("categories", UNSET))

        source = d.pop("source", UNSET)

        categorisation = cls(
            categories=categories,
            source=source,
        )

        categorisation.additional_properties = d
        return categorisation

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
