from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_constraints_response import DataConstraintsResponse
    from ..models.response_meta import ResponseMeta


T = TypeVar("T", bound="ApiListResponseOfDataConstraints")


@_attrs_define
class ApiListResponseOfDataConstraints:
    """
    Example:
        {'meta': {'tracingId': 'a43049c1dbc04d6f8c8e2dfdc523217a'}, 'data': [{'institutionId': 'mock-sandbox',
            'institutionCountryCode': 'GB', 'endpointPath': '/account-auth-requests', 'endpointMethod': 'POST', 'request':
            {'headers': {'title': 'Header', 'type': 'object', 'properties': {'psuID': {'title': 'PSU Id', 'type': 'string',
            'description': '__Mandatory__. The psu id'}}}, 'body': {'required': ['institutionId'], 'type': 'object',
            'properties': {'userUuid': {'title': 'User UUID', 'type': 'string', 'format': 'uuid'}, 'institutionId':
            {'title': 'Institution Identifier', 'type': 'string', 'description': '__Mandatory__. The reference to the
            `Institution` which identifies which institution the authorisation request is sent to.', 'example': 'yapily-
            mock'}, 'oneTimeToken': {'title': 'One Time Token', 'type': 'boolean', 'description': '__Conditional__. Used to
            receive a `oneTimeToken` rather than a `consentToken` at the `callback` for additional security. This can only
            be used when the `callback` is set. <br><br>See [Using a callback with an OTT
            (Optional)](https://docs.yapily.com/pages/knowledge/yapily-concepts/callback_url/#using-a-callback-with-an-ott-
            optional) for more information.', 'example': False}, 'callback': {'title': 'Callback', 'type': 'string',
            'description': '__Optional__. The server to redirect the user to after the user complete the authorisation at
            the `Institution`. <br><br>See [Using a callback (Optional)](https://docs.yapily.com/pages/knowledge/yapily-
            concepts/callback_url/#using-a-callback-optional) for more information.', 'example': 'https://display-
            parameters.com'}, 'accountRequest': {'title': 'Account Request', 'type': 'object', 'properties':
            {'transactionFrom': {'title': 'Transaction From Date', 'type': 'string', 'description': '__Optional__. Used to
            specify the lower bound on when to pull transaction. This should be declared when accessing transaction older
            than 90 days for banks in the [CBI Globe](https://docs.yapily.com/pages/knowledge/open-banking/cbi_globe/).',
            'format': 'date-time'}, 'transactionTo': {'title': 'Transaction To Date', 'type': 'string', 'description':
            '__Optional__. When performing a request using the consent, this is the latest date of transaction records that
            can be retrieved.', 'format': 'date-time'}, 'expiresAt': {'title': 'Expires At', 'type': 'string',
            'description': "__Optional__. Used to set a hard date for when the user's associated `Consent` will
            expire.<br><br>**Note**: If this supported by the bank, specifying this is property is opting out of having a
            long-lived consent that can be perpetually re-authorised by the user. This will add an `expiresAt` field on the
            `Consent` object which will render it unusable after this date.<br><br>**Note**: This is not supported by every
            `Institution`. In such case, the request will not fail but the property will be ignored and the created
            `Consent` will not have an expiry date.", 'format': 'date-time'}, 'accountIdentifiers': {'title': 'Account
            Info', 'required': ['accountIdentification'], 'type': 'object', 'properties': {'accountId': {'type': 'string',
            'description': '__Conditional__. Unique identifier of the account.', 'example': '500000000000000000000001'},
            'accountIdentification': {'title': 'Account Identifications', 'required': ['identification', 'type'], 'type':
            'object', 'properties': {'type': {'enum': ['SORT_CODE', 'ACCOUNT_NUMBER', 'IBAN', 'BBAN', 'BIC', 'PAN',
            'MASKED_PAN', 'MSISDN', 'BSB', 'NCC', 'ABA', 'ABA_WIRE', 'ABA_ACH', 'EMAIL', 'ROLL_NUMBER', 'BLZ', 'IFS',
            'CLABE', 'CTN', 'BRANCH_CODE', 'VIRTUAL_ACCOUNT_ID'], 'title': 'Account Identification Type', 'type': 'string',
            'description': '__Mandatory__. Used to describe the format of the account.<br><br> See [Account Identification
            Combinations](https://docs.yapily.com/pages/key-concepts/payments/payment-execution/intro-to-payment-
            execution/#account-identifications-combinations) for more information on when to specify each type.', 'example':
            'SORT_CODE'}, 'identification': {'title': 'Account Identification', 'type': 'string', 'description':
            '__Mandatory__. The value associated with the account identification type.<br><br> See [Account Identification
            Combinations](https://docs.yapily.com/pages/key-concepts/payments/payment-execution/intro-to-payment-
            execution/#account-identifications-combinations) for more information on the format of the values.', 'example':
            '401016'}}}}, 'description': '__Conditional__. Used to create a request for the balance of the account
            specified. Once the user authorises the request, only the balance can be obtained by executing [GET Account
            Balances](./#get-account-balances).<br><br> This can be specified in conjunction with
            `accountIdentifiersForTransaction` to generate a `Consent` that can both access the accounts balance and
            transactions.'}, 'accountIdentifiersForTransaction': {'type': 'array', 'items': {'required':
            ['accountIdentification'], 'type': 'object', 'properties': {'accountId': {'type': 'string', 'description':
            '__Conditional__. Unique identifier of the account.', 'example': '500000000000000000000001'},
            'accountIdentification': {'title': 'Account Identifications', 'required': ['identification', 'type'], 'type':
            'object', 'properties': {'type': {'enum': ['SORT_CODE', 'ACCOUNT_NUMBER', 'IBAN', 'BBAN', 'BIC', 'PAN',
            'MASKED_PAN', 'MSISDN', 'BSB', 'NCC', 'ABA', 'ABA_WIRE', 'ABA_ACH', 'EMAIL', 'ROLL_NUMBER', 'BLZ', 'IFS',
            'CLABE', 'CTN', 'BRANCH_CODE', 'VIRTUAL_ACCOUNT_ID'], 'title': 'Account Identification Type', 'type': 'string',
            'description': '__Mandatory__. Used to describe the format of the account.<br><br> See [Account Identification
            Combinations](https://docs.yapily.com/pages/key-concepts/payments/payment-execution/intro-to-payment-
            execution/#account-identifications-combinations) for more information on when to specify each type.', 'example':
            'SORT_CODE'}, 'identification': {'title': 'Account Identification', 'type': 'string', 'description':
            '__Mandatory__. The value associated with the account identification type.<br><br> See [Account Identification
            Combinations](https://docs.yapily.com/pages/key-concepts/payments/payment-execution/intro-to-payment-
            execution/#account-identifications-combinations) for more information on the format of the values.', 'example':
            '401016'}}}}}, 'description': '__Conditional__. Used to create a request for the transactions of the account
            specified. Once the user authorises the request, only the transactions can be obtained by executing [GET Account
            Transactions](./#get-account-transactions). <br><br>This can be specified in conjunction with
            `accountIdentifiersForBalance` to generate a `Consent` that can both access the accounts balance and
            transactions.'}, 'accountIdentifiersForBalance': {'type': 'array', 'items': {'required':
            ['accountIdentification'], 'type': 'object', 'properties': {'accountId': {'type': 'string', 'description':
            '__Conditional__. Unique identifier of the account.', 'example': '500000000000000000000001'},
            'accountIdentification': {'title': 'Account Identifications', 'required': ['identification', 'type'], 'type':
            'object', 'properties': {'type': {'enum': ['SORT_CODE', 'ACCOUNT_NUMBER', 'IBAN', 'BBAN', 'BIC', 'PAN',
            'MASKED_PAN', 'MSISDN', 'BSB', 'NCC', 'ABA', 'ABA_WIRE', 'ABA_ACH', 'EMAIL', 'ROLL_NUMBER', 'BLZ', 'IFS',
            'CLABE', 'CTN', 'BRANCH_CODE', 'VIRTUAL_ACCOUNT_ID'], 'title': 'Account Identification Type', 'type': 'string',
            'description': '__Mandatory__. Used to describe the format of the account.<br><br> See [Account Identification
            Combinations](https://docs.yapily.com/pages/key-concepts/payments/payment-execution/intro-to-payment-
            execution/#account-identifications-combinations) for more information on when to specify each type.', 'example':
            'SORT_CODE'}, 'identification': {'title': 'Account Identification', 'type': 'string', 'description':
            '__Mandatory__. The value associated with the account identification type.<br><br> See [Account Identification
            Combinations](https://docs.yapily.com/pages/key-concepts/payments/payment-execution/intro-to-payment-
            execution/#account-identifications-combinations) for more information on the format of the values.', 'example':
            '401016'}}}}}, 'description': '__Conditional__. Used to create a request for the transactions of the account
            specified. Once the user authorises the request, only the transactions can be obtained by executing [GET Account
            Transactions](./#get-account-transactions). <br><br>This can be specified in conjunction with
            `accountIdentifiersForBalance` to generate a `Consent` that can both access the accounts balance and
            transactions.'}, 'featureScope': {'title': 'Feature Scope', 'type': 'array', 'items': {'type': 'string'},
            'description': 'Used to describe what functions are supported by the associated `Institution`'}}, 'description':
            'Account authorisation request schema'}}, 'description': 'The request body containing an
            `AccountAuthorisationRequest` json payload'}}}]}

    Attributes:
        meta (Union[Unset, ResponseMeta]):
        data (Union[Unset, list['DataConstraintsResponse']]):
    """

    meta: Union[Unset, "ResponseMeta"] = UNSET
    data: Union[Unset, list["DataConstraintsResponse"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        data: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meta is not UNSET:
            field_dict["meta"] = meta
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_constraints_response import DataConstraintsResponse
        from ..models.response_meta import ResponseMeta

        d = dict(src_dict)
        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, ResponseMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = ResponseMeta.from_dict(_meta)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = DataConstraintsResponse.from_dict(data_item_data)

            data.append(data_item)

        api_list_response_of_data_constraints = cls(
            meta=meta,
            data=data,
        )

        api_list_response_of_data_constraints.additional_properties = d
        return api_list_response_of_data_constraints

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
