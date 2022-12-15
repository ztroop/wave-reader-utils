from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.device_sample_response import DeviceSampleResponse


T = TypeVar("T", bound="GetLocationSamplesResponse")


@attr.s(auto_attribs=True)
class GetLocationSamplesResponse:
    """
    Attributes:
        devices (List['DeviceSampleResponse']):
        id (str):
        name (str):
    """

    devices: List["DeviceSampleResponse"]
    id: str
    name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        devices = []
        for devices_item_data in self.devices:
            devices_item = devices_item_data.to_dict()

            devices.append(devices_item)

        id = self.id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "devices": devices,
                "id": id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_sample_response import DeviceSampleResponse

        d = src_dict.copy()
        devices = []
        _devices = d.pop("devices")
        for devices_item_data in _devices:
            devices_item = DeviceSampleResponse.from_dict(devices_item_data)

            devices.append(devices_item)

        id = d.pop("id")

        name = d.pop("name")

        get_location_samples_response = cls(
            devices=devices,
            id=id,
            name=name,
        )

        get_location_samples_response.additional_properties = d
        return get_location_samples_response

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
