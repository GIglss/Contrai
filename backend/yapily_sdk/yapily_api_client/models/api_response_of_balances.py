from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_response_of_balances_links import ApiResponseOfBalancesLinks
    from ..models.balances import Balances
    from ..models.raw_response import RawResponse
    from ..models.response_forwarded_data import ResponseForwardedData
    from ..models.response_meta import ResponseMeta


T = TypeVar("T", bound="ApiResponseOfBalances")


@_attrs_define
class ApiResponseOfBalances:
    """
    Attributes:
        meta (Union[Unset, ResponseMeta]):
        data (Union[Unset, Balances]):
        links (Union[Unset, ApiResponseOfBalancesLinks]):
        forwarded_data (Union[Unset, list['ResponseForwardedData']]):
        raw (Union[Unset, list['RawResponse']]):
        tracing_id (Union[Unset, str]):
    """

    meta: Union[Unset, "ResponseMeta"] = UNSET
    data: Union[Unset, "Balances"] = UNSET
    links: Union[Unset, "ApiResponseOfBalancesLinks"] = UNSET
    forwarded_data: Union[Unset, list["ResponseForwardedData"]] = UNSET
    raw: Union[Unset, list["RawResponse"]] = UNSET
    tracing_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        forwarded_data: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.forwarded_data, Unset):
            forwarded_data = []
            for forwarded_data_item_data in self.forwarded_data:
                forwarded_data_item = forwarded_data_item_data.to_dict()
                forwarded_data.append(forwarded_data_item)

        raw: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.raw, Unset):
            raw = []
            for raw_item_data in self.raw:
                raw_item = raw_item_data.to_dict()
                raw.append(raw_item)

        tracing_id = self.tracing_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meta is not UNSET:
            field_dict["meta"] = meta
        if data is not UNSET:
            field_dict["data"] = data
        if links is not UNSET:
            field_dict["links"] = links
        if forwarded_data is not UNSET:
            field_dict["forwardedData"] = forwarded_data
        if raw is not UNSET:
            field_dict["raw"] = raw
        if tracing_id is not UNSET:
            field_dict["tracingId"] = tracing_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_response_of_balances_links import ApiResponseOfBalancesLinks
        from ..models.balances import Balances
        from ..models.raw_response import RawResponse
        from ..models.response_forwarded_data import ResponseForwardedData
        from ..models.response_meta import ResponseMeta

        d = dict(src_dict)
        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, ResponseMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = ResponseMeta.from_dict(_meta)

        _data = d.pop("data", UNSET)
        data: Union[Unset, Balances]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = Balances.from_dict(_data)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ApiResponseOfBalancesLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ApiResponseOfBalancesLinks.from_dict(_links)

        forwarded_data = []
        _forwarded_data = d.pop("forwardedData", UNSET)
        for forwarded_data_item_data in _forwarded_data or []:
            forwarded_data_item = ResponseForwardedData.from_dict(forwarded_data_item_data)

            forwarded_data.append(forwarded_data_item)

        raw = []
        _raw = d.pop("raw", UNSET)
        for raw_item_data in _raw or []:
            raw_item = RawResponse.from_dict(raw_item_data)

            raw.append(raw_item)

        tracing_id = d.pop("tracingId", UNSET)

        api_response_of_balances = cls(
            meta=meta,
            data=data,
            links=links,
            forwarded_data=forwarded_data,
            raw=raw,
            tracing_id=tracing_id,
        )

        api_response_of_balances.additional_properties = d
        return api_response_of_balances

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
