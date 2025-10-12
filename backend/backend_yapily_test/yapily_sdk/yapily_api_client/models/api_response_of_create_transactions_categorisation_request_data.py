from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiResponseOfCreateTransactionsCategorisationRequestData")


@_attrs_define
class ApiResponseOfCreateTransactionsCategorisationRequestData:
    """
    Attributes:
        categorisation_id (Union[Unset, UUID]):
    """

    categorisation_id: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        categorisation_id: Union[Unset, str] = UNSET
        if not isinstance(self.categorisation_id, Unset):
            categorisation_id = str(self.categorisation_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if categorisation_id is not UNSET:
            field_dict["categorisationId"] = categorisation_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _categorisation_id = d.pop("categorisationId", UNSET)
        categorisation_id: Union[Unset, UUID]
        if isinstance(_categorisation_id, Unset):
            categorisation_id = UNSET
        else:
            categorisation_id = UUID(_categorisation_id)

        api_response_of_create_transactions_categorisation_request_data = cls(
            categorisation_id=categorisation_id,
        )

        api_response_of_create_transactions_categorisation_request_data.additional_properties = d
        return api_response_of_create_transactions_categorisation_request_data

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
