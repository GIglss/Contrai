from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.type_ import Type
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScaMethod")


@_attrs_define
class ScaMethod:
    """__Conditional__. Used to update the authorisation with the sca method of the user's choice for the `Institution`
    that uses the embedded authorisation flow. If the user has multiple sca methods configured, the `Institution` will
    allow the user to select from each of these options. <br><br>When the user has multiple sca methods for the
    `Institution`, this is the second step required in the embedded authorisation flow to authorise the `Consent`.

        Example:
            {'id': '944', 'type': 'PUSH_OTP', 'description': 'SecureSIGN'}

        Attributes:
            id (str): __Mandatory__. The id of the sca method provided by the `Institution` Example: 258211#OPTICAL.
            type_ (Union[Unset, Type]): The `SCA` method type available for the user
            description (Union[Unset, str]): __Optional__. A description of the sca method if provided by the `Institution`
                Example: Testkarte Hr. Haubach_1, optisch.
            information (Union[Unset, str]): Additional information from the institution to provide to the PSU to help with
                the selected SCA method. The language is determined by the institution and may vary. Example: Bitte bestätigen
                Sie den Vorgang in Ihrer SecureGo plus App.
            data (Union[Unset, list[str]]): Data from the institution to provide to the PSU to complete authorisation. The
                language is determined by the institution and may vary. Example:
                ['0488701109982928CY439040000100000010000520,00'].
    """

    id: str
    type_: Union[Unset, Type] = UNSET
    description: Union[Unset, str] = UNSET
    information: Union[Unset, str] = UNSET
    data: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        description = self.description

        information = self.information

        data: Union[Unset, list[str]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if description is not UNSET:
            field_dict["description"] = description
        if information is not UNSET:
            field_dict["information"] = information
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, Type]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = Type(_type_)

        description = d.pop("description", UNSET)

        information = d.pop("information", UNSET)

        data = cast(list[str], d.pop("data", UNSET))

        sca_method = cls(
            id=id,
            type_=type_,
            description=description,
            information=information,
            data=data,
        )

        sca_method.additional_properties = d
        return sca_method

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
