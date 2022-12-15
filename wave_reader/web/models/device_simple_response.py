from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.device_type import DeviceType

if TYPE_CHECKING:
    from ..models.segment_simple_response import SegmentSimpleResponse


T = TypeVar("T", bound="DeviceSimpleResponse")


@attr.s(auto_attribs=True)
class DeviceSimpleResponse:
    """
    Attributes:
        id (str):
        device_type (DeviceType):
        segment (SegmentSimpleResponse):
    """

    id: str
    device_type: DeviceType
    segment: "SegmentSimpleResponse"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        device_type = self.device_type.value

        segment = self.segment.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "deviceType": device_type,
                "segment": segment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.segment_simple_response import SegmentSimpleResponse

        d = src_dict.copy()
        id = d.pop("id")

        device_type = DeviceType(d.pop("deviceType"))

        segment = SegmentSimpleResponse.from_dict(d.pop("segment"))

        device_simple_response = cls(
            id=id,
            device_type=device_type,
            segment=segment,
        )

        device_simple_response.additional_properties = d
        return device_simple_response

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
