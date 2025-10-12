from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compliance_data_business import ComplianceDataBusiness
    from ..models.compliance_data_individual import ComplianceDataIndividual


T = TypeVar("T", bound="ComplianceDataPayer")


@_attrs_define
class ComplianceDataPayer:
    """__Conditional__. Payer details required for compliance checks.

    Attributes:
        type_ (str): The payer type. Allowed values: INDIVIDUAL, BUSINESS. The corresponding object must be included.
            Example: INDIVIDUAL.
        individual (Union[Unset, ComplianceDataIndividual]): __Conditional__. Mandatory if the type is INDIVIDUAL.
        business (Union[Unset, ComplianceDataBusiness]): __Conditional__. Mandatory if the type is BUSINESS.
    """

    type_: str
    individual: Union[Unset, "ComplianceDataIndividual"] = UNSET
    business: Union[Unset, "ComplianceDataBusiness"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        individual: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.individual, Unset):
            individual = self.individual.to_dict()

        business: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.business, Unset):
            business = self.business.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if individual is not UNSET:
            field_dict["individual"] = individual
        if business is not UNSET:
            field_dict["business"] = business

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compliance_data_business import ComplianceDataBusiness
        from ..models.compliance_data_individual import ComplianceDataIndividual

        d = dict(src_dict)
        type_ = d.pop("type")

        _individual = d.pop("individual", UNSET)
        individual: Union[Unset, ComplianceDataIndividual]
        if isinstance(_individual, Unset):
            individual = UNSET
        else:
            individual = ComplianceDataIndividual.from_dict(_individual)

        _business = d.pop("business", UNSET)
        business: Union[Unset, ComplianceDataBusiness]
        if isinstance(_business, Unset):
            business = UNSET
        else:
            business = ComplianceDataBusiness.from_dict(_business)

        compliance_data_payer = cls(
            type_=type_,
            individual=individual,
            business=business,
        )

        compliance_data_payer.additional_properties = d
        return compliance_data_payer

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
