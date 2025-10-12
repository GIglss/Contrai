from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserCredentials")


@_attrs_define
class UserCredentials:
    """__Conditional__. Used to capture the user's credentials to allow them to login to an `Institution` that uses the
    embedded account authorisation flow. <br><br>This is the first step required in the embedded account authorisation
    flow to authorise the `Consent`.

        Attributes:
            id (str): __Mandatory__. The login id for the user for a particular `Institution`. Example: 6154057725.
            password (str): __Mandatory__. The password of the user to login to a particular `Institution`. Example:
                PISPWD12.
            corporate_id (Union[Unset, str]): __Conditional__. The corporate login for the user for a particular corporate
                `Institution`. Example: 6345898763.
    """

    id: str
    password: str
    corporate_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        password = self.password

        corporate_id = self.corporate_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "password": password,
            }
        )
        if corporate_id is not UNSET:
            field_dict["corporateId"] = corporate_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        password = d.pop("password")

        corporate_id = d.pop("corporateId", UNSET)

        user_credentials = cls(
            id=id,
            password=password,
            corporate_id=corporate_id,
        )

        user_credentials.additional_properties = d
        return user_credentials

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
