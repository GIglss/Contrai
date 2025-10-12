from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_response_error import ApiResponseError
from ...models.api_response_of_payment_authorisation_request_response import (
    ApiResponseOfPaymentAuthorisationRequestResponse,
)
from ...models.payment_authorisation_request import PaymentAuthorisationRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PaymentAuthorisationRequest,
    psu_id: Union[Unset, str] = UNSET,
    psu_corporate_id: Union[Unset, str] = UNSET,
    psu_ip_address: Union[Unset, str] = UNSET,
    consent: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(psu_id, Unset):
        headers["psu-id"] = psu_id

    if not isinstance(psu_corporate_id, Unset):
        headers["psu-corporate-id"] = psu_corporate_id

    if not isinstance(psu_ip_address, Unset):
        headers["psu-ip-address"] = psu_ip_address

    headers["consent"] = consent

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/payment-auth-requests",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ApiResponseError, ApiResponseOfPaymentAuthorisationRequestResponse]:
    if response.status_code == 200:
        response_200 = ApiResponseOfPaymentAuthorisationRequestResponse.from_dict(response.json())

        return response_200

    response_default = ApiResponseError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiResponseError, ApiResponseOfPaymentAuthorisationRequestResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PaymentAuthorisationRequest,
    psu_id: Union[Unset, str] = UNSET,
    psu_corporate_id: Union[Unset, str] = UNSET,
    psu_ip_address: Union[Unset, str] = UNSET,
    consent: str,
) -> Response[Union[ApiResponseError, ApiResponseOfPaymentAuthorisationRequestResponse]]:
    """Update Payment Pre-authorisation

     Used to continue the authorisation process and for any `Institution` that contains the
    `INITIATE_PRE_AUTHORISATION` feature and direct user to the login screen of their financial
    institution in order to give consent to initiate a payment. <br><br>See [Redirect Payment
    Flows](https://docs.yapily.com/pages/key-concepts/payments/payment-authorisation/redirect-payment-
    flows/) for more information about this flow. <br><br>Feature: `INITIATE_PRE_AUTHORISATION`

    Args:
        psu_id (Union[Unset, str]):
        psu_corporate_id (Union[Unset, str]):
        psu_ip_address (Union[Unset, str]):
        consent (str):
        body (PaymentAuthorisationRequest): The request body containing an
            `PaymentAuthorisationRequest` json payload

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiResponseError, ApiResponseOfPaymentAuthorisationRequestResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        psu_id=psu_id,
        psu_corporate_id=psu_corporate_id,
        psu_ip_address=psu_ip_address,
        consent=consent,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PaymentAuthorisationRequest,
    psu_id: Union[Unset, str] = UNSET,
    psu_corporate_id: Union[Unset, str] = UNSET,
    psu_ip_address: Union[Unset, str] = UNSET,
    consent: str,
) -> Optional[Union[ApiResponseError, ApiResponseOfPaymentAuthorisationRequestResponse]]:
    """Update Payment Pre-authorisation

     Used to continue the authorisation process and for any `Institution` that contains the
    `INITIATE_PRE_AUTHORISATION` feature and direct user to the login screen of their financial
    institution in order to give consent to initiate a payment. <br><br>See [Redirect Payment
    Flows](https://docs.yapily.com/pages/key-concepts/payments/payment-authorisation/redirect-payment-
    flows/) for more information about this flow. <br><br>Feature: `INITIATE_PRE_AUTHORISATION`

    Args:
        psu_id (Union[Unset, str]):
        psu_corporate_id (Union[Unset, str]):
        psu_ip_address (Union[Unset, str]):
        consent (str):
        body (PaymentAuthorisationRequest): The request body containing an
            `PaymentAuthorisationRequest` json payload

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiResponseError, ApiResponseOfPaymentAuthorisationRequestResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
        psu_id=psu_id,
        psu_corporate_id=psu_corporate_id,
        psu_ip_address=psu_ip_address,
        consent=consent,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PaymentAuthorisationRequest,
    psu_id: Union[Unset, str] = UNSET,
    psu_corporate_id: Union[Unset, str] = UNSET,
    psu_ip_address: Union[Unset, str] = UNSET,
    consent: str,
) -> Response[Union[ApiResponseError, ApiResponseOfPaymentAuthorisationRequestResponse]]:
    """Update Payment Pre-authorisation

     Used to continue the authorisation process and for any `Institution` that contains the
    `INITIATE_PRE_AUTHORISATION` feature and direct user to the login screen of their financial
    institution in order to give consent to initiate a payment. <br><br>See [Redirect Payment
    Flows](https://docs.yapily.com/pages/key-concepts/payments/payment-authorisation/redirect-payment-
    flows/) for more information about this flow. <br><br>Feature: `INITIATE_PRE_AUTHORISATION`

    Args:
        psu_id (Union[Unset, str]):
        psu_corporate_id (Union[Unset, str]):
        psu_ip_address (Union[Unset, str]):
        consent (str):
        body (PaymentAuthorisationRequest): The request body containing an
            `PaymentAuthorisationRequest` json payload

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiResponseError, ApiResponseOfPaymentAuthorisationRequestResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        psu_id=psu_id,
        psu_corporate_id=psu_corporate_id,
        psu_ip_address=psu_ip_address,
        consent=consent,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PaymentAuthorisationRequest,
    psu_id: Union[Unset, str] = UNSET,
    psu_corporate_id: Union[Unset, str] = UNSET,
    psu_ip_address: Union[Unset, str] = UNSET,
    consent: str,
) -> Optional[Union[ApiResponseError, ApiResponseOfPaymentAuthorisationRequestResponse]]:
    """Update Payment Pre-authorisation

     Used to continue the authorisation process and for any `Institution` that contains the
    `INITIATE_PRE_AUTHORISATION` feature and direct user to the login screen of their financial
    institution in order to give consent to initiate a payment. <br><br>See [Redirect Payment
    Flows](https://docs.yapily.com/pages/key-concepts/payments/payment-authorisation/redirect-payment-
    flows/) for more information about this flow. <br><br>Feature: `INITIATE_PRE_AUTHORISATION`

    Args:
        psu_id (Union[Unset, str]):
        psu_corporate_id (Union[Unset, str]):
        psu_ip_address (Union[Unset, str]):
        consent (str):
        body (PaymentAuthorisationRequest): The request body containing an
            `PaymentAuthorisationRequest` json payload

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiResponseError, ApiResponseOfPaymentAuthorisationRequestResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            consent=consent,
        )
    ).parsed
