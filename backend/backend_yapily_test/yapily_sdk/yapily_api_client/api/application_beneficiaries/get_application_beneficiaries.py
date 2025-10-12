from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error_response_v2 import ApiErrorResponseV2
from ...models.get_application_beneficiaries_response_200 import GetApplicationBeneficiariesResponse200
from ...types import Response


def _get_kwargs(
    application_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/applications/{application_id}/beneficiaries",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiErrorResponseV2, GetApplicationBeneficiariesResponse200]]:
    if response.status_code == 200:
        response_200 = GetApplicationBeneficiariesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ApiErrorResponseV2.from_dict(response.json())

        return response_401

    if response.status_code == 500:
        response_500 = ApiErrorResponseV2.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiErrorResponseV2, GetApplicationBeneficiariesResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    application_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ApiErrorResponseV2, GetApplicationBeneficiariesResponse200]]:
    """Get all application beneficiaries

     Get all application beneficiaries from an application.

    Args:
        application_id (UUID):  Example: 6d97cf35-1000-4787-af16-7100912db9e4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponseV2, GetApplicationBeneficiariesResponse200]]
    """

    kwargs = _get_kwargs(
        application_id=application_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    application_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ApiErrorResponseV2, GetApplicationBeneficiariesResponse200]]:
    """Get all application beneficiaries

     Get all application beneficiaries from an application.

    Args:
        application_id (UUID):  Example: 6d97cf35-1000-4787-af16-7100912db9e4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponseV2, GetApplicationBeneficiariesResponse200]
    """

    return sync_detailed(
        application_id=application_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    application_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ApiErrorResponseV2, GetApplicationBeneficiariesResponse200]]:
    """Get all application beneficiaries

     Get all application beneficiaries from an application.

    Args:
        application_id (UUID):  Example: 6d97cf35-1000-4787-af16-7100912db9e4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponseV2, GetApplicationBeneficiariesResponse200]]
    """

    kwargs = _get_kwargs(
        application_id=application_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    application_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ApiErrorResponseV2, GetApplicationBeneficiariesResponse200]]:
    """Get all application beneficiaries

     Get all application beneficiaries from an application.

    Args:
        application_id (UUID):  Example: 6d97cf35-1000-4787-af16-7100912db9e4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponseV2, GetApplicationBeneficiariesResponse200]
    """

    return (
        await asyncio_detailed(
            application_id=application_id,
            client=client,
        )
    ).parsed
