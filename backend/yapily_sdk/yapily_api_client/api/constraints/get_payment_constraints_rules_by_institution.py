from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response_error import ApiResponseError
from ...models.get_payment_constraints_rules_by_institution_endpoint_method import (
    GetPaymentConstraintsRulesByInstitutionEndpointMethod,
)
from ...models.get_payment_constraints_rules_by_institution_payment_type import (
    GetPaymentConstraintsRulesByInstitutionPaymentType,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    institution_ids: list[str],
    institution_country_code: str,
    payment_type: GetPaymentConstraintsRulesByInstitutionPaymentType,
    endpoint_path: Union[Unset, str] = UNSET,
    endpoint_method: Union[Unset, GetPaymentConstraintsRulesByInstitutionEndpointMethod] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_institution_ids = institution_ids

    params["institutionIds"] = json_institution_ids

    params["institutionCountryCode"] = institution_country_code

    json_payment_type = payment_type.value
    params["paymentType"] = json_payment_type

    params["endpointPath"] = endpoint_path

    json_endpoint_method: Union[Unset, str] = UNSET
    if not isinstance(endpoint_method, Unset):
        json_endpoint_method = endpoint_method.value

    params["endpointMethod"] = json_endpoint_method

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/institutions/constraints/payments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiResponseError]:
    if response.status_code == 400:
        response_400 = ApiResponseError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiResponseError.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ApiResponseError.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ApiResponseError.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiResponseError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    institution_ids: list[str],
    institution_country_code: str,
    payment_type: GetPaymentConstraintsRulesByInstitutionPaymentType,
    endpoint_path: Union[Unset, str] = UNSET,
    endpoint_method: Union[Unset, GetPaymentConstraintsRulesByInstitutionEndpointMethod] = UNSET,
) -> Response[ApiResponseError]:
    """Get Payment Constraints Rules

     Retrieve institution specific constraints for payment authorisation and submission requests

    Args:
        institution_ids (list[str]):
        institution_country_code (str):
        payment_type (GetPaymentConstraintsRulesByInstitutionPaymentType):
        endpoint_path (Union[Unset, str]):
        endpoint_method (Union[Unset, GetPaymentConstraintsRulesByInstitutionEndpointMethod]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiResponseError]
    """

    kwargs = _get_kwargs(
        institution_ids=institution_ids,
        institution_country_code=institution_country_code,
        payment_type=payment_type,
        endpoint_path=endpoint_path,
        endpoint_method=endpoint_method,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    institution_ids: list[str],
    institution_country_code: str,
    payment_type: GetPaymentConstraintsRulesByInstitutionPaymentType,
    endpoint_path: Union[Unset, str] = UNSET,
    endpoint_method: Union[Unset, GetPaymentConstraintsRulesByInstitutionEndpointMethod] = UNSET,
) -> Optional[ApiResponseError]:
    """Get Payment Constraints Rules

     Retrieve institution specific constraints for payment authorisation and submission requests

    Args:
        institution_ids (list[str]):
        institution_country_code (str):
        payment_type (GetPaymentConstraintsRulesByInstitutionPaymentType):
        endpoint_path (Union[Unset, str]):
        endpoint_method (Union[Unset, GetPaymentConstraintsRulesByInstitutionEndpointMethod]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiResponseError
    """

    return sync_detailed(
        client=client,
        institution_ids=institution_ids,
        institution_country_code=institution_country_code,
        payment_type=payment_type,
        endpoint_path=endpoint_path,
        endpoint_method=endpoint_method,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    institution_ids: list[str],
    institution_country_code: str,
    payment_type: GetPaymentConstraintsRulesByInstitutionPaymentType,
    endpoint_path: Union[Unset, str] = UNSET,
    endpoint_method: Union[Unset, GetPaymentConstraintsRulesByInstitutionEndpointMethod] = UNSET,
) -> Response[ApiResponseError]:
    """Get Payment Constraints Rules

     Retrieve institution specific constraints for payment authorisation and submission requests

    Args:
        institution_ids (list[str]):
        institution_country_code (str):
        payment_type (GetPaymentConstraintsRulesByInstitutionPaymentType):
        endpoint_path (Union[Unset, str]):
        endpoint_method (Union[Unset, GetPaymentConstraintsRulesByInstitutionEndpointMethod]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiResponseError]
    """

    kwargs = _get_kwargs(
        institution_ids=institution_ids,
        institution_country_code=institution_country_code,
        payment_type=payment_type,
        endpoint_path=endpoint_path,
        endpoint_method=endpoint_method,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    institution_ids: list[str],
    institution_country_code: str,
    payment_type: GetPaymentConstraintsRulesByInstitutionPaymentType,
    endpoint_path: Union[Unset, str] = UNSET,
    endpoint_method: Union[Unset, GetPaymentConstraintsRulesByInstitutionEndpointMethod] = UNSET,
) -> Optional[ApiResponseError]:
    """Get Payment Constraints Rules

     Retrieve institution specific constraints for payment authorisation and submission requests

    Args:
        institution_ids (list[str]):
        institution_country_code (str):
        payment_type (GetPaymentConstraintsRulesByInstitutionPaymentType):
        endpoint_path (Union[Unset, str]):
        endpoint_method (Union[Unset, GetPaymentConstraintsRulesByInstitutionEndpointMethod]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiResponseError
    """

    return (
        await asyncio_detailed(
            client=client,
            institution_ids=institution_ids,
            institution_country_code=institution_country_code,
            payment_type=payment_type,
            endpoint_path=endpoint_path,
            endpoint_method=endpoint_method,
        )
    ).parsed
