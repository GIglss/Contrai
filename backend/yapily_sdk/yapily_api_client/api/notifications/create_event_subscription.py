from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response_of_event_subscription_response import ApiResponseOfEventSubscriptionResponse
from ...models.request_to_create_a_subscription_for_notifications import RequestToCreateASubscriptionForNotifications
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RequestToCreateASubscriptionForNotifications,
    sub_application: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(sub_application, Unset):
        headers["sub-application"] = sub_application

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/notifications/event-subscriptions",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ApiResponseOfEventSubscriptionResponse]]:
    if response.status_code == 201:
        response_201 = ApiResponseOfEventSubscriptionResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ApiResponseOfEventSubscriptionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RequestToCreateASubscriptionForNotifications,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Response[Union[Any, ApiResponseOfEventSubscriptionResponse]]:
    """Create Event Subscription

     Used to subscribe to notifications relating to a specified event type.

    Args:
        sub_application (Union[Unset, UUID]):
        body (RequestToCreateASubscriptionForNotifications):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponseOfEventSubscriptionResponse]]
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
    body: RequestToCreateASubscriptionForNotifications,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Optional[Union[Any, ApiResponseOfEventSubscriptionResponse]]:
    """Create Event Subscription

     Used to subscribe to notifications relating to a specified event type.

    Args:
        sub_application (Union[Unset, UUID]):
        body (RequestToCreateASubscriptionForNotifications):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiResponseOfEventSubscriptionResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
        sub_application=sub_application,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RequestToCreateASubscriptionForNotifications,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Response[Union[Any, ApiResponseOfEventSubscriptionResponse]]:
    """Create Event Subscription

     Used to subscribe to notifications relating to a specified event type.

    Args:
        sub_application (Union[Unset, UUID]):
        body (RequestToCreateASubscriptionForNotifications):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponseOfEventSubscriptionResponse]]
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
    body: RequestToCreateASubscriptionForNotifications,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Optional[Union[Any, ApiResponseOfEventSubscriptionResponse]]:
    """Create Event Subscription

     Used to subscribe to notifications relating to a specified event type.

    Args:
        sub_application (Union[Unset, UUID]):
        body (RequestToCreateASubscriptionForNotifications):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiResponseOfEventSubscriptionResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            sub_application=sub_application,
        )
    ).parsed
