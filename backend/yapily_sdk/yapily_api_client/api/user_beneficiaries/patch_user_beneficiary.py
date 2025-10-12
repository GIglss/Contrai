from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error_response_v2 import ApiErrorResponseV2
from ...models.patch_user_beneficiary_body_item import PatchUserBeneficiaryBodyItem
from ...models.user_beneficiary_response import UserBeneficiaryResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: UUID,
    beneficiary_id: UUID,
    *,
    body: list["PatchUserBeneficiaryBodyItem"],
    sub_application: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(sub_application, Unset):
        headers["sub-application"] = sub_application

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/users/{user_id}/beneficiaries/{beneficiary_id}",
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json-patch+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiErrorResponseV2, UserBeneficiaryResponse]]:
    if response.status_code == 200:
        response_200 = UserBeneficiaryResponse.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = ApiErrorResponseV2.from_dict(response.json())

        return response_409

    if response.status_code == 429:
        response_429 = ApiErrorResponseV2.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ApiErrorResponseV2.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiErrorResponseV2, UserBeneficiaryResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: UUID,
    beneficiary_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["PatchUserBeneficiaryBodyItem"],
    sub_application: Union[Unset, UUID] = UNSET,
) -> Response[Union[ApiErrorResponseV2, UserBeneficiaryResponse]]:
    """Patch User Beneficiary

     Patch the beneficiary details for a given application user and beneficiary

    Args:
        user_id (UUID):  Example: e7b7636d-a041-4013-8a1b-34dc85b7d341.
        beneficiary_id (UUID): Beneficiary Id Example: e7b7636d-a041-4013-8a1b-34dc85b7d341.
        sub_application (Union[Unset, UUID]):
        body (list['PatchUserBeneficiaryBodyItem']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponseV2, UserBeneficiaryResponse]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        beneficiary_id=beneficiary_id,
        body=body,
        sub_application=sub_application,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: UUID,
    beneficiary_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["PatchUserBeneficiaryBodyItem"],
    sub_application: Union[Unset, UUID] = UNSET,
) -> Optional[Union[ApiErrorResponseV2, UserBeneficiaryResponse]]:
    """Patch User Beneficiary

     Patch the beneficiary details for a given application user and beneficiary

    Args:
        user_id (UUID):  Example: e7b7636d-a041-4013-8a1b-34dc85b7d341.
        beneficiary_id (UUID): Beneficiary Id Example: e7b7636d-a041-4013-8a1b-34dc85b7d341.
        sub_application (Union[Unset, UUID]):
        body (list['PatchUserBeneficiaryBodyItem']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponseV2, UserBeneficiaryResponse]
    """

    return sync_detailed(
        user_id=user_id,
        beneficiary_id=beneficiary_id,
        client=client,
        body=body,
        sub_application=sub_application,
    ).parsed


async def asyncio_detailed(
    user_id: UUID,
    beneficiary_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["PatchUserBeneficiaryBodyItem"],
    sub_application: Union[Unset, UUID] = UNSET,
) -> Response[Union[ApiErrorResponseV2, UserBeneficiaryResponse]]:
    """Patch User Beneficiary

     Patch the beneficiary details for a given application user and beneficiary

    Args:
        user_id (UUID):  Example: e7b7636d-a041-4013-8a1b-34dc85b7d341.
        beneficiary_id (UUID): Beneficiary Id Example: e7b7636d-a041-4013-8a1b-34dc85b7d341.
        sub_application (Union[Unset, UUID]):
        body (list['PatchUserBeneficiaryBodyItem']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResponseV2, UserBeneficiaryResponse]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        beneficiary_id=beneficiary_id,
        body=body,
        sub_application=sub_application,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: UUID,
    beneficiary_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["PatchUserBeneficiaryBodyItem"],
    sub_application: Union[Unset, UUID] = UNSET,
) -> Optional[Union[ApiErrorResponseV2, UserBeneficiaryResponse]]:
    """Patch User Beneficiary

     Patch the beneficiary details for a given application user and beneficiary

    Args:
        user_id (UUID):  Example: e7b7636d-a041-4013-8a1b-34dc85b7d341.
        beneficiary_id (UUID): Beneficiary Id Example: e7b7636d-a041-4013-8a1b-34dc85b7d341.
        sub_application (Union[Unset, UUID]):
        body (list['PatchUserBeneficiaryBodyItem']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResponseV2, UserBeneficiaryResponse]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            beneficiary_id=beneficiary_id,
            client=client,
            body=body,
            sub_application=sub_application,
        )
    ).parsed
