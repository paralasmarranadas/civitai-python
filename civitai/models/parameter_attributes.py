# coding: utf-8

"""
    Civitai Orchestration Consumer API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ParameterAttributes(str, Enum):
    """
    ParameterAttributes
    """

    """
    allowed enum values
    """
    NONE = 'None'
    IN = 'In'
    OUT = 'Out'
    LCID = 'Lcid'
    RETVAL = 'Retval'
    OPTIONAL = 'Optional'
    HASDEFAULT = 'HasDefault'
    HASFIELDMARSHAL = 'HasFieldMarshal'
    RESERVED3 = 'Reserved3'
    RESERVED4 = 'Reserved4'
    RESERVEDMASK = 'ReservedMask'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ParameterAttributes from a JSON string"""
        return cls(json.loads(json_str))


