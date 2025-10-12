import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.sort_enum import SortEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterAndSort")


@_attrs_define
class FilterAndSort:
    """
    Attributes:
        from_ (Union[Unset, datetime.datetime]): __Optional__. The earliest date and time of resources / records that
            should be returned.
        before (Union[Unset, datetime.datetime]): __Optional__. The latest date and time of resources / records that
            should be returned.
        limit (Union[Unset, int]): __Optional__. The maximum number of resources / records that should be returned.
        sort (Union[Unset, SortEnum]): The attribute on which resources / records returned should be sorted. Valid
            options for the sort parameter.
        offset (Union[Unset, int]):
        cursor (Union[Unset, str]):
    """

    from_: Union[Unset, datetime.datetime] = UNSET
    before: Union[Unset, datetime.datetime] = UNSET
    limit: Union[Unset, int] = UNSET
    sort: Union[Unset, SortEnum] = UNSET
    offset: Union[Unset, int] = UNSET
    cursor: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_: Union[Unset, str] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        before: Union[Unset, str] = UNSET
        if not isinstance(self.before, Unset):
            before = self.before.isoformat()

        limit = self.limit

        sort: Union[Unset, str] = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort.value

        offset = self.offset

        cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if before is not UNSET:
            field_dict["before"] = before
        if limit is not UNSET:
            field_dict["limit"] = limit
        if sort is not UNSET:
            field_dict["sort"] = sort
        if offset is not UNSET:
            field_dict["offset"] = offset
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, datetime.datetime]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = isoparse(_from_)

        _before = d.pop("before", UNSET)
        before: Union[Unset, datetime.datetime]
        if isinstance(_before, Unset):
            before = UNSET
        else:
            before = isoparse(_before)

        limit = d.pop("limit", UNSET)

        _sort = d.pop("sort", UNSET)
        sort: Union[Unset, SortEnum]
        if isinstance(_sort, Unset):
            sort = UNSET
        else:
            sort = SortEnum(_sort)

        offset = d.pop("offset", UNSET)

        cursor = d.pop("cursor", UNSET)

        filter_and_sort = cls(
            from_=from_,
            before=before,
            limit=limit,
            sort=sort,
            offset=offset,
            cursor=cursor,
        )

        filter_and_sort.additional_properties = d
        return filter_and_sort

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
