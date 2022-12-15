from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.local_time import LocalTime


T = TypeVar("T", bound="LocationUsage")


@attr.s(auto_attribs=True)
class LocationUsage:
    """
    Attributes:
        closed (Union[Unset, bool]):
        from_ (Union[Unset, LocalTime]):
        to (Union[Unset, LocalTime]):
        nof_minutes_open (Union[Unset, int]):
    """

    closed: Union[Unset, bool] = UNSET
    from_: Union[Unset, "LocalTime"] = UNSET
    to: Union[Unset, "LocalTime"] = UNSET
    nof_minutes_open: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        closed = self.closed
        from_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        to: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()

        nof_minutes_open = self.nof_minutes_open

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if closed is not UNSET:
            field_dict["closed"] = closed
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if nof_minutes_open is not UNSET:
            field_dict["nofMinutesOpen"] = nof_minutes_open

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.local_time import LocalTime

        d = src_dict.copy()
        closed = d.pop("closed", UNSET)

        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, LocalTime]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = LocalTime.from_dict(_from_)

        _to = d.pop("to", UNSET)
        to: Union[Unset, LocalTime]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = LocalTime.from_dict(_to)

        nof_minutes_open = d.pop("nofMinutesOpen", UNSET)

        location_usage = cls(
            closed=closed,
            from_=from_,
            to=to,
            nof_minutes_open=nof_minutes_open,
        )

        location_usage.additional_properties = d
        return location_usage

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
