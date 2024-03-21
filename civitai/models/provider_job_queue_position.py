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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from civitai.models.time_span import TimeSpan
from typing import Optional, Set
from typing_extensions import Self

class ProviderJobQueuePosition(BaseModel):
    """
    ProviderJobQueuePosition
    """ # noqa: E501
    preceding_jobs: Optional[StrictInt] = Field(default=None, description="The exact position in the queue", alias="precedingJobs")
    preceding_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The exact cost that is preceding", alias="precedingCost")
    throughput_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The estimated throughput rate of the queue", alias="throughputRate")
    worker_id: Optional[StrictStr] = Field(default=None, description="The id of the worker that this job is queued with", alias="workerId")
    estimated_start_duration: Optional[TimeSpan] = Field(default=None, alias="estimatedStartDuration")
    estimated_start_date: Optional[datetime] = Field(default=None, description="The date before the job is estimated to be started. Null if we do not have an estimate yet", alias="estimatedStartDate")
    __properties: ClassVar[List[str]] = ["precedingJobs", "precedingCost", "throughputRate", "workerId", "estimatedStartDuration", "estimatedStartDate"]

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
        """Create an instance of ProviderJobQueuePosition from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "estimated_start_date",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of estimated_start_duration
        if self.estimated_start_duration:
            _dict['estimatedStartDuration'] = self.estimated_start_duration.to_dict()
        # set to None if worker_id (nullable) is None
        # and model_fields_set contains the field
        if self.worker_id is None and "worker_id" in self.model_fields_set:
            _dict['workerId'] = None

        # set to None if estimated_start_date (nullable) is None
        # and model_fields_set contains the field
        if self.estimated_start_date is None and "estimated_start_date" in self.model_fields_set:
            _dict['estimatedStartDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProviderJobQueuePosition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "precedingJobs": obj.get("precedingJobs"),
            "precedingCost": obj.get("precedingCost"),
            "throughputRate": obj.get("throughputRate"),
            "workerId": obj.get("workerId"),
            "estimatedStartDuration": TimeSpan.from_dict(obj["estimatedStartDuration"]) if obj.get("estimatedStartDuration") is not None else None,
            "estimatedStartDate": obj.get("estimatedStartDate")
        })
        return _obj


