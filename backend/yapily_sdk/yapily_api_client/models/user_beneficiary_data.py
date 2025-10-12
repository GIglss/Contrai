from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.beneficiary_status import BeneficiaryStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_beneficiary_data_details import UserBeneficiaryDataDetails


T = TypeVar("T", bound="UserBeneficiaryData")


@_attrs_define
class UserBeneficiaryData:
    """Beneficiary data response.

    Attributes:
        beneficiary_id (Union[Unset, UUID]): id of the beneficiary Example: e7b7636d-a041-4013-8a1b-34dc85b7d341.
        status (Union[Unset, BeneficiaryStatus]): Status of the beneficiary check.
        details (Union[Unset, UserBeneficiaryDataDetails]): Beneficiary response with the details of the VoP result.
    """

    beneficiary_id: Union[Unset, UUID] = UNSET
    status: Union[Unset, BeneficiaryStatus] = UNSET
    details: Union[Unset, "UserBeneficiaryDataDetails"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        beneficiary_id: Union[Unset, str] = UNSET
        if not isinstance(self.beneficiary_id, Unset):
            beneficiary_id = str(self.beneficiary_id)

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if beneficiary_id is not UNSET:
            field_dict["beneficiaryId"] = beneficiary_id
        if status is not UNSET:
            field_dict["status"] = status
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_beneficiary_data_details import UserBeneficiaryDataDetails

        d = dict(src_dict)
        _beneficiary_id = d.pop("beneficiaryId", UNSET)
        beneficiary_id: Union[Unset, UUID]
        if isinstance(_beneficiary_id, Unset):
            beneficiary_id = UNSET
        else:
            beneficiary_id = UUID(_beneficiary_id)

        _status = d.pop("status", UNSET)
        status: Union[Unset, BeneficiaryStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BeneficiaryStatus(_status)

        _details = d.pop("details", UNSET)
        details: Union[Unset, UserBeneficiaryDataDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = UserBeneficiaryDataDetails.from_dict(_details)

        user_beneficiary_data = cls(
            beneficiary_id=beneficiary_id,
            status=status,
            details=details,
        )

        user_beneficiary_data.additional_properties = d
        return user_beneficiary_data

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
