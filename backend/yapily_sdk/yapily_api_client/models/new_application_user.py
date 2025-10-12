from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewApplicationUser")


@_attrs_define
class NewApplicationUser:
    """Details of a new user to be created for the application.

    Attributes:
        application_user_id (Union[Unset, str]): __Optional__. The unique identifier of the `Application User` assigned
            by the Application Owner. Example: user-234562290.
        reference_id (Union[Unset, str]): __Deprecated__. A non-unique reference Id for the `Application User`.
        vop_opt_out (Union[Unset, bool]): __Optional__. A flag to indicate whether the user has opted out of VOP.
            Default: False.
    """

    application_user_id: Union[Unset, str] = UNSET
    reference_id: Union[Unset, str] = UNSET
    vop_opt_out: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_user_id = self.application_user_id

        reference_id = self.reference_id

        vop_opt_out = self.vop_opt_out

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if application_user_id is not UNSET:
            field_dict["applicationUserId"] = application_user_id
        if reference_id is not UNSET:
            field_dict["referenceId"] = reference_id
        if vop_opt_out is not UNSET:
            field_dict["vopOptOut"] = vop_opt_out

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        application_user_id = d.pop("applicationUserId", UNSET)

        reference_id = d.pop("referenceId", UNSET)

        vop_opt_out = d.pop("vopOptOut", UNSET)

        new_application_user = cls(
            application_user_id=application_user_id,
            reference_id=reference_id,
            vop_opt_out=vop_opt_out,
        )

        new_application_user.additional_properties = d
        return new_application_user

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
