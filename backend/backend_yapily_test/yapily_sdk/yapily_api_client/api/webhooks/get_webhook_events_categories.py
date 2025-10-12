from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error_response_v2 import ApiErrorResponseV2
from ...models.get_webhook_events_categories_response_200 import GetWebhookEventsCategoriesResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webhook/events/categories",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiErrorResponseV2, GetWebhookEventsCategoriesResponse200]]:
    if response.status_code == 200:
        response_200 = GetWebhookEventsCategoriesResponse200.from_dict(response.json())

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
) -> Response[Union[ApiErrorResponseV2, GetWebhookEventsCategoriesResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ApiErrorResponseV2, GetWebhookEventsCategoriesResponse200]]:
    """Get Webhook Categories

     Retrieve a comprehensive list of event categories that can be registered for webhook notifications
    in your application. These event categories can be used to subscribe a webhook to specific events,
    enabling your application to receive real-time notifications when these events occur.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponseV2, GetWebhookEventsCategoriesResponse200]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ApiErrorResponseV2, GetWebhookEventsCategoriesResponse200]]:
    """Get Webhook Categories

     Retrieve a comprehensive list of event categories that can be registered for webhook notifications
    in your application. These event categories can be used to subscribe a webhook to specific events,
    enabling your application to receive real-time notifications when these events occur.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponseV2, GetWebhookEventsCategoriesResponse200]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ApiErrorResponseV2, GetWebhookEventsCategoriesResponse200]]:
    """Get Webhook Categories

     Retrieve a comprehensive list of event categories that can be registered for webhook notifications
    in your application. These event categories can be used to subscribe a webhook to specific events,
    enabling your application to receive real-time notifications when these events occur.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponseV2, GetWebhookEventsCategoriesResponse200]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ApiErrorResponseV2, GetWebhookEventsCategoriesResponse200]]:
    """Get Webhook Categories

     Retrieve a comprehensive list of event categories that can be registered for webhook notifications
    in your application. These event categories can be used to subscribe a webhook to specific events,
    enabling your application to receive real-time notifications when these events occur.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponseV2, GetWebhookEventsCategoriesResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
