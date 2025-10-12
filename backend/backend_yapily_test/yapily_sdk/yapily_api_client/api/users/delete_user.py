from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_response_error import ApiResponseError
from ...models.api_response_of_user_delete_response import ApiResponseOfUserDeleteResponse
from ...types import Response


def _get_kwargs(
    user_uuid: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/users/{user_uuid}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ApiResponseError, ApiResponseOfUserDeleteResponse]:
    if response.status_code == 200:
        response_200 = ApiResponseOfUserDeleteResponse.from_dict(response.json())

        return response_200

    response_default = ApiResponseError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiResponseError, ApiResponseOfUserDeleteResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_uuid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ApiResponseError, ApiResponseOfUserDeleteResponse]]:
    """Delete User

     Delete a user from your application along with any sub-resources (including consent resources on
    institution APIs if they exist)

    Args:
        user_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiResponseError, ApiResponseOfUserDeleteResponse]]
    """

    kwargs = _get_kwargs(
        user_uuid=user_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_uuid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ApiResponseError, ApiResponseOfUserDeleteResponse]]:
    """Delete User

     Delete a user from your application along with any sub-resources (including consent resources on
    institution APIs if they exist)

    Args:
        user_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiResponseError, ApiResponseOfUserDeleteResponse]
    """

    return sync_detailed(
        user_uuid=user_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_uuid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ApiResponseError, ApiResponseOfUserDeleteResponse]]:
    """Delete User

     Delete a user from your application along with any sub-resources (including consent resources on
    institution APIs if they exist)

    Args:
        user_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiResponseError, ApiResponseOfUserDeleteResponse]]
    """

    kwargs = _get_kwargs(
        user_uuid=user_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_uuid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ApiResponseError, ApiResponseOfUserDeleteResponse]]:
    """Delete User

     Delete a user from your application along with any sub-resources (including consent resources on
    institution APIs if they exist)

    Args:
        user_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiResponseError, ApiResponseOfUserDeleteResponse]
    """

    return (
        await asyncio_detailed(
            user_uuid=user_uuid,
            client=client,
        )
    ).parsed
