from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_statement import AccountStatement
    from ..models.api_call import ApiCall
    from ..models.filtered_client_payload_list_account_statement_paging_map import (
        FilteredClientPayloadListAccountStatementPagingMap,
    )


T = TypeVar("T", bound="FilteredClientPayloadListAccountStatement")


@_attrs_define
class FilteredClientPayloadListAccountStatement:
    """
    Attributes:
        api_call (Union[Unset, ApiCall]):
        data (Union[Unset, list['AccountStatement']]):
        next_cursor_hash (Union[Unset, str]):
        next_link (Union[Unset, str]):
        paging_map (Union[Unset, FilteredClientPayloadListAccountStatementPagingMap]):
        total_count (Union[Unset, int]):
    """

    api_call: Union[Unset, "ApiCall"] = UNSET
    data: Union[Unset, list["AccountStatement"]] = UNSET
    next_cursor_hash: Union[Unset, str] = UNSET
    next_link: Union[Unset, str] = UNSET
    paging_map: Union[Unset, "FilteredClientPayloadListAccountStatementPagingMap"] = UNSET
    total_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_call: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.api_call, Unset):
            api_call = self.api_call.to_dict()

        data: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        next_cursor_hash = self.next_cursor_hash

        next_link = self.next_link

        paging_map: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.paging_map, Unset):
            paging_map = self.paging_map.to_dict()

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_call is not UNSET:
            field_dict["apiCall"] = api_call
        if data is not UNSET:
            field_dict["data"] = data
        if next_cursor_hash is not UNSET:
            field_dict["nextCursorHash"] = next_cursor_hash
        if next_link is not UNSET:
            field_dict["nextLink"] = next_link
        if paging_map is not UNSET:
            field_dict["pagingMap"] = paging_map
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_statement import AccountStatement
        from ..models.api_call import ApiCall
        from ..models.filtered_client_payload_list_account_statement_paging_map import (
            FilteredClientPayloadListAccountStatementPagingMap,
        )

        d = dict(src_dict)
        _api_call = d.pop("apiCall", UNSET)
        api_call: Union[Unset, ApiCall]
        if isinstance(_api_call, Unset):
            api_call = UNSET
        else:
            api_call = ApiCall.from_dict(_api_call)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = AccountStatement.from_dict(data_item_data)

            data.append(data_item)

        next_cursor_hash = d.pop("nextCursorHash", UNSET)

        next_link = d.pop("nextLink", UNSET)

        _paging_map = d.pop("pagingMap", UNSET)
        paging_map: Union[Unset, FilteredClientPayloadListAccountStatementPagingMap]
        if isinstance(_paging_map, Unset):
            paging_map = UNSET
        else:
            paging_map = FilteredClientPayloadListAccountStatementPagingMap.from_dict(_paging_map)

        total_count = d.pop("totalCount", UNSET)

        filtered_client_payload_list_account_statement = cls(
            api_call=api_call,
            data=data,
            next_cursor_hash=next_cursor_hash,
            next_link=next_link,
            paging_map=paging_map,
            total_count=total_count,
        )

        filtered_client_payload_list_account_statement.additional_properties = d
        return filtered_client_payload_list_account_statement

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
