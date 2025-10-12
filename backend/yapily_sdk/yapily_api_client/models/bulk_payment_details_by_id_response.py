from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_payment_details_by_id_response_data import BulkPaymentDetailsByIdResponseData
    from ..models.bulk_payment_details_by_id_response_meta import BulkPaymentDetailsByIdResponseMeta


T = TypeVar("T", bound="BulkPaymentDetailsByIdResponse")


@_attrs_define
class BulkPaymentDetailsByIdResponse:
    """
    Attributes:
        meta (Union[Unset, BulkPaymentDetailsByIdResponseMeta]):
        data (Union[Unset, BulkPaymentDetailsByIdResponseData]):
    """

    meta: Union[Unset, "BulkPaymentDetailsByIdResponseMeta"] = UNSET
    data: Union[Unset, "BulkPaymentDetailsByIdResponseData"] = UNSET
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
        from ..models.bulk_payment_details_by_id_response_data import BulkPaymentDetailsByIdResponseData
        from ..models.bulk_payment_details_by_id_response_meta import BulkPaymentDetailsByIdResponseMeta

        d = dict(src_dict)
        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, BulkPaymentDetailsByIdResponseMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = BulkPaymentDetailsByIdResponseMeta.from_dict(_meta)

        _data = d.pop("data", UNSET)
        data: Union[Unset, BulkPaymentDetailsByIdResponseData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = BulkPaymentDetailsByIdResponseData.from_dict(_data)

        bulk_payment_details_by_id_response = cls(
            meta=meta,
            data=data,
        )

        bulk_payment_details_by_id_response.additional_properties = d
        return bulk_payment_details_by_id_response

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
