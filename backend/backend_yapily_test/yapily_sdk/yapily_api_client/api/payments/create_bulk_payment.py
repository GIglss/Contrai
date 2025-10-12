from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_response_error import ApiResponseError
from ...models.api_response_of_create_bulk_payment_request import ApiResponseOfCreateBulkPaymentRequest
from ...models.submit_bulk_payment_request import SubmitBulkPaymentRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SubmitBulkPaymentRequest,
    consent: str,
    psu_id: Union[Unset, str] = UNSET,
    psu_corporate_id: Union[Unset, str] = UNSET,
    psu_ip_address: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["consent"] = consent

    if not isinstance(psu_id, Unset):
        headers["psu-id"] = psu_id

    if not isinstance(psu_corporate_id, Unset):
        headers["psu-corporate-id"] = psu_corporate_id

    if not isinstance(psu_ip_address, Unset):
        headers["psu-ip-address"] = psu_ip_address

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/bulk-payments",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ApiResponseError, ApiResponseOfCreateBulkPaymentRequest]:
    if response.status_code == 201:
        response_201 = ApiResponseOfCreateBulkPaymentRequest.from_dict(response.json())

        return response_201

    response_default = ApiResponseError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiResponseError, ApiResponseOfCreateBulkPaymentRequest]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SubmitBulkPaymentRequest,
    consent: str,
    psu_id: Union[Unset, str] = UNSET,
    psu_corporate_id: Union[Unset, str] = UNSET,
    psu_ip_address: Union[Unset, str] = UNSET,
) -> Response[Union[ApiResponseError, ApiResponseOfCreateBulkPaymentRequest]]:
    """Create Bulk Payment

     Creates a bulk payment after obtaining the user's authorisation. <br><br>Feature:
    `CREATE_BULK_PAYMENT`

    Args:
        consent (str):
        psu_id (Union[Unset, str]):
        psu_corporate_id (Union[Unset, str]):
        psu_ip_address (Union[Unset, str]):
        body (SubmitBulkPaymentRequest): The payment request object defining the details of the
            bulk payment

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiResponseError, ApiResponseOfCreateBulkPaymentRequest]]
    """

    kwargs = _get_kwargs(
        body=body,
        consent=consent,
        psu_id=psu_id,
        psu_corporate_id=psu_corporate_id,
        psu_ip_address=psu_ip_address,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SubmitBulkPaymentRequest,
    consent: str,
    psu_id: Union[Unset, str] = UNSET,
    psu_corporate_id: Union[Unset, str] = UNSET,
    psu_ip_address: Union[Unset, str] = UNSET,
) -> Optional[Union[ApiResponseError, ApiResponseOfCreateBulkPaymentRequest]]:
    """Create Bulk Payment

     Creates a bulk payment after obtaining the user's authorisation. <br><br>Feature:
    `CREATE_BULK_PAYMENT`

    Args:
        consent (str):
        psu_id (Union[Unset, str]):
        psu_corporate_id (Union[Unset, str]):
        psu_ip_address (Union[Unset, str]):
        body (SubmitBulkPaymentRequest): The payment request object defining the details of the
            bulk payment

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiResponseError, ApiResponseOfCreateBulkPaymentRequest]
    """

    return sync_detailed(
        client=client,
        body=body,
        consent=consent,
        psu_id=psu_id,
        psu_corporate_id=psu_corporate_id,
        psu_ip_address=psu_ip_address,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SubmitBulkPaymentRequest,
    consent: str,
    psu_id: Union[Unset, str] = UNSET,
    psu_corporate_id: Union[Unset, str] = UNSET,
    psu_ip_address: Union[Unset, str] = UNSET,
) -> Response[Union[ApiResponseError, ApiResponseOfCreateBulkPaymentRequest]]:
    """Create Bulk Payment

     Creates a bulk payment after obtaining the user's authorisation. <br><br>Feature:
    `CREATE_BULK_PAYMENT`

    Args:
        consent (str):
        psu_id (Union[Unset, str]):
        psu_corporate_id (Union[Unset, str]):
        psu_ip_address (Union[Unset, str]):
        body (SubmitBulkPaymentRequest): The payment request object defining the details of the
            bulk payment

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiResponseError, ApiResponseOfCreateBulkPaymentRequest]]
    """

    kwargs = _get_kwargs(
        body=body,
        consent=consent,
        psu_id=psu_id,
        psu_corporate_id=psu_corporate_id,
        psu_ip_address=psu_ip_address,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SubmitBulkPaymentRequest,
    consent: str,
    psu_id: Union[Unset, str] = UNSET,
    psu_corporate_id: Union[Unset, str] = UNSET,
    psu_ip_address: Union[Unset, str] = UNSET,
) -> Optional[Union[ApiResponseError, ApiResponseOfCreateBulkPaymentRequest]]:
    """Create Bulk Payment

     Creates a bulk payment after obtaining the user's authorisation. <br><br>Feature:
    `CREATE_BULK_PAYMENT`

    Args:
        consent (str):
        psu_id (Union[Unset, str]):
        psu_corporate_id (Union[Unset, str]):
        psu_ip_address (Union[Unset, str]):
        body (SubmitBulkPaymentRequest): The payment request object defining the details of the
            bulk payment

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiResponseError, ApiResponseOfCreateBulkPaymentRequest]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            consent=consent,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
        )
    ).parsed
