from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.patch_operation_op import PatchOperationOp
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_operation_value import PatchOperationValue


T = TypeVar("T", bound="PatchOperation")


@attr.s(auto_attribs=True)
class PatchOperation:
    """
    Attributes:
        op (PatchOperationOp): Operation to perform on webhook locations
        path (str): The field to be edited (eg. `locations` for editing webhook locations)
        value (Union[Unset, PatchOperationValue]): The value to apply to path, value type depends on path
    """

    op: PatchOperationOp
    path: str
    value: Union[Unset, "PatchOperationValue"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        op = self.op.value

        path = self.path
        value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "op": op,
                "path": path,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_operation_value import PatchOperationValue

        d = src_dict.copy()
        op = PatchOperationOp(d.pop("op"))

        path = d.pop("path")

        _value = d.pop("value", UNSET)
        value: Union[Unset, PatchOperationValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = PatchOperationValue.from_dict(_value)

        patch_operation = cls(
            op=op,
            path=path,
            value=value,
        )

        patch_operation.additional_properties = d
        return patch_operation

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
