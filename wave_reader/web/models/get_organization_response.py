from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="GetOrganizationResponse")


@attr.s(auto_attribs=True)
class GetOrganizationResponse:
    """
    Attributes:
        id (str):
        name (str):
        user_group_id (str):
    """

    id: str
    name: str
    user_group_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        user_group_id = self.user_group_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "userGroupId": user_group_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        user_group_id = d.pop("userGroupId")

        get_organization_response = cls(
            id=id,
            name=name,
            user_group_id=user_group_id,
        )

        get_organization_response.additional_properties = d
        return get_organization_response

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
