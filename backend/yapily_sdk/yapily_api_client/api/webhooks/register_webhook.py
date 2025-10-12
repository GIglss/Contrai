from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error_response_v2 import ApiErrorResponseV2
from ...models.register_webhook_body import RegisterWebhookBody
from ...models.register_webhook_response_201 import RegisterWebhookResponse201
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RegisterWebhookBody,
    sub_application: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(sub_application, Unset):
        headers["sub-application"] = sub_application

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/webhook/events",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiErrorResponseV2, RegisterWebhookResponse201]]:
    if response.status_code == 201:
        response_201 = RegisterWebhookResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ApiErrorResponseV2.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiErrorResponseV2.from_dict(response.json())

        return response_401

    if response.status_code == 406:
        response_406 = ApiErrorResponseV2.from_dict(response.json())

        return response_406

    if response.status_code == 500:
        response_500 = ApiErrorResponseV2.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiErrorResponseV2, RegisterWebhookResponse201]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RegisterWebhookBody,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Response[Union[ApiErrorResponseV2, RegisterWebhookResponse201]]:
    """Register Webhook Event

     Register a webhook to one or multiple event categories to receive real-time notifications when
    specific events occur in your application.

    Args:
        sub_application (Union[Unset, UUID]):
        body (RegisterWebhookBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponseV2, RegisterWebhookResponse201]]
    """

    kwargs = _get_kwargs(
        body=body,
        sub_application=sub_application,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RegisterWebhookBody,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Optional[Union[ApiErrorResponseV2, RegisterWebhookResponse201]]:
    """Register Webhook Event

     Register a webhook to one or multiple event categories to receive real-time notifications when
    specific events occur in your application.

    Args:
        sub_application (Union[Unset, UUID]):
        body (RegisterWebhookBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponseV2, RegisterWebhookResponse201]
    """

    return sync_detailed(
        client=client,
        body=body,
        sub_application=sub_application,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RegisterWebhookBody,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Response[Union[ApiErrorResponseV2, RegisterWebhookResponse201]]:
    """Register Webhook Event

     Register a webhook to one or multiple event categories to receive real-time notifications when
    specific events occur in your application.

    Args:
        sub_application (Union[Unset, UUID]):
        body (RegisterWebhookBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponseV2, RegisterWebhookResponse201]]
    """

    kwargs = _get_kwargs(
        body=body,
        sub_application=sub_application,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RegisterWebhookBody,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Optional[Union[ApiErrorResponseV2, RegisterWebhookResponse201]]:
    """Register Webhook Event

     Register a webhook to one or multiple event categories to receive real-time notifications when
    specific events occur in your application.

    Args:
        sub_application (Union[Unset, UUID]):
        body (RegisterWebhookBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponseV2, RegisterWebhookResponse201]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            sub_application=sub_application,
        )
    ).parsed
