from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.segment_simple_response import SegmentSimpleResponse
    from ..models.single_sample_data import SingleSampleData


T = TypeVar("T", bound="DeviceSampleResponse")


@attr.s(auto_attribs=True)
class DeviceSampleResponse:
    """
    Attributes:
        id (str):
        data (SingleSampleData):
        segment (SegmentSimpleResponse):
    """

    id: str
    data: "SingleSampleData"
    segment: "SegmentSimpleResponse"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        data = self.data.to_dict()

        segment = self.segment.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "data": data,
                "segment": segment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.segment_simple_response import SegmentSimpleResponse
        from ..models.single_sample_data import SingleSampleData

        d = src_dict.copy()
        id = d.pop("id")

        data = SingleSampleData.from_dict(d.pop("data"))

        segment = SegmentSimpleResponse.from_dict(d.pop("segment"))

        device_sample_response = cls(
            id=id,
            data=data,
            segment=segment,
        )

        device_sample_response.additional_properties = d
        return device_sample_response

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
