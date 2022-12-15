from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.threshold_breach import ThresholdBreach


T = TypeVar("T", bound="GetThresholdBreachesResponse")


@attr.s(auto_attribs=True)
class GetThresholdBreachesResponse:
    """
    Attributes:
        device_id (Union[Unset, str]):
        breaches (Union[Unset, List['ThresholdBreach']]):
    """

    device_id: Union[Unset, str] = UNSET
    breaches: Union[Unset, List["ThresholdBreach"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        device_id = self.device_id
        breaches: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.breaches, Unset):
            breaches = []
            for breaches_item_data in self.breaches:
                breaches_item = breaches_item_data.to_dict()

                breaches.append(breaches_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if breaches is not UNSET:
            field_dict["breaches"] = breaches

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.threshold_breach import ThresholdBreach

        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        breaches = []
        _breaches = d.pop("breaches", UNSET)
        for breaches_item_data in _breaches or []:
            breaches_item = ThresholdBreach.from_dict(breaches_item_data)

            breaches.append(breaches_item)

        get_threshold_breaches_response = cls(
            device_id=device_id,
            breaches=breaches,
        )

        get_threshold_breaches_response.additional_properties = d
        return get_threshold_breaches_response

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
