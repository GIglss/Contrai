from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_response_error import ApiResponseError
from ...models.api_response_of_create_hosted_consent_request import ApiResponseOfCreateHostedConsentRequest
from ...models.create_hosted_consent_request import CreateHostedConsentRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateHostedConsentRequest,
    sub_application: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(sub_application, Unset):
        headers["sub-application"] = sub_application

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/hosted/consent-requests",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ApiResponseError, ApiResponseOfCreateHostedConsentRequest]:
    if response.status_code == 201:
        response_201 = ApiResponseOfCreateHostedConsentRequest.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ApiResponseError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiResponseError.from_dict(response.json())

        return response_401

    if response.status_code == 500:
        response_500 = ApiResponseError.from_dict(response.json())

        return response_500

    response_default = ApiResponseError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiResponseError, ApiResponseOfCreateHostedConsentRequest]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateHostedConsentRequest,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Response[Union[ApiResponseError, ApiResponseOfCreateHostedConsentRequest]]:
    """Create Hosted Consent Request

     Used to initiate a consent request using Yapily Hosted Pages.

    Args:
        sub_application (Union[Unset, UUID]):
        body (CreateHostedConsentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiResponseError, ApiResponseOfCreateHostedConsentRequest]]
    """

    kwargs = _get_kwargs(
        body=body,
        sub_application=sub_application,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateHostedConsentRequest,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Optional[Union[ApiResponseError, ApiResponseOfCreateHostedConsentRequest]]:
    """Create Hosted Consent Request

     Used to initiate a consent request using Yapily Hosted Pages.

    Args:
        sub_application (Union[Unset, UUID]):
        body (CreateHostedConsentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiResponseError, ApiResponseOfCreateHostedConsentRequest]
    """

    return sync_detailed(
        client=client,
        body=body,
        sub_application=sub_application,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateHostedConsentRequest,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Response[Union[ApiResponseError, ApiResponseOfCreateHostedConsentRequest]]:
    """Create Hosted Consent Request

     Used to initiate a consent request using Yapily Hosted Pages.

    Args:
        sub_application (Union[Unset, UUID]):
        body (CreateHostedConsentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiResponseError, ApiResponseOfCreateHostedConsentRequest]]
    """

    kwargs = _get_kwargs(
        body=body,
        sub_application=sub_application,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateHostedConsentRequest,
    sub_application: Union[Unset, UUID] = UNSET,
) -> Optional[Union[ApiResponseError, ApiResponseOfCreateHostedConsentRequest]]:
    """Create Hosted Consent Request

     Used to initiate a consent request using Yapily Hosted Pages.

    Args:
        sub_application (Union[Unset, UUID]):
        body (CreateHostedConsentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiResponseError, ApiResponseOfCreateHostedConsentRequest]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            sub_application=sub_application,
        )
    ).parsed
