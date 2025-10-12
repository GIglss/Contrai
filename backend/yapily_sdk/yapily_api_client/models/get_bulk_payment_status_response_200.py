from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_bulk_payment_status_response_200_data import GetBulkPaymentStatusResponse200Data
    from ..models.get_bulk_payment_status_response_200_meta import GetBulkPaymentStatusResponse200Meta


T = TypeVar("T", bound="GetBulkPaymentStatusResponse200")


@_attrs_define
class GetBulkPaymentStatusResponse200:
    """
    Attributes:
        meta (Union[Unset, GetBulkPaymentStatusResponse200Meta]):
        data (Union[Unset, GetBulkPaymentStatusResponse200Data]):
    """

    meta: Union[Unset, "GetBulkPaymentStatusResponse200Meta"] = UNSET
    data: Union[Unset, "GetBulkPaymentStatusResponse200Data"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

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
        from ..models.get_bulk_payment_status_response_200_data import GetBulkPaymentStatusResponse200Data
        from ..models.get_bulk_payment_status_response_200_meta import GetBulkPaymentStatusResponse200Meta

        d = dict(src_dict)
        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, GetBulkPaymentStatusResponse200Meta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = GetBulkPaymentStatusResponse200Meta.from_dict(_meta)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GetBulkPaymentStatusResponse200Data]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GetBulkPaymentStatusResponse200Data.from_dict(_data)

        get_bulk_payment_status_response_200 = cls(
            meta=meta,
            data=data,
        )

        get_bulk_payment_status_response_200.additional_properties = d
        return get_bulk_payment_status_response_200

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
