from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error_response import ApiErrorResponse
from ...models.api_response_of_application_response import ApiResponseOfApplicationResponse
from ...models.application_request import ApplicationRequest
from ...models.validation_error_response import ValidationErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: ApplicationRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/applications",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiErrorResponse, ApiResponseOfApplicationResponse, ValidationErrorResponse]]:
    if response.status_code == 201:
        response_201 = ApiResponseOfApplicationResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ValidationErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ApiErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ApiErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ApiErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiErrorResponse, ApiResponseOfApplicationResponse, ValidationErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApplicationRequest,
) -> Response[Union[ApiErrorResponse, ApiResponseOfApplicationResponse, ValidationErrorResponse]]:
    """Creates a sub-application for the root application id provided in the authentication token

     Creates a sub-application under the given root application id provided in the authentication token.
    The sub-application can use the root's credentials to call the API

    Args:
        body (ApplicationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponse, ApiResponseOfApplicationResponse, ValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApplicationRequest,
) -> Optional[Union[ApiErrorResponse, ApiResponseOfApplicationResponse, ValidationErrorResponse]]:
    """Creates a sub-application for the root application id provided in the authentication token

     Creates a sub-application under the given root application id provided in the authentication token.
    The sub-application can use the root's credentials to call the API

    Args:
        body (ApplicationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponse, ApiResponseOfApplicationResponse, ValidationErrorResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApplicationRequest,
) -> Response[Union[ApiErrorResponse, ApiResponseOfApplicationResponse, ValidationErrorResponse]]:
    """Creates a sub-application for the root application id provided in the authentication token

     Creates a sub-application under the given root application id provided in the authentication token.
    The sub-application can use the root's credentials to call the API

    Args:
        body (ApplicationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponse, ApiResponseOfApplicationResponse, ValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApplicationRequest,
) -> Optional[Union[ApiErrorResponse, ApiResponseOfApplicationResponse, ValidationErrorResponse]]:
    """Creates a sub-application for the root application id provided in the authentication token

     Creates a sub-application under the given root application id provided in the authentication token.
    The sub-application can use the root's credentials to call the API

    Args:
        body (ApplicationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponse, ApiResponseOfApplicationResponse, ValidationErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
