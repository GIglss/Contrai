from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

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
        "url": "/payment-auth-requests",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ApiResponseError, ApiResponseOfPaymentAuthorisationRequestResponse]:
    if response.status_code == 201:
        response_201 = ApiResponseOfPaymentAuthorisationRequestResponse.from_dict(response.json())

        return response_201

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
    sub_application: Union[Unset, UUID] = UNSET,
) -> Response[Union[ApiResponseError, ApiResponseOfPaymentAuthorisationRequestResponse]]:
    """Create Payment Authorisation

     Used to initiate the authorisation process and direct users to the login screen of their financial
    Institution in order to give their consent for a payment. This endpoint is used to initiate all the
    different payment listed below. Based on the type of payment you wish to make, you may be required
    to provide specific properties in [PaymentRequest](https://docs.yapily.com/api/reference/#operation/
    createPaymentAuthorisation!path=paymentRequest&t=request). First make sure that the payment feature
    you wish to execute is supported by the bank by checking the features array in [GET
    Institution](https://docs.yapily.com/api/reference/#operation/getInstitution). <br><br>See [Redirect
    Payment Flows](https://docs.yapily.com/pages/key-concepts/payments/payment-authorisation/redirect-
    payment-flows/) for more information about this flow.<br><br>Features:<ul><li>`INITIATE_DOMESTIC_PER
    IODIC_PAYMENT`</li><li>`INITIATE_DOMESTIC_SCHEDULED_PAYMENT`</li><li>`INITIATE_DOMESTIC_SINGLE_INSTA
    NT_PAYMENT`</li><li>`INITIATE_DOMESTIC_SINGLE_PAYMENT`</li><li>`INITIATE_INTERNATIONAL_PERIODIC_PAYM
    ENT`</li><li>`INITIATE_INTERNATIONAL_SCHEDULED_PAYMENT`</li><li>`INITIATE_INTERNATIONAL_SINGLE_PAYME
    NT`</li></ul>

    Args:
        psu_id (Union[Unset, str]):
        psu_corporate_id (Union[Unset, str]):
        psu_ip_address (Union[Unset, str]):
        sub_application (Union[Unset, UUID]):
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
        sub_application=sub_application,
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
    sub_application: Union[Unset, UUID] = UNSET,
) -> Optional[Union[ApiResponseError, ApiResponseOfPaymentAuthorisationRequestResponse]]:
    """Create Payment Authorisation

     Used to initiate the authorisation process and direct users to the login screen of their financial
    Institution in order to give their consent for a payment. This endpoint is used to initiate all the
    different payment listed below. Based on the type of payment you wish to make, you may be required
    to provide specific properties in [PaymentRequest](https://docs.yapily.com/api/reference/#operation/
    createPaymentAuthorisation!path=paymentRequest&t=request). First make sure that the payment feature
    you wish to execute is supported by the bank by checking the features array in [GET
    Institution](https://docs.yapily.com/api/reference/#operation/getInstitution). <br><br>See [Redirect
    Payment Flows](https://docs.yapily.com/pages/key-concepts/payments/payment-authorisation/redirect-
    payment-flows/) for more information about this flow.<br><br>Features:<ul><li>`INITIATE_DOMESTIC_PER
    IODIC_PAYMENT`</li><li>`INITIATE_DOMESTIC_SCHEDULED_PAYMENT`</li><li>`INITIATE_DOMESTIC_SINGLE_INSTA
    NT_PAYMENT`</li><li>`INITIATE_DOMESTIC_SINGLE_PAYMENT`</li><li>`INITIATE_INTERNATIONAL_PERIODIC_PAYM
    ENT`</li><li>`INITIATE_INTERNATIONAL_SCHEDULED_PAYMENT`</li><li>`INITIATE_INTERNATIONAL_SINGLE_PAYME
    NT`</li></ul>

    Args:
        psu_id (Union[Unset, str]):
        psu_corporate_id (Union[Unset, str]):
        psu_ip_address (Union[Unset, str]):
        sub_application (Union[Unset, UUID]):
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
        sub_application=sub_application,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PaymentAuthorisationRequest,
    psu_id: Union[Unset, str] = UNSET,
    psu_corporate_id: Union[Unset, str] = UNSET,
    psu_ip_address: Union[Unset, str] = UNSET,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Response[Union[ApiResponseError, ApiResponseOfPaymentAuthorisationRequestResponse]]:
    """Create Payment Authorisation

     Used to initiate the authorisation process and direct users to the login screen of their financial
    Institution in order to give their consent for a payment. This endpoint is used to initiate all the
    different payment listed below. Based on the type of payment you wish to make, you may be required
    to provide specific properties in [PaymentRequest](https://docs.yapily.com/api/reference/#operation/
    createPaymentAuthorisation!path=paymentRequest&t=request). First make sure that the payment feature
    you wish to execute is supported by the bank by checking the features array in [GET
    Institution](https://docs.yapily.com/api/reference/#operation/getInstitution). <br><br>See [Redirect
    Payment Flows](https://docs.yapily.com/pages/key-concepts/payments/payment-authorisation/redirect-
    payment-flows/) for more information about this flow.<br><br>Features:<ul><li>`INITIATE_DOMESTIC_PER
    IODIC_PAYMENT`</li><li>`INITIATE_DOMESTIC_SCHEDULED_PAYMENT`</li><li>`INITIATE_DOMESTIC_SINGLE_INSTA
    NT_PAYMENT`</li><li>`INITIATE_DOMESTIC_SINGLE_PAYMENT`</li><li>`INITIATE_INTERNATIONAL_PERIODIC_PAYM
    ENT`</li><li>`INITIATE_INTERNATIONAL_SCHEDULED_PAYMENT`</li><li>`INITIATE_INTERNATIONAL_SINGLE_PAYME
    NT`</li></ul>

    Args:
        psu_id (Union[Unset, str]):
        psu_corporate_id (Union[Unset, str]):
        psu_ip_address (Union[Unset, str]):
        sub_application (Union[Unset, UUID]):
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
        sub_application=sub_application,
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
    sub_application: Union[Unset, UUID] = UNSET,
) -> Optional[Union[ApiResponseError, ApiResponseOfPaymentAuthorisationRequestResponse]]:
    """Create Payment Authorisation

     Used to initiate the authorisation process and direct users to the login screen of their financial
    Institution in order to give their consent for a payment. This endpoint is used to initiate all the
    different payment listed below. Based on the type of payment you wish to make, you may be required
    to provide specific properties in [PaymentRequest](https://docs.yapily.com/api/reference/#operation/
    createPaymentAuthorisation!path=paymentRequest&t=request). First make sure that the payment feature
    you wish to execute is supported by the bank by checking the features array in [GET
    Institution](https://docs.yapily.com/api/reference/#operation/getInstitution). <br><br>See [Redirect
    Payment Flows](https://docs.yapily.com/pages/key-concepts/payments/payment-authorisation/redirect-
    payment-flows/) for more information about this flow.<br><br>Features:<ul><li>`INITIATE_DOMESTIC_PER
    IODIC_PAYMENT`</li><li>`INITIATE_DOMESTIC_SCHEDULED_PAYMENT`</li><li>`INITIATE_DOMESTIC_SINGLE_INSTA
    NT_PAYMENT`</li><li>`INITIATE_DOMESTIC_SINGLE_PAYMENT`</li><li>`INITIATE_INTERNATIONAL_PERIODIC_PAYM
    ENT`</li><li>`INITIATE_INTERNATIONAL_SCHEDULED_PAYMENT`</li><li>`INITIATE_INTERNATIONAL_SINGLE_PAYME
    NT`</li></ul>

    Args:
        psu_id (Union[Unset, str]):
        psu_corporate_id (Union[Unset, str]):
        psu_ip_address (Union[Unset, str]):
        sub_application (Union[Unset, UUID]):
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
            sub_application=sub_application,
        )
    ).parsed
