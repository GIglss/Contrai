from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category_structure import CategoryStructure


T = TypeVar("T", bound="GetWebhookEventsCategoriesResponse200Data")


@_attrs_define
class GetWebhookEventsCategoriesResponse200Data:
    """
    Attributes:
        categories (Union[Unset, list['CategoryStructure']]):
    """

    categories: Union[Unset, list["CategoryStructure"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        categories: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()
                categories.append(categories_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.category_structure import CategoryStructure

        d = dict(src_dict)
        categories = []
        _categories = d.pop("categories", UNSET)
        for categories_item_data in _categories or []:
            categories_item = CategoryStructure.from_dict(categories_item_data)

            categories.append(categories_item)

        get_webhook_events_categories_response_200_data = cls(
            categories=categories,
        )

        get_webhook_events_categories_response_200_data.additional_properties = d
        return get_webhook_events_categories_response_200_data

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
