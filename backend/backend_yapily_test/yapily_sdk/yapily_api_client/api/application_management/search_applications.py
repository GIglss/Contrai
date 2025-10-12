from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error_response import ApiErrorResponse
from ...models.api_list_of_application_response import ApiListOfApplicationResponse
from ...models.search_applications_public_filter_values import SearchApplicationsPublicFilterValues
from ...models.validation_error_response import ValidationErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    public_filter_values: Union[Unset, "SearchApplicationsPublicFilterValues"] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_public_filter_values: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(public_filter_values, Unset):
        json_public_filter_values = public_filter_values.to_dict()
    if not isinstance(json_public_filter_values, Unset):
        params.update(json_public_filter_values)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/applications",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiErrorResponse, ApiListOfApplicationResponse, ValidationErrorResponse]]:
    if response.status_code == 200:
        response_200 = ApiListOfApplicationResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ValidationErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ApiErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = ApiErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiErrorResponse, ApiListOfApplicationResponse, ValidationErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    public_filter_values: Union[Unset, "SearchApplicationsPublicFilterValues"] = UNSET,
) -> Response[Union[ApiErrorResponse, ApiListOfApplicationResponse, ValidationErrorResponse]]:
    """Retrieve sub-applications for the root application provided in the authentication token.

     Retrieves sub-applications for the root application provided in the authentication token. If a sub-
    application is provided in the authentication token, it will return an empty list.

    Args:
        public_filter_values (Union[Unset, SearchApplicationsPublicFilterValues]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponse, ApiListOfApplicationResponse, ValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        public_filter_values=public_filter_values,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    public_filter_values: Union[Unset, "SearchApplicationsPublicFilterValues"] = UNSET,
) -> Optional[Union[ApiErrorResponse, ApiListOfApplicationResponse, ValidationErrorResponse]]:
    """Retrieve sub-applications for the root application provided in the authentication token.

     Retrieves sub-applications for the root application provided in the authentication token. If a sub-
    application is provided in the authentication token, it will return an empty list.

    Args:
        public_filter_values (Union[Unset, SearchApplicationsPublicFilterValues]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponse, ApiListOfApplicationResponse, ValidationErrorResponse]
    """

    return sync_detailed(
        client=client,
        public_filter_values=public_filter_values,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    public_filter_values: Union[Unset, "SearchApplicationsPublicFilterValues"] = UNSET,
) -> Response[Union[ApiErrorResponse, ApiListOfApplicationResponse, ValidationErrorResponse]]:
    """Retrieve sub-applications for the root application provided in the authentication token.

     Retrieves sub-applications for the root application provided in the authentication token. If a sub-
    application is provided in the authentication token, it will return an empty list.

    Args:
        public_filter_values (Union[Unset, SearchApplicationsPublicFilterValues]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponse, ApiListOfApplicationResponse, ValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        public_filter_values=public_filter_values,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    public_filter_values: Union[Unset, "SearchApplicationsPublicFilterValues"] = UNSET,
) -> Optional[Union[ApiErrorResponse, ApiListOfApplicationResponse, ValidationErrorResponse]]:
    """Retrieve sub-applications for the root application provided in the authentication token.

     Retrieves sub-applications for the root application provided in the authentication token. If a sub-
    application is provided in the authentication token, it will return an empty list.

    Args:
        public_filter_values (Union[Unset, SearchApplicationsPublicFilterValues]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponse, ApiListOfApplicationResponse, ValidationErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            public_filter_values=public_filter_values,
        )
    ).parsed
