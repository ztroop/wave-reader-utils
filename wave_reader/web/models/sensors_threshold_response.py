from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sensors_threshold_response_thresholds import (
        SensorsThresholdResponseThresholds,
    )


T = TypeVar("T", bound="SensorsThresholdResponse")


@attr.s(auto_attribs=True)
class SensorsThresholdResponse:
    """
    Attributes:
        thresholds (Union[Unset, SensorsThresholdResponseThresholds]):
    """

    thresholds: Union[Unset, "SensorsThresholdResponseThresholds"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        thresholds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.thresholds, Unset):
            thresholds = self.thresholds.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if thresholds is not UNSET:
            field_dict["thresholds"] = thresholds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sensors_threshold_response_thresholds import (
            SensorsThresholdResponseThresholds,
        )

        d = src_dict.copy()
        _thresholds = d.pop("thresholds", UNSET)
        thresholds: Union[Unset, SensorsThresholdResponseThresholds]
        if isinstance(_thresholds, Unset):
            thresholds = UNSET
        else:
            thresholds = SensorsThresholdResponseThresholds.from_dict(_thresholds)

        sensors_threshold_response = cls(
            thresholds=thresholds,
        )

        sensors_threshold_response.additional_properties = d
        return sensors_threshold_response

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
