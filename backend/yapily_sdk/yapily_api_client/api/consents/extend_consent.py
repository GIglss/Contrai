from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_error_response import ApiErrorResponse
from ...models.api_response_of_consent import ApiResponseOfConsent
from ...models.extend_consent_request import ExtendConsentRequest
from ...types import Response


def _get_kwargs(
    consent_id: UUID,
    *,
    body: ExtendConsentRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/consents/{consent_id}/extend",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ApiErrorResponse, ApiResponseOfConsent]:
    if response.status_code == 200:
        response_200 = ApiResponseOfConsent.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiErrorResponse.from_dict(response.json())

        return response_400

    response_default = ApiErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiErrorResponse, ApiResponseOfConsent]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    consent_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ExtendConsentRequest,
) -> Response[Union[ApiErrorResponse, ApiResponseOfConsent]]:
    """Extend Consent

     Used to indicate to Yapily that reconfirmation has occurred for a given Consent, and to update
    lastUpdatedAt and reconfirmBy for that Consent. Returns the Consent.

    Args:
        consent_id (UUID):
        body (ExtendConsentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponse, ApiResponseOfConsent]]
    """

    kwargs = _get_kwargs(
        consent_id=consent_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    consent_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ExtendConsentRequest,
) -> Optional[Union[ApiErrorResponse, ApiResponseOfConsent]]:
    """Extend Consent

     Used to indicate to Yapily that reconfirmation has occurred for a given Consent, and to update
    lastUpdatedAt and reconfirmBy for that Consent. Returns the Consent.

    Args:
        consent_id (UUID):
        body (ExtendConsentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponse, ApiResponseOfConsent]
    """

    return sync_detailed(
        consent_id=consent_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    consent_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ExtendConsentRequest,
) -> Response[Union[ApiErrorResponse, ApiResponseOfConsent]]:
    """Extend Consent

     Used to indicate to Yapily that reconfirmation has occurred for a given Consent, and to update
    lastUpdatedAt and reconfirmBy for that Consent. Returns the Consent.

    Args:
        consent_id (UUID):
        body (ExtendConsentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponse, ApiResponseOfConsent]]
    """

    kwargs = _get_kwargs(
        consent_id=consent_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    consent_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ExtendConsentRequest,
) -> Optional[Union[ApiErrorResponse, ApiResponseOfConsent]]:
    """Extend Consent

     Used to indicate to Yapily that reconfirmation has occurred for a given Consent, and to update
    lastUpdatedAt and reconfirmBy for that Consent. Returns the Consent.

    Args:
        consent_id (UUID):
        body (ExtendConsentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponse, ApiResponseOfConsent]
    """

    return (
        await asyncio_detailed(
            consent_id=consent_id,
            client=client,
            body=body,
        )
    ).parsed
