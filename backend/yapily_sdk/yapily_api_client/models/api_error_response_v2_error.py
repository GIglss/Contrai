from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_error_response_v2_error_issues_item import ApiErrorResponseV2ErrorIssuesItem


T = TypeVar("T", bound="ApiErrorResponseV2Error")


@_attrs_define
class ApiErrorResponseV2Error:
    """
    Attributes:
        tracing_id (str): Unique identifier of the request, used by Yapily for support purposes
        code (int): Numeric HTTP status code associated with the error
        status (str): Textual description of the HTTP status
        issues (list['ApiErrorResponseV2ErrorIssuesItem']): List of issues relating to the error
        support_url (Union[Unset, str]): Link to where further information regarding the error can be found
        source (Union[Unset, str]): Source of the error. This may be YAPILY, the INSTITUTION, or the USER
    """

    tracing_id: str
    code: int
    status: str
    issues: list["ApiErrorResponseV2ErrorIssuesItem"]
    support_url: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tracing_id = self.tracing_id

        code = self.code

        status = self.status

        issues = []
        for issues_item_data in self.issues:
            issues_item = issues_item_data.to_dict()
            issues.append(issues_item)

        support_url = self.support_url

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tracingId": tracing_id,
                "code": code,
                "status": status,
                "issues": issues,
            }
        )
        if support_url is not UNSET:
            field_dict["supportUrl"] = support_url
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_error_response_v2_error_issues_item import ApiErrorResponseV2ErrorIssuesItem

        d = dict(src_dict)
        tracing_id = d.pop("tracingId")

        code = d.pop("code")

        status = d.pop("status")

        issues = []
        _issues = d.pop("issues")
        for issues_item_data in _issues:
            issues_item = ApiErrorResponseV2ErrorIssuesItem.from_dict(issues_item_data)

            issues.append(issues_item)

        support_url = d.pop("supportUrl", UNSET)

        source = d.pop("source", UNSET)

        api_error_response_v2_error = cls(
            tracing_id=tracing_id,
            code=code,
            status=status,
            issues=issues,
            support_url=support_url,
            source=source,
        )

        api_error_response_v2_error.additional_properties = d
        return api_error_response_v2_error

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
