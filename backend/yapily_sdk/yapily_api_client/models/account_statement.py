import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountStatement")


@_attrs_define
class AccountStatement:
    """Statement information belonging to the account.

    Attributes:
        id (Union[Unset, str]): Unique identifier for the statement.
        start_date_time (Union[Unset, datetime.datetime]): Date and time of when the statement period starts.
        end_date_time (Union[Unset, datetime.datetime]): Date and time of when the statement period ends.
        creation_date_time (Union[Unset, datetime.datetime]): Date and time of when the statement was created.
    """

    id: Union[Unset, str] = UNSET
    start_date_time: Union[Unset, datetime.datetime] = UNSET
    end_date_time: Union[Unset, datetime.datetime] = UNSET
    creation_date_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        start_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_date_time, Unset):
            start_date_time = self.start_date_time.isoformat()

        end_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_date_time, Unset):
            end_date_time = self.end_date_time.isoformat()

        creation_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date_time, Unset):
            creation_date_time = self.creation_date_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if start_date_time is not UNSET:
            field_dict["startDateTime"] = start_date_time
        if end_date_time is not UNSET:
            field_dict["endDateTime"] = end_date_time
        if creation_date_time is not UNSET:
            field_dict["creationDateTime"] = creation_date_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _start_date_time = d.pop("startDateTime", UNSET)
        start_date_time: Union[Unset, datetime.datetime]
        if isinstance(_start_date_time, Unset):
            start_date_time = UNSET
        else:
            start_date_time = isoparse(_start_date_time)

        _end_date_time = d.pop("endDateTime", UNSET)
        end_date_time: Union[Unset, datetime.datetime]
        if isinstance(_end_date_time, Unset):
            end_date_time = UNSET
        else:
            end_date_time = isoparse(_end_date_time)

        _creation_date_time = d.pop("creationDateTime", UNSET)
        creation_date_time: Union[Unset, datetime.datetime]
        if isinstance(_creation_date_time, Unset):
            creation_date_time = UNSET
        else:
            creation_date_time = isoparse(_creation_date_time)

        account_statement = cls(
            id=id,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            creation_date_time=creation_date_time,
        )

        account_statement.additional_properties = d
        return account_statement

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
