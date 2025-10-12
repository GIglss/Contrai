from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_identifier import AccountIdentifier
    from ..models.user_beneficiary_match import UserBeneficiaryMatch


T = TypeVar("T", bound="UserBeneficiaryValidationRequest")


@_attrs_define
class UserBeneficiaryValidationRequest:
    """Beneficiary request with the details of the VoP result.

    Attributes:
        name (str): name of the beneficiary Example: John Doe.
        account_identifier (AccountIdentifier): Account's details.
        match (Union[Unset, UserBeneficiaryMatch]): Details of the match given by the institution.
    """

    name: str
    account_identifier: "AccountIdentifier"
    match: Union[Unset, "UserBeneficiaryMatch"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        account_identifier = self.account_identifier.to_dict()

        match: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.match, Unset):
            match = self.match.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "accountIdentifier": account_identifier,
            }
        )
        if match is not UNSET:
            field_dict["match"] = match

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_identifier import AccountIdentifier
        from ..models.user_beneficiary_match import UserBeneficiaryMatch

        d = dict(src_dict)
        name = d.pop("name")

        account_identifier = AccountIdentifier.from_dict(d.pop("accountIdentifier"))

        _match = d.pop("match", UNSET)
        match: Union[Unset, UserBeneficiaryMatch]
        if isinstance(_match, Unset):
            match = UNSET
        else:
            match = UserBeneficiaryMatch.from_dict(_match)

        user_beneficiary_validation_request = cls(
            name=name,
            account_identifier=account_identifier,
            match=match,
        )

        user_beneficiary_validation_request.additional_properties = d
        return user_beneficiary_validation_request

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
