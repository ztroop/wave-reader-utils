import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.location_simple_response import LocationSimpleResponse
    from ..models.segment_response_labels import SegmentResponseLabels


T = TypeVar("T", bound="SegmentResponse")


@attr.s(auto_attribs=True)
class SegmentResponse:
    """
    Attributes:
        id (str):
        started (datetime.datetime):
        name (str):
        ended (Union[Unset, datetime.datetime]):
        location (Union[Unset, LocationSimpleResponse]):
        device_id (Union[Unset, str]):
        labels (Union[Unset, SegmentResponseLabels]):
    """

    id: str
    started: datetime.datetime
    name: str
    ended: Union[Unset, datetime.datetime] = UNSET
    location: Union[Unset, "LocationSimpleResponse"] = UNSET
    device_id: Union[Unset, str] = UNSET
    labels: Union[Unset, "SegmentResponseLabels"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        started = self.started.isoformat()

        name = self.name
        ended: Union[Unset, str] = UNSET
        if not isinstance(self.ended, Unset):
            ended = self.ended.isoformat()

        location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        device_id = self.device_id
        labels: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "started": started,
                "name": name,
            }
        )
        if ended is not UNSET:
            field_dict["ended"] = ended
        if location is not UNSET:
            field_dict["location"] = location
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.location_simple_response import LocationSimpleResponse
        from ..models.segment_response_labels import SegmentResponseLabels

        d = src_dict.copy()
        id = d.pop("id")

        started = isoparse(d.pop("started"))

        name = d.pop("name")

        _ended = d.pop("ended", UNSET)
        ended: Union[Unset, datetime.datetime]
        if isinstance(_ended, Unset):
            ended = UNSET
        else:
            ended = isoparse(_ended)

        _location = d.pop("location", UNSET)
        location: Union[Unset, LocationSimpleResponse]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = LocationSimpleResponse.from_dict(_location)

        device_id = d.pop("deviceId", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: Union[Unset, SegmentResponseLabels]
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = SegmentResponseLabels.from_dict(_labels)

        segment_response = cls(
            id=id,
            started=started,
            name=name,
            ended=ended,
            location=location,
            device_id=device_id,
            labels=labels,
        )

        segment_response.additional_properties = d
        return segment_response

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
