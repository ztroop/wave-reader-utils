from typing import Any, Dict, Union

import httpx

from ...client import AuthenticatedClient
from ...types import UNSET, Response, Unset


def _get_kwargs(
    location_id: str,
    *,
    client: AuthenticatedClient,
    show_inactive: Union[Unset, None, bool] = False,
    organization_id: Union[Unset, None, str] = UNSET,
    user_group_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/locations/{locationId}/latest-samples".format(
        client.base_url, locationId=location_id
    )

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "showInactive": show_inactive,
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
    location_id: str,
    *,
    client: AuthenticatedClient,
    show_inactive: Union[Unset, None, bool] = False,
    organization_id: Union[Unset, None, str] = UNSET,
    user_group_id: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    kwargs = _get_kwargs(
        location_id=location_id,
        client=client,
        show_inactive=show_inactive,
        organization_id=organization_id,
        user_group_id=user_group_id,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    location_id: str,
    *,
    client: AuthenticatedClient,
    show_inactive: Union[Unset, None, bool] = False,
    organization_id: Union[Unset, None, str] = UNSET,
    user_group_id: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    kwargs = _get_kwargs(
        location_id=location_id,
        client=client,
        show_inactive=show_inactive,
        organization_id=organization_id,
        user_group_id=user_group_id,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)
