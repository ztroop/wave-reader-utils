import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="HookEvent")


@attr.s(auto_attribs=True)
class HookEvent:
    """
    Attributes:
        hook_id (Union[Unset, str]):
        correlation_id (Union[Unset, str]):
        url (Union[Unset, str]):
        content (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        completed_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
        status_code (Union[Unset, int]):
    """

    hook_id: Union[Unset, str] = UNSET
    correlation_id: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    content: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    completed_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    status_code: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hook_id = self.hook_id
        correlation_id = self.correlation_id
        url = self.url
        content = self.content
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        completed_at: Union[Unset, str] = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        status_code = self.status_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hook_id is not UNSET:
            field_dict["hookId"] = hook_id
        if correlation_id is not UNSET:
            field_dict["correlationId"] = correlation_id
        if url is not UNSET:
            field_dict["url"] = url
        if content is not UNSET:
            field_dict["content"] = content
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hook_id = d.pop("hookId", UNSET)

        correlation_id = d.pop("correlationId", UNSET)

        url = d.pop("url", UNSET)

        content = d.pop("content", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _completed_at = d.pop("completedAt", UNSET)
        completed_at: Union[Unset, datetime.datetime]
        if isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = isoparse(_completed_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        status_code = d.pop("statusCode", UNSET)

        hook_event = cls(
            hook_id=hook_id,
            correlation_id=correlation_id,
            url=url,
            content=content,
            created_at=created_at,
            completed_at=completed_at,
            updated_at=updated_at,
            status_code=status_code,
        )

        hook_event.additional_properties = d
        return hook_event

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
