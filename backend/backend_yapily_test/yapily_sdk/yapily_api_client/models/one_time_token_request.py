from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OneTimeTokenRequest")


@_attrs_define
class OneTimeTokenRequest:
    """The request body containing the `OneTimeTokenRequest` json payload

    Attributes:
        one_time_token (str): __Mandatory__. The one time token to exchange for a consent token. Example: eyJ0eXAiOiJKV1
            QiLCJhbGciOiJIUzUxMiJ9.eyJJTlNUSVRVVElPTiI6ImJidmEtc2FuZGJveCIsIlVVSUQiOiJmMzNmNGU4ZC1jMDQ0LTQ2YTktOTlkMC0wYmRlM
            zIyYTJjOTIifQ.4Qv3NJI6av2nKi1U3aNmm71cIwJ3TvRsIlYDafQUVv_Khy_e-8oEpV_BoP4V1CII12oT-Yq4cPveHILz8BOwjg.
    """

    one_time_token: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        one_time_token = self.one_time_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "oneTimeToken": one_time_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        one_time_token = d.pop("oneTimeToken")

        one_time_token_request = cls(
            one_time_token=one_time_token,
        )

        one_time_token_request.additional_properties = d
        return one_time_token_request

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
