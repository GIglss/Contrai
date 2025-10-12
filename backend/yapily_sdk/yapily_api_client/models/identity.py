from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identity_address import IdentityAddress


T = TypeVar("T", bound="Identity")


@_attrs_define
class Identity:
    """Identification details of a party associated with an account e.g. (account owner or operator).

    Attributes:
        id (Union[Unset, str]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        full_name (Union[Unset, str]):
        gender (Union[Unset, str]):
        birthdate (Union[Unset, str]):
        email (Union[Unset, str]):
        phone (Union[Unset, str]):
        addresses (Union[Unset, list['IdentityAddress']]):
    """

    id: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    gender: Union[Unset, str] = UNSET
    birthdate: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    addresses: Union[Unset, list["IdentityAddress"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        first_name = self.first_name

        last_name = self.last_name

        full_name = self.full_name

        gender = self.gender

        birthdate = self.birthdate

        email = self.email

        phone = self.phone

        addresses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = []
            for addresses_item_data in self.addresses:
                addresses_item = addresses_item_data.to_dict()
                addresses.append(addresses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if gender is not UNSET:
            field_dict["gender"] = gender
        if birthdate is not UNSET:
            field_dict["birthdate"] = birthdate
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if addresses is not UNSET:
            field_dict["addresses"] = addresses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.identity_address import IdentityAddress

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        full_name = d.pop("fullName", UNSET)

        gender = d.pop("gender", UNSET)

        birthdate = d.pop("birthdate", UNSET)

        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        addresses = []
        _addresses = d.pop("addresses", UNSET)
        for addresses_item_data in _addresses or []:
            addresses_item = IdentityAddress.from_dict(addresses_item_data)

            addresses.append(addresses_item)

        identity = cls(
            id=id,
            first_name=first_name,
            last_name=last_name,
            full_name=full_name,
            gender=gender,
            birthdate=birthdate,
            email=email,
            phone=phone,
            addresses=addresses,
        )

        identity.additional_properties = d
        return identity

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
