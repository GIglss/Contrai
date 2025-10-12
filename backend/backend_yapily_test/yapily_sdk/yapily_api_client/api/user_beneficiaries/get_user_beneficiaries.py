from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error_response_v2 import ApiErrorResponseV2
from ...models.get_user_beneficiaries_response_200 import GetUserBeneficiariesResponse200
from ...types import Response


def _get_kwargs(
    user_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/users/{user_id}/beneficiaries",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiErrorResponseV2, GetUserBeneficiariesResponse200]]:
    if response.status_code == 200:
        response_200 = GetUserBeneficiariesResponse200.from_dict(response.json())

        return response_200

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
) -> Response[Union[ApiErrorResponseV2, GetUserBeneficiariesResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ApiErrorResponseV2, GetUserBeneficiariesResponse200]]:
    """Get all users beneficiaries

     Get all users beneficiaries from an userId.

    Args:
        user_id (UUID):  Example: e7b7636d-a041-4013-8a1b-34dc85b7d341.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponseV2, GetUserBeneficiariesResponse200]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ApiErrorResponseV2, GetUserBeneficiariesResponse200]]:
    """Get all users beneficiaries

     Get all users beneficiaries from an userId.

    Args:
        user_id (UUID):  Example: e7b7636d-a041-4013-8a1b-34dc85b7d341.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponseV2, GetUserBeneficiariesResponse200]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ApiErrorResponseV2, GetUserBeneficiariesResponse200]]:
    """Get all users beneficiaries

     Get all users beneficiaries from an userId.

    Args:
        user_id (UUID):  Example: e7b7636d-a041-4013-8a1b-34dc85b7d341.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponseV2, GetUserBeneficiariesResponse200]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ApiErrorResponseV2, GetUserBeneficiariesResponse200]]:
    """Get all users beneficiaries

     Get all users beneficiaries from an userId.

    Args:
        user_id (UUID):  Example: e7b7636d-a041-4013-8a1b-34dc85b7d341.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponseV2, GetUserBeneficiariesResponse200]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed
