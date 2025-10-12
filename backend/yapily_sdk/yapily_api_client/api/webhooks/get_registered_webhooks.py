from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error_response_v2 import ApiErrorResponseV2
from ...models.get_registered_webhooks_response_200 import GetRegisteredWebhooksResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    sub_application: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(sub_application, Unset):
        headers["sub-application"] = sub_application

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webhook/events",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiErrorResponseV2, GetRegisteredWebhooksResponse200]]:
    if response.status_code == 200:
        response_200 = GetRegisteredWebhooksResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiErrorResponseV2.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiErrorResponseV2.from_dict(response.json())

        return response_401

    if response.status_code == 500:
        response_500 = ApiErrorResponseV2.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiErrorResponseV2, GetRegisteredWebhooksResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    sub_application: Union[Unset, UUID] = UNSET,
) -> Response[Union[ApiErrorResponseV2, GetRegisteredWebhooksResponse200]]:
    """Retrieve All Webhook Events

     Retrieve the list of registered webhooks for your application

    Args:
        sub_application (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponseV2, GetRegisteredWebhooksResponse200]]
    """

    kwargs = _get_kwargs(
        sub_application=sub_application,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    sub_application: Union[Unset, UUID] = UNSET,
) -> Optional[Union[ApiErrorResponseV2, GetRegisteredWebhooksResponse200]]:
    """Retrieve All Webhook Events

     Retrieve the list of registered webhooks for your application

    Args:
        sub_application (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponseV2, GetRegisteredWebhooksResponse200]
    """

    return sync_detailed(
        client=client,
        sub_application=sub_application,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    sub_application: Union[Unset, UUID] = UNSET,
) -> Response[Union[ApiErrorResponseV2, GetRegisteredWebhooksResponse200]]:
    """Retrieve All Webhook Events

     Retrieve the list of registered webhooks for your application

    Args:
        sub_application (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponseV2, GetRegisteredWebhooksResponse200]]
    """

    kwargs = _get_kwargs(
        sub_application=sub_application,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    sub_application: Union[Unset, UUID] = UNSET,
) -> Optional[Union[ApiErrorResponseV2, GetRegisteredWebhooksResponse200]]:
    """Retrieve All Webhook Events

     Retrieve the list of registered webhooks for your application

    Args:
        sub_application (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponseV2, GetRegisteredWebhooksResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            sub_application=sub_application,
        )
    ).parsed
