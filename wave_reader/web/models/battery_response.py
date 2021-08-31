from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.battery_response_data import BatteryResponseData
from ..types import UNSET, Unset

T = TypeVar("T", bound="BatteryResponse")


@attr.s(auto_attribs=True)
class BatteryResponse:
    id: str
    data: Union[Unset, BatteryResponseData] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        _data = d.pop("data", UNSET)
        data: Union[Unset, BatteryResponseData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = BatteryResponseData.from_dict(_data)

        battery_response = cls(
            id=id,
            data=data,
        )

        battery_response.additional_properties = d
        return battery_response

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
