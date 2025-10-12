from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchApplicationsPublicFilterValues")


@_attrs_define
class SearchApplicationsPublicFilterValues:
    """
    Attributes:
        application_ids (Union[Unset, list[UUID]]): Sub-application ids to filter the results for. If provided, the
            results will only include sub-applications with the given ids. Non-existent ids will be ignored.
        offset (Union[Unset, int]): The number of results to skip. Default: 0.
        limit (Union[Unset, int]): The maximum number of results to return. Default: 1000.
        sort (Union[Unset, str]): The field to sort the results by.<br><br>Possible values:<ul><li>`last_updated`
            (ascending)</li><li>`-last_updated` (descending)</li><li>`name` (ascending)</li><li>`-name`
            (descending)</li><li>`uuid` (ascending)</li><li>`-uuid` (descending)</li></ul> Default: 'name'.
    """

    application_ids: Union[Unset, list[UUID]] = UNSET
    offset: Union[Unset, int] = 0
    limit: Union[Unset, int] = 1000
    sort: Union[Unset, str] = "name"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.application_ids, Unset):
            application_ids = []
            for application_ids_item_data in self.application_ids:
                application_ids_item = str(application_ids_item_data)
                application_ids.append(application_ids_item)

        offset = self.offset

        limit = self.limit

        sort = self.sort

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if application_ids is not UNSET:
            field_dict["applicationIds"] = application_ids
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
        application_ids = []
        _application_ids = d.pop("applicationIds", UNSET)
        for application_ids_item_data in _application_ids or []:
            application_ids_item = UUID(application_ids_item_data)

            application_ids.append(application_ids_item)

        offset = d.pop("offset", UNSET)

        limit = d.pop("limit", UNSET)

        sort = d.pop("sort", UNSET)

        search_applications_public_filter_values = cls(
            application_ids=application_ids,
            offset=offset,
            limit=limit,
            sort=sort,
        )

        search_applications_public_filter_values.additional_properties = d
        return search_applications_public_filter_values

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
