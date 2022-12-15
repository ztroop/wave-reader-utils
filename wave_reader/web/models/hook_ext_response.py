from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.measurement_system import MeasurementSystem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_device_detailed_response import GetDeviceDetailedResponse
    from ..models.hook_event import HookEvent
    from ..models.hook_ext_response_headers import HookExtResponseHeaders
    from ..models.hook_ext_response_labels import HookExtResponseLabels
    from ..models.hook_sensor_units import HookSensorUnits
    from ..models.location import Location


T = TypeVar("T", bound="HookExtResponse")


@attr.s(auto_attribs=True)
class HookExtResponse:
    """
    Attributes:
        name (str):
        id (str):
        url (str):
        locations (List['Location']):
        devices (List['GetDeviceDetailedResponse']):
        event_types (List[str]):
        labels (HookExtResponseLabels):
        headers (HookExtResponseHeaders):
        measurement_system (MeasurementSystem):
        sensor_units (HookSensorUnits):
        active (bool):
        most_recent_event (Union[Unset, HookEvent]):
    """

    name: str
    id: str
    url: str
    locations: List["Location"]
    devices: List["GetDeviceDetailedResponse"]
    event_types: List[str]
    labels: "HookExtResponseLabels"
    headers: "HookExtResponseHeaders"
    measurement_system: MeasurementSystem
    sensor_units: "HookSensorUnits"
    active: bool
    most_recent_event: Union[Unset, "HookEvent"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id
        url = self.url
        locations = []
        for locations_item_data in self.locations:
            locations_item = locations_item_data.to_dict()

            locations.append(locations_item)

        devices = []
        for devices_item_data in self.devices:
            devices_item = devices_item_data.to_dict()

            devices.append(devices_item)

        event_types = self.event_types

        labels = self.labels.to_dict()

        headers = self.headers.to_dict()

        measurement_system = self.measurement_system.value

        sensor_units = self.sensor_units.to_dict()

        active = self.active
        most_recent_event: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.most_recent_event, Unset):
            most_recent_event = self.most_recent_event.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "id": id,
                "url": url,
                "locations": locations,
                "devices": devices,
                "eventTypes": event_types,
                "labels": labels,
                "headers": headers,
                "measurementSystem": measurement_system,
                "sensorUnits": sensor_units,
                "active": active,
            }
        )
        if most_recent_event is not UNSET:
            field_dict["mostRecentEvent"] = most_recent_event

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_device_detailed_response import (
            GetDeviceDetailedResponse,
        )
        from ..models.hook_event import HookEvent
        from ..models.hook_ext_response_headers import HookExtResponseHeaders
        from ..models.hook_ext_response_labels import HookExtResponseLabels
        from ..models.hook_sensor_units import HookSensorUnits
        from ..models.location import Location

        d = src_dict.copy()
        name = d.pop("name")

        id = d.pop("id")

        url = d.pop("url")

        locations = []
        _locations = d.pop("locations")
        for locations_item_data in _locations:
            locations_item = Location.from_dict(locations_item_data)

            locations.append(locations_item)

        devices = []
        _devices = d.pop("devices")
        for devices_item_data in _devices:
            devices_item = GetDeviceDetailedResponse.from_dict(devices_item_data)

            devices.append(devices_item)

        event_types = cast(List[str], d.pop("eventTypes"))

        labels = HookExtResponseLabels.from_dict(d.pop("labels"))

        headers = HookExtResponseHeaders.from_dict(d.pop("headers"))

        measurement_system = MeasurementSystem(d.pop("measurementSystem"))

        sensor_units = HookSensorUnits.from_dict(d.pop("sensorUnits"))

        active = d.pop("active")

        _most_recent_event = d.pop("mostRecentEvent", UNSET)
        most_recent_event: Union[Unset, HookEvent]
        if isinstance(_most_recent_event, Unset):
            most_recent_event = UNSET
        else:
            most_recent_event = HookEvent.from_dict(_most_recent_event)

        hook_ext_response = cls(
            name=name,
            id=id,
            url=url,
            locations=locations,
            devices=devices,
            event_types=event_types,
            labels=labels,
            headers=headers,
            measurement_system=measurement_system,
            sensor_units=sensor_units,
            active=active,
            most_recent_event=most_recent_event,
        )

        hook_ext_response.additional_properties = d
        return hook_ext_response

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
