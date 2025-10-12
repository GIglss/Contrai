from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_response_error import ApiResponseError
from ...models.consent import Consent
from ...models.one_time_token_request import OneTimeTokenRequest
from ...types import Response


def _get_kwargs(
    *,
    body: OneTimeTokenRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/consent-one-time-token",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ApiResponseError, Consent]:
    if response.status_code == 201:
        response_201 = Consent.from_dict(response.json())

        return response_201

    response_default = ApiResponseError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiResponseError, Consent]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: OneTimeTokenRequest,
) -> Response[Union[ApiResponseError, Consent]]:
    """Exchange One Time Token

     Exchange a One-time-token for the consent token

    Args:
        body (OneTimeTokenRequest): The request body containing the `OneTimeTokenRequest` json
            payload

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiResponseError, Consent]]
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
    body: OneTimeTokenRequest,
) -> Optional[Union[ApiResponseError, Consent]]:
    """Exchange One Time Token

     Exchange a One-time-token for the consent token

    Args:
        body (OneTimeTokenRequest): The request body containing the `OneTimeTokenRequest` json
            payload

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiResponseError, Consent]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: OneTimeTokenRequest,
) -> Response[Union[ApiResponseError, Consent]]:
    """Exchange One Time Token

     Exchange a One-time-token for the consent token

    Args:
        body (OneTimeTokenRequest): The request body containing the `OneTimeTokenRequest` json
            payload

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiResponseError, Consent]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: OneTimeTokenRequest,
) -> Optional[Union[ApiResponseError, Consent]]:
    """Exchange One Time Token

     Exchange a One-time-token for the consent token

    Args:
        body (OneTimeTokenRequest): The request body containing the `OneTimeTokenRequest` json
            payload

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiResponseError, Consent]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
