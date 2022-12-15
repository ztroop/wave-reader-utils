from http import HTTPStatus
from typing import Any, Dict, Union

import httpx

from ...client import AuthenticatedClient
from ...models.sensor_unit import SensorUnit
from ...types import UNSET, Response, Unset


def _get_kwargs(
    segment_id: str,
    *,
    client: AuthenticatedClient,
    start: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    resolution: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, str] = UNSET,
    measurement_system: Union[Unset, None, str] = UNSET,
    radon_unit: Union[Unset, None, SensorUnit] = UNSET,
    temp_unit: Union[Unset, None, SensorUnit] = UNSET,
    pressure_unit: Union[Unset, None, SensorUnit] = UNSET,
    organization_id: Union[Unset, None, str] = UNSET,
    user_group_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/segments/{segmentId}/mold-samples".format(
        client.base_url, segmentId=segment_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["start"] = start

    params["end"] = end

    params["pageSize"] = page_size

    params["resolution"] = resolution

    params["cursor"] = cursor

    params["measurementSystem"] = measurement_system

    json_radon_unit: Union[Unset, None, str] = UNSET
    if not isinstance(radon_unit, Unset):
        json_radon_unit = radon_unit.value if radon_unit else None

    params["radonUnit"] = json_radon_unit

    json_temp_unit: Union[Unset, None, str] = UNSET
    if not isinstance(temp_unit, Unset):
        json_temp_unit = temp_unit.value if temp_unit else None

    params["tempUnit"] = json_temp_unit

    json_pressure_unit: Union[Unset, None, str] = UNSET
    if not isinstance(pressure_unit, Unset):
        json_pressure_unit = pressure_unit.value if pressure_unit else None

    params["pressureUnit"] = json_pressure_unit

    params["organizationId"] = organization_id

    params["userGroupId"] = user_group_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
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
    segment_id: str,
    *,
    client: AuthenticatedClient,
    start: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    resolution: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, str] = UNSET,
    measurement_system: Union[Unset, None, str] = UNSET,
    radon_unit: Union[Unset, None, SensorUnit] = UNSET,
    temp_unit: Union[Unset, None, SensorUnit] = UNSET,
    pressure_unit: Union[Unset, None, SensorUnit] = UNSET,
    organization_id: Union[Unset, None, str] = UNSET,
    user_group_id: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Get Samples within a specific Measurement Segment

    Args:
        segment_id (str):
        start (Union[Unset, None, str]):
        end (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        resolution (Union[Unset, None, str]):
        cursor (Union[Unset, None, str]):
        measurement_system (Union[Unset, None, str]):
        radon_unit (Union[Unset, None, SensorUnit]):
        temp_unit (Union[Unset, None, SensorUnit]):
        pressure_unit (Union[Unset, None, SensorUnit]):
        organization_id (Union[Unset, None, str]):
        user_group_id (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        segment_id=segment_id,
        client=client,
        start=start,
        end=end,
        page_size=page_size,
        resolution=resolution,
        cursor=cursor,
        measurement_system=measurement_system,
        radon_unit=radon_unit,
        temp_unit=temp_unit,
        pressure_unit=pressure_unit,
        organization_id=organization_id,
        user_group_id=user_group_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    segment_id: str,
    *,
    client: AuthenticatedClient,
    start: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    resolution: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, str] = UNSET,
    measurement_system: Union[Unset, None, str] = UNSET,
    radon_unit: Union[Unset, None, SensorUnit] = UNSET,
    temp_unit: Union[Unset, None, SensorUnit] = UNSET,
    pressure_unit: Union[Unset, None, SensorUnit] = UNSET,
    organization_id: Union[Unset, None, str] = UNSET,
    user_group_id: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Get Samples within a specific Measurement Segment

    Args:
        segment_id (str):
        start (Union[Unset, None, str]):
        end (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        resolution (Union[Unset, None, str]):
        cursor (Union[Unset, None, str]):
        measurement_system (Union[Unset, None, str]):
        radon_unit (Union[Unset, None, SensorUnit]):
        temp_unit (Union[Unset, None, SensorUnit]):
        pressure_unit (Union[Unset, None, SensorUnit]):
        organization_id (Union[Unset, None, str]):
        user_group_id (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        segment_id=segment_id,
        client=client,
        start=start,
        end=end,
        page_size=page_size,
        resolution=resolution,
        cursor=cursor,
        measurement_system=measurement_system,
        radon_unit=radon_unit,
        temp_unit=temp_unit,
        pressure_unit=pressure_unit,
        organization_id=organization_id,
        user_group_id=user_group_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
