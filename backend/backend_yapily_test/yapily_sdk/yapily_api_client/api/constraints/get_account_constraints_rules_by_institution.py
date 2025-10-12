from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_list_response_of_data_constraints import ApiListResponseOfDataConstraints
from ...models.api_response_error import ApiResponseError
from ...models.get_account_constraints_rules_by_institution_endpoint_method import (
    GetAccountConstraintsRulesByInstitutionEndpointMethod,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    institution_ids: list[str],
    institution_country_code: str,
    endpoint_path: Union[Unset, str] = UNSET,
    endpoint_method: Union[Unset, GetAccountConstraintsRulesByInstitutionEndpointMethod] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_institution_ids = institution_ids

    params["institutionIds"] = json_institution_ids

    params["institutionCountryCode"] = institution_country_code

    params["endpointPath"] = endpoint_path

    json_endpoint_method: Union[Unset, str] = UNSET
    if not isinstance(endpoint_method, Unset):
        json_endpoint_method = endpoint_method.value

    params["endpointMethod"] = json_endpoint_method

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/institutions/constraints/data",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiListResponseOfDataConstraints, ApiResponseError]]:
    if response.status_code == 200:
        response_200 = ApiListResponseOfDataConstraints.from_dict(response.json())

        return response_200

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
) -> Response[Union[ApiListResponseOfDataConstraints, ApiResponseError]]:
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
    endpoint_path: Union[Unset, str] = UNSET,
    endpoint_method: Union[Unset, GetAccountConstraintsRulesByInstitutionEndpointMethod] = UNSET,
) -> Response[Union[ApiListResponseOfDataConstraints, ApiResponseError]]:
    """Get Data Constraints Rules

     Get Data Constraints Rules against an Institution for Account Authorisation requests

    Args:
        institution_ids (list[str]):
        institution_country_code (str):
        endpoint_path (Union[Unset, str]):
        endpoint_method (Union[Unset, GetAccountConstraintsRulesByInstitutionEndpointMethod]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiListResponseOfDataConstraints, ApiResponseError]]
    """

    kwargs = _get_kwargs(
        institution_ids=institution_ids,
        institution_country_code=institution_country_code,
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
    endpoint_path: Union[Unset, str] = UNSET,
    endpoint_method: Union[Unset, GetAccountConstraintsRulesByInstitutionEndpointMethod] = UNSET,
) -> Optional[Union[ApiListResponseOfDataConstraints, ApiResponseError]]:
    """Get Data Constraints Rules

     Get Data Constraints Rules against an Institution for Account Authorisation requests

    Args:
        institution_ids (list[str]):
        institution_country_code (str):
        endpoint_path (Union[Unset, str]):
        endpoint_method (Union[Unset, GetAccountConstraintsRulesByInstitutionEndpointMethod]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiListResponseOfDataConstraints, ApiResponseError]
    """

    return sync_detailed(
        client=client,
        institution_ids=institution_ids,
        institution_country_code=institution_country_code,
        endpoint_path=endpoint_path,
        endpoint_method=endpoint_method,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    institution_ids: list[str],
    institution_country_code: str,
    endpoint_path: Union[Unset, str] = UNSET,
    endpoint_method: Union[Unset, GetAccountConstraintsRulesByInstitutionEndpointMethod] = UNSET,
) -> Response[Union[ApiListResponseOfDataConstraints, ApiResponseError]]:
    """Get Data Constraints Rules

     Get Data Constraints Rules against an Institution for Account Authorisation requests

    Args:
        institution_ids (list[str]):
        institution_country_code (str):
        endpoint_path (Union[Unset, str]):
        endpoint_method (Union[Unset, GetAccountConstraintsRulesByInstitutionEndpointMethod]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiListResponseOfDataConstraints, ApiResponseError]]
    """

    kwargs = _get_kwargs(
        institution_ids=institution_ids,
        institution_country_code=institution_country_code,
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
    endpoint_path: Union[Unset, str] = UNSET,
    endpoint_method: Union[Unset, GetAccountConstraintsRulesByInstitutionEndpointMethod] = UNSET,
) -> Optional[Union[ApiListResponseOfDataConstraints, ApiResponseError]]:
    """Get Data Constraints Rules

     Get Data Constraints Rules against an Institution for Account Authorisation requests

    Args:
        institution_ids (list[str]):
        institution_country_code (str):
        endpoint_path (Union[Unset, str]):
        endpoint_method (Union[Unset, GetAccountConstraintsRulesByInstitutionEndpointMethod]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiListResponseOfDataConstraints, ApiResponseError]
    """

    return (
        await asyncio_detailed(
            client=client,
            institution_ids=institution_ids,
            institution_country_code=institution_country_code,
            endpoint_path=endpoint_path,
            endpoint_method=endpoint_method,
        )
    ).parsed
