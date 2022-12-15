import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.sensor_type import SensorType
from ..models.sensor_unit import SensorUnit
from ..models.threshold_level import ThresholdLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="ThresholdBreach")


@attr.s(auto_attribs=True)
class ThresholdBreach:
    """
    Attributes:
        sensor_type (Union[Unset, SensorType]):
        threshold_level (Union[Unset, ThresholdLevel]):
        sensor_value (Union[Unset, float]):
        sensor_unit (Union[Unset, SensorUnit]):
        recorded (Union[Unset, datetime.datetime]):
    """

    sensor_type: Union[Unset, SensorType] = UNSET
    threshold_level: Union[Unset, ThresholdLevel] = UNSET
    sensor_value: Union[Unset, float] = UNSET
    sensor_unit: Union[Unset, SensorUnit] = UNSET
    recorded: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sensor_type: Union[Unset, str] = UNSET
        if not isinstance(self.sensor_type, Unset):
            sensor_type = self.sensor_type.value

        threshold_level: Union[Unset, str] = UNSET
        if not isinstance(self.threshold_level, Unset):
            threshold_level = self.threshold_level.value

        sensor_value = self.sensor_value
        sensor_unit: Union[Unset, str] = UNSET
        if not isinstance(self.sensor_unit, Unset):
            sensor_unit = self.sensor_unit.value

        recorded: Union[Unset, str] = UNSET
        if not isinstance(self.recorded, Unset):
            recorded = self.recorded.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sensor_type is not UNSET:
            field_dict["sensorType"] = sensor_type
        if threshold_level is not UNSET:
            field_dict["thresholdLevel"] = threshold_level
        if sensor_value is not UNSET:
            field_dict["sensorValue"] = sensor_value
        if sensor_unit is not UNSET:
            field_dict["sensorUnit"] = sensor_unit
        if recorded is not UNSET:
            field_dict["recorded"] = recorded

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _sensor_type = d.pop("sensorType", UNSET)
        sensor_type: Union[Unset, SensorType]
        if isinstance(_sensor_type, Unset):
            sensor_type = UNSET
        else:
            sensor_type = SensorType(_sensor_type)

        _threshold_level = d.pop("thresholdLevel", UNSET)
        threshold_level: Union[Unset, ThresholdLevel]
        if isinstance(_threshold_level, Unset):
            threshold_level = UNSET
        else:
            threshold_level = ThresholdLevel(_threshold_level)

        sensor_value = d.pop("sensorValue", UNSET)

        _sensor_unit = d.pop("sensorUnit", UNSET)
        sensor_unit: Union[Unset, SensorUnit]
        if isinstance(_sensor_unit, Unset):
            sensor_unit = UNSET
        else:
            sensor_unit = SensorUnit(_sensor_unit)

        _recorded = d.pop("recorded", UNSET)
        recorded: Union[Unset, datetime.datetime]
        if isinstance(_recorded, Unset):
            recorded = UNSET
        else:
            recorded = isoparse(_recorded)

        threshold_breach = cls(
            sensor_type=sensor_type,
            threshold_level=threshold_level,
            sensor_value=sensor_value,
            sensor_unit=sensor_unit,
            recorded=recorded,
        )

        threshold_breach.additional_properties = d
        return threshold_breach

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
