from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_list_response_of_direct_debit_response import ApiListResponseOfDirectDebitResponse
from ...models.api_response_error import ApiResponseError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    limit: Union[Unset, int] = UNSET,
    consent: str,
    sub_application: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["consent"] = consent

    if not isinstance(sub_application, Unset):
        headers["sub-application"] = sub_application

    params: dict[str, Any] = {}

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/accounts/{account_id}/direct-debits",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ApiListResponseOfDirectDebitResponse, ApiResponseError]:
    if response.status_code == 200:
        response_200 = ApiListResponseOfDirectDebitResponse.from_dict(response.json())

        return response_200

    response_default = ApiResponseError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiListResponseOfDirectDebitResponse, ApiResponseError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    consent: str,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Response[Union[ApiListResponseOfDirectDebitResponse, ApiResponseError]]:
    """Get Account Direct Debits

     Returns the list of direct debits for an account.<br><br>Feature: `ACCOUNT_DIRECT_DEBITS`

    Args:
        account_id (str):
        limit (Union[Unset, int]):
        consent (str):
        sub_application (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiListResponseOfDirectDebitResponse, ApiResponseError]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        limit=limit,
        consent=consent,
        sub_application=sub_application,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    consent: str,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Optional[Union[ApiListResponseOfDirectDebitResponse, ApiResponseError]]:
    """Get Account Direct Debits

     Returns the list of direct debits for an account.<br><br>Feature: `ACCOUNT_DIRECT_DEBITS`

    Args:
        account_id (str):
        limit (Union[Unset, int]):
        consent (str):
        sub_application (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiListResponseOfDirectDebitResponse, ApiResponseError]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        limit=limit,
        consent=consent,
        sub_application=sub_application,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    consent: str,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Response[Union[ApiListResponseOfDirectDebitResponse, ApiResponseError]]:
    """Get Account Direct Debits

     Returns the list of direct debits for an account.<br><br>Feature: `ACCOUNT_DIRECT_DEBITS`

    Args:
        account_id (str):
        limit (Union[Unset, int]):
        consent (str):
        sub_application (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiListResponseOfDirectDebitResponse, ApiResponseError]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        limit=limit,
        consent=consent,
        sub_application=sub_application,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    consent: str,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Optional[Union[ApiListResponseOfDirectDebitResponse, ApiResponseError]]:
    """Get Account Direct Debits

     Returns the list of direct debits for an account.<br><br>Feature: `ACCOUNT_DIRECT_DEBITS`

    Args:
        account_id (str):
        limit (Union[Unset, int]):
        consent (str):
        sub_application (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiListResponseOfDirectDebitResponse, ApiResponseError]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            limit=limit,
            consent=consent,
            sub_application=sub_application,
        )
    ).parsed
