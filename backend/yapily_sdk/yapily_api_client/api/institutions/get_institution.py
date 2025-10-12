from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_response_error import ApiResponseError
from ...models.institution import Institution
from ...types import Response


def _get_kwargs(
    institution_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/institutions/{institution_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ApiResponseError, Institution]:
    if response.status_code == 200:
        response_200 = Institution.from_dict(response.json())

        return response_200

    response_default = ApiResponseError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiResponseError, Institution]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    institution_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ApiResponseError, Institution]]:
    """Get Institution

     Used to retrieves details of a specific `Institution` within an application

    Args:
        institution_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiResponseError, Institution]]
    """

    kwargs = _get_kwargs(
        institution_id=institution_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    institution_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ApiResponseError, Institution]]:
    """Get Institution

     Used to retrieves details of a specific `Institution` within an application

    Args:
        institution_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiResponseError, Institution]
    """

    return sync_detailed(
        institution_id=institution_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    institution_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ApiResponseError, Institution]]:
    """Get Institution

     Used to retrieves details of a specific `Institution` within an application

    Args:
        institution_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiResponseError, Institution]]
    """

    kwargs = _get_kwargs(
        institution_id=institution_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    institution_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ApiResponseError, Institution]]:
    """Get Institution

     Used to retrieves details of a specific `Institution` within an application

    Args:
        institution_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiResponseError, Institution]
    """

    return (
        await asyncio_detailed(
            institution_id=institution_id,
            client=client,
        )
    ).parsed
