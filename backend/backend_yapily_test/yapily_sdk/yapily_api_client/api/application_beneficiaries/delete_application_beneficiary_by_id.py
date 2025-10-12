from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error_response_v2 import ApiErrorResponseV2
from ...types import Response


def _get_kwargs(
    application_id: UUID,
    beneficiary_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/applications/{application_id}/beneficiaries/{beneficiary_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ApiErrorResponseV2]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Union[Any, ApiErrorResponseV2]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    application_id: UUID,
    beneficiary_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ApiErrorResponseV2]]:
    """Delete application beneficiary by id

     Delete application beneficiary.

    Args:
        application_id (UUID):  Example: 6d97cf35-1000-4787-af16-7100912db9e4.
        beneficiary_id (UUID): Beneficiary Id Example: e7b7636d-a041-4013-8a1b-34dc85b7d341.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiErrorResponseV2]]
    """

    kwargs = _get_kwargs(
        application_id=application_id,
        beneficiary_id=beneficiary_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    application_id: UUID,
    beneficiary_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ApiErrorResponseV2]]:
    """Delete application beneficiary by id

     Delete application beneficiary.

    Args:
        application_id (UUID):  Example: 6d97cf35-1000-4787-af16-7100912db9e4.
        beneficiary_id (UUID): Beneficiary Id Example: e7b7636d-a041-4013-8a1b-34dc85b7d341.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiErrorResponseV2]
    """

    return sync_detailed(
        application_id=application_id,
        beneficiary_id=beneficiary_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    application_id: UUID,
    beneficiary_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ApiErrorResponseV2]]:
    """Delete application beneficiary by id

     Delete application beneficiary.

    Args:
        application_id (UUID):  Example: 6d97cf35-1000-4787-af16-7100912db9e4.
        beneficiary_id (UUID): Beneficiary Id Example: e7b7636d-a041-4013-8a1b-34dc85b7d341.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiErrorResponseV2]]
    """

    kwargs = _get_kwargs(
        application_id=application_id,
        beneficiary_id=beneficiary_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    application_id: UUID,
    beneficiary_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ApiErrorResponseV2]]:
    """Delete application beneficiary by id

     Delete application beneficiary.

    Args:
        application_id (UUID):  Example: 6d97cf35-1000-4787-af16-7100912db9e4.
        beneficiary_id (UUID): Beneficiary Id Example: e7b7636d-a041-4013-8a1b-34dc85b7d341.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiErrorResponseV2]
    """

    return (
        await asyncio_detailed(
            application_id=application_id,
            beneficiary_id=beneficiary_id,
            client=client,
        )
    ).parsed
