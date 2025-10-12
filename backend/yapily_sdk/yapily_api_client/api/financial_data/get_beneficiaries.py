from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_list_response_of_beneficiary import ApiListResponseOfBeneficiary
from ...models.api_response_error import ApiResponseError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    consent: str,
    sub_application: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["consent"] = consent

    if not isinstance(sub_application, Unset):
        headers["sub-application"] = sub_application

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/accounts/{account_id}/beneficiaries",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ApiListResponseOfBeneficiary, ApiResponseError]:
    if response.status_code == 200:
        response_200 = ApiListResponseOfBeneficiary.from_dict(response.json())

        return response_200

    response_default = ApiResponseError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiListResponseOfBeneficiary, ApiResponseError]]:
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
    consent: str,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Response[Union[ApiListResponseOfBeneficiary, ApiResponseError]]:
    """Get Account Beneficiaries

     Returns all the beneficiaries of a user's account.<br><br>Feature: `ACCOUNT_BENEFICIARIES`

    Args:
        account_id (str):
        consent (str):
        sub_application (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiListResponseOfBeneficiary, ApiResponseError]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
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
    consent: str,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Optional[Union[ApiListResponseOfBeneficiary, ApiResponseError]]:
    """Get Account Beneficiaries

     Returns all the beneficiaries of a user's account.<br><br>Feature: `ACCOUNT_BENEFICIARIES`

    Args:
        account_id (str):
        consent (str):
        sub_application (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiListResponseOfBeneficiary, ApiResponseError]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        consent=consent,
        sub_application=sub_application,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    consent: str,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Response[Union[ApiListResponseOfBeneficiary, ApiResponseError]]:
    """Get Account Beneficiaries

     Returns all the beneficiaries of a user's account.<br><br>Feature: `ACCOUNT_BENEFICIARIES`

    Args:
        account_id (str):
        consent (str):
        sub_application (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiListResponseOfBeneficiary, ApiResponseError]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        consent=consent,
        sub_application=sub_application,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    consent: str,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Optional[Union[ApiListResponseOfBeneficiary, ApiResponseError]]:
    """Get Account Beneficiaries

     Returns all the beneficiaries of a user's account.<br><br>Feature: `ACCOUNT_BENEFICIARIES`

    Args:
        account_id (str):
        consent (str):
        sub_application (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiListResponseOfBeneficiary, ApiResponseError]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            consent=consent,
            sub_application=sub_application,
        )
    ).parsed
