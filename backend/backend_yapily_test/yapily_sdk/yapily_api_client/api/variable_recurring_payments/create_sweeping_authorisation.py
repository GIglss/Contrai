from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_error_response import ApiErrorResponse
from ...models.api_response_of_sweeping_authorisation_response import ApiResponseOfSweepingAuthorisationResponse
from ...models.sweeping_authorisation_request import SweepingAuthorisationRequest
from ...types import Response


def _get_kwargs(
    *,
    body: SweepingAuthorisationRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/variable-recurring-payments/sweeping/consents",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ApiErrorResponse, ApiResponseOfSweepingAuthorisationResponse]:
    if response.status_code == 201:
        response_201 = ApiResponseOfSweepingAuthorisationResponse.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = ApiErrorResponse.from_dict(response.json())

        return response_401

    response_default = ApiErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiErrorResponse, ApiResponseOfSweepingAuthorisationResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SweepingAuthorisationRequest,
) -> Response[Union[ApiErrorResponse, ApiResponseOfSweepingAuthorisationResponse]]:
    """Create Sweeping Variable Recurring Payment Authorisation

     Used to initiate the authorisation process and direct users to the login screen of their financial
    Institution in order to give their consent for Sweeping Variable Recurring Payments. The request
    would return an Authorization URL and an Identifier for the consent created at the Institution.
    First make sure that the payment feature you wish to execute is supported by the bank by checking
    the features array in [GET Institution](https://docs.yapily.com/api/#get-institution). <br><br>See
    [Redirect Payment Flows](https://docs.yapily.com/guides/payments/payment-authorisation-
    flows/redirect/) for more information about this
    flow.<br><br>Features:<ul><li>`INITIATE_DOMESTIC_VARIABLE_RECURRING_PAYMENT_SWEEPING`</li></ul>

    Args:
        body (SweepingAuthorisationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponse, ApiResponseOfSweepingAuthorisationResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SweepingAuthorisationRequest,
) -> Optional[Union[ApiErrorResponse, ApiResponseOfSweepingAuthorisationResponse]]:
    """Create Sweeping Variable Recurring Payment Authorisation

     Used to initiate the authorisation process and direct users to the login screen of their financial
    Institution in order to give their consent for Sweeping Variable Recurring Payments. The request
    would return an Authorization URL and an Identifier for the consent created at the Institution.
    First make sure that the payment feature you wish to execute is supported by the bank by checking
    the features array in [GET Institution](https://docs.yapily.com/api/#get-institution). <br><br>See
    [Redirect Payment Flows](https://docs.yapily.com/guides/payments/payment-authorisation-
    flows/redirect/) for more information about this
    flow.<br><br>Features:<ul><li>`INITIATE_DOMESTIC_VARIABLE_RECURRING_PAYMENT_SWEEPING`</li></ul>

    Args:
        body (SweepingAuthorisationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponse, ApiResponseOfSweepingAuthorisationResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SweepingAuthorisationRequest,
) -> Response[Union[ApiErrorResponse, ApiResponseOfSweepingAuthorisationResponse]]:
    """Create Sweeping Variable Recurring Payment Authorisation

     Used to initiate the authorisation process and direct users to the login screen of their financial
    Institution in order to give their consent for Sweeping Variable Recurring Payments. The request
    would return an Authorization URL and an Identifier for the consent created at the Institution.
    First make sure that the payment feature you wish to execute is supported by the bank by checking
    the features array in [GET Institution](https://docs.yapily.com/api/#get-institution). <br><br>See
    [Redirect Payment Flows](https://docs.yapily.com/guides/payments/payment-authorisation-
    flows/redirect/) for more information about this
    flow.<br><br>Features:<ul><li>`INITIATE_DOMESTIC_VARIABLE_RECURRING_PAYMENT_SWEEPING`</li></ul>

    Args:
        body (SweepingAuthorisationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponse, ApiResponseOfSweepingAuthorisationResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SweepingAuthorisationRequest,
) -> Optional[Union[ApiErrorResponse, ApiResponseOfSweepingAuthorisationResponse]]:
    """Create Sweeping Variable Recurring Payment Authorisation

     Used to initiate the authorisation process and direct users to the login screen of their financial
    Institution in order to give their consent for Sweeping Variable Recurring Payments. The request
    would return an Authorization URL and an Identifier for the consent created at the Institution.
    First make sure that the payment feature you wish to execute is supported by the bank by checking
    the features array in [GET Institution](https://docs.yapily.com/api/#get-institution). <br><br>See
    [Redirect Payment Flows](https://docs.yapily.com/guides/payments/payment-authorisation-
    flows/redirect/) for more information about this
    flow.<br><br>Features:<ul><li>`INITIATE_DOMESTIC_VARIABLE_RECURRING_PAYMENT_SWEEPING`</li></ul>

    Args:
        body (SweepingAuthorisationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponse, ApiResponseOfSweepingAuthorisationResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
