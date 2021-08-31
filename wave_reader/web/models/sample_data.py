from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SampleData")


@attr.s(auto_attribs=True)
class SampleData:
    co2: Union[Unset, List[float]] = UNSET
    humidity: Union[Unset, List[float]] = UNSET
    light: Union[Unset, List[int]] = UNSET
    mold: Union[Unset, List[float]] = UNSET
    pm1: Union[Unset, List[float]] = UNSET
    pm10: Union[Unset, List[float]] = UNSET
    pm25: Union[Unset, List[float]] = UNSET
    pressure: Union[Unset, List[float]] = UNSET
    radon_short_term_avg: Union[Unset, List[float]] = UNSET
    sla: Union[Unset, List[float]] = UNSET
    temp: Union[Unset, List[float]] = UNSET
    time: Union[Unset, List[int]] = UNSET
    virus_risk: Union[Unset, List[float]] = UNSET
    voc: Union[Unset, List[float]] = UNSET
    outdoor_temp: Union[Unset, List[float]] = UNSET
    outdoor_humidity: Union[Unset, List[float]] = UNSET
    outdoor_pressure: Union[Unset, List[float]] = UNSET
    outdoor_pm_1: Union[Unset, List[float]] = UNSET
    outdoor_pm_10: Union[Unset, List[float]] = UNSET
    outdoor_pm_25: Union[Unset, List[float]] = UNSET
    outdoor_no_2: Union[Unset, List[float]] = UNSET
    outdoor_o3: Union[Unset, List[float]] = UNSET
    outdoor_so_2: Union[Unset, List[float]] = UNSET
    outdoor_co: Union[Unset, List[float]] = UNSET
    control_signal: Union[Unset, List[float]] = UNSET
    regulation_pressure: Union[Unset, List[float]] = UNSET
    regulation_height: Union[Unset, List[float]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        co2: Union[Unset, List[float]] = UNSET
        if not isinstance(self.co2, Unset):
            co2 = self.co2

        humidity: Union[Unset, List[float]] = UNSET
        if not isinstance(self.humidity, Unset):
            humidity = self.humidity

        light: Union[Unset, List[int]] = UNSET
        if not isinstance(self.light, Unset):
            light = self.light

        mold: Union[Unset, List[float]] = UNSET
        if not isinstance(self.mold, Unset):
            mold = self.mold

        pm1: Union[Unset, List[float]] = UNSET
        if not isinstance(self.pm1, Unset):
            pm1 = self.pm1

        pm10: Union[Unset, List[float]] = UNSET
        if not isinstance(self.pm10, Unset):
            pm10 = self.pm10

        pm25: Union[Unset, List[float]] = UNSET
        if not isinstance(self.pm25, Unset):
            pm25 = self.pm25

        pressure: Union[Unset, List[float]] = UNSET
        if not isinstance(self.pressure, Unset):
            pressure = self.pressure

        radon_short_term_avg: Union[Unset, List[float]] = UNSET
        if not isinstance(self.radon_short_term_avg, Unset):
            radon_short_term_avg = self.radon_short_term_avg

        sla: Union[Unset, List[float]] = UNSET
        if not isinstance(self.sla, Unset):
            sla = self.sla

        temp: Union[Unset, List[float]] = UNSET
        if not isinstance(self.temp, Unset):
            temp = self.temp

        time: Union[Unset, List[int]] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time

        virus_risk: Union[Unset, List[float]] = UNSET
        if not isinstance(self.virus_risk, Unset):
            virus_risk = self.virus_risk

        voc: Union[Unset, List[float]] = UNSET
        if not isinstance(self.voc, Unset):
            voc = self.voc

        outdoor_temp: Union[Unset, List[float]] = UNSET
        if not isinstance(self.outdoor_temp, Unset):
            outdoor_temp = self.outdoor_temp

        outdoor_humidity: Union[Unset, List[float]] = UNSET
        if not isinstance(self.outdoor_humidity, Unset):
            outdoor_humidity = self.outdoor_humidity

        outdoor_pressure: Union[Unset, List[float]] = UNSET
        if not isinstance(self.outdoor_pressure, Unset):
            outdoor_pressure = self.outdoor_pressure

        outdoor_pm_1: Union[Unset, List[float]] = UNSET
        if not isinstance(self.outdoor_pm_1, Unset):
            outdoor_pm_1 = self.outdoor_pm_1

        outdoor_pm_10: Union[Unset, List[float]] = UNSET
        if not isinstance(self.outdoor_pm_10, Unset):
            outdoor_pm_10 = self.outdoor_pm_10

        outdoor_pm_25: Union[Unset, List[float]] = UNSET
        if not isinstance(self.outdoor_pm_25, Unset):
            outdoor_pm_25 = self.outdoor_pm_25

        outdoor_no_2: Union[Unset, List[float]] = UNSET
        if not isinstance(self.outdoor_no_2, Unset):
            outdoor_no_2 = self.outdoor_no_2

        outdoor_o3: Union[Unset, List[float]] = UNSET
        if not isinstance(self.outdoor_o3, Unset):
            outdoor_o3 = self.outdoor_o3

        outdoor_so_2: Union[Unset, List[float]] = UNSET
        if not isinstance(self.outdoor_so_2, Unset):
            outdoor_so_2 = self.outdoor_so_2

        outdoor_co: Union[Unset, List[float]] = UNSET
        if not isinstance(self.outdoor_co, Unset):
            outdoor_co = self.outdoor_co

        control_signal: Union[Unset, List[float]] = UNSET
        if not isinstance(self.control_signal, Unset):
            control_signal = self.control_signal

        regulation_pressure: Union[Unset, List[float]] = UNSET
        if not isinstance(self.regulation_pressure, Unset):
            regulation_pressure = self.regulation_pressure

        regulation_height: Union[Unset, List[float]] = UNSET
        if not isinstance(self.regulation_height, Unset):
            regulation_height = self.regulation_height

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if co2 is not UNSET:
            field_dict["co2"] = co2
        if humidity is not UNSET:
            field_dict["humidity"] = humidity
        if light is not UNSET:
            field_dict["light"] = light
        if mold is not UNSET:
            field_dict["mold"] = mold
        if pm1 is not UNSET:
            field_dict["pm1"] = pm1
        if pm10 is not UNSET:
            field_dict["pm10"] = pm10
        if pm25 is not UNSET:
            field_dict["pm25"] = pm25
        if pressure is not UNSET:
            field_dict["pressure"] = pressure
        if radon_short_term_avg is not UNSET:
            field_dict["radonShortTermAvg"] = radon_short_term_avg
        if sla is not UNSET:
            field_dict["sla"] = sla
        if temp is not UNSET:
            field_dict["temp"] = temp
        if time is not UNSET:
            field_dict["time"] = time
        if virus_risk is not UNSET:
            field_dict["virusRisk"] = virus_risk
        if voc is not UNSET:
            field_dict["voc"] = voc
        if outdoor_temp is not UNSET:
            field_dict["outdoorTemp"] = outdoor_temp
        if outdoor_humidity is not UNSET:
            field_dict["outdoorHumidity"] = outdoor_humidity
        if outdoor_pressure is not UNSET:
            field_dict["outdoorPressure"] = outdoor_pressure
        if outdoor_pm_1 is not UNSET:
            field_dict["outdoorPm1"] = outdoor_pm_1
        if outdoor_pm_10 is not UNSET:
            field_dict["outdoorPm10"] = outdoor_pm_10
        if outdoor_pm_25 is not UNSET:
            field_dict["outdoorPm25"] = outdoor_pm_25
        if outdoor_no_2 is not UNSET:
            field_dict["outdoorNo2"] = outdoor_no_2
        if outdoor_o3 is not UNSET:
            field_dict["outdoorO3"] = outdoor_o3
        if outdoor_so_2 is not UNSET:
            field_dict["outdoorSo2"] = outdoor_so_2
        if outdoor_co is not UNSET:
            field_dict["outdoorCo"] = outdoor_co
        if control_signal is not UNSET:
            field_dict["controlSignal"] = control_signal
        if regulation_pressure is not UNSET:
            field_dict["regulationPressure"] = regulation_pressure
        if regulation_height is not UNSET:
            field_dict["regulationHeight"] = regulation_height

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        co2 = cast(List[float], d.pop("co2", UNSET))

        humidity = cast(List[float], d.pop("humidity", UNSET))

        light = cast(List[int], d.pop("light", UNSET))

        mold = cast(List[float], d.pop("mold", UNSET))

        pm1 = cast(List[float], d.pop("pm1", UNSET))

        pm10 = cast(List[float], d.pop("pm10", UNSET))

        pm25 = cast(List[float], d.pop("pm25", UNSET))

        pressure = cast(List[float], d.pop("pressure", UNSET))

        radon_short_term_avg = cast(List[float], d.pop("radonShortTermAvg", UNSET))

        sla = cast(List[float], d.pop("sla", UNSET))

        temp = cast(List[float], d.pop("temp", UNSET))

        time = cast(List[int], d.pop("time", UNSET))

        virus_risk = cast(List[float], d.pop("virusRisk", UNSET))

        voc = cast(List[float], d.pop("voc", UNSET))

        outdoor_temp = cast(List[float], d.pop("outdoorTemp", UNSET))

        outdoor_humidity = cast(List[float], d.pop("outdoorHumidity", UNSET))

        outdoor_pressure = cast(List[float], d.pop("outdoorPressure", UNSET))

        outdoor_pm_1 = cast(List[float], d.pop("outdoorPm1", UNSET))

        outdoor_pm_10 = cast(List[float], d.pop("outdoorPm10", UNSET))

        outdoor_pm_25 = cast(List[float], d.pop("outdoorPm25", UNSET))

        outdoor_no_2 = cast(List[float], d.pop("outdoorNo2", UNSET))

        outdoor_o3 = cast(List[float], d.pop("outdoorO3", UNSET))

        outdoor_so_2 = cast(List[float], d.pop("outdoorSo2", UNSET))

        outdoor_co = cast(List[float], d.pop("outdoorCo", UNSET))

        control_signal = cast(List[float], d.pop("controlSignal", UNSET))

        regulation_pressure = cast(List[float], d.pop("regulationPressure", UNSET))

        regulation_height = cast(List[float], d.pop("regulationHeight", UNSET))

        sample_data = cls(
            co2=co2,
            humidity=humidity,
            light=light,
            mold=mold,
            pm1=pm1,
            pm10=pm10,
            pm25=pm25,
            pressure=pressure,
            radon_short_term_avg=radon_short_term_avg,
            sla=sla,
            temp=temp,
            time=time,
            virus_risk=virus_risk,
            voc=voc,
            outdoor_temp=outdoor_temp,
            outdoor_humidity=outdoor_humidity,
            outdoor_pressure=outdoor_pressure,
            outdoor_pm_1=outdoor_pm_1,
            outdoor_pm_10=outdoor_pm_10,
            outdoor_pm_25=outdoor_pm_25,
            outdoor_no_2=outdoor_no_2,
            outdoor_o3=outdoor_o3,
            outdoor_so_2=outdoor_so_2,
            outdoor_co=outdoor_co,
            control_signal=control_signal,
            regulation_pressure=regulation_pressure,
            regulation_height=regulation_height,
        )

        sample_data.additional_properties = d
        return sample_data

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
