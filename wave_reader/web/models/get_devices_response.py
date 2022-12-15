from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_device_detailed_response import GetDeviceDetailedResponse


T = TypeVar("T", bound="GetDevicesResponse")


@attr.s(auto_attribs=True)
class GetDevicesResponse:
    """
    Attributes:
        devices (Union[Unset, List['GetDeviceDetailedResponse']]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        total (Union[Unset, int]):
    """

    devices: Union[Unset, List["GetDeviceDetailedResponse"]] = UNSET
    limit: Union[Unset, int] = UNSET
    offset: Union[Unset, int] = UNSET
    total: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        devices: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.devices, Unset):
            devices = []
            for devices_item_data in self.devices:
                devices_item = devices_item_data.to_dict()

                devices.append(devices_item)

        limit = self.limit
        offset = self.offset
        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if devices is not UNSET:
            field_dict["devices"] = devices
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_device_detailed_response import (
            GetDeviceDetailedResponse,
        )

        d = src_dict.copy()
        devices = []
        _devices = d.pop("devices", UNSET)
        for devices_item_data in _devices or []:
            devices_item = GetDeviceDetailedResponse.from_dict(devices_item_data)

            devices.append(devices_item)

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        total = d.pop("total", UNSET)

        get_devices_response = cls(
            devices=devices,
            limit=limit,
            offset=offset,
            total=total,
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
