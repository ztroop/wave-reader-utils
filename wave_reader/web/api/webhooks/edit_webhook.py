from http import HTTPStatus
from typing import Any, Dict, Union

import httpx

from ...client import AuthenticatedClient
from ...models.patch_request import PatchRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    hook_id: str,
    *,
    client: AuthenticatedClient,
    json_body: PatchRequest,
    organization_id: Union[Unset, None, str] = UNSET,
    user_group_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/webhooks/{hookId}".format(client.base_url, hookId=hook_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["organizationId"] = organization_id

    params["userGroupId"] = user_group_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    hook_id: str,
    *,
    client: AuthenticatedClient,
    json_body: PatchRequest,
    organization_id: Union[Unset, None, str] = UNSET,
    user_group_id: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Edit a webhook in an organization. Only `locations` is supported at this time. Value type of this
    endpoint is currently a list of location IDs that you wish to perform the operation on.

    Args:
        hook_id (str):
        organization_id (Union[Unset, None, str]):
        user_group_id (Union[Unset, None, str]):
        json_body (PatchRequest):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        hook_id=hook_id,
        client=client,
        json_body=json_body,
        organization_id=organization_id,
        user_group_id=user_group_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    hook_id: str,
    *,
    client: AuthenticatedClient,
    json_body: PatchRequest,
    organization_id: Union[Unset, None, str] = UNSET,
    user_group_id: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Edit a webhook in an organization. Only `locations` is supported at this time. Value type of this
    endpoint is currently a list of location IDs that you wish to perform the operation on.

    Args:
        hook_id (str):
        organization_id (Union[Unset, None, str]):
        user_group_id (Union[Unset, None, str]):
        json_body (PatchRequest):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        hook_id=hook_id,
        client=client,
        json_body=json_body,
        organization_id=organization_id,
        user_group_id=user_group_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
