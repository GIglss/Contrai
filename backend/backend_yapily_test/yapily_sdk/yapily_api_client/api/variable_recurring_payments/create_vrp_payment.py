from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_error_response import ApiErrorResponse
from ...models.api_response_of_submission_response import ApiResponseOfSubmissionResponse
from ...models.submission_request import SubmissionRequest
from ...types import Response


def _get_kwargs(
    *,
    body: SubmissionRequest,
    consent: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["consent"] = consent

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/variable-recurring-payments/payments",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ApiErrorResponse, ApiResponseOfSubmissionResponse]:
    if response.status_code == 201:
        response_201 = ApiResponseOfSubmissionResponse.from_dict(response.json())

        return response_201

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
    *,
    client: Union[AuthenticatedClient, Client],
    body: SubmissionRequest,
    consent: str,
) -> Response[Union[ApiErrorResponse, ApiResponseOfSubmissionResponse]]:
    """Create Variable Recurring Payment

     Creates a Variable Recurring Payment transaction after obtaining the user's authorisation.<br><br>Fe
    atures:<ul><li>`CREATE_DOMESTIC_VARIABLE_RECURRING_PAYMENT_SWEEPING`</li></ul>

    Args:
        consent (str):
        body (SubmissionRequest): __Mandatory__. The payment request object defining the details
            of the payment for execution under the Variable Recurring Payment consent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponse, ApiResponseOfSubmissionResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        consent=consent,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SubmissionRequest,
    consent: str,
) -> Optional[Union[ApiErrorResponse, ApiResponseOfSubmissionResponse]]:
    """Create Variable Recurring Payment

     Creates a Variable Recurring Payment transaction after obtaining the user's authorisation.<br><br>Fe
    atures:<ul><li>`CREATE_DOMESTIC_VARIABLE_RECURRING_PAYMENT_SWEEPING`</li></ul>

    Args:
        consent (str):
        body (SubmissionRequest): __Mandatory__. The payment request object defining the details
            of the payment for execution under the Variable Recurring Payment consent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponse, ApiResponseOfSubmissionResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
        consent=consent,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SubmissionRequest,
    consent: str,
) -> Response[Union[ApiErrorResponse, ApiResponseOfSubmissionResponse]]:
    """Create Variable Recurring Payment

     Creates a Variable Recurring Payment transaction after obtaining the user's authorisation.<br><br>Fe
    atures:<ul><li>`CREATE_DOMESTIC_VARIABLE_RECURRING_PAYMENT_SWEEPING`</li></ul>

    Args:
        consent (str):
        body (SubmissionRequest): __Mandatory__. The payment request object defining the details
            of the payment for execution under the Variable Recurring Payment consent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponse, ApiResponseOfSubmissionResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        consent=consent,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SubmissionRequest,
    consent: str,
) -> Optional[Union[ApiErrorResponse, ApiResponseOfSubmissionResponse]]:
    """Create Variable Recurring Payment

     Creates a Variable Recurring Payment transaction after obtaining the user's authorisation.<br><br>Fe
    atures:<ul><li>`CREATE_DOMESTIC_VARIABLE_RECURRING_PAYMENT_SWEEPING`</li></ul>

    Args:
        consent (str):
        body (SubmissionRequest): __Mandatory__. The payment request object defining the details
            of the payment for execution under the Variable Recurring Payment consent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponse, ApiResponseOfSubmissionResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            consent=consent,
        )
    ).parsed
