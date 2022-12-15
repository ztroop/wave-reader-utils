import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="SegmentSimpleResponse")


@attr.s(auto_attribs=True)
class SegmentSimpleResponse:
    """
    Attributes:
        id (str):
        name (str):
        started (datetime.datetime):
        active (bool):
    """

    id: str
    name: str
    started: datetime.datetime
    active: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        started = self.started.isoformat()

        active = self.active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "started": started,
                "active": active,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        started = isoparse(d.pop("started"))

        active = d.pop("active")

        segment_simple_response = cls(
            id=id,
            name=name,
            started=started,
            active=active,
        )

        segment_simple_response.additional_properties = d
        return segment_simple_response

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
