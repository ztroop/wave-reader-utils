from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.sensor_type import SensorType
from ..models.sensor_unit import SensorUnit
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.threshold_range import ThresholdRange


T = TypeVar("T", bound="SensorThreshold")


@attr.s(auto_attribs=True)
class SensorThreshold:
    """
    Attributes:
        type (Union[Unset, SensorType]):
        unit (Union[Unset, SensorUnit]):
        ranges (Union[Unset, List['ThresholdRange']]):
    """

    type: Union[Unset, SensorType] = UNSET
    unit: Union[Unset, SensorUnit] = UNSET
    ranges: Union[Unset, List["ThresholdRange"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        unit: Union[Unset, str] = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value

        ranges: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ranges, Unset):
            ranges = []
            for ranges_item_data in self.ranges:
                ranges_item = ranges_item_data.to_dict()

                ranges.append(ranges_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if unit is not UNSET:
            field_dict["unit"] = unit
        if ranges is not UNSET:
            field_dict["ranges"] = ranges

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.threshold_range import ThresholdRange

        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, SensorType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = SensorType(_type)

        _unit = d.pop("unit", UNSET)
        unit: Union[Unset, SensorUnit]
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = SensorUnit(_unit)

        ranges = []
        _ranges = d.pop("ranges", UNSET)
        for ranges_item_data in _ranges or []:
            ranges_item = ThresholdRange.from_dict(ranges_item_data)

            ranges.append(ranges_item)

        sensor_threshold = cls(
            type=type,
            unit=unit,
            ranges=ranges,
        )

        sensor_threshold.additional_properties = d
        return sensor_threshold

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
