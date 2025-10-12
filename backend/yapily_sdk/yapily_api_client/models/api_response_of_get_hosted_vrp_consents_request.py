from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_hosted_vrp_consents_response_item import GetHostedVRPConsentsResponseItem
    from ..models.response_meta import ResponseMeta


T = TypeVar("T", bound="ApiResponseOfGetHostedVRPConsentsRequest")


@_attrs_define
class ApiResponseOfGetHostedVRPConsentsRequest:
    """
    Attributes:
        meta (Union[Unset, ResponseMeta]):
        data (Union[Unset, list['GetHostedVRPConsentsResponseItem']]):
    """

    meta: Union[Unset, "ResponseMeta"] = UNSET
    data: Union[Unset, list["GetHostedVRPConsentsResponseItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        data: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for componentsschemas_get_hosted_vrp_consents_response_item_data in self.data:
                componentsschemas_get_hosted_vrp_consents_response_item = (
                    componentsschemas_get_hosted_vrp_consents_response_item_data.to_dict()
                )
                data.append(componentsschemas_get_hosted_vrp_consents_response_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meta is not UNSET:
            field_dict["meta"] = meta
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_hosted_vrp_consents_response_item import GetHostedVRPConsentsResponseItem
        from ..models.response_meta import ResponseMeta

        d = dict(src_dict)
        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, ResponseMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = ResponseMeta.from_dict(_meta)

        data = []
        _data = d.pop("data", UNSET)
        for componentsschemas_get_hosted_vrp_consents_response_item_data in _data or []:
            componentsschemas_get_hosted_vrp_consents_response_item = GetHostedVRPConsentsResponseItem.from_dict(
                componentsschemas_get_hosted_vrp_consents_response_item_data
            )

            data.append(componentsschemas_get_hosted_vrp_consents_response_item)

        api_response_of_get_hosted_vrp_consents_request = cls(
            meta=meta,
            data=data,
        )

        api_response_of_get_hosted_vrp_consents_request.additional_properties = d
        return api_response_of_get_hosted_vrp_consents_request

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
