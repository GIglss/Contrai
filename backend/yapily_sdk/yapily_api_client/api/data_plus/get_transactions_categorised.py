from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error_response_v2 import ApiErrorResponseV2
from ...models.api_response_of_get_categorised_transactions_request import (
    ApiResponseOfGetCategorisedTransactionsRequest,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    categorisation_id: str,
    *,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    sub_application: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(sub_application, Unset):
        headers["sub-application"] = sub_application

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/transactions/categorisation/{categorisation_id}",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiErrorResponseV2, ApiResponseOfGetCategorisedTransactionsRequest]]:
    if response.status_code == 200:
        response_200 = ApiResponseOfGetCategorisedTransactionsRequest.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiErrorResponseV2.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiErrorResponseV2.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ApiErrorResponseV2.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ApiErrorResponseV2.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiErrorResponseV2, ApiResponseOfGetCategorisedTransactionsRequest]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    categorisation_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Response[Union[ApiErrorResponseV2, ApiResponseOfGetCategorisedTransactionsRequest]]:
    """Get Enrichment Results

     Retrieve a set of enriched transactions using a Categorisation ID.

    Args:
        categorisation_id (str):
        limit (Union[Unset, int]):
        page (Union[Unset, int]):
        sub_application (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponseV2, ApiResponseOfGetCategorisedTransactionsRequest]]
    """

    kwargs = _get_kwargs(
        categorisation_id=categorisation_id,
        limit=limit,
        page=page,
        sub_application=sub_application,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    categorisation_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Optional[Union[ApiErrorResponseV2, ApiResponseOfGetCategorisedTransactionsRequest]]:
    """Get Enrichment Results

     Retrieve a set of enriched transactions using a Categorisation ID.

    Args:
        categorisation_id (str):
        limit (Union[Unset, int]):
        page (Union[Unset, int]):
        sub_application (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponseV2, ApiResponseOfGetCategorisedTransactionsRequest]
    """

    return sync_detailed(
        categorisation_id=categorisation_id,
        client=client,
        limit=limit,
        page=page,
        sub_application=sub_application,
    ).parsed


async def asyncio_detailed(
    categorisation_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Response[Union[ApiErrorResponseV2, ApiResponseOfGetCategorisedTransactionsRequest]]:
    """Get Enrichment Results

     Retrieve a set of enriched transactions using a Categorisation ID.

    Args:
        categorisation_id (str):
        limit (Union[Unset, int]):
        page (Union[Unset, int]):
        sub_application (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponseV2, ApiResponseOfGetCategorisedTransactionsRequest]]
    """

    kwargs = _get_kwargs(
        categorisation_id=categorisation_id,
        limit=limit,
        page=page,
        sub_application=sub_application,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    categorisation_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Optional[Union[ApiErrorResponseV2, ApiResponseOfGetCategorisedTransactionsRequest]]:
    """Get Enrichment Results

     Retrieve a set of enriched transactions using a Categorisation ID.

    Args:
        categorisation_id (str):
        limit (Union[Unset, int]):
        page (Union[Unset, int]):
        sub_application (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponseV2, ApiResponseOfGetCategorisedTransactionsRequest]
    """

    return (
        await asyncio_detailed(
            categorisation_id=categorisation_id,
            client=client,
            limit=limit,
            page=page,
            sub_application=sub_application,
        )
    ).parsed
