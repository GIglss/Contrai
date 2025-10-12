from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplicationResponseListMetaPaginationSelf")


@_attrs_define
class ApplicationResponseListMetaPaginationSelf:
    """
    Attributes:
        offset (Union[Unset, int]): The number of skipped applications.
        limit (Union[Unset, int]): The maximum number of applications for the current page.
        sort (Union[Unset, str]): The field by which results are sorted by. Default direction is ascending, descending
            is identified by a "-" prefix.
    """

    offset: Union[Unset, int] = UNSET
    limit: Union[Unset, int] = UNSET
    sort: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        limit = self.limit

        sort = self.sort

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if offset is not UNSET:
            field_dict["offset"] = offset
        if limit is not UNSET:
            field_dict["limit"] = limit
        if sort is not UNSET:
            field_dict["sort"] = sort

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        offset = d.pop("offset", UNSET)

        limit = d.pop("limit", UNSET)

        sort = d.pop("sort", UNSET)

        application_response_list_meta_pagination_self = cls(
            offset=offset,
            limit=limit,
            sort=sort,
        )

        application_response_list_meta_pagination_self.additional_properties = d
        return application_response_list_meta_pagination_self

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
