from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_response_error import ApiResponseError
from ...models.application_user import ApplicationUser
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filterapplication_user_id: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_filterapplication_user_id: Union[Unset, list[str]] = UNSET
    if not isinstance(filterapplication_user_id, Unset):
        json_filterapplication_user_id = filterapplication_user_id

    params["filter[applicationUserId]"] = json_filterapplication_user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ApiResponseError, list["ApplicationUser"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ApplicationUser.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    response_default = ApiResponseError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiResponseError, list["ApplicationUser"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    filterapplication_user_id: Union[Unset, list[str]] = UNSET,
) -> Response[Union[ApiResponseError, list["ApplicationUser"]]]:
    """Get Users

     Retrieves all users created in your application for a specified applicationUserId using the
    filter[applicationUserId] query parameter. If filter[applicationUserId] is not provided, the
    response will include up to 50,000 users.

    Args:
        filterapplication_user_id (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiResponseError, list['ApplicationUser']]]
    """

    kwargs = _get_kwargs(
        filterapplication_user_id=filterapplication_user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    filterapplication_user_id: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[ApiResponseError, list["ApplicationUser"]]]:
    """Get Users

     Retrieves all users created in your application for a specified applicationUserId using the
    filter[applicationUserId] query parameter. If filter[applicationUserId] is not provided, the
    response will include up to 50,000 users.

    Args:
        filterapplication_user_id (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiResponseError, list['ApplicationUser']]
    """

    return sync_detailed(
        client=client,
        filterapplication_user_id=filterapplication_user_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    filterapplication_user_id: Union[Unset, list[str]] = UNSET,
) -> Response[Union[ApiResponseError, list["ApplicationUser"]]]:
    """Get Users

     Retrieves all users created in your application for a specified applicationUserId using the
    filter[applicationUserId] query parameter. If filter[applicationUserId] is not provided, the
    response will include up to 50,000 users.

    Args:
        filterapplication_user_id (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiResponseError, list['ApplicationUser']]]
    """

    kwargs = _get_kwargs(
        filterapplication_user_id=filterapplication_user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    filterapplication_user_id: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[ApiResponseError, list["ApplicationUser"]]]:
    """Get Users

     Retrieves all users created in your application for a specified applicationUserId using the
    filter[applicationUserId] query parameter. If filter[applicationUserId] is not provided, the
    response will include up to 50,000 users.

    Args:
        filterapplication_user_id (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiResponseError, list['ApplicationUser']]
    """

    return (
        await asyncio_detailed(
            client=client,
            filterapplication_user_id=filterapplication_user_id,
        )
    ).parsed
