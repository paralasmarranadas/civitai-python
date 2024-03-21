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


class FieldAttributes(str, Enum):
    """
    FieldAttributes
    """

    """
    allowed enum values
    """
    PRIVATESCOPE = 'PrivateScope'
    PRIVATE = 'Private'
    FAMANDASSEM = 'FamANDAssem'
    ASSEMBLY = 'Assembly'
    FAMILY = 'Family'
    FAMORASSEM = 'FamORAssem'
    PUBLIC = 'Public'
    FIELDACCESSMASK = 'FieldAccessMask'
    STATIC = 'Static'
    INITONLY = 'InitOnly'
    LITERAL = 'Literal'
    NOTSERIALIZED = 'NotSerialized'
    HASFIELDRVA = 'HasFieldRVA'
    SPECIALNAME = 'SpecialName'
    RTSPECIALNAME = 'RTSpecialName'
    HASFIELDMARSHAL = 'HasFieldMarshal'
    PINVOKEIMPL = 'PinvokeImpl'
    HASDEFAULT = 'HasDefault'
    RESERVEDMASK = 'ReservedMask'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FieldAttributes from a JSON string"""
        return cls(json.loads(json_str))


