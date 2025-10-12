from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.application_response_list_meta_pagination_self import ApplicationResponseListMetaPaginationSelf


T = TypeVar("T", bound="ApplicationResponseListMetaPagination")


@_attrs_define
class ApplicationResponseListMetaPagination:
    """
    Attributes:
        self_ (Union[Unset, ApplicationResponseListMetaPaginationSelf]):
        total_count (Union[Unset, int]): The total number of applications that match the given filter.
    """

    self_: Union[Unset, "ApplicationResponseListMetaPaginationSelf"] = UNSET
    total_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.application_response_list_meta_pagination_self import ApplicationResponseListMetaPaginationSelf

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, ApplicationResponseListMetaPaginationSelf]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = ApplicationResponseListMetaPaginationSelf.from_dict(_self_)

        total_count = d.pop("totalCount", UNSET)

        application_response_list_meta_pagination = cls(
            self_=self_,
            total_count=total_count,
        )

        application_response_list_meta_pagination.additional_properties = d
        return application_response_list_meta_pagination

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
