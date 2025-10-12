from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_response_error import ApiResponseError
from ...models.api_response_of_payment_embedded_authorisation_request_response import (
    ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse,
)
from ...models.bulk_payment_embedded_authorisation_request import BulkPaymentEmbeddedAuthorisationRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    consent_id: str,
    *,
    body: BulkPaymentEmbeddedAuthorisationRequest,
    psu_id: Union[Unset, str] = UNSET,
    psu_corporate_id: Union[Unset, str] = UNSET,
    psu_ip_address: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(psu_id, Unset):
        headers["psu-id"] = psu_id

    if not isinstance(psu_corporate_id, Unset):
        headers["psu-corporate-id"] = psu_corporate_id

    if not isinstance(psu_ip_address, Unset):
        headers["psu-ip-address"] = psu_ip_address

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/embedded-bulk-payment-auth-requests/{consent_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ApiResponseError, ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse]:
    if response.status_code == 200:
        response_200 = ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse.from_dict(response.json())

        return response_200

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
    consent_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: BulkPaymentEmbeddedAuthorisationRequest,
    psu_id: Union[Unset, str] = UNSET,
    psu_corporate_id: Union[Unset, str] = UNSET,
    psu_ip_address: Union[Unset, str] = UNSET,
) -> Response[Union[ApiResponseError, ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse]]:
    """Update Embedded Bulk Payment Authorisation

     Used to pass the SCA Code received from the `Institution` (and the SCA method selected by the user
    where multiple SCA methods are supported by the `Institution`) in order to complete the embedded
    authorisation to initiate a bulk payment. See [Bulk Payments](https://docs.yapily.com/pages/key-
    concepts/payments/payment-execution/bulk-payments/) for more information. <br><br>See [Embedded
    Payment Flows](https://docs.yapily.com/pages/key-concepts/payments/payment-authorisation/embedded-
    payment-flows/) for more information about this flow.<br><br>Feature:
    `INITIATE_EMBEDDED_BULK_PAYMENT`

    Args:
        consent_id (str):
        psu_id (Union[Unset, str]):
        psu_corporate_id (Union[Unset, str]):
        psu_ip_address (Union[Unset, str]):
        body (BulkPaymentEmbeddedAuthorisationRequest): The request body containing a
            `BulkPaymentEmbeddedAuthorisationRequest` json payload

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiResponseError, ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse]]
    """

    kwargs = _get_kwargs(
        consent_id=consent_id,
        body=body,
        psu_id=psu_id,
        psu_corporate_id=psu_corporate_id,
        psu_ip_address=psu_ip_address,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    consent_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: BulkPaymentEmbeddedAuthorisationRequest,
    psu_id: Union[Unset, str] = UNSET,
    psu_corporate_id: Union[Unset, str] = UNSET,
    psu_ip_address: Union[Unset, str] = UNSET,
) -> Optional[Union[ApiResponseError, ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse]]:
    """Update Embedded Bulk Payment Authorisation

     Used to pass the SCA Code received from the `Institution` (and the SCA method selected by the user
    where multiple SCA methods are supported by the `Institution`) in order to complete the embedded
    authorisation to initiate a bulk payment. See [Bulk Payments](https://docs.yapily.com/pages/key-
    concepts/payments/payment-execution/bulk-payments/) for more information. <br><br>See [Embedded
    Payment Flows](https://docs.yapily.com/pages/key-concepts/payments/payment-authorisation/embedded-
    payment-flows/) for more information about this flow.<br><br>Feature:
    `INITIATE_EMBEDDED_BULK_PAYMENT`

    Args:
        consent_id (str):
        psu_id (Union[Unset, str]):
        psu_corporate_id (Union[Unset, str]):
        psu_ip_address (Union[Unset, str]):
        body (BulkPaymentEmbeddedAuthorisationRequest): The request body containing a
            `BulkPaymentEmbeddedAuthorisationRequest` json payload

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiResponseError, ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse]
    """

    return sync_detailed(
        consent_id=consent_id,
        client=client,
        body=body,
        psu_id=psu_id,
        psu_corporate_id=psu_corporate_id,
        psu_ip_address=psu_ip_address,
    ).parsed


async def asyncio_detailed(
    consent_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: BulkPaymentEmbeddedAuthorisationRequest,
    psu_id: Union[Unset, str] = UNSET,
    psu_corporate_id: Union[Unset, str] = UNSET,
    psu_ip_address: Union[Unset, str] = UNSET,
) -> Response[Union[ApiResponseError, ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse]]:
    """Update Embedded Bulk Payment Authorisation

     Used to pass the SCA Code received from the `Institution` (and the SCA method selected by the user
    where multiple SCA methods are supported by the `Institution`) in order to complete the embedded
    authorisation to initiate a bulk payment. See [Bulk Payments](https://docs.yapily.com/pages/key-
    concepts/payments/payment-execution/bulk-payments/) for more information. <br><br>See [Embedded
    Payment Flows](https://docs.yapily.com/pages/key-concepts/payments/payment-authorisation/embedded-
    payment-flows/) for more information about this flow.<br><br>Feature:
    `INITIATE_EMBEDDED_BULK_PAYMENT`

    Args:
        consent_id (str):
        psu_id (Union[Unset, str]):
        psu_corporate_id (Union[Unset, str]):
        psu_ip_address (Union[Unset, str]):
        body (BulkPaymentEmbeddedAuthorisationRequest): The request body containing a
            `BulkPaymentEmbeddedAuthorisationRequest` json payload

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiResponseError, ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse]]
    """

    kwargs = _get_kwargs(
        consent_id=consent_id,
        body=body,
        psu_id=psu_id,
        psu_corporate_id=psu_corporate_id,
        psu_ip_address=psu_ip_address,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    consent_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: BulkPaymentEmbeddedAuthorisationRequest,
    psu_id: Union[Unset, str] = UNSET,
    psu_corporate_id: Union[Unset, str] = UNSET,
    psu_ip_address: Union[Unset, str] = UNSET,
) -> Optional[Union[ApiResponseError, ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse]]:
    """Update Embedded Bulk Payment Authorisation

     Used to pass the SCA Code received from the `Institution` (and the SCA method selected by the user
    where multiple SCA methods are supported by the `Institution`) in order to complete the embedded
    authorisation to initiate a bulk payment. See [Bulk Payments](https://docs.yapily.com/pages/key-
    concepts/payments/payment-execution/bulk-payments/) for more information. <br><br>See [Embedded
    Payment Flows](https://docs.yapily.com/pages/key-concepts/payments/payment-authorisation/embedded-
    payment-flows/) for more information about this flow.<br><br>Feature:
    `INITIATE_EMBEDDED_BULK_PAYMENT`

    Args:
        consent_id (str):
        psu_id (Union[Unset, str]):
        psu_corporate_id (Union[Unset, str]):
        psu_ip_address (Union[Unset, str]):
        body (BulkPaymentEmbeddedAuthorisationRequest): The request body containing a
            `BulkPaymentEmbeddedAuthorisationRequest` json payload

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiResponseError, ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse]
    """

    return (
        await asyncio_detailed(
            consent_id=consent_id,
            client=client,
            body=body,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
        )
    ).parsed
