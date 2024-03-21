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
from civitai.models.model_error import ModelError
from civitai.models.model_validation_state import ModelValidationState
from typing import Optional, Set
from typing_extensions import Self

class ModelStateEntry(BaseModel):
    """
    ModelStateEntry
    """ # noqa: E501
    raw_value: Optional[Any] = Field(default=None, alias="rawValue")
    attempted_value: Optional[StrictStr] = Field(default=None, alias="attemptedValue")
    errors: Optional[List[ModelError]] = None
    validation_state: Optional[ModelValidationState] = Field(default=None, alias="validationState")
    is_container_node: Optional[StrictBool] = Field(default=None, alias="isContainerNode")
    children: Optional[List[ModelStateEntry]] = None
    __properties: ClassVar[List[str]] = ["rawValue", "attemptedValue", "errors", "validationState", "isContainerNode", "children"]

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
        """Create an instance of ModelStateEntry from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "errors",
            "is_container_node",
            "children",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item in self.errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['errors'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in children (list)
        _items = []
        if self.children:
            for _item in self.children:
                if _item:
                    _items.append(_item.to_dict())
            _dict['children'] = _items
        # set to None if raw_value (nullable) is None
        # and model_fields_set contains the field
        if self.raw_value is None and "raw_value" in self.model_fields_set:
            _dict['rawValue'] = None

        # set to None if attempted_value (nullable) is None
        # and model_fields_set contains the field
        if self.attempted_value is None and "attempted_value" in self.model_fields_set:
            _dict['attemptedValue'] = None

        # set to None if errors (nullable) is None
        # and model_fields_set contains the field
        if self.errors is None and "errors" in self.model_fields_set:
            _dict['errors'] = None

        # set to None if children (nullable) is None
        # and model_fields_set contains the field
        if self.children is None and "children" in self.model_fields_set:
            _dict['children'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ModelStateEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "rawValue": obj.get("rawValue"),
            "attemptedValue": obj.get("attemptedValue"),
            "errors": [ModelError.from_dict(_item) for _item in obj["errors"]] if obj.get("errors") is not None else None,
            "validationState": obj.get("validationState"),
            "isContainerNode": obj.get("isContainerNode"),
            "children": [ModelStateEntry.from_dict(_item) for _item in obj["children"]] if obj.get("children") is not None else None
        })
        return _obj

# TODO: Rewrite to not use raise_errors
ModelStateEntry.model_rebuild(raise_errors=False)

