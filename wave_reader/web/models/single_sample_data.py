from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SingleSampleData")


@attr.s(auto_attribs=True)
class SingleSampleData:
    """
    Attributes:
        battery (Union[Unset, int]):
        co2 (Union[Unset, float]):
        humidity (Union[Unset, float]):
        light (Union[Unset, int]):
        lux (Union[Unset, int]):
        mold (Union[Unset, float]):
        pm1 (Union[Unset, float]):
        pm10 (Union[Unset, float]):
        pm25 (Union[Unset, float]):
        pressure (Union[Unset, float]):
        pressure_difference (Union[Unset, float]):
        radon_short_term_avg (Union[Unset, float]):
        rssi (Union[Unset, int]):
        sla (Union[Unset, float]):
        temp (Union[Unset, float]):
        time (Union[Unset, int]):
        virus_risk (Union[Unset, float]):
        voc (Union[Unset, float]):
        outdoor_temp (Union[Unset, float]):
        outdoor_humidity (Union[Unset, float]):
        outdoor_pressure (Union[Unset, float]):
        outdoor_pm_10 (Union[Unset, float]):
        outdoor_pm_1 (Union[Unset, float]):
        outdoor_pm_25 (Union[Unset, float]):
        outdoor_no_2 (Union[Unset, float]):
        outdoor_o3 (Union[Unset, float]):
        outdoor_so_2 (Union[Unset, float]):
        outdoor_co (Union[Unset, float]):
        outdoor_no (Union[Unset, float]):
        control_signal (Union[Unset, float]):
        control_signal_slot_01 (Union[Unset, float]):
        control_signal_slot_02 (Union[Unset, float]):
        control_signal_slot_03 (Union[Unset, float]):
        control_signal_slot_04 (Union[Unset, float]):
        control_signal_slot_05 (Union[Unset, float]):
        control_signal_slot_06 (Union[Unset, float]):
        control_signal_slot_07 (Union[Unset, float]):
        control_signal_slot_08 (Union[Unset, float]):
        regulation_pressure (Union[Unset, float]):
        regulation_height (Union[Unset, float]):
        relay_device_type (Union[Unset, str]):
    """

    battery: Union[Unset, int] = UNSET
    co2: Union[Unset, float] = UNSET
    humidity: Union[Unset, float] = UNSET
    light: Union[Unset, int] = UNSET
    lux: Union[Unset, int] = UNSET
    mold: Union[Unset, float] = UNSET
    pm1: Union[Unset, float] = UNSET
    pm10: Union[Unset, float] = UNSET
    pm25: Union[Unset, float] = UNSET
    pressure: Union[Unset, float] = UNSET
    pressure_difference: Union[Unset, float] = UNSET
    radon_short_term_avg: Union[Unset, float] = UNSET
    rssi: Union[Unset, int] = UNSET
    sla: Union[Unset, float] = UNSET
    temp: Union[Unset, float] = UNSET
    time: Union[Unset, int] = UNSET
    virus_risk: Union[Unset, float] = UNSET
    voc: Union[Unset, float] = UNSET
    outdoor_temp: Union[Unset, float] = UNSET
    outdoor_humidity: Union[Unset, float] = UNSET
    outdoor_pressure: Union[Unset, float] = UNSET
    outdoor_pm_10: Union[Unset, float] = UNSET
    outdoor_pm_1: Union[Unset, float] = UNSET
    outdoor_pm_25: Union[Unset, float] = UNSET
    outdoor_no_2: Union[Unset, float] = UNSET
    outdoor_o3: Union[Unset, float] = UNSET
    outdoor_so_2: Union[Unset, float] = UNSET
    outdoor_co: Union[Unset, float] = UNSET
    outdoor_no: Union[Unset, float] = UNSET
    control_signal: Union[Unset, float] = UNSET
    control_signal_slot_01: Union[Unset, float] = UNSET
    control_signal_slot_02: Union[Unset, float] = UNSET
    control_signal_slot_03: Union[Unset, float] = UNSET
    control_signal_slot_04: Union[Unset, float] = UNSET
    control_signal_slot_05: Union[Unset, float] = UNSET
    control_signal_slot_06: Union[Unset, float] = UNSET
    control_signal_slot_07: Union[Unset, float] = UNSET
    control_signal_slot_08: Union[Unset, float] = UNSET
    regulation_pressure: Union[Unset, float] = UNSET
    regulation_height: Union[Unset, float] = UNSET
    relay_device_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        battery = self.battery
        co2 = self.co2
        humidity = self.humidity
        light = self.light
        lux = self.lux
        mold = self.mold
        pm1 = self.pm1
        pm10 = self.pm10
        pm25 = self.pm25
        pressure = self.pressure
        pressure_difference = self.pressure_difference
        radon_short_term_avg = self.radon_short_term_avg
        rssi = self.rssi
        sla = self.sla
        temp = self.temp
        time = self.time
        virus_risk = self.virus_risk
        voc = self.voc
        outdoor_temp = self.outdoor_temp
        outdoor_humidity = self.outdoor_humidity
        outdoor_pressure = self.outdoor_pressure
        outdoor_pm_10 = self.outdoor_pm_10
        outdoor_pm_1 = self.outdoor_pm_1
        outdoor_pm_25 = self.outdoor_pm_25
        outdoor_no_2 = self.outdoor_no_2
        outdoor_o3 = self.outdoor_o3
        outdoor_so_2 = self.outdoor_so_2
        outdoor_co = self.outdoor_co
        outdoor_no = self.outdoor_no
        control_signal = self.control_signal
        control_signal_slot_01 = self.control_signal_slot_01
        control_signal_slot_02 = self.control_signal_slot_02
        control_signal_slot_03 = self.control_signal_slot_03
        control_signal_slot_04 = self.control_signal_slot_04
        control_signal_slot_05 = self.control_signal_slot_05
        control_signal_slot_06 = self.control_signal_slot_06
        control_signal_slot_07 = self.control_signal_slot_07
        control_signal_slot_08 = self.control_signal_slot_08
        regulation_pressure = self.regulation_pressure
        regulation_height = self.regulation_height
        relay_device_type = self.relay_device_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if battery is not UNSET:
            field_dict["battery"] = battery
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
        if rssi is not UNSET:
            field_dict["rssi"] = rssi
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
        if outdoor_pm_10 is not UNSET:
            field_dict["outdoorPm10"] = outdoor_pm_10
        if outdoor_pm_1 is not UNSET:
            field_dict["outdoorPm1"] = outdoor_pm_1
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
        if relay_device_type is not UNSET:
            field_dict["relayDeviceType"] = relay_device_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        battery = d.pop("battery", UNSET)

        co2 = d.pop("co2", UNSET)

        humidity = d.pop("humidity", UNSET)

        light = d.pop("light", UNSET)

        lux = d.pop("lux", UNSET)

        mold = d.pop("mold", UNSET)

        pm1 = d.pop("pm1", UNSET)

        pm10 = d.pop("pm10", UNSET)

        pm25 = d.pop("pm25", UNSET)

        pressure = d.pop("pressure", UNSET)

        pressure_difference = d.pop("pressureDifference", UNSET)

        radon_short_term_avg = d.pop("radonShortTermAvg", UNSET)

        rssi = d.pop("rssi", UNSET)

        sla = d.pop("sla", UNSET)

        temp = d.pop("temp", UNSET)

        time = d.pop("time", UNSET)

        virus_risk = d.pop("virusRisk", UNSET)

        voc = d.pop("voc", UNSET)

        outdoor_temp = d.pop("outdoorTemp", UNSET)

        outdoor_humidity = d.pop("outdoorHumidity", UNSET)

        outdoor_pressure = d.pop("outdoorPressure", UNSET)

        outdoor_pm_10 = d.pop("outdoorPm10", UNSET)

        outdoor_pm_1 = d.pop("outdoorPm1", UNSET)

        outdoor_pm_25 = d.pop("outdoorPm25", UNSET)

        outdoor_no_2 = d.pop("outdoorNo2", UNSET)

        outdoor_o3 = d.pop("outdoorO3", UNSET)

        outdoor_so_2 = d.pop("outdoorSo2", UNSET)

        outdoor_co = d.pop("outdoorCo", UNSET)

        outdoor_no = d.pop("outdoorNo", UNSET)

        control_signal = d.pop("controlSignal", UNSET)

        control_signal_slot_01 = d.pop("controlSignalSlot01", UNSET)

        control_signal_slot_02 = d.pop("controlSignalSlot02", UNSET)

        control_signal_slot_03 = d.pop("controlSignalSlot03", UNSET)

        control_signal_slot_04 = d.pop("controlSignalSlot04", UNSET)

        control_signal_slot_05 = d.pop("controlSignalSlot05", UNSET)

        control_signal_slot_06 = d.pop("controlSignalSlot06", UNSET)

        control_signal_slot_07 = d.pop("controlSignalSlot07", UNSET)

        control_signal_slot_08 = d.pop("controlSignalSlot08", UNSET)

        regulation_pressure = d.pop("regulationPressure", UNSET)

        regulation_height = d.pop("regulationHeight", UNSET)

        relay_device_type = d.pop("relayDeviceType", UNSET)

        single_sample_data = cls(
            battery=battery,
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
            rssi=rssi,
            sla=sla,
            temp=temp,
            time=time,
            virus_risk=virus_risk,
            voc=voc,
            outdoor_temp=outdoor_temp,
            outdoor_humidity=outdoor_humidity,
            outdoor_pressure=outdoor_pressure,
            outdoor_pm_10=outdoor_pm_10,
            outdoor_pm_1=outdoor_pm_1,
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
            relay_device_type=relay_device_type,
        )

        single_sample_data.additional_properties = d
        return single_sample_data

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
