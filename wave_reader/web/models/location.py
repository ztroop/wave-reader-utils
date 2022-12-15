from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.location_labels import LocationLabels


T = TypeVar("T", bound="Location")


@attr.s(auto_attribs=True)
class Location:
    """
    Attributes:
        id (str):
        name (str):
        labels (LocationLabels):
    """

    id: str
    name: str
    labels: "LocationLabels"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        labels = self.labels.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "labels": labels,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.location_labels import LocationLabels

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        labels = LocationLabels.from_dict(d.pop("labels"))

        location = cls(
            id=id,
            name=name,
            labels=labels,
        )

        location.additional_properties = d
        return location

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
