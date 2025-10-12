from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_response_error import ApiResponseError
from ...models.application_user import ApplicationUser
from ...models.new_application_user import NewApplicationUser
from ...types import Response


def _get_kwargs(
    *,
    body: NewApplicationUser,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/users",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ApiResponseError, ApplicationUser]:
    if response.status_code == 201:
        response_201 = ApplicationUser.from_dict(response.json())

        return response_201

    response_default = ApiResponseError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiResponseError, ApplicationUser]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: NewApplicationUser,
) -> Response[Union[ApiResponseError, ApplicationUser]]:
    """Create User

     Create a new user in your application

    Args:
        body (NewApplicationUser): Details of a new user to be created for the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiResponseError, ApplicationUser]]
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
    body: NewApplicationUser,
) -> Optional[Union[ApiResponseError, ApplicationUser]]:
    """Create User

     Create a new user in your application

    Args:
        body (NewApplicationUser): Details of a new user to be created for the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiResponseError, ApplicationUser]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: NewApplicationUser,
) -> Response[Union[ApiResponseError, ApplicationUser]]:
    """Create User

     Create a new user in your application

    Args:
        body (NewApplicationUser): Details of a new user to be created for the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiResponseError, ApplicationUser]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: NewApplicationUser,
) -> Optional[Union[ApiResponseError, ApplicationUser]]:
    """Create User

     Create a new user in your application

    Args:
        body (NewApplicationUser): Details of a new user to be created for the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiResponseError, ApplicationUser]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
