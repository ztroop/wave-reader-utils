from typing import Any, Dict, Union

import httpx

from ...client import AuthenticatedClient
from ...types import UNSET, Response, Unset


def _get_kwargs(
    serial_number: str,
    *,
    client: AuthenticatedClient,
    start: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    resolution: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, str] = UNSET,
    organization_id: Union[Unset, None, str] = UNSET,
    user_group_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/devices/{serialNumber}/samples".format(
        client.base_url, serialNumber=serial_number
    )

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "start": start,
        "end": end,
        "pageSize": page_size,
        "resolution": resolution,
        "cursor": cursor,
        "organizationId": organization_id,
        "userGroupId": user_group_id,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    serial_number: str,
    *,
    client: AuthenticatedClient,
    start: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    resolution: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, str] = UNSET,
    organization_id: Union[Unset, None, str] = UNSET,
    user_group_id: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    kwargs = _get_kwargs(
        serial_number=serial_number,
        client=client,
        start=start,
        end=end,
        page_size=page_size,
        resolution=resolution,
        cursor=cursor,
        organization_id=organization_id,
        user_group_id=user_group_id,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    serial_number: str,
    *,
    client: AuthenticatedClient,
    start: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    resolution: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, str] = UNSET,
    organization_id: Union[Unset, None, str] = UNSET,
    user_group_id: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    kwargs = _get_kwargs(
        serial_number=serial_number,
        client=client,
        start=start,
        end=end,
        page_size=page_size,
        resolution=resolution,
        cursor=cursor,
        organization_id=organization_id,
        user_group_id=user_group_id,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)