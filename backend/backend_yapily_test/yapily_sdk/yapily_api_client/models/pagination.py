from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_and_sort import FilterAndSort
    from ..models.next_ import Next


T = TypeVar("T", bound="Pagination")


@_attrs_define
class Pagination:
    """
    Attributes:
        total_count (Union[Unset, int]):
        self_ (Union[Unset, FilterAndSort]):
        next_ (Union[Unset, Next]):
    """

    total_count: Union[Unset, int] = UNSET
    self_: Union[Unset, "FilterAndSort"] = UNSET
    next_: Union[Unset, "Next"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        next_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.next_, Unset):
            next_ = self.next_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count
        if self_ is not UNSET:
            field_dict["self"] = self_
        if next_ is not UNSET:
            field_dict["next"] = next_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_and_sort import FilterAndSort
        from ..models.next_ import Next

        d = dict(src_dict)
        total_count = d.pop("totalCount", UNSET)

        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, FilterAndSort]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = FilterAndSort.from_dict(_self_)

        _next_ = d.pop("next", UNSET)
        next_: Union[Unset, Next]
        if isinstance(_next_, Unset):
            next_ = UNSET
        else:
            next_ = Next.from_dict(_next_)

        pagination = cls(
            total_count=total_count,
            self_=self_,
            next_=next_,
        )

        pagination.additional_properties = d
        return pagination

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
