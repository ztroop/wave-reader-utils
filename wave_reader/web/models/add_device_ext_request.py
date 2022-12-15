from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddDeviceExtRequest")


@attr.s(auto_attribs=True)
class AddDeviceExtRequest:
    """
    Attributes:
        serial_number (Union[Unset, str]):
        id (Union[Unset, str]):
        name (Union[Unset, str]):
    """

    serial_number: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        serial_number = self.serial_number
        id = self.id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        serial_number = d.pop("serialNumber", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        add_device_ext_request = cls(
            serial_number=serial_number,
            id=id,
            name=name,
        )

        add_device_ext_request.additional_properties = d
        return add_device_ext_request

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
