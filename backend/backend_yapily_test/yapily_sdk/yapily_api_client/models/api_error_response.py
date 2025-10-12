from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_details import ErrorDetails


T = TypeVar("T", bound="ApiErrorResponse")


@_attrs_define
class ApiErrorResponse:
    """Used to return errors from the bank from each request<ul><li>`400` - Returned by any `POST` endpoint when the body
    does not conform to the contract</li><li>`401` - Returned by any endpoint when an invalid `authToken` is used for
    authentication</li><li>`403` - Returned by any [Financial Data](https://docs.yapily.com/api/#yapily-api-financial-
    data) and any [Payments](https://docs.yapily.com/api/#yapily-api-payments) endpoint when the `Consent` is no longer
    authorised to access financial data or to make a payment</li><li>`404` - Returned by any endpoint where there are
    path parameters and the path parameters supplied are unable to find the desired resource</li><li>`409` - Returned by
    any `POST` endpoint when creating a resource that conflicts with any other existing resource e.g. [Create
    User](https://docs.yapily.com/api/#create-user)</li><li>`424` - Returned by any [Financial
    Data](https://docs.yapily.com/api/#yapily-api-financial-data) and any
    [Payments](https://docs.yapily.com/api/#yapily-api-payments) endpoint when the feature to be accessed is not
    supported by the `Institution`.</li><li>`500` - Returned by any endpoint when Yapily is down. If you encounter any
    false positives, please <a href="mailto:support@yapily.com">notify us</a></li></ul>

        Example:
            {'error': {'tracingId': '0c2d0973bdd24224a65e5d0f7d1b6154', 'code': 400, 'status': 'BAD_REQUEST', 'supportUrl':
                'https://support.yapily.com/', 'source': 'YAPILY', 'issues': [{'type': 'INVALID_REQUEST', 'code':
                'INVALID_PROPERTY_UNEXPECTED_VALUE', 'parameter': '$.payer.accountidentifications.type', 'message': 'Type Should
                be one of [PAN, SORT_CODE, ACCOUNT_NUMBER]', 'institutionError': {'errorMessage': '{"Code":"400
                BadRequest","Id":"3517bfc2-c3ee-4f2f-b4f8-12f62478e0d1","Message":"No Resource
                found","Errors":[{"ErrorCode":"UK.OBIE.Resource.NotFound","Message":"No resource found corresponding to the
                consent id"}]}', 'httpStatusCode': 400}}]}}

        Attributes:
            error (Union[Unset, ErrorDetails]):
    """

    error: Union[Unset, "ErrorDetails"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_details import ErrorDetails

        d = dict(src_dict)
        _error = d.pop("error", UNSET)
        error: Union[Unset, ErrorDetails]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = ErrorDetails.from_dict(_error)

        api_error_response = cls(
            error=error,
        )

        api_error_response.additional_properties = d
        return api_error_response

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
