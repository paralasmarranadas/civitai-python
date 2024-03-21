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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from civitai.models.job_event_type import JobEventType
from civitai.models.provider import Provider
from civitai.models.time_span import TimeSpan
from typing import Optional, Set
from typing_extensions import Self

class JobEvent(BaseModel):
    """
    JobEvent
    """ # noqa: E501
    job_id: Optional[StrictStr] = Field(default=None, alias="jobId")
    type: Optional[JobEventType] = None
    date_time: Optional[datetime] = Field(default=None, description="Get the absolute datetime on which this event got created", alias="dateTime")
    provider: Optional[Provider] = None
    worker_id: Optional[StrictStr] = Field(default=None, description="Get or set the workerId that is associated with this event", alias="workerId")
    context: Optional[Dict[str, Any]] = Field(default=None, description="An optional set of key/value pairs that can be used to provide additional context.")
    claim_duration: Optional[TimeSpan] = Field(default=None, alias="claimDuration")
    job_duration: Optional[TimeSpan] = Field(default=None, alias="jobDuration")
    retry_attempt: Optional[StrictInt] = Field(default=None, description="The retry attempt of this job", alias="retryAttempt")
    cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The cost of the job associated with this event")
    job_properties: Optional[Dict[str, Any]] = Field(default=None, description="The properties of the job associated with this event", alias="jobProperties")
    job_type: Optional[StrictStr] = Field(default=None, description="Get the type of the job", alias="jobType")
    job_priority: Optional[StrictInt] = Field(default=None, description="The priority that is associated with this job", alias="jobPriority")
    claim_has_completed: Optional[StrictBool] = Field(default=None, description="Get wether this event marks the completion of a claim", alias="claimHasCompleted")
    job_has_completed: Optional[StrictBool] = Field(default=None, description="Get wether this event marks the completion of a job  This is determined based on the Civitai.Orchestration.Grains.Jobs.JobEvent.Type of this event", alias="jobHasCompleted")
    __properties: ClassVar[List[str]] = ["jobId", "type", "dateTime", "provider", "workerId", "context", "claimDuration", "jobDuration", "retryAttempt", "cost", "jobProperties", "jobType", "jobPriority", "claimHasCompleted", "jobHasCompleted"]

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
        """Create an instance of JobEvent from a JSON string"""
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
            "claim_has_completed",
            "job_has_completed",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of claim_duration
        if self.claim_duration:
            _dict['claimDuration'] = self.claim_duration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of job_duration
        if self.job_duration:
            _dict['jobDuration'] = self.job_duration.to_dict()
        # set to None if job_id (nullable) is None
        # and model_fields_set contains the field
        if self.job_id is None and "job_id" in self.model_fields_set:
            _dict['jobId'] = None

        # set to None if worker_id (nullable) is None
        # and model_fields_set contains the field
        if self.worker_id is None and "worker_id" in self.model_fields_set:
            _dict['workerId'] = None

        # set to None if context (nullable) is None
        # and model_fields_set contains the field
        if self.context is None and "context" in self.model_fields_set:
            _dict['context'] = None

        # set to None if job_properties (nullable) is None
        # and model_fields_set contains the field
        if self.job_properties is None and "job_properties" in self.model_fields_set:
            _dict['jobProperties'] = None

        # set to None if job_type (nullable) is None
        # and model_fields_set contains the field
        if self.job_type is None and "job_type" in self.model_fields_set:
            _dict['jobType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of JobEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "jobId": obj.get("jobId"),
            "type": obj.get("type"),
            "dateTime": obj.get("dateTime"),
            "provider": obj.get("provider"),
            "workerId": obj.get("workerId"),
            "context": obj.get("context"),
            "claimDuration": TimeSpan.from_dict(obj["claimDuration"]) if obj.get("claimDuration") is not None else None,
            "jobDuration": TimeSpan.from_dict(obj["jobDuration"]) if obj.get("jobDuration") is not None else None,
            "retryAttempt": obj.get("retryAttempt"),
            "cost": obj.get("cost"),
            "jobProperties": obj.get("jobProperties"),
            "jobType": obj.get("jobType"),
            "jobPriority": obj.get("jobPriority"),
            "claimHasCompleted": obj.get("claimHasCompleted"),
            "jobHasCompleted": obj.get("jobHasCompleted")
        })
        return _obj


