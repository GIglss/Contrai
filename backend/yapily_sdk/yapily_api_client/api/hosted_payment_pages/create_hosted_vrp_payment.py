from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_response_error import ApiResponseError
from ...models.create_hosted_vrp_payment_request import CreateHostedVRPPaymentRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    consent_request_id: UUID,
    *,
    body: CreateHostedVRPPaymentRequest,
    consent_token: str,
    sub_application: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["consent-token"] = consent_token

    if not isinstance(sub_application, Unset):
        headers["sub-application"] = sub_application

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/hosted/vrp/consent-requests/{consent_request_id}/payments",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> ApiResponseError:
    if response.status_code == 401:
        response_401 = ApiResponseError.from_dict(response.json())

        return response_401

    response_default = ApiResponseError.from_dict(response.json())

    return response_default


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
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateHostedVRPPaymentRequest,
    consent_token: str,
    sub_application: Union[Unset, str] = UNSET,
) -> Response[ApiResponseError]:
    """Create VRP Payment

     Creates a Variable Recurring Payment

    Args:
        consent_request_id (UUID):
        consent_token (str):
        sub_application (Union[Unset, str]):
        body (CreateHostedVRPPaymentRequest): __Mandatory__. The payment request object defining
            the details of the payment for execution under the Variable Recurring Payment consent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiResponseError]
    """

    kwargs = _get_kwargs(
        consent_request_id=consent_request_id,
        body=body,
        consent_token=consent_token,
        sub_application=sub_application,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    consent_request_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateHostedVRPPaymentRequest,
    consent_token: str,
    sub_application: Union[Unset, str] = UNSET,
) -> Optional[ApiResponseError]:
    """Create VRP Payment

     Creates a Variable Recurring Payment

    Args:
        consent_request_id (UUID):
        consent_token (str):
        sub_application (Union[Unset, str]):
        body (CreateHostedVRPPaymentRequest): __Mandatory__. The payment request object defining
            the details of the payment for execution under the Variable Recurring Payment consent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiResponseError
    """

    return sync_detailed(
        consent_request_id=consent_request_id,
        client=client,
        body=body,
        consent_token=consent_token,
        sub_application=sub_application,
    ).parsed


async def asyncio_detailed(
    consent_request_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateHostedVRPPaymentRequest,
    consent_token: str,
    sub_application: Union[Unset, str] = UNSET,
) -> Response[ApiResponseError]:
    """Create VRP Payment

     Creates a Variable Recurring Payment

    Args:
        consent_request_id (UUID):
        consent_token (str):
        sub_application (Union[Unset, str]):
        body (CreateHostedVRPPaymentRequest): __Mandatory__. The payment request object defining
            the details of the payment for execution under the Variable Recurring Payment consent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiResponseError]
    """

    kwargs = _get_kwargs(
        consent_request_id=consent_request_id,
        body=body,
        consent_token=consent_token,
        sub_application=sub_application,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    consent_request_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateHostedVRPPaymentRequest,
    consent_token: str,
    sub_application: Union[Unset, str] = UNSET,
) -> Optional[ApiResponseError]:
    """Create VRP Payment

     Creates a Variable Recurring Payment

    Args:
        consent_request_id (UUID):
        consent_token (str):
        sub_application (Union[Unset, str]):
        body (CreateHostedVRPPaymentRequest): __Mandatory__. The payment request object defining
            the details of the payment for execution under the Variable Recurring Payment consent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiResponseError
    """

    return (
        await asyncio_detailed(
            consent_request_id=consent_request_id,
            client=client,
            body=body,
            consent_token=consent_token,
            sub_application=sub_application,
        )
    ).parsed
