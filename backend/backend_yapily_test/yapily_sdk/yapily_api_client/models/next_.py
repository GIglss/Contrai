import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Next")


@_attrs_define
class Next:
    """
    Attributes:
        from_ (Union[Unset, datetime.datetime]):
        before (Union[Unset, datetime.datetime]):
        limit (Union[Unset, int]):
        cursor (Union[Unset, str]):
    """

    from_: Union[Unset, datetime.datetime] = UNSET
    before: Union[Unset, datetime.datetime] = UNSET
    limit: Union[Unset, int] = UNSET
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

        cursor = d.pop("cursor", UNSET)

        next_ = cls(
            from_=from_,
            before=before,
            limit=limit,
            cursor=cursor,
        )

        next_.additional_properties = d
        return next_

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
