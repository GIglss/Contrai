from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.application_beneficiary_data_details import ApplicationBeneficiaryDataDetails


T = TypeVar("T", bound="ApplicationBeneficiaryData")


@_attrs_define
class ApplicationBeneficiaryData:
    """Application beneficiary data response.

    Attributes:
        beneficiary_id (Union[Unset, UUID]): Beneficiary Id Example: e7b7636d-a041-4013-8a1b-34dc85b7d341.
        details (Union[Unset, ApplicationBeneficiaryDataDetails]):
    """

    beneficiary_id: Union[Unset, UUID] = UNSET
    details: Union[Unset, "ApplicationBeneficiaryDataDetails"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        beneficiary_id: Union[Unset, str] = UNSET
        if not isinstance(self.beneficiary_id, Unset):
            beneficiary_id = str(self.beneficiary_id)

        details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if beneficiary_id is not UNSET:
            field_dict["beneficiaryId"] = beneficiary_id
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.application_beneficiary_data_details import ApplicationBeneficiaryDataDetails

        d = dict(src_dict)
        _beneficiary_id = d.pop("beneficiaryId", UNSET)
        beneficiary_id: Union[Unset, UUID]
        if isinstance(_beneficiary_id, Unset):
            beneficiary_id = UNSET
        else:
            beneficiary_id = UUID(_beneficiary_id)

        _details = d.pop("details", UNSET)
        details: Union[Unset, ApplicationBeneficiaryDataDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = ApplicationBeneficiaryDataDetails.from_dict(_details)

        application_beneficiary_data = cls(
            beneficiary_id=beneficiary_id,
            details=details,
        )

        application_beneficiary_data.additional_properties = d
        return application_beneficiary_data

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
