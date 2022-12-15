from http import HTTPStatus
from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...models.measurement_system import MeasurementSystem
from ...models.sensor_unit import SensorUnit
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    measurement_system: Union[Unset, None, MeasurementSystem] = UNSET,
    radon_unit: Union[Unset, None, SensorUnit] = UNSET,
    temp_unit: Union[Unset, None, SensorUnit] = UNSET,
    pressure_unit: Union[Unset, None, SensorUnit] = UNSET,
) -> Dict[str, Any]:
    url = "{}/thresholds".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_measurement_system: Union[Unset, None, str] = UNSET
    if not isinstance(measurement_system, Unset):
        json_measurement_system = (
            measurement_system.value if measurement_system else None
        )

    params["measurementSystem"] = json_measurement_system

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
    *,
    client: Client,
    measurement_system: Union[Unset, None, MeasurementSystem] = UNSET,
    radon_unit: Union[Unset, None, SensorUnit] = UNSET,
    temp_unit: Union[Unset, None, SensorUnit] = UNSET,
    pressure_unit: Union[Unset, None, SensorUnit] = UNSET,
) -> Response[Any]:
    """Get threshold values for a device's sensors

    Args:
        measurement_system (Union[Unset, None, MeasurementSystem]):
        radon_unit (Union[Unset, None, SensorUnit]):
        temp_unit (Union[Unset, None, SensorUnit]):
        pressure_unit (Union[Unset, None, SensorUnit]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        measurement_system=measurement_system,
        radon_unit=radon_unit,
        temp_unit=temp_unit,
        pressure_unit=pressure_unit,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    measurement_system: Union[Unset, None, MeasurementSystem] = UNSET,
    radon_unit: Union[Unset, None, SensorUnit] = UNSET,
    temp_unit: Union[Unset, None, SensorUnit] = UNSET,
    pressure_unit: Union[Unset, None, SensorUnit] = UNSET,
) -> Response[Any]:
    """Get threshold values for a device's sensors

    Args:
        measurement_system (Union[Unset, None, MeasurementSystem]):
        radon_unit (Union[Unset, None, SensorUnit]):
        temp_unit (Union[Unset, None, SensorUnit]):
        pressure_unit (Union[Unset, None, SensorUnit]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        measurement_system=measurement_system,
        radon_unit=radon_unit,
        temp_unit=temp_unit,
        pressure_unit=pressure_unit,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
