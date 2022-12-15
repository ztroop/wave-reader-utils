from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.single_battery_response_data import SingleBatteryResponseData


T = TypeVar("T", bound="SingleBatteryResponse")


@attr.s(auto_attribs=True)
class SingleBatteryResponse:
    """
    Attributes:
        id (str):
        data (Union[Unset, SingleBatteryResponseData]):
    """

    id: str
    data: Union[Unset, "SingleBatteryResponseData"] = UNSET
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
        from ..models.single_battery_response_data import (
            SingleBatteryResponseData,
        )

        d = src_dict.copy()
        id = d.pop("id")

        _data = d.pop("data", UNSET)
        data: Union[Unset, SingleBatteryResponseData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = SingleBatteryResponseData.from_dict(_data)

        single_battery_response = cls(
            id=id,
            data=data,
        )

        single_battery_response.additional_properties = d
        return single_battery_response

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
