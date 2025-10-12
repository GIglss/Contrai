from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_response_error import ApiResponseError
from ...models.sort_enum import SortEnum
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    from_: Union[Unset, str] = UNSET,
    before: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    sort: Union[Unset, SortEnum] = UNSET,
    offset: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
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

    params: dict[str, Any] = {}

    params["from"] = from_

    params["before"] = before

    params["limit"] = limit

    json_sort: Union[Unset, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params["offset"] = offset

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/accounts/{account_id}/transactions",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> ApiResponseError:
    response_default = ApiResponseError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiResponseError]:
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
    from_: Union[Unset, str] = UNSET,
    before: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    sort: Union[Unset, SortEnum] = UNSET,
    offset: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    consent: str,
    psu_id: Union[Unset, str] = UNSET,
    psu_corporate_id: Union[Unset, str] = UNSET,
    psu_ip_address: Union[Unset, str] = UNSET,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Response[ApiResponseError]:
    """Get Account Transactions

     Returns the account transactions for an account.<br><br>Feature: `ACCOUNT_TRANSACTIONS`

    Args:
        account_id (str):
        from_ (Union[Unset, str]):
        before (Union[Unset, str]):
        limit (Union[Unset, int]):
        sort (Union[Unset, SortEnum]): The attribute on which resources / records returned should
            be sorted. Valid options for the sort parameter.
        offset (Union[Unset, int]):
        cursor (Union[Unset, str]):
        consent (str):
        psu_id (Union[Unset, str]):
        psu_corporate_id (Union[Unset, str]):
        psu_ip_address (Union[Unset, str]):
        sub_application (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiResponseError]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        from_=from_,
        before=before,
        limit=limit,
        sort=sort,
        offset=offset,
        cursor=cursor,
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
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    from_: Union[Unset, str] = UNSET,
    before: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    sort: Union[Unset, SortEnum] = UNSET,
    offset: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    consent: str,
    psu_id: Union[Unset, str] = UNSET,
    psu_corporate_id: Union[Unset, str] = UNSET,
    psu_ip_address: Union[Unset, str] = UNSET,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Optional[ApiResponseError]:
    """Get Account Transactions

     Returns the account transactions for an account.<br><br>Feature: `ACCOUNT_TRANSACTIONS`

    Args:
        account_id (str):
        from_ (Union[Unset, str]):
        before (Union[Unset, str]):
        limit (Union[Unset, int]):
        sort (Union[Unset, SortEnum]): The attribute on which resources / records returned should
            be sorted. Valid options for the sort parameter.
        offset (Union[Unset, int]):
        cursor (Union[Unset, str]):
        consent (str):
        psu_id (Union[Unset, str]):
        psu_corporate_id (Union[Unset, str]):
        psu_ip_address (Union[Unset, str]):
        sub_application (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiResponseError
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        from_=from_,
        before=before,
        limit=limit,
        sort=sort,
        offset=offset,
        cursor=cursor,
        consent=consent,
        psu_id=psu_id,
        psu_corporate_id=psu_corporate_id,
        psu_ip_address=psu_ip_address,
        sub_application=sub_application,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    from_: Union[Unset, str] = UNSET,
    before: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    sort: Union[Unset, SortEnum] = UNSET,
    offset: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    consent: str,
    psu_id: Union[Unset, str] = UNSET,
    psu_corporate_id: Union[Unset, str] = UNSET,
    psu_ip_address: Union[Unset, str] = UNSET,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Response[ApiResponseError]:
    """Get Account Transactions

     Returns the account transactions for an account.<br><br>Feature: `ACCOUNT_TRANSACTIONS`

    Args:
        account_id (str):
        from_ (Union[Unset, str]):
        before (Union[Unset, str]):
        limit (Union[Unset, int]):
        sort (Union[Unset, SortEnum]): The attribute on which resources / records returned should
            be sorted. Valid options for the sort parameter.
        offset (Union[Unset, int]):
        cursor (Union[Unset, str]):
        consent (str):
        psu_id (Union[Unset, str]):
        psu_corporate_id (Union[Unset, str]):
        psu_ip_address (Union[Unset, str]):
        sub_application (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiResponseError]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        from_=from_,
        before=before,
        limit=limit,
        sort=sort,
        offset=offset,
        cursor=cursor,
        consent=consent,
        psu_id=psu_id,
        psu_corporate_id=psu_corporate_id,
        psu_ip_address=psu_ip_address,
        sub_application=sub_application,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    from_: Union[Unset, str] = UNSET,
    before: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    sort: Union[Unset, SortEnum] = UNSET,
    offset: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    consent: str,
    psu_id: Union[Unset, str] = UNSET,
    psu_corporate_id: Union[Unset, str] = UNSET,
    psu_ip_address: Union[Unset, str] = UNSET,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Optional[ApiResponseError]:
    """Get Account Transactions

     Returns the account transactions for an account.<br><br>Feature: `ACCOUNT_TRANSACTIONS`

    Args:
        account_id (str):
        from_ (Union[Unset, str]):
        before (Union[Unset, str]):
        limit (Union[Unset, int]):
        sort (Union[Unset, SortEnum]): The attribute on which resources / records returned should
            be sorted. Valid options for the sort parameter.
        offset (Union[Unset, int]):
        cursor (Union[Unset, str]):
        consent (str):
        psu_id (Union[Unset, str]):
        psu_corporate_id (Union[Unset, str]):
        psu_ip_address (Union[Unset, str]):
        sub_application (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiResponseError
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            from_=from_,
            before=before,
            limit=limit,
            sort=sort,
            offset=offset,
            cursor=cursor,
            consent=consent,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            sub_application=sub_application,
        )
    ).parsed
