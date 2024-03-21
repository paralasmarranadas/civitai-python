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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from civitai.models.calling_conventions import CallingConventions
from civitai.models.member_types import MemberTypes
from civitai.models.method_attributes import MethodAttributes
from civitai.models.method_impl_attributes import MethodImplAttributes
from civitai.models.runtime_method_handle import RuntimeMethodHandle
from typing import Optional, Set
from typing_extensions import Self

class MethodBase(BaseModel):
    """
    MethodBase
    """ # noqa: E501
    member_type: Optional[MemberTypes] = Field(default=None, alias="memberType")
    name: Optional[StrictStr] = None
    declaring_type: Optional[Type] = Field(default=None, alias="declaringType")
    reflected_type: Optional[Type] = Field(default=None, alias="reflectedType")
    module: Optional[Module] = None
    custom_attributes: Optional[List[CustomAttributeData]] = Field(default=None, alias="customAttributes")
    is_collectible: Optional[StrictBool] = Field(default=None, alias="isCollectible")
    metadata_token: Optional[StrictInt] = Field(default=None, alias="metadataToken")
    attributes: Optional[MethodAttributes] = None
    method_implementation_flags: Optional[MethodImplAttributes] = Field(default=None, alias="methodImplementationFlags")
    calling_convention: Optional[CallingConventions] = Field(default=None, alias="callingConvention")
    is_abstract: Optional[StrictBool] = Field(default=None, alias="isAbstract")
    is_constructor: Optional[StrictBool] = Field(default=None, alias="isConstructor")
    is_final: Optional[StrictBool] = Field(default=None, alias="isFinal")
    is_hide_by_sig: Optional[StrictBool] = Field(default=None, alias="isHideBySig")
    is_special_name: Optional[StrictBool] = Field(default=None, alias="isSpecialName")
    is_static: Optional[StrictBool] = Field(default=None, alias="isStatic")
    is_virtual: Optional[StrictBool] = Field(default=None, alias="isVirtual")
    is_assembly: Optional[StrictBool] = Field(default=None, alias="isAssembly")
    is_family: Optional[StrictBool] = Field(default=None, alias="isFamily")
    is_family_and_assembly: Optional[StrictBool] = Field(default=None, alias="isFamilyAndAssembly")
    is_family_or_assembly: Optional[StrictBool] = Field(default=None, alias="isFamilyOrAssembly")
    is_private: Optional[StrictBool] = Field(default=None, alias="isPrivate")
    is_public: Optional[StrictBool] = Field(default=None, alias="isPublic")
    is_constructed_generic_method: Optional[StrictBool] = Field(default=None, alias="isConstructedGenericMethod")
    is_generic_method: Optional[StrictBool] = Field(default=None, alias="isGenericMethod")
    is_generic_method_definition: Optional[StrictBool] = Field(default=None, alias="isGenericMethodDefinition")
    contains_generic_parameters: Optional[StrictBool] = Field(default=None, alias="containsGenericParameters")
    method_handle: Optional[RuntimeMethodHandle] = Field(default=None, alias="methodHandle")
    is_security_critical: Optional[StrictBool] = Field(default=None, alias="isSecurityCritical")
    is_security_safe_critical: Optional[StrictBool] = Field(default=None, alias="isSecuritySafeCritical")
    is_security_transparent: Optional[StrictBool] = Field(default=None, alias="isSecurityTransparent")
    __properties: ClassVar[List[str]] = ["memberType", "name", "declaringType", "reflectedType", "module", "customAttributes", "isCollectible", "metadataToken", "attributes", "methodImplementationFlags", "callingConvention", "isAbstract", "isConstructor", "isFinal", "isHideBySig", "isSpecialName", "isStatic", "isVirtual", "isAssembly", "isFamily", "isFamilyAndAssembly", "isFamilyOrAssembly", "isPrivate", "isPublic", "isConstructedGenericMethod", "isGenericMethod", "isGenericMethodDefinition", "containsGenericParameters", "methodHandle", "isSecurityCritical", "isSecuritySafeCritical", "isSecurityTransparent"]

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
        """Create an instance of MethodBase from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "name",
            "custom_attributes",
            "is_collectible",
            "metadata_token",
            "is_abstract",
            "is_constructor",
            "is_final",
            "is_hide_by_sig",
            "is_special_name",
            "is_static",
            "is_virtual",
            "is_assembly",
            "is_family",
            "is_family_and_assembly",
            "is_family_or_assembly",
            "is_private",
            "is_public",
            "is_constructed_generic_method",
            "is_generic_method",
            "is_generic_method_definition",
            "contains_generic_parameters",
            "is_security_critical",
            "is_security_safe_critical",
            "is_security_transparent",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of declaring_type
        if self.declaring_type:
            _dict['declaringType'] = self.declaring_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reflected_type
        if self.reflected_type:
            _dict['reflectedType'] = self.reflected_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of module
        if self.module:
            _dict['module'] = self.module.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in custom_attributes (list)
        _items = []
        if self.custom_attributes:
            for _item in self.custom_attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['customAttributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of method_handle
        if self.method_handle:
            _dict['methodHandle'] = self.method_handle.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if custom_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.custom_attributes is None and "custom_attributes" in self.model_fields_set:
            _dict['customAttributes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MethodBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "memberType": obj.get("memberType"),
            "name": obj.get("name"),
            "declaringType": Type.from_dict(obj["declaringType"]) if obj.get("declaringType") is not None else None,
            "reflectedType": Type.from_dict(obj["reflectedType"]) if obj.get("reflectedType") is not None else None,
            "module": Module.from_dict(obj["module"]) if obj.get("module") is not None else None,
            "customAttributes": [CustomAttributeData.from_dict(_item) for _item in obj["customAttributes"]] if obj.get("customAttributes") is not None else None,
            "isCollectible": obj.get("isCollectible"),
            "metadataToken": obj.get("metadataToken"),
            "attributes": obj.get("attributes"),
            "methodImplementationFlags": obj.get("methodImplementationFlags"),
            "callingConvention": obj.get("callingConvention"),
            "isAbstract": obj.get("isAbstract"),
            "isConstructor": obj.get("isConstructor"),
            "isFinal": obj.get("isFinal"),
            "isHideBySig": obj.get("isHideBySig"),
            "isSpecialName": obj.get("isSpecialName"),
            "isStatic": obj.get("isStatic"),
            "isVirtual": obj.get("isVirtual"),
            "isAssembly": obj.get("isAssembly"),
            "isFamily": obj.get("isFamily"),
            "isFamilyAndAssembly": obj.get("isFamilyAndAssembly"),
            "isFamilyOrAssembly": obj.get("isFamilyOrAssembly"),
            "isPrivate": obj.get("isPrivate"),
            "isPublic": obj.get("isPublic"),
            "isConstructedGenericMethod": obj.get("isConstructedGenericMethod"),
            "isGenericMethod": obj.get("isGenericMethod"),
            "isGenericMethodDefinition": obj.get("isGenericMethodDefinition"),
            "containsGenericParameters": obj.get("containsGenericParameters"),
            "methodHandle": RuntimeMethodHandle.from_dict(obj["methodHandle"]) if obj.get("methodHandle") is not None else None,
            "isSecurityCritical": obj.get("isSecurityCritical"),
            "isSecuritySafeCritical": obj.get("isSecuritySafeCritical"),
            "isSecurityTransparent": obj.get("isSecurityTransparent")
        })
        return _obj

from civitai.models.custom_attribute_data import CustomAttributeData
from civitai.models.module import Module
from civitai.models.type import Type
# TODO: Rewrite to not use raise_errors
MethodBase.model_rebuild(raise_errors=False)

