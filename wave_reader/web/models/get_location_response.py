from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.device_simple_response import DeviceSimpleResponse
from ..models.get_location_response_labels import GetLocationResponseLabels

T = TypeVar("T", bound="GetLocationResponse")


@attr.s(auto_attribs=True)
class GetLocationResponse:
    id: str
    name: str
    labels: GetLocationResponseLabels
    devices: List[DeviceSimpleResponse]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        labels = self.labels.to_dict()

        devices = []
        for devices_item_data in self.devices:
            devices_item = devices_item_data.to_dict()

            devices.append(devices_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "labels": labels,
                "devices": devices,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        labels = GetLocationResponseLabels.from_dict(d.pop("labels"))

        devices = []
        _devices = d.pop("devices")
        for devices_item_data in _devices:
            devices_item = DeviceSimpleResponse.from_dict(devices_item_data)

            devices.append(devices_item)

        get_location_response = cls(
            id=id,
            name=name,
            labels=labels,
            devices=devices,
        )

        get_location_response.additional_properties = d
        return get_location_response

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
