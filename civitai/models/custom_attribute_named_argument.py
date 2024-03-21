# coding: utf-8

"""
    Civitai Orchestration Consumer API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CustomAttributeNamedArgument(BaseModel):
    """
    CustomAttributeNamedArgument
    """ # noqa: E501
    member_info: Optional[MemberInfo] = Field(default=None, alias="memberInfo")
    typed_value: Optional[CustomAttributeTypedArgument] = Field(default=None, alias="typedValue")
    member_name: Optional[StrictStr] = Field(default=None, alias="memberName")
    is_field: Optional[StrictBool] = Field(default=None, alias="isField")
    __properties: ClassVar[List[str]] = ["memberInfo", "typedValue", "memberName", "isField"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CustomAttributeNamedArgument from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "member_name",
            "is_field",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of member_info
        if self.member_info:
            _dict['memberInfo'] = self.member_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of typed_value
        if self.typed_value:
            _dict['typedValue'] = self.typed_value.to_dict()
        # set to None if member_name (nullable) is None
        # and model_fields_set contains the field
        if self.member_name is None and "member_name" in self.model_fields_set:
            _dict['memberName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CustomAttributeNamedArgument from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "memberInfo": MemberInfo.from_dict(obj["memberInfo"]) if obj.get("memberInfo") is not None else None,
            "typedValue": CustomAttributeTypedArgument.from_dict(obj["typedValue"]) if obj.get("typedValue") is not None else None,
            "memberName": obj.get("memberName"),
            "isField": obj.get("isField")
        })
        return _obj

from civitai.models.custom_attribute_typed_argument import CustomAttributeTypedArgument
from civitai.models.member_info import MemberInfo
# TODO: Rewrite to not use raise_errors
CustomAttributeNamedArgument.model_rebuild(raise_errors=False)

