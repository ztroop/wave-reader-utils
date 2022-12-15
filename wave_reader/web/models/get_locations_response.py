from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.location import Location


T = TypeVar("T", bound="GetLocationsResponse")


@attr.s(auto_attribs=True)
class GetLocationsResponse:
    """
    Attributes:
        locations (List['Location']):
    """

    locations: List["Location"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        locations = []
        for locations_item_data in self.locations:
            locations_item = locations_item_data.to_dict()

            locations.append(locations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "locations": locations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.location import Location

        d = src_dict.copy()
        locations = []
        _locations = d.pop("locations")
        for locations_item_data in _locations:
            locations_item = Location.from_dict(locations_item_data)

            locations.append(locations_item)

        get_locations_response = cls(
            locations=locations,
        )

        get_locations_response.additional_properties = d
        return get_locations_response

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
