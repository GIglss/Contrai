from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_error_response import ApiErrorResponse
from ...models.api_response_of_sweeping_authorisation_response import ApiResponseOfSweepingAuthorisationResponse
from ...types import Response


def _get_kwargs(
    consent_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/variable-recurring-payments/sweeping/consents/{consent_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ApiErrorResponse, ApiResponseOfSweepingAuthorisationResponse]:
    if response.status_code == 200:
        response_200 = ApiResponseOfSweepingAuthorisationResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ApiErrorResponse.from_dict(response.json())

        return response_401

    response_default = ApiErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiErrorResponse, ApiResponseOfSweepingAuthorisationResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    consent_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ApiErrorResponse, ApiResponseOfSweepingAuthorisationResponse]]:
    """Get Sweeping Variable Recurring Payment Consent Details

     Get Sweeping Variable Recurring Payments consent details using the consent Id

    Args:
        consent_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponse, ApiResponseOfSweepingAuthorisationResponse]]
    """

    kwargs = _get_kwargs(
        consent_id=consent_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    consent_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ApiErrorResponse, ApiResponseOfSweepingAuthorisationResponse]]:
    """Get Sweeping Variable Recurring Payment Consent Details

     Get Sweeping Variable Recurring Payments consent details using the consent Id

    Args:
        consent_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponse, ApiResponseOfSweepingAuthorisationResponse]
    """

    return sync_detailed(
        consent_id=consent_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    consent_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ApiErrorResponse, ApiResponseOfSweepingAuthorisationResponse]]:
    """Get Sweeping Variable Recurring Payment Consent Details

     Get Sweeping Variable Recurring Payments consent details using the consent Id

    Args:
        consent_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponse, ApiResponseOfSweepingAuthorisationResponse]]
    """

    kwargs = _get_kwargs(
        consent_id=consent_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    consent_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ApiErrorResponse, ApiResponseOfSweepingAuthorisationResponse]]:
    """Get Sweeping Variable Recurring Payment Consent Details

     Get Sweeping Variable Recurring Payments consent details using the consent Id

    Args:
        consent_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponse, ApiResponseOfSweepingAuthorisationResponse]
    """

    return (
        await asyncio_detailed(
            consent_id=consent_id,
            client=client,
        )
    ).parsed
