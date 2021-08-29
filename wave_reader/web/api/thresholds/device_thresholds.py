from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...models.measurement_system import MeasurementSystem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    measurement_system: Union[Unset, None, MeasurementSystem] = UNSET,
) -> Dict[str, Any]:
    url = "{}/thresholds".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_measurement_system: Union[Unset, None, str] = UNSET
    if not isinstance(measurement_system, Unset):
        json_measurement_system = (
            measurement_system.value if measurement_system else None
        )

    params: Dict[str, Any] = {
        "measurementSystem": json_measurement_system,
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
    *,
    client: Client,
    measurement_system: Union[Unset, None, MeasurementSystem] = UNSET,
) -> Response[Any]:
    kwargs = _get_kwargs(
        client=client,
        measurement_system=measurement_system,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    measurement_system: Union[Unset, None, MeasurementSystem] = UNSET,
) -> Response[Any]:
    kwargs = _get_kwargs(
        client=client,
        measurement_system=measurement_system,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)
