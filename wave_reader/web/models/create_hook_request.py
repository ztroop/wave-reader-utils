from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.measurement_system import MeasurementSystem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_hook_request_headers import CreateHookRequestHeaders
    from ..models.create_hook_request_labels import CreateHookRequestLabels
    from ..models.hook_sensor_units import HookSensorUnits


T = TypeVar("T", bound="CreateHookRequest")


@attr.s(auto_attribs=True)
class CreateHookRequest:
    """
    Attributes:
        name (str):
        url (str):
        labels (Union[Unset, CreateHookRequestLabels]):
        headers (Union[Unset, CreateHookRequestHeaders]):
        event_types (Union[Unset, List[str]]):
        measurement_system (Union[Unset, MeasurementSystem]):
        sensor_units (Union[Unset, HookSensorUnits]):
        locations (Union[Unset, List[str]]):
        devices (Union[Unset, List[str]]):
        active (Union[Unset, bool]):
    """

    name: str
    url: str
    labels: Union[Unset, "CreateHookRequestLabels"] = UNSET
    headers: Union[Unset, "CreateHookRequestHeaders"] = UNSET
    event_types: Union[Unset, List[str]] = UNSET
    measurement_system: Union[Unset, MeasurementSystem] = UNSET
    sensor_units: Union[Unset, "HookSensorUnits"] = UNSET
    locations: Union[Unset, List[str]] = UNSET
    devices: Union[Unset, List[str]] = UNSET
    active: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        url = self.url
        labels: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        headers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        event_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.event_types, Unset):
            event_types = self.event_types

        measurement_system: Union[Unset, str] = UNSET
        if not isinstance(self.measurement_system, Unset):
            measurement_system = self.measurement_system.value

        sensor_units: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sensor_units, Unset):
            sensor_units = self.sensor_units.to_dict()

        locations: Union[Unset, List[str]] = UNSET
        if not isinstance(self.locations, Unset):
            locations = self.locations

        devices: Union[Unset, List[str]] = UNSET
        if not isinstance(self.devices, Unset):
            devices = self.devices

        active = self.active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "url": url,
            }
        )
        if labels is not UNSET:
            field_dict["labels"] = labels
        if headers is not UNSET:
            field_dict["headers"] = headers
        if event_types is not UNSET:
            field_dict["eventTypes"] = event_types
        if measurement_system is not UNSET:
            field_dict["measurementSystem"] = measurement_system
        if sensor_units is not UNSET:
            field_dict["sensorUnits"] = sensor_units
        if locations is not UNSET:
            field_dict["locations"] = locations
        if devices is not UNSET:
            field_dict["devices"] = devices
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_hook_request_headers import (
            CreateHookRequestHeaders,
        )
        from ..models.create_hook_request_labels import CreateHookRequestLabels
        from ..models.hook_sensor_units import HookSensorUnits

        d = src_dict.copy()
        name = d.pop("name")

        url = d.pop("url")

        _labels = d.pop("labels", UNSET)
        labels: Union[Unset, CreateHookRequestLabels]
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = CreateHookRequestLabels.from_dict(_labels)

        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, CreateHookRequestHeaders]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = CreateHookRequestHeaders.from_dict(_headers)

        event_types = cast(List[str], d.pop("eventTypes", UNSET))

        _measurement_system = d.pop("measurementSystem", UNSET)
        measurement_system: Union[Unset, MeasurementSystem]
        if isinstance(_measurement_system, Unset):
            measurement_system = UNSET
        else:
            measurement_system = MeasurementSystem(_measurement_system)

        _sensor_units = d.pop("sensorUnits", UNSET)
        sensor_units: Union[Unset, HookSensorUnits]
        if isinstance(_sensor_units, Unset):
            sensor_units = UNSET
        else:
            sensor_units = HookSensorUnits.from_dict(_sensor_units)

        locations = cast(List[str], d.pop("locations", UNSET))

        devices = cast(List[str], d.pop("devices", UNSET))

        active = d.pop("active", UNSET)

        create_hook_request = cls(
            name=name,
            url=url,
            labels=labels,
            headers=headers,
            event_types=event_types,
            measurement_system=measurement_system,
            sensor_units=sensor_units,
            locations=locations,
            devices=devices,
            active=active,
        )

        create_hook_request.additional_properties = d
        return create_hook_request

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
