from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SampleData")


@attr.s(auto_attribs=True)
class SampleData:
    """
    Attributes:
        co2 (Union[Unset, List[float]]):
        humidity (Union[Unset, List[float]]):
        light (Union[Unset, List[int]]):
        lux (Union[Unset, List[int]]):
        mold (Union[Unset, List[float]]):
        pm1 (Union[Unset, List[float]]):
        pm10 (Union[Unset, List[float]]):
        pm25 (Union[Unset, List[float]]):
        pressure (Union[Unset, List[float]]):
        pressure_difference (Union[Unset, List[float]]):
        radon_short_term_avg (Union[Unset, List[float]]):
        hourly_radon (Union[Unset, List[float]]):
        hourly_radon_std_dev (Union[Unset, List[float]]):
        sla (Union[Unset, List[float]]):
        temp (Union[Unset, List[float]]):
        time (Union[Unset, List[int]]):
        virus_risk (Union[Unset, List[float]]):
        voc (Union[Unset, List[float]]):
        outdoor_temp (Union[Unset, List[float]]):
        outdoor_humidity (Union[Unset, List[float]]):
        outdoor_pressure (Union[Unset, List[float]]):
        outdoor_pm_1 (Union[Unset, List[float]]):
        outdoor_pm_10 (Union[Unset, List[float]]):
        outdoor_pm_25 (Union[Unset, List[float]]):
        outdoor_no_2 (Union[Unset, List[float]]):
        outdoor_o3 (Union[Unset, List[float]]):
        outdoor_so_2 (Union[Unset, List[float]]):
        outdoor_co (Union[Unset, List[float]]):
        outdoor_no (Union[Unset, List[float]]):
        control_signal (Union[Unset, List[float]]):
        control_signal_slot_01 (Union[Unset, List[float]]):
        control_signal_slot_02 (Union[Unset, List[float]]):
        control_signal_slot_03 (Union[Unset, List[float]]):
        control_signal_slot_04 (Union[Unset, List[float]]):
        control_signal_slot_05 (Union[Unset, List[float]]):
        control_signal_slot_06 (Union[Unset, List[float]]):
        control_signal_slot_07 (Union[Unset, List[float]]):
        control_signal_slot_08 (Union[Unset, List[float]]):
        regulation_pressure (Union[Unset, List[float]]):
        regulation_height (Union[Unset, List[float]]):
    """

    co2: Union[Unset, List[float]] = UNSET
    humidity: Union[Unset, List[float]] = UNSET
    light: Union[Unset, List[int]] = UNSET
    lux: Union[Unset, List[int]] = UNSET
    mold: Union[Unset, List[float]] = UNSET
    pm1: Union[Unset, List[float]] = UNSET
    pm10: Union[Unset, List[float]] = UNSET
    pm25: Union[Unset, List[float]] = UNSET
    pressure: Union[Unset, List[float]] = UNSET
    pressure_difference: Union[Unset, List[float]] = UNSET
    radon_short_term_avg: Union[Unset, List[float]] = UNSET
    hourly_radon: Union[Unset, List[float]] = UNSET
    hourly_radon_std_dev: Union[Unset, List[float]] = UNSET
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
    outdoor_no: Union[Unset, List[float]] = UNSET
    control_signal: Union[Unset, List[float]] = UNSET
    control_signal_slot_01: Union[Unset, List[float]] = UNSET
    control_signal_slot_02: Union[Unset, List[float]] = UNSET
    control_signal_slot_03: Union[Unset, List[float]] = UNSET
    control_signal_slot_04: Union[Unset, List[float]] = UNSET
    control_signal_slot_05: Union[Unset, List[float]] = UNSET
    control_signal_slot_06: Union[Unset, List[float]] = UNSET
    control_signal_slot_07: Union[Unset, List[float]] = UNSET
    control_signal_slot_08: Union[Unset, List[float]] = UNSET
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

        lux: Union[Unset, List[int]] = UNSET
        if not isinstance(self.lux, Unset):
            lux = self.lux

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

        pressure_difference: Union[Unset, List[float]] = UNSET
        if not isinstance(self.pressure_difference, Unset):
            pressure_difference = self.pressure_difference

        radon_short_term_avg: Union[Unset, List[float]] = UNSET
        if not isinstance(self.radon_short_term_avg, Unset):
            radon_short_term_avg = self.radon_short_term_avg

        hourly_radon: Union[Unset, List[float]] = UNSET
        if not isinstance(self.hourly_radon, Unset):
            hourly_radon = self.hourly_radon

        hourly_radon_std_dev: Union[Unset, List[float]] = UNSET
        if not isinstance(self.hourly_radon_std_dev, Unset):
            hourly_radon_std_dev = self.hourly_radon_std_dev

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

        outdoor_no: Union[Unset, List[float]] = UNSET
        if not isinstance(self.outdoor_no, Unset):
            outdoor_no = self.outdoor_no

        control_signal: Union[Unset, List[float]] = UNSET
        if not isinstance(self.control_signal, Unset):
            control_signal = self.control_signal

        control_signal_slot_01: Union[Unset, List[float]] = UNSET
        if not isinstance(self.control_signal_slot_01, Unset):
            control_signal_slot_01 = self.control_signal_slot_01

        control_signal_slot_02: Union[Unset, List[float]] = UNSET
        if not isinstance(self.control_signal_slot_02, Unset):
            control_signal_slot_02 = self.control_signal_slot_02

        control_signal_slot_03: Union[Unset, List[float]] = UNSET
        if not isinstance(self.control_signal_slot_03, Unset):
            control_signal_slot_03 = self.control_signal_slot_03

        control_signal_slot_04: Union[Unset, List[float]] = UNSET
        if not isinstance(self.control_signal_slot_04, Unset):
            control_signal_slot_04 = self.control_signal_slot_04

        control_signal_slot_05: Union[Unset, List[float]] = UNSET
        if not isinstance(self.control_signal_slot_05, Unset):
            control_signal_slot_05 = self.control_signal_slot_05

        control_signal_slot_06: Union[Unset, List[float]] = UNSET
        if not isinstance(self.control_signal_slot_06, Unset):
            control_signal_slot_06 = self.control_signal_slot_06

        control_signal_slot_07: Union[Unset, List[float]] = UNSET
        if not isinstance(self.control_signal_slot_07, Unset):
            control_signal_slot_07 = self.control_signal_slot_07

        control_signal_slot_08: Union[Unset, List[float]] = UNSET
        if not isinstance(self.control_signal_slot_08, Unset):
            control_signal_slot_08 = self.control_signal_slot_08

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
        if lux is not UNSET:
            field_dict["lux"] = lux
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
        if pressure_difference is not UNSET:
            field_dict["pressureDifference"] = pressure_difference
        if radon_short_term_avg is not UNSET:
            field_dict["radonShortTermAvg"] = radon_short_term_avg
        if hourly_radon is not UNSET:
            field_dict["hourlyRadon"] = hourly_radon
        if hourly_radon_std_dev is not UNSET:
            field_dict["hourlyRadonStdDev"] = hourly_radon_std_dev
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
        if outdoor_no is not UNSET:
            field_dict["outdoorNo"] = outdoor_no
        if control_signal is not UNSET:
            field_dict["controlSignal"] = control_signal
        if control_signal_slot_01 is not UNSET:
            field_dict["controlSignalSlot01"] = control_signal_slot_01
        if control_signal_slot_02 is not UNSET:
            field_dict["controlSignalSlot02"] = control_signal_slot_02
        if control_signal_slot_03 is not UNSET:
            field_dict["controlSignalSlot03"] = control_signal_slot_03
        if control_signal_slot_04 is not UNSET:
            field_dict["controlSignalSlot04"] = control_signal_slot_04
        if control_signal_slot_05 is not UNSET:
            field_dict["controlSignalSlot05"] = control_signal_slot_05
        if control_signal_slot_06 is not UNSET:
            field_dict["controlSignalSlot06"] = control_signal_slot_06
        if control_signal_slot_07 is not UNSET:
            field_dict["controlSignalSlot07"] = control_signal_slot_07
        if control_signal_slot_08 is not UNSET:
            field_dict["controlSignalSlot08"] = control_signal_slot_08
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

        lux = cast(List[int], d.pop("lux", UNSET))

        mold = cast(List[float], d.pop("mold", UNSET))

        pm1 = cast(List[float], d.pop("pm1", UNSET))

        pm10 = cast(List[float], d.pop("pm10", UNSET))

        pm25 = cast(List[float], d.pop("pm25", UNSET))

        pressure = cast(List[float], d.pop("pressure", UNSET))

        pressure_difference = cast(List[float], d.pop("pressureDifference", UNSET))

        radon_short_term_avg = cast(List[float], d.pop("radonShortTermAvg", UNSET))

        hourly_radon = cast(List[float], d.pop("hourlyRadon", UNSET))

        hourly_radon_std_dev = cast(List[float], d.pop("hourlyRadonStdDev", UNSET))

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

        outdoor_no = cast(List[float], d.pop("outdoorNo", UNSET))

        control_signal = cast(List[float], d.pop("controlSignal", UNSET))

        control_signal_slot_01 = cast(List[float], d.pop("controlSignalSlot01", UNSET))

        control_signal_slot_02 = cast(List[float], d.pop("controlSignalSlot02", UNSET))

        control_signal_slot_03 = cast(List[float], d.pop("controlSignalSlot03", UNSET))

        control_signal_slot_04 = cast(List[float], d.pop("controlSignalSlot04", UNSET))

        control_signal_slot_05 = cast(List[float], d.pop("controlSignalSlot05", UNSET))

        control_signal_slot_06 = cast(List[float], d.pop("controlSignalSlot06", UNSET))

        control_signal_slot_07 = cast(List[float], d.pop("controlSignalSlot07", UNSET))

        control_signal_slot_08 = cast(List[float], d.pop("controlSignalSlot08", UNSET))

        regulation_pressure = cast(List[float], d.pop("regulationPressure", UNSET))

        regulation_height = cast(List[float], d.pop("regulationHeight", UNSET))

        sample_data = cls(
            co2=co2,
            humidity=humidity,
            light=light,
            lux=lux,
            mold=mold,
            pm1=pm1,
            pm10=pm10,
            pm25=pm25,
            pressure=pressure,
            pressure_difference=pressure_difference,
            radon_short_term_avg=radon_short_term_avg,
            hourly_radon=hourly_radon,
            hourly_radon_std_dev=hourly_radon_std_dev,
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
            outdoor_no=outdoor_no,
            control_signal=control_signal,
            control_signal_slot_01=control_signal_slot_01,
            control_signal_slot_02=control_signal_slot_02,
            control_signal_slot_03=control_signal_slot_03,
            control_signal_slot_04=control_signal_slot_04,
            control_signal_slot_05=control_signal_slot_05,
            control_signal_slot_06=control_signal_slot_06,
            control_signal_slot_07=control_signal_slot_07,
            control_signal_slot_08=control_signal_slot_08,
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
