from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_location_response_building_type import (
    GetLocationResponseBuildingType,
)
from ..models.get_location_response_ventilation_type import (
    GetLocationResponseVentilationType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_simple_response import DeviceSimpleResponse
    from ..models.get_location_response_labels import GetLocationResponseLabels
    from ..models.get_location_response_usage_hours import (
        GetLocationResponseUsageHours,
    )


T = TypeVar("T", bound="GetLocationResponse")


@attr.s(auto_attribs=True)
class GetLocationResponse:
    """
    Attributes:
        id (str):
        name (str):
        labels (GetLocationResponseLabels):
        devices (List['DeviceSimpleResponse']):
        lat (float):
        lng (float):
        address (Union[Unset, str]):
        country_code (Union[Unset, str]):
        building_type (Union[Unset, GetLocationResponseBuildingType]):
        building_year (Union[Unset, int]):
        ventilation_type (Union[Unset, GetLocationResponseVentilationType]):
        timezone (Union[Unset, str]):
        usage_hours (Union[Unset, GetLocationResponseUsageHours]):
        building_height (Union[Unset, float]):
        building_size (Union[Unset, float]):
        building_volume (Union[Unset, float]):
        floors (Union[Unset, int]):
    """

    id: str
    name: str
    labels: "GetLocationResponseLabels"
    devices: List["DeviceSimpleResponse"]
    lat: float
    lng: float
    address: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    building_type: Union[Unset, GetLocationResponseBuildingType] = UNSET
    building_year: Union[Unset, int] = UNSET
    ventilation_type: Union[Unset, GetLocationResponseVentilationType] = UNSET
    timezone: Union[Unset, str] = UNSET
    usage_hours: Union[Unset, "GetLocationResponseUsageHours"] = UNSET
    building_height: Union[Unset, float] = UNSET
    building_size: Union[Unset, float] = UNSET
    building_volume: Union[Unset, float] = UNSET
    floors: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        labels = self.labels.to_dict()

        devices = []
        for devices_item_data in self.devices:
            devices_item = devices_item_data.to_dict()

            devices.append(devices_item)

        lat = self.lat
        lng = self.lng
        address = self.address
        country_code = self.country_code
        building_type: Union[Unset, str] = UNSET
        if not isinstance(self.building_type, Unset):
            building_type = self.building_type.value

        building_year = self.building_year
        ventilation_type: Union[Unset, str] = UNSET
        if not isinstance(self.ventilation_type, Unset):
            ventilation_type = self.ventilation_type.value

        timezone = self.timezone
        usage_hours: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.usage_hours, Unset):
            usage_hours = self.usage_hours.to_dict()

        building_height = self.building_height
        building_size = self.building_size
        building_volume = self.building_volume
        floors = self.floors

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "labels": labels,
                "devices": devices,
                "lat": lat,
                "lng": lng,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if building_type is not UNSET:
            field_dict["buildingType"] = building_type
        if building_year is not UNSET:
            field_dict["buildingYear"] = building_year
        if ventilation_type is not UNSET:
            field_dict["ventilationType"] = ventilation_type
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if usage_hours is not UNSET:
            field_dict["usageHours"] = usage_hours
        if building_height is not UNSET:
            field_dict["buildingHeight"] = building_height
        if building_size is not UNSET:
            field_dict["buildingSize"] = building_size
        if building_volume is not UNSET:
            field_dict["buildingVolume"] = building_volume
        if floors is not UNSET:
            field_dict["floors"] = floors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_simple_response import DeviceSimpleResponse
        from ..models.get_location_response_labels import (
            GetLocationResponseLabels,
        )
        from ..models.get_location_response_usage_hours import (
            GetLocationResponseUsageHours,
        )

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        labels = GetLocationResponseLabels.from_dict(d.pop("labels"))

        devices = []
        _devices = d.pop("devices")
        for devices_item_data in _devices:
            devices_item = DeviceSimpleResponse.from_dict(devices_item_data)

            devices.append(devices_item)

        lat = d.pop("lat")

        lng = d.pop("lng")

        address = d.pop("address", UNSET)

        country_code = d.pop("countryCode", UNSET)

        _building_type = d.pop("buildingType", UNSET)
        building_type: Union[Unset, GetLocationResponseBuildingType]
        if isinstance(_building_type, Unset):
            building_type = UNSET
        else:
            building_type = GetLocationResponseBuildingType(_building_type)

        building_year = d.pop("buildingYear", UNSET)

        _ventilation_type = d.pop("ventilationType", UNSET)
        ventilation_type: Union[Unset, GetLocationResponseVentilationType]
        if isinstance(_ventilation_type, Unset):
            ventilation_type = UNSET
        else:
            ventilation_type = GetLocationResponseVentilationType(_ventilation_type)

        timezone = d.pop("timezone", UNSET)

        _usage_hours = d.pop("usageHours", UNSET)
        usage_hours: Union[Unset, GetLocationResponseUsageHours]
        if isinstance(_usage_hours, Unset):
            usage_hours = UNSET
        else:
            usage_hours = GetLocationResponseUsageHours.from_dict(_usage_hours)

        building_height = d.pop("buildingHeight", UNSET)

        building_size = d.pop("buildingSize", UNSET)

        building_volume = d.pop("buildingVolume", UNSET)

        floors = d.pop("floors", UNSET)

        get_location_response = cls(
            id=id,
            name=name,
            labels=labels,
            devices=devices,
            lat=lat,
            lng=lng,
            address=address,
            country_code=country_code,
            building_type=building_type,
            building_year=building_year,
            ventilation_type=ventilation_type,
            timezone=timezone,
            usage_hours=usage_hours,
            building_height=building_height,
            building_size=building_size,
            building_volume=building_volume,
            floors=floors,
        )

        get_location_response.additional_properties = d
        return get_location_response

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
