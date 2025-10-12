from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.request_constraints import RequestConstraints


T = TypeVar("T", bound="DataConstraintsResponse")


@_attrs_define
class DataConstraintsResponse:
    """
    Attributes:
        institution_id (str): The id to represent the `Institution`. Example: modelo-sandbox.
        request (RequestConstraints): Object defining the constraints rules applicable for a given requests.
        institution_country_code (Union[Unset, str]): 2 letter ISO Country code of the `Institution`. Example: GB.
        endpoint_path (Union[Unset, str]): Define the applicable API end point.
        endpoint_method (Union[Unset, str]): Https Method for the endpoint.
    """

    institution_id: str
    request: "RequestConstraints"
    institution_country_code: Union[Unset, str] = UNSET
    endpoint_path: Union[Unset, str] = UNSET
    endpoint_method: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        institution_id = self.institution_id

        request = self.request.to_dict()

        institution_country_code = self.institution_country_code

        endpoint_path = self.endpoint_path

        endpoint_method = self.endpoint_method

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "institutionId": institution_id,
                "request": request,
            }
        )
        if institution_country_code is not UNSET:
            field_dict["institutionCountryCode"] = institution_country_code
        if endpoint_path is not UNSET:
            field_dict["endpointPath"] = endpoint_path
        if endpoint_method is not UNSET:
            field_dict["endpointMethod"] = endpoint_method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.request_constraints import RequestConstraints

        d = dict(src_dict)
        institution_id = d.pop("institutionId")

        request = RequestConstraints.from_dict(d.pop("request"))

        institution_country_code = d.pop("institutionCountryCode", UNSET)

        endpoint_path = d.pop("endpointPath", UNSET)

        endpoint_method = d.pop("endpointMethod", UNSET)

        data_constraints_response = cls(
            institution_id=institution_id,
            request=request,
            institution_country_code=institution_country_code,
            endpoint_path=endpoint_path,
            endpoint_method=endpoint_method,
        )

        data_constraints_response.additional_properties = d
        return data_constraints_response

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
