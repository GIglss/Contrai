from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response_error import ApiResponseError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    consent_request_id: UUID,
    payment_id: str,
    *,
    sub_application: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(sub_application, Unset):
        headers["sub-application"] = sub_application

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/hosted/vrp/consent-requests/{consent_request_id}/payments/{payment_id}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiResponseError]:
    if response.status_code == 401:
        response_401 = ApiResponseError.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ApiResponseError.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ApiResponseError.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiResponseError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    consent_request_id: UUID,
    payment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    sub_application: Union[Unset, str] = UNSET,
) -> Response[ApiResponseError]:
    """Get VRP payment

     Used to get details of a VRP Payment

    Args:
        consent_request_id (UUID):
        payment_id (str):
        sub_application (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiResponseError]
    """

    kwargs = _get_kwargs(
        consent_request_id=consent_request_id,
        payment_id=payment_id,
        sub_application=sub_application,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    consent_request_id: UUID,
    payment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    sub_application: Union[Unset, str] = UNSET,
) -> Optional[ApiResponseError]:
    """Get VRP payment

     Used to get details of a VRP Payment

    Args:
        consent_request_id (UUID):
        payment_id (str):
        sub_application (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiResponseError
    """

    return sync_detailed(
        consent_request_id=consent_request_id,
        payment_id=payment_id,
        client=client,
        sub_application=sub_application,
    ).parsed


async def asyncio_detailed(
    consent_request_id: UUID,
    payment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    sub_application: Union[Unset, str] = UNSET,
) -> Response[ApiResponseError]:
    """Get VRP payment

     Used to get details of a VRP Payment

    Args:
        consent_request_id (UUID):
        payment_id (str):
        sub_application (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiResponseError]
    """

    kwargs = _get_kwargs(
        consent_request_id=consent_request_id,
        payment_id=payment_id,
        sub_application=sub_application,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    consent_request_id: UUID,
    payment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    sub_application: Union[Unset, str] = UNSET,
) -> Optional[ApiResponseError]:
    """Get VRP payment

     Used to get details of a VRP Payment

    Args:
        consent_request_id (UUID):
        payment_id (str):
        sub_application (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiResponseError
    """

    return (
        await asyncio_detailed(
            consent_request_id=consent_request_id,
            payment_id=payment_id,
            client=client,
            sub_application=sub_application,
        )
    ).parsed
