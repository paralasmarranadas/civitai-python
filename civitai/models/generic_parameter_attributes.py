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


class GenericParameterAttributes(str, Enum):
    """
    GenericParameterAttributes
    """

    """
    allowed enum values
    """
    NONE = 'None'
    COVARIANT = 'Covariant'
    CONTRAVARIANT = 'Contravariant'
    VARIANCEMASK = 'VarianceMask'
    REFERENCETYPECONSTRAINT = 'ReferenceTypeConstraint'
    NOTNULLABLEVALUETYPECONSTRAINT = 'NotNullableValueTypeConstraint'
    DEFAULTCONSTRUCTORCONSTRAINT = 'DefaultConstructorConstraint'
    SPECIALCONSTRAINTMASK = 'SpecialConstraintMask'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of GenericParameterAttributes from a JSON string"""
        return cls(json.loads(json_str))


