from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_response_error import ApiResponseError
from ...models.application_user import ApplicationUser
from ...models.application_user_patch_request import ApplicationUserPatchRequest
from ...types import Response


def _get_kwargs(
    user_uuid: UUID,
    *,
    body: list["ApplicationUserPatchRequest"],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/users/{user_uuid}",
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json-patch+json"

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
    user_uuid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["ApplicationUserPatchRequest"],
) -> Response[Union[ApiResponseError, ApplicationUser]]:
    """Update User

     Update the users information

    Args:
        user_uuid (UUID):
        body (list['ApplicationUserPatchRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiResponseError, ApplicationUser]]
    """

    kwargs = _get_kwargs(
        user_uuid=user_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_uuid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["ApplicationUserPatchRequest"],
) -> Optional[Union[ApiResponseError, ApplicationUser]]:
    """Update User

     Update the users information

    Args:
        user_uuid (UUID):
        body (list['ApplicationUserPatchRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiResponseError, ApplicationUser]
    """

    return sync_detailed(
        user_uuid=user_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    user_uuid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["ApplicationUserPatchRequest"],
) -> Response[Union[ApiResponseError, ApplicationUser]]:
    """Update User

     Update the users information

    Args:
        user_uuid (UUID):
        body (list['ApplicationUserPatchRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiResponseError, ApplicationUser]]
    """

    kwargs = _get_kwargs(
        user_uuid=user_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_uuid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["ApplicationUserPatchRequest"],
) -> Optional[Union[ApiResponseError, ApplicationUser]]:
    """Update User

     Update the users information

    Args:
        user_uuid (UUID):
        body (list['ApplicationUserPatchRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiResponseError, ApplicationUser]
    """

    return (
        await asyncio_detailed(
            user_uuid=user_uuid,
            client=client,
            body=body,
        )
    ).parsed
