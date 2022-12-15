from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.location_usage import LocationUsage


T = TypeVar("T", bound="GetLocationResponseUsageHours")


@attr.s(auto_attribs=True)
class GetLocationResponseUsageHours:
    """ """

    additional_properties: Dict[str, "LocationUsage"] = attr.ib(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        pass

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.location_usage import LocationUsage

        d = src_dict.copy()
        get_location_response_usage_hours = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = LocationUsage.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        get_location_response_usage_hours.additional_properties = additional_properties
        return get_location_response_usage_hours

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "LocationUsage":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "LocationUsage") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
