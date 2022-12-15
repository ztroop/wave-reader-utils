import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.measurement_system import MeasurementSystem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sample_data import SampleData


T = TypeVar("T", bound="SamplesResponse")


@attr.s(auto_attribs=True)
class SamplesResponse:
    """
    Attributes:
        data (Union[Unset, SampleData]):
        start (Union[Unset, datetime.datetime]):
        end (Union[Unset, datetime.datetime]):
        measurement_system (Union[Unset, MeasurementSystem]):
        cursor (Union[Unset, str]):
    """

    data: Union[Unset, "SampleData"] = UNSET
    start: Union[Unset, datetime.datetime] = UNSET
    end: Union[Unset, datetime.datetime] = UNSET
    measurement_system: Union[Unset, MeasurementSystem] = UNSET
    cursor: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        start: Union[Unset, str] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        end: Union[Unset, str] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        measurement_system: Union[Unset, str] = UNSET
        if not isinstance(self.measurement_system, Unset):
            measurement_system = self.measurement_system.value

        cursor = self.cursor

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if measurement_system is not UNSET:
            field_dict["measurementSystem"] = measurement_system
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sample_data import SampleData

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, SampleData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = SampleData.from_dict(_data)

        _start = d.pop("start", UNSET)
        start: Union[Unset, datetime.datetime]
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = isoparse(_start)

        _end = d.pop("end", UNSET)
        end: Union[Unset, datetime.datetime]
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = isoparse(_end)

        _measurement_system = d.pop("measurementSystem", UNSET)
        measurement_system: Union[Unset, MeasurementSystem]
        if isinstance(_measurement_system, Unset):
            measurement_system = UNSET
        else:
            measurement_system = MeasurementSystem(_measurement_system)

        cursor = d.pop("cursor", UNSET)

        samples_response = cls(
            data=data,
            start=start,
            end=end,
            measurement_system=measurement_system,
            cursor=cursor,
        )

        samples_response.additional_properties = d
        return samples_response

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
