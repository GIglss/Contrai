from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_response_error import ApiResponseError
from ...models.api_response_of_consent_delete_response import ApiResponseOfConsentDeleteResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    consent_id: UUID,
    *,
    force_delete: Union[Unset, bool] = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["forceDelete"] = force_delete

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/consents/{consent_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ApiResponseError, ApiResponseOfConsentDeleteResponse]:
    if response.status_code == 200:
        response_200 = ApiResponseOfConsentDeleteResponse.from_dict(response.json())

        return response_200

    response_default = ApiResponseError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiResponseError, ApiResponseOfConsentDeleteResponse]]:
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
    force_delete: Union[Unset, bool] = True,
) -> Response[Union[ApiResponseError, ApiResponseOfConsentDeleteResponse]]:
    """Delete Consent

     Delete a consent using the consent Id

    Args:
        consent_id (UUID):
        force_delete (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiResponseError, ApiResponseOfConsentDeleteResponse]]
    """

    kwargs = _get_kwargs(
        consent_id=consent_id,
        force_delete=force_delete,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    consent_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    force_delete: Union[Unset, bool] = True,
) -> Optional[Union[ApiResponseError, ApiResponseOfConsentDeleteResponse]]:
    """Delete Consent

     Delete a consent using the consent Id

    Args:
        consent_id (UUID):
        force_delete (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiResponseError, ApiResponseOfConsentDeleteResponse]
    """

    return sync_detailed(
        consent_id=consent_id,
        client=client,
        force_delete=force_delete,
    ).parsed


async def asyncio_detailed(
    consent_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    force_delete: Union[Unset, bool] = True,
) -> Response[Union[ApiResponseError, ApiResponseOfConsentDeleteResponse]]:
    """Delete Consent

     Delete a consent using the consent Id

    Args:
        consent_id (UUID):
        force_delete (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiResponseError, ApiResponseOfConsentDeleteResponse]]
    """

    kwargs = _get_kwargs(
        consent_id=consent_id,
        force_delete=force_delete,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    consent_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    force_delete: Union[Unset, bool] = True,
) -> Optional[Union[ApiResponseError, ApiResponseOfConsentDeleteResponse]]:
    """Delete Consent

     Delete a consent using the consent Id

    Args:
        consent_id (UUID):
        force_delete (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiResponseError, ApiResponseOfConsentDeleteResponse]
    """

    return (
        await asyncio_detailed(
            consent_id=consent_id,
            client=client,
            force_delete=force_delete,
        )
    ).parsed
