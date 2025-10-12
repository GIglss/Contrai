from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_response_error import ApiResponseError
from ...models.api_response_of_payment_responses import ApiResponseOfPaymentResponses
from ...types import UNSET, Response, Unset


def _get_kwargs(
    payment_id: str,
    *,
    consent: str,
    psu_id: Union[Unset, str] = UNSET,
    psu_corporate_id: Union[Unset, str] = UNSET,
    psu_ip_address: Union[Unset, str] = UNSET,
    sub_application: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["consent"] = consent

    if not isinstance(psu_id, Unset):
        headers["psu-id"] = psu_id

    if not isinstance(psu_corporate_id, Unset):
        headers["psu-corporate-id"] = psu_corporate_id

    if not isinstance(psu_ip_address, Unset):
        headers["psu-ip-address"] = psu_ip_address

    if not isinstance(sub_application, Unset):
        headers["sub-application"] = sub_application

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/payments/{payment_id}/details",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ApiResponseError, ApiResponseOfPaymentResponses]:
    if response.status_code == 200:
        response_200 = ApiResponseOfPaymentResponses.from_dict(response.json())

        return response_200

    response_default = ApiResponseError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiResponseError, ApiResponseOfPaymentResponses]]:
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
    psu_id: Union[Unset, str] = UNSET,
    psu_corporate_id: Union[Unset, str] = UNSET,
    psu_ip_address: Union[Unset, str] = UNSET,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Response[Union[ApiResponseError, ApiResponseOfPaymentResponses]]:
    """Get Payment Details

     Returns the details of a payment. <br><br>Most commonly used to check for payment status updates.
    <br><br>Feature: `EXISTING_PAYMENTS_DETAILS`

    Args:
        payment_id (str):
        consent (str):
        psu_id (Union[Unset, str]):
        psu_corporate_id (Union[Unset, str]):
        psu_ip_address (Union[Unset, str]):
        sub_application (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiResponseError, ApiResponseOfPaymentResponses]]
    """

    kwargs = _get_kwargs(
        payment_id=payment_id,
        consent=consent,
        psu_id=psu_id,
        psu_corporate_id=psu_corporate_id,
        psu_ip_address=psu_ip_address,
        sub_application=sub_application,
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
    psu_id: Union[Unset, str] = UNSET,
    psu_corporate_id: Union[Unset, str] = UNSET,
    psu_ip_address: Union[Unset, str] = UNSET,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Optional[Union[ApiResponseError, ApiResponseOfPaymentResponses]]:
    """Get Payment Details

     Returns the details of a payment. <br><br>Most commonly used to check for payment status updates.
    <br><br>Feature: `EXISTING_PAYMENTS_DETAILS`

    Args:
        payment_id (str):
        consent (str):
        psu_id (Union[Unset, str]):
        psu_corporate_id (Union[Unset, str]):
        psu_ip_address (Union[Unset, str]):
        sub_application (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiResponseError, ApiResponseOfPaymentResponses]
    """

    return sync_detailed(
        payment_id=payment_id,
        client=client,
        consent=consent,
        psu_id=psu_id,
        psu_corporate_id=psu_corporate_id,
        psu_ip_address=psu_ip_address,
        sub_application=sub_application,
    ).parsed


async def asyncio_detailed(
    payment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    consent: str,
    psu_id: Union[Unset, str] = UNSET,
    psu_corporate_id: Union[Unset, str] = UNSET,
    psu_ip_address: Union[Unset, str] = UNSET,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Response[Union[ApiResponseError, ApiResponseOfPaymentResponses]]:
    """Get Payment Details

     Returns the details of a payment. <br><br>Most commonly used to check for payment status updates.
    <br><br>Feature: `EXISTING_PAYMENTS_DETAILS`

    Args:
        payment_id (str):
        consent (str):
        psu_id (Union[Unset, str]):
        psu_corporate_id (Union[Unset, str]):
        psu_ip_address (Union[Unset, str]):
        sub_application (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiResponseError, ApiResponseOfPaymentResponses]]
    """

    kwargs = _get_kwargs(
        payment_id=payment_id,
        consent=consent,
        psu_id=psu_id,
        psu_corporate_id=psu_corporate_id,
        psu_ip_address=psu_ip_address,
        sub_application=sub_application,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    payment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    consent: str,
    psu_id: Union[Unset, str] = UNSET,
    psu_corporate_id: Union[Unset, str] = UNSET,
    psu_ip_address: Union[Unset, str] = UNSET,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Optional[Union[ApiResponseError, ApiResponseOfPaymentResponses]]:
    """Get Payment Details

     Returns the details of a payment. <br><br>Most commonly used to check for payment status updates.
    <br><br>Feature: `EXISTING_PAYMENTS_DETAILS`

    Args:
        payment_id (str):
        consent (str):
        psu_id (Union[Unset, str]):
        psu_corporate_id (Union[Unset, str]):
        psu_ip_address (Union[Unset, str]):
        sub_application (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiResponseError, ApiResponseOfPaymentResponses]
    """

    return (
        await asyncio_detailed(
            payment_id=payment_id,
            client=client,
            consent=consent,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            sub_application=sub_application,
        )
    ).parsed
