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
from importlib import import_module
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from civitai.models.job_request_priority import JobRequestPriority
from civitai.models.provider import Provider
from civitai.models.time_span import TimeSpan
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from civitai.models.clear_asset_request import ClearAssetRequest
    from civitai.models.comfy_job_request import ComfyJobRequest
    from civitai.models.copy_asset_request import CopyAssetRequest
    from civitai.models.delete_blob_request import DeleteBlobRequest
    from civitai.models.get_blob_request import GetBlobRequest
    from civitai.models.image_embedding_job_request import ImageEmbeddingJobRequest
    from civitai.models.image_resource_training_job_request import ImageResourceTrainingJobRequest
    from civitai.models.image_transform_job_request import ImageTransformJobRequest
    from civitai.models.media_tagging_job_request import MediaTaggingJobRequest
    from civitai.models.pin_blob_request import PinBlobRequest
    from civitai.models.prepare_model_job_request import PrepareModelJobRequest
    from civitai.models.reboot_worker_job_request import RebootWorkerJobRequest
    from civitai.models.text_to_image_job_request import TextToImageJobRequest
    from civitai.models.unpin_blob_request import UnpinBlobRequest
    from civitai.models.upload_blob_request import UploadBlobRequest
    from civitai.models.wd_tagging_job_request import WDTaggingJobRequest

class JobRequest(BaseModel):
    """
    JobRequest
    """ # noqa: E501
    type: StrictStr = Field(alias="$type")
    name: Optional[StrictStr] = Field(default=None, description="Get or set the name of this job so that it can be referenced by other jobs")
    priority: Optional[JobRequestPriority] = None
    providers: Optional[List[Provider]] = Field(default=None, description="Get or set a list of service providers to target with this job  If not specified then all providers will be targeted")
    expire_at: Optional[datetime] = Field(default=None, description="An optional expiration date for this job", alias="expireAt")
    properties: Optional[Dict[str, Any]] = Field(default=None, description="A dictionary of user defined properties that are associated with this job template")
    callback_url: Optional[StrictStr] = Field(default=None, description="Get or set a url that will be invoked upon completion of this job", alias="callbackUrl")
    timeout: Optional[TimeSpan] = None
    retries: Optional[StrictInt] = Field(default=None, description="The max number of retries before we give up")
    dependencies: Optional[List[StrictStr]] = Field(default=None, description="Get or set a list of dependencies that this job has  These are the names of jobs that this job is dependent upon")
    __properties: ClassVar[List[str]] = ["$type", "name", "priority", "providers", "expireAt", "properties", "callbackUrl", "timeout", "retries", "dependencies"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = '$type'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'ClearAssetTemplate': 'ClearAssetRequest','ComfyJobTemplate': 'ComfyJobRequest','CopyAssetTemplate': 'CopyAssetRequest','DeleteBlobTemplate': 'DeleteBlobRequest','GetBlobTemplate': 'GetBlobRequest','ImageEmbeddingJobTemplate': 'ImageEmbeddingJobRequest','ImageResourceTrainingJobTemplate': 'ImageResourceTrainingJobRequest','ImageTransformJobTemplate': 'ImageTransformJobRequest','MediaTaggingJobTemplate': 'MediaTaggingJobRequest','PinBlobTemplate': 'PinBlobRequest','PrepareModelJobTemplate': 'PrepareModelJobRequest','RebootWorkerJobTemplate': 'RebootWorkerJobRequest','TextToImageJobTemplate': 'TextToImageJobRequest','UnpinBlobTemplate': 'UnpinBlobRequest','UploadBlobTemplate': 'UploadBlobRequest','WDTaggingJobTemplate': 'WDTaggingJobRequest'
    }

    @classmethod
    def get_discriminator_value(cls, obj: Dict[str, Any]) -> Optional[str]:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Union[ClearAssetRequest, ComfyJobRequest, CopyAssetRequest, DeleteBlobRequest, GetBlobRequest, ImageEmbeddingJobRequest, ImageResourceTrainingJobRequest, ImageTransformJobRequest, MediaTaggingJobRequest, PinBlobRequest, PrepareModelJobRequest, RebootWorkerJobRequest, TextToImageJobRequest, UnpinBlobRequest, UploadBlobRequest, WDTaggingJobRequest]]:
        """Create an instance of JobRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of priority
        if self.priority:
            _dict['priority'] = self.priority.to_dict()
        # override the default output from pydantic by calling `to_dict()` of timeout
        if self.timeout:
            _dict['timeout'] = self.timeout.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if priority (nullable) is None
        # and model_fields_set contains the field
        if self.priority is None and "priority" in self.model_fields_set:
            _dict['priority'] = None

        # set to None if providers (nullable) is None
        # and model_fields_set contains the field
        if self.providers is None and "providers" in self.model_fields_set:
            _dict['providers'] = None

        # set to None if expire_at (nullable) is None
        # and model_fields_set contains the field
        if self.expire_at is None and "expire_at" in self.model_fields_set:
            _dict['expireAt'] = None

        # set to None if properties (nullable) is None
        # and model_fields_set contains the field
        if self.properties is None and "properties" in self.model_fields_set:
            _dict['properties'] = None

        # set to None if callback_url (nullable) is None
        # and model_fields_set contains the field
        if self.callback_url is None and "callback_url" in self.model_fields_set:
            _dict['callbackUrl'] = None

        # set to None if retries (nullable) is None
        # and model_fields_set contains the field
        if self.retries is None and "retries" in self.model_fields_set:
            _dict['retries'] = None

        # set to None if dependencies (nullable) is None
        # and model_fields_set contains the field
        if self.dependencies is None and "dependencies" in self.model_fields_set:
            _dict['dependencies'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[ClearAssetRequest, ComfyJobRequest, CopyAssetRequest, DeleteBlobRequest, GetBlobRequest, ImageEmbeddingJobRequest, ImageResourceTrainingJobRequest, ImageTransformJobRequest, MediaTaggingJobRequest, PinBlobRequest, PrepareModelJobRequest, RebootWorkerJobRequest, TextToImageJobRequest, UnpinBlobRequest, UploadBlobRequest, WDTaggingJobRequest]]:
        """Create an instance of JobRequest from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'ClearAssetTemplate':
            return import_module("civitai.models.clear_asset_request").ClearAssetRequest.from_dict(obj)
        if object_type ==  'ComfyJobTemplate':
            return import_module("civitai.models.comfy_job_request").ComfyJobRequest.from_dict(obj)
        if object_type ==  'CopyAssetTemplate':
            return import_module("civitai.models.copy_asset_request").CopyAssetRequest.from_dict(obj)
        if object_type ==  'DeleteBlobTemplate':
            return import_module("civitai.models.delete_blob_request").DeleteBlobRequest.from_dict(obj)
        if object_type ==  'GetBlobTemplate':
            return import_module("civitai.models.get_blob_request").GetBlobRequest.from_dict(obj)
        if object_type ==  'ImageEmbeddingJobTemplate':
            return import_module("civitai.models.image_embedding_job_request").ImageEmbeddingJobRequest.from_dict(obj)
        if object_type ==  'ImageResourceTrainingJobTemplate':
            return import_module("civitai.models.image_resource_training_job_request").ImageResourceTrainingJobRequest.from_dict(obj)
        if object_type ==  'ImageTransformJobTemplate':
            return import_module("civitai.models.image_transform_job_request").ImageTransformJobRequest.from_dict(obj)
        if object_type ==  'MediaTaggingJobTemplate':
            return import_module("civitai.models.media_tagging_job_request").MediaTaggingJobRequest.from_dict(obj)
        if object_type ==  'PinBlobTemplate':
            return import_module("civitai.models.pin_blob_request").PinBlobRequest.from_dict(obj)
        if object_type ==  'PrepareModelJobTemplate':
            return import_module("civitai.models.prepare_model_job_request").PrepareModelJobRequest.from_dict(obj)
        if object_type ==  'RebootWorkerJobTemplate':
            return import_module("civitai.models.reboot_worker_job_request").RebootWorkerJobRequest.from_dict(obj)
        if object_type ==  'TextToImageJobTemplate':
            return import_module("civitai.models.text_to_image_job_request").TextToImageJobRequest.from_dict(obj)
        if object_type ==  'UnpinBlobTemplate':
            return import_module("civitai.models.unpin_blob_request").UnpinBlobRequest.from_dict(obj)
        if object_type ==  'UploadBlobTemplate':
            return import_module("civitai.models.upload_blob_request").UploadBlobRequest.from_dict(obj)
        if object_type ==  'WDTaggingJobTemplate':
            return import_module("civitai.models.wd_tagging_job_request").WDTaggingJobRequest.from_dict(obj)

        raise ValueError("JobRequest failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


