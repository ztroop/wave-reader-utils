from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.sensor_unit import SensorUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="HookSensorUnits")


@attr.s(auto_attribs=True)
class HookSensorUnits:
    """
    Attributes:
        radon_unit (Union[Unset, SensorUnit]):
        temp_unit (Union[Unset, SensorUnit]):
        pressure_unit (Union[Unset, SensorUnit]):
    """

    radon_unit: Union[Unset, SensorUnit] = UNSET
    temp_unit: Union[Unset, SensorUnit] = UNSET
    pressure_unit: Union[Unset, SensorUnit] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        radon_unit: Union[Unset, str] = UNSET
        if not isinstance(self.radon_unit, Unset):
            radon_unit = self.radon_unit.value

        temp_unit: Union[Unset, str] = UNSET
        if not isinstance(self.temp_unit, Unset):
            temp_unit = self.temp_unit.value

        pressure_unit: Union[Unset, str] = UNSET
        if not isinstance(self.pressure_unit, Unset):
            pressure_unit = self.pressure_unit.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if radon_unit is not UNSET:
            field_dict["radonUnit"] = radon_unit
        if temp_unit is not UNSET:
            field_dict["tempUnit"] = temp_unit
        if pressure_unit is not UNSET:
            field_dict["pressureUnit"] = pressure_unit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _radon_unit = d.pop("radonUnit", UNSET)
        radon_unit: Union[Unset, SensorUnit]
        if isinstance(_radon_unit, Unset):
            radon_unit = UNSET
        else:
            radon_unit = SensorUnit(_radon_unit)

        _temp_unit = d.pop("tempUnit", UNSET)
        temp_unit: Union[Unset, SensorUnit]
        if isinstance(_temp_unit, Unset):
            temp_unit = UNSET
        else:
            temp_unit = SensorUnit(_temp_unit)

        _pressure_unit = d.pop("pressureUnit", UNSET)
        pressure_unit: Union[Unset, SensorUnit]
        if isinstance(_pressure_unit, Unset):
            pressure_unit = UNSET
        else:
            pressure_unit = SensorUnit(_pressure_unit)

        hook_sensor_units = cls(
            radon_unit=radon_unit,
            temp_unit=temp_unit,
            pressure_unit=pressure_unit,
        )

        hook_sensor_units.additional_properties = d
        return hook_sensor_units

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
