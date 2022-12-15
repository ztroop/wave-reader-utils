from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_operation import PatchOperation


T = TypeVar("T", bound="PatchRequest")


@attr.s(auto_attribs=True)
class PatchRequest:
    """
    Attributes:
        operations (Union[Unset, List['PatchOperation']]):
    """

    operations: Union[Unset, List["PatchOperation"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.operations, Unset):
            operations = []
            for operations_item_data in self.operations:
                operations_item = operations_item_data.to_dict()

                operations.append(operations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if operations is not UNSET:
            field_dict["operations"] = operations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_operation import PatchOperation

        d = src_dict.copy()
        operations = []
        _operations = d.pop("operations", UNSET)
        for operations_item_data in _operations or []:
            operations_item = PatchOperation.from_dict(operations_item_data)

            operations.append(operations_item)

        patch_request = cls(
            operations=operations,
        )

        patch_request.additional_properties = d
        return patch_request

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
