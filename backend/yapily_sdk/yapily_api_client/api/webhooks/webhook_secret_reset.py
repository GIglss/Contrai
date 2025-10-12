from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error_response_v2 import ApiErrorResponseV2
from ...models.webhook_secret_reset_body import WebhookSecretResetBody
from ...models.webhook_secret_reset_response_201 import WebhookSecretResetResponse201
from ...types import UNSET, Response, Unset


def _get_kwargs(
    webhook_id: UUID,
    *,
    body: WebhookSecretResetBody,
    sub_application: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(sub_application, Unset):
        headers["sub-application"] = sub_application

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/webhook/secrets/{webhook_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiErrorResponseV2, WebhookSecretResetResponse201]]:
    if response.status_code == 201:
        response_201 = WebhookSecretResetResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ApiErrorResponseV2.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiErrorResponseV2.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ApiErrorResponseV2.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ApiErrorResponseV2.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiErrorResponseV2, WebhookSecretResetResponse201]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    webhook_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: WebhookSecretResetBody,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Response[Union[ApiErrorResponseV2, WebhookSecretResetResponse201]]:
    """Reset Webhook Secret

     Reset webhook secret for a webhook that is already registered to your application

    Args:
        webhook_id (UUID):
        sub_application (Union[Unset, UUID]):
        body (WebhookSecretResetBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponseV2, WebhookSecretResetResponse201]]
    """

    kwargs = _get_kwargs(
        webhook_id=webhook_id,
        body=body,
        sub_application=sub_application,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    webhook_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: WebhookSecretResetBody,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Optional[Union[ApiErrorResponseV2, WebhookSecretResetResponse201]]:
    """Reset Webhook Secret

     Reset webhook secret for a webhook that is already registered to your application

    Args:
        webhook_id (UUID):
        sub_application (Union[Unset, UUID]):
        body (WebhookSecretResetBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponseV2, WebhookSecretResetResponse201]
    """

    return sync_detailed(
        webhook_id=webhook_id,
        client=client,
        body=body,
        sub_application=sub_application,
    ).parsed


async def asyncio_detailed(
    webhook_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: WebhookSecretResetBody,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Response[Union[ApiErrorResponseV2, WebhookSecretResetResponse201]]:
    """Reset Webhook Secret

     Reset webhook secret for a webhook that is already registered to your application

    Args:
        webhook_id (UUID):
        sub_application (Union[Unset, UUID]):
        body (WebhookSecretResetBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponseV2, WebhookSecretResetResponse201]]
    """

    kwargs = _get_kwargs(
        webhook_id=webhook_id,
        body=body,
        sub_application=sub_application,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    webhook_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: WebhookSecretResetBody,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Optional[Union[ApiErrorResponseV2, WebhookSecretResetResponse201]]:
    """Reset Webhook Secret

     Reset webhook secret for a webhook that is already registered to your application

    Args:
        webhook_id (UUID):
        sub_application (Union[Unset, UUID]):
        body (WebhookSecretResetBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponseV2, WebhookSecretResetResponse201]
    """

    return (
        await asyncio_detailed(
            webhook_id=webhook_id,
            client=client,
            body=body,
            sub_application=sub_application,
        )
    ).parsed
