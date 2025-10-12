from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_response_error import ApiResponseError
from ...models.api_response_of_funds_confirmation_response import ApiResponseOfFundsConfirmationResponse
from ...models.funds_confirmation_request import FundsConfirmationRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    consent_request_id: UUID,
    *,
    body: FundsConfirmationRequest,
    consent_token: str,
    sub_application: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["consent-token"] = consent_token

    if not isinstance(sub_application, Unset):
        headers["sub-application"] = sub_application

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/hosted/vrp/consent-requests/{consent_request_id}/funds-confirmation",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ApiResponseError, ApiResponseOfFundsConfirmationResponse]:
    if response.status_code == 201:
        response_201 = ApiResponseOfFundsConfirmationResponse.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = ApiResponseError.from_dict(response.json())

        return response_401

    response_default = ApiResponseError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiResponseError, ApiResponseOfFundsConfirmationResponse]]:
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
    body: FundsConfirmationRequest,
    consent_token: str,
    sub_application: Union[Unset, str] = UNSET,
) -> Response[Union[ApiResponseError, ApiResponseOfFundsConfirmationResponse]]:
    """Check Funds Availability

     Confirms whether there are available funds on the Payer account to execute a Variable Recurring
    Payment after obtaining the user's authorisation.
    <br><br>Features:<ul><li>`VARIABLE_RECURRING_PAYMENT_FUNDS_CONFIRMATION`</li></ul>

    Args:
        consent_request_id (UUID):
        consent_token (str):
        sub_application (Union[Unset, str]):
        body (FundsConfirmationRequest): The fund confirmation object defining the details of the
            account and funds to be checked under the Variable Recurring Payment consent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiResponseError, ApiResponseOfFundsConfirmationResponse]]
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
    body: FundsConfirmationRequest,
    consent_token: str,
    sub_application: Union[Unset, str] = UNSET,
) -> Optional[Union[ApiResponseError, ApiResponseOfFundsConfirmationResponse]]:
    """Check Funds Availability

     Confirms whether there are available funds on the Payer account to execute a Variable Recurring
    Payment after obtaining the user's authorisation.
    <br><br>Features:<ul><li>`VARIABLE_RECURRING_PAYMENT_FUNDS_CONFIRMATION`</li></ul>

    Args:
        consent_request_id (UUID):
        consent_token (str):
        sub_application (Union[Unset, str]):
        body (FundsConfirmationRequest): The fund confirmation object defining the details of the
            account and funds to be checked under the Variable Recurring Payment consent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiResponseError, ApiResponseOfFundsConfirmationResponse]
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
    body: FundsConfirmationRequest,
    consent_token: str,
    sub_application: Union[Unset, str] = UNSET,
) -> Response[Union[ApiResponseError, ApiResponseOfFundsConfirmationResponse]]:
    """Check Funds Availability

     Confirms whether there are available funds on the Payer account to execute a Variable Recurring
    Payment after obtaining the user's authorisation.
    <br><br>Features:<ul><li>`VARIABLE_RECURRING_PAYMENT_FUNDS_CONFIRMATION`</li></ul>

    Args:
        consent_request_id (UUID):
        consent_token (str):
        sub_application (Union[Unset, str]):
        body (FundsConfirmationRequest): The fund confirmation object defining the details of the
            account and funds to be checked under the Variable Recurring Payment consent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiResponseError, ApiResponseOfFundsConfirmationResponse]]
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
    body: FundsConfirmationRequest,
    consent_token: str,
    sub_application: Union[Unset, str] = UNSET,
) -> Optional[Union[ApiResponseError, ApiResponseOfFundsConfirmationResponse]]:
    """Check Funds Availability

     Confirms whether there are available funds on the Payer account to execute a Variable Recurring
    Payment after obtaining the user's authorisation.
    <br><br>Features:<ul><li>`VARIABLE_RECURRING_PAYMENT_FUNDS_CONFIRMATION`</li></ul>

    Args:
        consent_request_id (UUID):
        consent_token (str):
        sub_application (Union[Unset, str]):
        body (FundsConfirmationRequest): The fund confirmation object defining the details of the
            account and funds to be checked under the Variable Recurring Payment consent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiResponseError, ApiResponseOfFundsConfirmationResponse]
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
