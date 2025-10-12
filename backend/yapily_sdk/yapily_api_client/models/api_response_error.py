from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_error import ApiError
    from ..models.raw_response import RawResponse


T = TypeVar("T", bound="ApiResponseError")


@_attrs_define
class ApiResponseError:
    """Used to return errors from the bank from each request<ul><li>`400` - Returned by any `POST` endpoint when the body
    does not conform to the contract</li><li>`401` - Returned by any endpoint when an invalid `authToken` is used for
    authentication</li><li>`403` - Returned by any [Financial
    Data](https://docs.yapily.com/api/reference/#tag/Financial-Data) and any
    [Payments](https://docs.yapily.com/api/reference/#tag/Payments) endpoint when the `Consent` is no longer authorised
    to access financial data or to make a payment</li><li>`404` - Returned by any endpoint where there are path
    parameters and the path parameters supplied are unable to find the desired resource</li><li>`409` - Returned by any
    `POST` endpoint when creating a resource that conflicts with any other existing resource e.g. [Create
    User](https://docs.yapily.com/api/reference/#operation/addUser)</li><li>`424` - Returned by any [Financial
    Data](https://docs.yapily.com/api/reference/#tag/Financial-Data) and any
    [Payments](https://docs.yapily.com/api/reference/#tag/Payments) endpoint when the feature to be accessed is not
    supported by the `Institution`.</li><li>`500` - Returned by any endpoint when Yapily is down. If you encounter any
    false positives, please <a href="mailto:support@yapily.com">notify us</a></li></ul>

        Example:
            {'error': {'tracingId': '74b13ce8ed51419f92c5d609e04532de', 'code': 424, 'institutionError': {'errorMessage':
                '{"Code":"500 Internal Server Error","Id":"5ff8d331-4282-41e0-b5ef-1ac9ac39f009","Message":"Technical Error.
                Please try again later","Errors":[{"ErrorCode":"UK.OBIE.UnexpectedError","Message":"There was a problem
                processing your request. Please try again later"}]}', 'httpStatusCode': 500}, 'source': 'INSTITUTION', 'status':
                'FAILED_DEPENDENCY'}}

        Attributes:
            error (Union[Unset, ApiError]): Provides details of the error that has occurred.
            raw (Union[Unset, list['RawResponse']]):
    """

    error: Union[Unset, "ApiError"] = UNSET
    raw: Union[Unset, list["RawResponse"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        raw: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.raw, Unset):
            raw = []
            for raw_item_data in self.raw:
                raw_item = raw_item_data.to_dict()
                raw.append(raw_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if raw is not UNSET:
            field_dict["raw"] = raw

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_error import ApiError
        from ..models.raw_response import RawResponse

        d = dict(src_dict)
        _error = d.pop("error", UNSET)
        error: Union[Unset, ApiError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = ApiError.from_dict(_error)

        raw = []
        _raw = d.pop("raw", UNSET)
        for raw_item_data in _raw or []:
            raw_item = RawResponse.from_dict(raw_item_data)

            raw.append(raw_item)

        api_response_error = cls(
            error=error,
            raw=raw,
        )

        api_response_error.additional_properties = d
        return api_response_error

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
