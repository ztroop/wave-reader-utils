import datetime
from typing import Any, Dict, List, Type, TypeVar, cast

import attr
from dateutil.parser import isoparse

from ..models.battery_type import BatteryType

T = TypeVar("T", bound="BatteryResponseData")


@attr.s(auto_attribs=True)
class BatteryResponseData:
    """
    Attributes:
        time (List[int]):
        battery_level (List[int]):
        battery_type (BatteryType):
        battery_changed (datetime.datetime):
    """

    time: List[int]
    battery_level: List[int]
    battery_type: BatteryType
    battery_changed: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time = self.time

        battery_level = self.battery_level

        battery_type = self.battery_type.value

        battery_changed = self.battery_changed.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "time": time,
                "batteryLevel": battery_level,
                "batteryType": battery_type,
                "batteryChanged": battery_changed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        time = cast(List[int], d.pop("time"))

        battery_level = cast(List[int], d.pop("batteryLevel"))

        battery_type = BatteryType(d.pop("batteryType"))

        battery_changed = isoparse(d.pop("batteryChanged"))

        battery_response_data = cls(
            time=time,
            battery_level=battery_level,
            battery_type=battery_type,
            battery_changed=battery_changed,
        )

        battery_response_data.additional_properties = d
        return battery_response_data

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
