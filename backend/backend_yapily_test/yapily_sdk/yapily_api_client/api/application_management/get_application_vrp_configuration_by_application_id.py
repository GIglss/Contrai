from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error_response import ApiErrorResponse
from ...models.validation_error_response import ValidationErrorResponse
from ...models.vrp_configuration import VrpConfiguration
from ...types import Response


def _get_kwargs(
    application_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/applications/{application_id}/vrp",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiErrorResponse, ValidationErrorResponse, VrpConfiguration]]:
    if response.status_code == 200:
        response_200 = VrpConfiguration.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ValidationErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ApiErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ApiErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ApiErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiErrorResponse, ValidationErrorResponse, VrpConfiguration]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    application_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ApiErrorResponse, ValidationErrorResponse, VrpConfiguration]]:
    """Get application VRP configuration by Application Id

     Get application vrp configuration

    Args:
        application_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponse, ValidationErrorResponse, VrpConfiguration]]
    """

    kwargs = _get_kwargs(
        application_id=application_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    application_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ApiErrorResponse, ValidationErrorResponse, VrpConfiguration]]:
    """Get application VRP configuration by Application Id

     Get application vrp configuration

    Args:
        application_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponse, ValidationErrorResponse, VrpConfiguration]
    """

    return sync_detailed(
        application_id=application_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    application_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ApiErrorResponse, ValidationErrorResponse, VrpConfiguration]]:
    """Get application VRP configuration by Application Id

     Get application vrp configuration

    Args:
        application_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponse, ValidationErrorResponse, VrpConfiguration]]
    """

    kwargs = _get_kwargs(
        application_id=application_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    application_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ApiErrorResponse, ValidationErrorResponse, VrpConfiguration]]:
    """Get application VRP configuration by Application Id

     Get application vrp configuration

    Args:
        application_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponse, ValidationErrorResponse, VrpConfiguration]
    """

    return (
        await asyncio_detailed(
            application_id=application_id,
            client=client,
        )
    ).parsed
