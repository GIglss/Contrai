from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error_response_v2 import ApiErrorResponseV2
from ...models.get_bulk_payment_status_response_200 import GetBulkPaymentStatusResponse200
from ...types import Response


def _get_kwargs(
    bulk_payment_id: str,
    *,
    consent: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["consent"] = consent

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/bulk-payments/{bulk_payment_id}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiErrorResponseV2, GetBulkPaymentStatusResponse200]]:
    if response.status_code == 200:
        response_200 = GetBulkPaymentStatusResponse200.from_dict(response.json())

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
) -> Response[Union[ApiErrorResponseV2, GetBulkPaymentStatusResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bulk_payment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    consent: str,
) -> Response[Union[ApiErrorResponseV2, GetBulkPaymentStatusResponse200]]:
    """Get Bulk Payment File Status

     Returns the bulk file status of the bulk payment for given bulkPaymentId

    Args:
        bulk_payment_id (str):
        consent (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponseV2, GetBulkPaymentStatusResponse200]]
    """

    kwargs = _get_kwargs(
        bulk_payment_id=bulk_payment_id,
        consent=consent,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bulk_payment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    consent: str,
) -> Optional[Union[ApiErrorResponseV2, GetBulkPaymentStatusResponse200]]:
    """Get Bulk Payment File Status

     Returns the bulk file status of the bulk payment for given bulkPaymentId

    Args:
        bulk_payment_id (str):
        consent (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponseV2, GetBulkPaymentStatusResponse200]
    """

    return sync_detailed(
        bulk_payment_id=bulk_payment_id,
        client=client,
        consent=consent,
    ).parsed


async def asyncio_detailed(
    bulk_payment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    consent: str,
) -> Response[Union[ApiErrorResponseV2, GetBulkPaymentStatusResponse200]]:
    """Get Bulk Payment File Status

     Returns the bulk file status of the bulk payment for given bulkPaymentId

    Args:
        bulk_payment_id (str):
        consent (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponseV2, GetBulkPaymentStatusResponse200]]
    """

    kwargs = _get_kwargs(
        bulk_payment_id=bulk_payment_id,
        consent=consent,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bulk_payment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    consent: str,
) -> Optional[Union[ApiErrorResponseV2, GetBulkPaymentStatusResponse200]]:
    """Get Bulk Payment File Status

     Returns the bulk file status of the bulk payment for given bulkPaymentId

    Args:
        bulk_payment_id (str):
        consent (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponseV2, GetBulkPaymentStatusResponse200]
    """

    return (
        await asyncio_detailed(
            bulk_payment_id=bulk_payment_id,
            client=client,
            consent=consent,
        )
    ).parsed
