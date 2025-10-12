from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.beneficiary_match_status import BeneficiaryMatchStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserBeneficiaryMatch")


@_attrs_define
class UserBeneficiaryMatch:
    """Details of the match given by the institution.

    Attributes:
        status (Union[Unset, BeneficiaryMatchStatus]):
        close_match_name (Union[Unset, str]): the name returned by the institution, in a case of CLOSE_MATCH Example:
            John Doe.
    """

    status: Union[Unset, BeneficiaryMatchStatus] = UNSET
    close_match_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        close_match_name = self.close_match_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if close_match_name is not UNSET:
            field_dict["closeMatchName"] = close_match_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: Union[Unset, BeneficiaryMatchStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BeneficiaryMatchStatus(_status)

        close_match_name = d.pop("closeMatchName", UNSET)

        user_beneficiary_match = cls(
            status=status,
            close_match_name=close_match_name,
        )

        user_beneficiary_match.additional_properties = d
        return user_beneficiary_match

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
