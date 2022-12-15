from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.device_type import DeviceType
from ..models.sensor_type import SensorType

if TYPE_CHECKING:
    from ..models.location_simple_response import LocationSimpleResponse
    from ..models.segment_simple_response import SegmentSimpleResponse


T = TypeVar("T", bound="GetDeviceDetailedResponse")


@attr.s(auto_attribs=True)
class GetDeviceDetailedResponse:
    """
    Attributes:
        id (str):
        device_type (DeviceType):
        sensors (List[SensorType]):
        segment (SegmentSimpleResponse):
        location (LocationSimpleResponse):
    """

    id: str
    device_type: DeviceType
    sensors: List[SensorType]
    segment: "SegmentSimpleResponse"
    location: "LocationSimpleResponse"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        device_type = self.device_type.value

        sensors = []
        for sensors_item_data in self.sensors:
            sensors_item = sensors_item_data.value

            sensors.append(sensors_item)

        segment = self.segment.to_dict()

        location = self.location.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "deviceType": device_type,
                "sensors": sensors,
                "segment": segment,
                "location": location,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.location_simple_response import LocationSimpleResponse
        from ..models.segment_simple_response import SegmentSimpleResponse

        d = src_dict.copy()
        id = d.pop("id")

        device_type = DeviceType(d.pop("deviceType"))

        sensors = []
        _sensors = d.pop("sensors")
        for sensors_item_data in _sensors:
            sensors_item = SensorType(sensors_item_data)

            sensors.append(sensors_item)

        segment = SegmentSimpleResponse.from_dict(d.pop("segment"))

        location = LocationSimpleResponse.from_dict(d.pop("location"))

        get_device_detailed_response = cls(
            id=id,
            device_type=device_type,
            sensors=sensors,
            segment=segment,
            location=location,
        )

        get_device_detailed_response.additional_properties = d
        return get_device_detailed_response

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
