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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class TimeSpan(BaseModel):
    """
    TimeSpan
    """ # noqa: E501
    ticks: Optional[StrictInt] = None
    days: Optional[StrictInt] = None
    hours: Optional[StrictInt] = None
    milliseconds: Optional[StrictInt] = None
    microseconds: Optional[StrictInt] = None
    nanoseconds: Optional[StrictInt] = None
    minutes: Optional[StrictInt] = None
    seconds: Optional[StrictInt] = None
    total_days: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalDays")
    total_hours: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalHours")
    total_milliseconds: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalMilliseconds")
    total_microseconds: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalMicroseconds")
    total_nanoseconds: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalNanoseconds")
    total_minutes: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalMinutes")
    total_seconds: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalSeconds")
    __properties: ClassVar[List[str]] = ["ticks", "days", "hours", "milliseconds", "microseconds", "nanoseconds", "minutes", "seconds", "totalDays", "totalHours", "totalMilliseconds", "totalMicroseconds", "totalNanoseconds", "totalMinutes", "totalSeconds"]

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
        """Create an instance of TimeSpan from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "days",
            "hours",
            "milliseconds",
            "microseconds",
            "nanoseconds",
            "minutes",
            "seconds",
            "total_days",
            "total_hours",
            "total_milliseconds",
            "total_microseconds",
            "total_nanoseconds",
            "total_minutes",
            "total_seconds",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TimeSpan from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ticks": obj.get("ticks"),
            "days": obj.get("days"),
            "hours": obj.get("hours"),
            "milliseconds": obj.get("milliseconds"),
            "microseconds": obj.get("microseconds"),
            "nanoseconds": obj.get("nanoseconds"),
            "minutes": obj.get("minutes"),
            "seconds": obj.get("seconds"),
            "totalDays": obj.get("totalDays"),
            "totalHours": obj.get("totalHours"),
            "totalMilliseconds": obj.get("totalMilliseconds"),
            "totalMicroseconds": obj.get("totalMicroseconds"),
            "totalNanoseconds": obj.get("totalNanoseconds"),
            "totalMinutes": obj.get("totalMinutes"),
            "totalSeconds": obj.get("totalSeconds")
        })
        return _obj


