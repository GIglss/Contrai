from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.application_response_list_meta_pagination import ApplicationResponseListMetaPagination


T = TypeVar("T", bound="ApplicationResponseListMeta")


@_attrs_define
class ApplicationResponseListMeta:
    """
    Attributes:
        tracing_id (Union[Unset, str]):
        count (Union[Unset, int]): The number of applications in the current page.
        pagination (Union[Unset, ApplicationResponseListMetaPagination]):
    """

    tracing_id: Union[Unset, str] = UNSET
    count: Union[Unset, int] = UNSET
    pagination: Union[Unset, "ApplicationResponseListMetaPagination"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tracing_id = self.tracing_id

        count = self.count

        pagination: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tracing_id is not UNSET:
            field_dict["tracingId"] = tracing_id
        if count is not UNSET:
            field_dict["count"] = count
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.application_response_list_meta_pagination import ApplicationResponseListMetaPagination

        d = dict(src_dict)
        tracing_id = d.pop("tracingId", UNSET)

        count = d.pop("count", UNSET)

        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, ApplicationResponseListMetaPagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = ApplicationResponseListMetaPagination.from_dict(_pagination)

        application_response_list_meta = cls(
            tracing_id=tracing_id,
            count=count,
            pagination=pagination,
        )

        application_response_list_meta.additional_properties = d
        return application_response_list_meta

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
