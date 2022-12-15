from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.add_location_request_building_type import (
    AddLocationRequestBuildingType,
)
from ..models.add_location_request_ventilation_type import (
    AddLocationRequestVentilationType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_location_request_usage_hours import (
        AddLocationRequestUsageHours,
    )


T = TypeVar("T", bound="AddLocationRequest")


@attr.s(auto_attribs=True)
class AddLocationRequest:
    """
    Attributes:
        name (str):
        lat (float):
        lng (float):
        address (Union[Unset, str]):
        building_type (Union[Unset, AddLocationRequestBuildingType]):
        ventilation_type (Union[Unset, AddLocationRequestVentilationType]):
        floors (Union[Unset, int]):
        timezone (Union[Unset, str]):  Example: Europe/Oslo.
        building_year (Union[Unset, int]):
        usage_hours (Union[Unset, AddLocationRequestUsageHours]):
            Object key must be a day of week (`MONDAY`, `TUESDAY`,
            `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, `SUNDAY`)
        building_height (Union[Unset, float]): In meter(m)
        building_size (Union[Unset, float]): In square meter(m²)
        building_volume (Union[Unset, float]): In cubic meter(m³)
    """

    name: str
    lat: float
    lng: float
    address: Union[Unset, str] = UNSET
    building_type: Union[Unset, AddLocationRequestBuildingType] = UNSET
    ventilation_type: Union[Unset, AddLocationRequestVentilationType] = UNSET
    floors: Union[Unset, int] = UNSET
    timezone: Union[Unset, str] = UNSET
    building_year: Union[Unset, int] = UNSET
    usage_hours: Union[Unset, "AddLocationRequestUsageHours"] = UNSET
    building_height: Union[Unset, float] = UNSET
    building_size: Union[Unset, float] = UNSET
    building_volume: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        lat = self.lat
        lng = self.lng
        address = self.address
        building_type: Union[Unset, str] = UNSET
        if not isinstance(self.building_type, Unset):
            building_type = self.building_type.value

        ventilation_type: Union[Unset, str] = UNSET
        if not isinstance(self.ventilation_type, Unset):
            ventilation_type = self.ventilation_type.value

        floors = self.floors
        timezone = self.timezone
        building_year = self.building_year
        usage_hours: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.usage_hours, Unset):
            usage_hours = self.usage_hours.to_dict()

        building_height = self.building_height
        building_size = self.building_size
        building_volume = self.building_volume

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "lat": lat,
                "lng": lng,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if building_type is not UNSET:
            field_dict["buildingType"] = building_type
        if ventilation_type is not UNSET:
            field_dict["ventilationType"] = ventilation_type
        if floors is not UNSET:
            field_dict["floors"] = floors
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if building_year is not UNSET:
            field_dict["buildingYear"] = building_year
        if usage_hours is not UNSET:
            field_dict["usageHours"] = usage_hours
        if building_height is not UNSET:
            field_dict["buildingHeight"] = building_height
        if building_size is not UNSET:
            field_dict["buildingSize"] = building_size
        if building_volume is not UNSET:
            field_dict["buildingVolume"] = building_volume

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.add_location_request_usage_hours import (
            AddLocationRequestUsageHours,
        )

        d = src_dict.copy()
        name = d.pop("name")

        lat = d.pop("lat")

        lng = d.pop("lng")

        address = d.pop("address", UNSET)

        _building_type = d.pop("buildingType", UNSET)
        building_type: Union[Unset, AddLocationRequestBuildingType]
        if isinstance(_building_type, Unset):
            building_type = UNSET
        else:
            building_type = AddLocationRequestBuildingType(_building_type)

        _ventilation_type = d.pop("ventilationType", UNSET)
        ventilation_type: Union[Unset, AddLocationRequestVentilationType]
        if isinstance(_ventilation_type, Unset):
            ventilation_type = UNSET
        else:
            ventilation_type = AddLocationRequestVentilationType(_ventilation_type)

        floors = d.pop("floors", UNSET)

        timezone = d.pop("timezone", UNSET)

        building_year = d.pop("buildingYear", UNSET)

        _usage_hours = d.pop("usageHours", UNSET)
        usage_hours: Union[Unset, AddLocationRequestUsageHours]
        if isinstance(_usage_hours, Unset):
            usage_hours = UNSET
        else:
            usage_hours = AddLocationRequestUsageHours.from_dict(_usage_hours)

        building_height = d.pop("buildingHeight", UNSET)

        building_size = d.pop("buildingSize", UNSET)

        building_volume = d.pop("buildingVolume", UNSET)

        add_location_request = cls(
            name=name,
            lat=lat,
            lng=lng,
            address=address,
            building_type=building_type,
            ventilation_type=ventilation_type,
            floors=floors,
            timezone=timezone,
            building_year=building_year,
            usage_hours=usage_hours,
            building_height=building_height,
            building_size=building_size,
            building_volume=building_volume,
        )

        add_location_request.additional_properties = d
        return add_location_request

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
