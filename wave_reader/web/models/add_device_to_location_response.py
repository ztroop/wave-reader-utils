from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="AddDeviceToLocationResponse")


@attr.s(auto_attribs=True)
class AddDeviceToLocationResponse:
    """
    Attributes:
        serial_number (str):
        name (str):
        location_id (str):
    """

    serial_number: str
    name: str
    location_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        serial_number = self.serial_number
        name = self.name
        location_id = self.location_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serialNumber": serial_number,
                "name": name,
                "locationId": location_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        serial_number = d.pop("serialNumber")

        name = d.pop("name")

        location_id = d.pop("locationId")

        add_device_to_location_response = cls(
            serial_number=serial_number,
            name=name,
            location_id=location_id,
        )

        add_device_to_location_response.additional_properties = d
        return add_device_to_location_response

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
