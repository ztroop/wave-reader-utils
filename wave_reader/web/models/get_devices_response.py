from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_device_detailed_response import GetDeviceDetailedResponse
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetDevicesResponse")


@attr.s(auto_attribs=True)
class GetDevicesResponse:
    devices: Union[Unset, List[GetDeviceDetailedResponse]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        devices: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.devices, Unset):
            devices = []
            for devices_item_data in self.devices:
                devices_item = devices_item_data.to_dict()

                devices.append(devices_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if devices is not UNSET:
            field_dict["devices"] = devices

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        devices = []
        _devices = d.pop("devices", UNSET)
        for devices_item_data in _devices or []:
            devices_item = GetDeviceDetailedResponse.from_dict(devices_item_data)

            devices.append(devices_item)

        get_devices_response = cls(
            devices=devices,
        )

        get_devices_response.additional_properties = d
        return get_devices_response

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
