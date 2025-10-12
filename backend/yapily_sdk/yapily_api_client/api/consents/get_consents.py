from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_list_response_of_consent import ApiListResponseOfConsent
from ...models.api_response_error import ApiResponseError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filterapplication_user_id: Union[Unset, list[str]] = UNSET,
    filteruser_uuid: Union[Unset, list[UUID]] = UNSET,
    filterinstitution: Union[Unset, list[str]] = UNSET,
    filterstatus: Union[Unset, list[str]] = UNSET,
    from_: Union[Unset, str] = UNSET,
    before: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_filterapplication_user_id: Union[Unset, list[str]] = UNSET
    if not isinstance(filterapplication_user_id, Unset):
        json_filterapplication_user_id = filterapplication_user_id

    params["filter[applicationUserId]"] = json_filterapplication_user_id

    json_filteruser_uuid: Union[Unset, list[str]] = UNSET
    if not isinstance(filteruser_uuid, Unset):
        json_filteruser_uuid = []
        for filteruser_uuid_item_data in filteruser_uuid:
            filteruser_uuid_item = str(filteruser_uuid_item_data)
            json_filteruser_uuid.append(filteruser_uuid_item)

    params["filter[userUuid]"] = json_filteruser_uuid

    json_filterinstitution: Union[Unset, list[str]] = UNSET
    if not isinstance(filterinstitution, Unset):
        json_filterinstitution = filterinstitution

    params["filter[institution]"] = json_filterinstitution

    json_filterstatus: Union[Unset, list[str]] = UNSET
    if not isinstance(filterstatus, Unset):
        json_filterstatus = filterstatus

    params["filter[status]"] = json_filterstatus

    params["from"] = from_

    params["before"] = before

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/consents",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ApiListResponseOfConsent, ApiResponseError]:
    if response.status_code == 200:
        response_200 = ApiListResponseOfConsent.from_dict(response.json())

        return response_200

    response_default = ApiResponseError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiListResponseOfConsent, ApiResponseError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    filterapplication_user_id: Union[Unset, list[str]] = UNSET,
    filteruser_uuid: Union[Unset, list[UUID]] = UNSET,
    filterinstitution: Union[Unset, list[str]] = UNSET,
    filterstatus: Union[Unset, list[str]] = UNSET,
    from_: Union[Unset, str] = UNSET,
    before: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = 0,
) -> Response[Union[ApiListResponseOfConsent, ApiResponseError]]:
    """Get Consents

     Used to retrieve all the consents created for each user within an application. At least one of the
    following filters needs to be applied: filter[applicationUserId], filter[userUuid]=, limit=.

    Args:
        filterapplication_user_id (Union[Unset, list[str]]):
        filteruser_uuid (Union[Unset, list[UUID]]):
        filterinstitution (Union[Unset, list[str]]):
        filterstatus (Union[Unset, list[str]]):
        from_ (Union[Unset, str]):
        before (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiListResponseOfConsent, ApiResponseError]]
    """

    kwargs = _get_kwargs(
        filterapplication_user_id=filterapplication_user_id,
        filteruser_uuid=filteruser_uuid,
        filterinstitution=filterinstitution,
        filterstatus=filterstatus,
        from_=from_,
        before=before,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    filterapplication_user_id: Union[Unset, list[str]] = UNSET,
    filteruser_uuid: Union[Unset, list[UUID]] = UNSET,
    filterinstitution: Union[Unset, list[str]] = UNSET,
    filterstatus: Union[Unset, list[str]] = UNSET,
    from_: Union[Unset, str] = UNSET,
    before: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = 0,
) -> Optional[Union[ApiListResponseOfConsent, ApiResponseError]]:
    """Get Consents

     Used to retrieve all the consents created for each user within an application. At least one of the
    following filters needs to be applied: filter[applicationUserId], filter[userUuid]=, limit=.

    Args:
        filterapplication_user_id (Union[Unset, list[str]]):
        filteruser_uuid (Union[Unset, list[UUID]]):
        filterinstitution (Union[Unset, list[str]]):
        filterstatus (Union[Unset, list[str]]):
        from_ (Union[Unset, str]):
        before (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiListResponseOfConsent, ApiResponseError]
    """

    return sync_detailed(
        client=client,
        filterapplication_user_id=filterapplication_user_id,
        filteruser_uuid=filteruser_uuid,
        filterinstitution=filterinstitution,
        filterstatus=filterstatus,
        from_=from_,
        before=before,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    filterapplication_user_id: Union[Unset, list[str]] = UNSET,
    filteruser_uuid: Union[Unset, list[UUID]] = UNSET,
    filterinstitution: Union[Unset, list[str]] = UNSET,
    filterstatus: Union[Unset, list[str]] = UNSET,
    from_: Union[Unset, str] = UNSET,
    before: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = 0,
) -> Response[Union[ApiListResponseOfConsent, ApiResponseError]]:
    """Get Consents

     Used to retrieve all the consents created for each user within an application. At least one of the
    following filters needs to be applied: filter[applicationUserId], filter[userUuid]=, limit=.

    Args:
        filterapplication_user_id (Union[Unset, list[str]]):
        filteruser_uuid (Union[Unset, list[UUID]]):
        filterinstitution (Union[Unset, list[str]]):
        filterstatus (Union[Unset, list[str]]):
        from_ (Union[Unset, str]):
        before (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiListResponseOfConsent, ApiResponseError]]
    """

    kwargs = _get_kwargs(
        filterapplication_user_id=filterapplication_user_id,
        filteruser_uuid=filteruser_uuid,
        filterinstitution=filterinstitution,
        filterstatus=filterstatus,
        from_=from_,
        before=before,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    filterapplication_user_id: Union[Unset, list[str]] = UNSET,
    filteruser_uuid: Union[Unset, list[UUID]] = UNSET,
    filterinstitution: Union[Unset, list[str]] = UNSET,
    filterstatus: Union[Unset, list[str]] = UNSET,
    from_: Union[Unset, str] = UNSET,
    before: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = 0,
) -> Optional[Union[ApiListResponseOfConsent, ApiResponseError]]:
    """Get Consents

     Used to retrieve all the consents created for each user within an application. At least one of the
    following filters needs to be applied: filter[applicationUserId], filter[userUuid]=, limit=.

    Args:
        filterapplication_user_id (Union[Unset, list[str]]):
        filteruser_uuid (Union[Unset, list[UUID]]):
        filterinstitution (Union[Unset, list[str]]):
        filterstatus (Union[Unset, list[str]]):
        from_ (Union[Unset, str]):
        before (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiListResponseOfConsent, ApiResponseError]
    """

    return (
        await asyncio_detailed(
            client=client,
            filterapplication_user_id=filterapplication_user_id,
            filteruser_uuid=filteruser_uuid,
            filterinstitution=filterinstitution,
            filterstatus=filterstatus,
            from_=from_,
            before=before,
            limit=limit,
            offset=offset,
        )
    ).parsed
