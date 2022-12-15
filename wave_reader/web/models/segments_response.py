from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.segment_response import SegmentResponse


T = TypeVar("T", bound="SegmentsResponse")


@attr.s(auto_attribs=True)
class SegmentsResponse:
    """
    Attributes:
        segments (List['SegmentResponse']):
    """

    segments: List["SegmentResponse"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        segments = []
        for segments_item_data in self.segments:
            segments_item = segments_item_data.to_dict()

            segments.append(segments_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "segments": segments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.segment_response import SegmentResponse

        d = src_dict.copy()
        segments = []
        _segments = d.pop("segments")
        for segments_item_data in _segments:
            segments_item = SegmentResponse.from_dict(segments_item_data)

            segments.append(segments_item)

        segments_response = cls(
            segments=segments,
        )

        segments_response.additional_properties = d
        return segments_response

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
