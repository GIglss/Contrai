from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response_of_event_subscription_delete_response import ApiResponseOfEventSubscriptionDeleteResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    event_type_id: str,
    *,
    sub_application: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(sub_application, Unset):
        headers["sub-application"] = sub_application

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/notifications/event-subscriptions/{event_type_id}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ApiResponseOfEventSubscriptionDeleteResponse]]:
    if response.status_code == 200:
        response_200 = ApiResponseOfEventSubscriptionDeleteResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ApiResponseOfEventSubscriptionDeleteResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    event_type_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    sub_application: Union[Unset, UUID] = UNSET,
) -> Response[Union[Any, ApiResponseOfEventSubscriptionDeleteResponse]]:
    """Delete Event Subscription

     Used to unsubscribe to notifications relating to a specified event type.

    Args:
        event_type_id (str): Valid event type Id
        sub_application (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponseOfEventSubscriptionDeleteResponse]]
    """

    kwargs = _get_kwargs(
        event_type_id=event_type_id,
        sub_application=sub_application,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    event_type_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    sub_application: Union[Unset, UUID] = UNSET,
) -> Optional[Union[Any, ApiResponseOfEventSubscriptionDeleteResponse]]:
    """Delete Event Subscription

     Used to unsubscribe to notifications relating to a specified event type.

    Args:
        event_type_id (str): Valid event type Id
        sub_application (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiResponseOfEventSubscriptionDeleteResponse]
    """

    return sync_detailed(
        event_type_id=event_type_id,
        client=client,
        sub_application=sub_application,
    ).parsed


async def asyncio_detailed(
    event_type_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    sub_application: Union[Unset, UUID] = UNSET,
) -> Response[Union[Any, ApiResponseOfEventSubscriptionDeleteResponse]]:
    """Delete Event Subscription

     Used to unsubscribe to notifications relating to a specified event type.

    Args:
        event_type_id (str): Valid event type Id
        sub_application (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponseOfEventSubscriptionDeleteResponse]]
    """

    kwargs = _get_kwargs(
        event_type_id=event_type_id,
        sub_application=sub_application,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event_type_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    sub_application: Union[Unset, UUID] = UNSET,
) -> Optional[Union[Any, ApiResponseOfEventSubscriptionDeleteResponse]]:
    """Delete Event Subscription

     Used to unsubscribe to notifications relating to a specified event type.

    Args:
        event_type_id (str): Valid event type Id
        sub_application (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiResponseOfEventSubscriptionDeleteResponse]
    """

    return (
        await asyncio_detailed(
            event_type_id=event_type_id,
            client=client,
            sub_application=sub_application,
        )
    ).parsed
