from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response_error import ApiResponseError
from ...models.api_response_of_get_hosted_vrp_consents_request import ApiResponseOfGetHostedVRPConsentsRequest
from ...types import Response


def _get_kwargs(
    *,
    sub_application: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["sub-application"] = sub_application

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/hosted/vrp/consent-requests",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiResponseError, ApiResponseOfGetHostedVRPConsentsRequest]]:
    if response.status_code == 200:
        response_200 = ApiResponseOfGetHostedVRPConsentsRequest.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiResponseError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiResponseError.from_dict(response.json())

        return response_401

    if response.status_code == 500:
        response_500 = ApiResponseError.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiResponseError, ApiResponseOfGetHostedVRPConsentsRequest]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    sub_application: str,
) -> Response[Union[ApiResponseError, ApiResponseOfGetHostedVRPConsentsRequest]]:
    """Get Hosted VRP Consent Requests

     Used to get all VRP consent requests initiated through Yapily Hosted Pages

    Args:
        sub_application (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiResponseError, ApiResponseOfGetHostedVRPConsentsRequest]]
    """

    kwargs = _get_kwargs(
        sub_application=sub_application,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    sub_application: str,
) -> Optional[Union[ApiResponseError, ApiResponseOfGetHostedVRPConsentsRequest]]:
    """Get Hosted VRP Consent Requests

     Used to get all VRP consent requests initiated through Yapily Hosted Pages

    Args:
        sub_application (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiResponseError, ApiResponseOfGetHostedVRPConsentsRequest]
    """

    return sync_detailed(
        client=client,
        sub_application=sub_application,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    sub_application: str,
) -> Response[Union[ApiResponseError, ApiResponseOfGetHostedVRPConsentsRequest]]:
    """Get Hosted VRP Consent Requests

     Used to get all VRP consent requests initiated through Yapily Hosted Pages

    Args:
        sub_application (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiResponseError, ApiResponseOfGetHostedVRPConsentsRequest]]
    """

    kwargs = _get_kwargs(
        sub_application=sub_application,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    sub_application: str,
) -> Optional[Union[ApiResponseError, ApiResponseOfGetHostedVRPConsentsRequest]]:
    """Get Hosted VRP Consent Requests

     Used to get all VRP consent requests initiated through Yapily Hosted Pages

    Args:
        sub_application (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiResponseError, ApiResponseOfGetHostedVRPConsentsRequest]
    """

    return (
        await asyncio_detailed(
            client=client,
            sub_application=sub_application,
        )
    ).parsed
