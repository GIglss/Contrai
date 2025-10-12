from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_response_error import ApiResponseError
from ...models.api_response_of_payment_embedded_authorisation_request_response import (
    ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse,
)
from ...models.payment_embedded_authorisation_request import PaymentEmbeddedAuthorisationRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PaymentEmbeddedAuthorisationRequest,
    psu_id: Union[Unset, str] = UNSET,
    psu_corporate_id: Union[Unset, str] = UNSET,
    psu_ip_address: Union[Unset, str] = UNSET,
    sub_application: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(psu_id, Unset):
        headers["psu-id"] = psu_id

    if not isinstance(psu_corporate_id, Unset):
        headers["psu-corporate-id"] = psu_corporate_id

    if not isinstance(psu_ip_address, Unset):
        headers["psu-ip-address"] = psu_ip_address

    if not isinstance(sub_application, Unset):
        headers["sub-application"] = sub_application

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/embedded-payment-auth-requests",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ApiResponseError, ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse]:
    if response.status_code == 201:
        response_201 = ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse.from_dict(response.json())

        return response_201

    response_default = ApiResponseError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiResponseError, ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PaymentEmbeddedAuthorisationRequest,
    psu_id: Union[Unset, str] = UNSET,
    psu_corporate_id: Union[Unset, str] = UNSET,
    psu_ip_address: Union[Unset, str] = UNSET,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Response[Union[ApiResponseError, ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse]]:
    """Create Embedded Payment Authorisation

     Used to initiate the embedded authorisation process for an `Institution` that contains the
    `INITIATE_EMBEDDED_DOMESTIC_SINGLE_PAYMENT` feature in order to obtain the the user's authorisation
    for a payment.<br><br> See [Embedded Payment Flows](https://docs.yapily.com/pages/key-
    concepts/payments/payment-authorisation/embedded-payment-flows/) for more information about this
    flow.<br><br>Feature: `INITIATE_EMBEDDED_DOMESTIC_SINGLE_PAYMENT`

    Args:
        psu_id (Union[Unset, str]):
        psu_corporate_id (Union[Unset, str]):
        psu_ip_address (Union[Unset, str]):
        sub_application (Union[Unset, UUID]):
        body (PaymentEmbeddedAuthorisationRequest): The request body containing an
            `PaymentEmbeddedAuthorisationRequest` json payload

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiResponseError, ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
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
    *,
    client: Union[AuthenticatedClient, Client],
    body: PaymentEmbeddedAuthorisationRequest,
    psu_id: Union[Unset, str] = UNSET,
    psu_corporate_id: Union[Unset, str] = UNSET,
    psu_ip_address: Union[Unset, str] = UNSET,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Optional[Union[ApiResponseError, ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse]]:
    """Create Embedded Payment Authorisation

     Used to initiate the embedded authorisation process for an `Institution` that contains the
    `INITIATE_EMBEDDED_DOMESTIC_SINGLE_PAYMENT` feature in order to obtain the the user's authorisation
    for a payment.<br><br> See [Embedded Payment Flows](https://docs.yapily.com/pages/key-
    concepts/payments/payment-authorisation/embedded-payment-flows/) for more information about this
    flow.<br><br>Feature: `INITIATE_EMBEDDED_DOMESTIC_SINGLE_PAYMENT`

    Args:
        psu_id (Union[Unset, str]):
        psu_corporate_id (Union[Unset, str]):
        psu_ip_address (Union[Unset, str]):
        sub_application (Union[Unset, UUID]):
        body (PaymentEmbeddedAuthorisationRequest): The request body containing an
            `PaymentEmbeddedAuthorisationRequest` json payload

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiResponseError, ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
        psu_id=psu_id,
        psu_corporate_id=psu_corporate_id,
        psu_ip_address=psu_ip_address,
        sub_application=sub_application,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PaymentEmbeddedAuthorisationRequest,
    psu_id: Union[Unset, str] = UNSET,
    psu_corporate_id: Union[Unset, str] = UNSET,
    psu_ip_address: Union[Unset, str] = UNSET,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Response[Union[ApiResponseError, ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse]]:
    """Create Embedded Payment Authorisation

     Used to initiate the embedded authorisation process for an `Institution` that contains the
    `INITIATE_EMBEDDED_DOMESTIC_SINGLE_PAYMENT` feature in order to obtain the the user's authorisation
    for a payment.<br><br> See [Embedded Payment Flows](https://docs.yapily.com/pages/key-
    concepts/payments/payment-authorisation/embedded-payment-flows/) for more information about this
    flow.<br><br>Feature: `INITIATE_EMBEDDED_DOMESTIC_SINGLE_PAYMENT`

    Args:
        psu_id (Union[Unset, str]):
        psu_corporate_id (Union[Unset, str]):
        psu_ip_address (Union[Unset, str]):
        sub_application (Union[Unset, UUID]):
        body (PaymentEmbeddedAuthorisationRequest): The request body containing an
            `PaymentEmbeddedAuthorisationRequest` json payload

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiResponseError, ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        psu_id=psu_id,
        psu_corporate_id=psu_corporate_id,
        psu_ip_address=psu_ip_address,
        sub_application=sub_application,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PaymentEmbeddedAuthorisationRequest,
    psu_id: Union[Unset, str] = UNSET,
    psu_corporate_id: Union[Unset, str] = UNSET,
    psu_ip_address: Union[Unset, str] = UNSET,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Optional[Union[ApiResponseError, ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse]]:
    """Create Embedded Payment Authorisation

     Used to initiate the embedded authorisation process for an `Institution` that contains the
    `INITIATE_EMBEDDED_DOMESTIC_SINGLE_PAYMENT` feature in order to obtain the the user's authorisation
    for a payment.<br><br> See [Embedded Payment Flows](https://docs.yapily.com/pages/key-
    concepts/payments/payment-authorisation/embedded-payment-flows/) for more information about this
    flow.<br><br>Feature: `INITIATE_EMBEDDED_DOMESTIC_SINGLE_PAYMENT`

    Args:
        psu_id (Union[Unset, str]):
        psu_corporate_id (Union[Unset, str]):
        psu_ip_address (Union[Unset, str]):
        sub_application (Union[Unset, UUID]):
        body (PaymentEmbeddedAuthorisationRequest): The request body containing an
            `PaymentEmbeddedAuthorisationRequest` json payload

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiResponseError, ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            sub_application=sub_application,
        )
    ).parsed
