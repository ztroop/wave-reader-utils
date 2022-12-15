from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.range_rating import RangeRating
from ..types import UNSET, Unset

T = TypeVar("T", bound="ThresholdRange")


@attr.s(auto_attribs=True)
class ThresholdRange:
    """
    Attributes:
        from_ (Union[Unset, float]):
        to (Union[Unset, float]):
        rating (Union[Unset, RangeRating]):
    """

    from_: Union[Unset, float] = UNSET
    to: Union[Unset, float] = UNSET
    rating: Union[Unset, RangeRating] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_ = self.from_
        to = self.to
        rating: Union[Unset, str] = UNSET
        if not isinstance(self.rating, Unset):
            rating = self.rating.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if rating is not UNSET:
            field_dict["rating"] = rating

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        _rating = d.pop("rating", UNSET)
        rating: Union[Unset, RangeRating]
        if isinstance(_rating, Unset):
            rating = UNSET
        else:
            rating = RangeRating(_rating)

        threshold_range = cls(
            from_=from_,
            to=to,
            rating=rating,
        )

        threshold_range.additional_properties = d
        return threshold_range

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
