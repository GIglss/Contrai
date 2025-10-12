import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostAccountsAccountIdTransactionsCategorisationBody")


@_attrs_define
class PostAccountsAccountIdTransactionsCategorisationBody:
    """
    Attributes:
        country_code (str): __Mandatory__. Two-letter country code in ISO 3166-1 alpha-2 format (e.g. GB)
        categorisation_type (str): __Mandatory__. Allowed values are `consumer` and `business`.
        from_ (Union[Unset, datetime.datetime]): __Optional__. Returned transactions will be on or after this date
            (yyyy-MM-dd'T'HH:mm:ss.SSSZ).
        before (Union[Unset, datetime.datetime]): __Optional__. Returned transactions will be on or before this date
            (yyyy-MM-dd'T'HH:mm:ss.SSSZ).
    """

    country_code: str
    categorisation_type: str
    from_: Union[Unset, datetime.datetime] = UNSET
    before: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country_code = self.country_code

        categorisation_type = self.categorisation_type

        from_: Union[Unset, str] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        before: Union[Unset, str] = UNSET
        if not isinstance(self.before, Unset):
            before = self.before.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "countryCode": country_code,
                "categorisationType": categorisation_type,
            }
        )
        if from_ is not UNSET:
            field_dict["from"] = from_
        if before is not UNSET:
            field_dict["before"] = before

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        country_code = d.pop("countryCode")

        categorisation_type = d.pop("categorisationType")

        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, datetime.datetime]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = isoparse(_from_)

        _before = d.pop("before", UNSET)
        before: Union[Unset, datetime.datetime]
        if isinstance(_before, Unset):
            before = UNSET
        else:
            before = isoparse(_before)

        post_accounts_account_id_transactions_categorisation_body = cls(
            country_code=country_code,
            categorisation_type=categorisation_type,
            from_=from_,
            before=before,
        )

        post_accounts_account_id_transactions_categorisation_body.additional_properties = d
        return post_accounts_account_id_transactions_categorisation_body

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
