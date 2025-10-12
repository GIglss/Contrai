from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_error_response import ApiErrorResponse
from ...models.api_response_of_submission_response import ApiResponseOfSubmissionResponse
from ...types import Response


def _get_kwargs(
    payment_id: str,
    *,
    consent: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["consent"] = consent

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/variable-recurring-payments/payments/{payment_id}/details",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ApiErrorResponse, ApiResponseOfSubmissionResponse]:
    if response.status_code == 200:
        response_200 = ApiResponseOfSubmissionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ApiErrorResponse.from_dict(response.json())

        return response_401

    response_default = ApiErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiErrorResponse, ApiResponseOfSubmissionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    payment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    consent: str,
) -> Response[Union[ApiErrorResponse, ApiResponseOfSubmissionResponse]]:
    """Get Variable Recurring Payment Details

     Get Variable Recurring Payment details using the Payment Id

    Args:
        payment_id (str):
        consent (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponse, ApiResponseOfSubmissionResponse]]
    """

    kwargs = _get_kwargs(
        payment_id=payment_id,
        consent=consent,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    payment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    consent: str,
) -> Optional[Union[ApiErrorResponse, ApiResponseOfSubmissionResponse]]:
    """Get Variable Recurring Payment Details

     Get Variable Recurring Payment details using the Payment Id

    Args:
        payment_id (str):
        consent (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponse, ApiResponseOfSubmissionResponse]
    """

    return sync_detailed(
        payment_id=payment_id,
        client=client,
        consent=consent,
    ).parsed


async def asyncio_detailed(
    payment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    consent: str,
) -> Response[Union[ApiErrorResponse, ApiResponseOfSubmissionResponse]]:
    """Get Variable Recurring Payment Details

     Get Variable Recurring Payment details using the Payment Id

    Args:
        payment_id (str):
        consent (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponse, ApiResponseOfSubmissionResponse]]
    """

    kwargs = _get_kwargs(
        payment_id=payment_id,
        consent=consent,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    payment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    consent: str,
) -> Optional[Union[ApiErrorResponse, ApiResponseOfSubmissionResponse]]:
    """Get Variable Recurring Payment Details

     Get Variable Recurring Payment details using the Payment Id

    Args:
        payment_id (str):
        consent (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponse, ApiResponseOfSubmissionResponse]
    """

    return (
        await asyncio_detailed(
            payment_id=payment_id,
            client=client,
            consent=consent,
        )
    ).parsed
