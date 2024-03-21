# coding: utf-8

"""
    Civitai Orchestration Consumer API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from civitai.models.air import AIR

class TestAIR(unittest.TestCase):
    """AIR unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AIR:
        """Test AIR
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AIR`
        """
        model = AIR()
        if include_optional:
            return AIR(
                value = '',
                legacy_id = '',
                base_model = 'SD_1_5',
                ecosystem = civitai.models.read_only_span_1.ReadOnlySpan_1(
                    length = 56, 
                    is_empty = True, ),
                type = civitai.models.read_only_span_1.ReadOnlySpan_1(
                    length = 56, 
                    is_empty = True, ),
                source = civitai.models.read_only_span_1.ReadOnlySpan_1(
                    length = 56, 
                    is_empty = True, ),
                id = civitai.models.read_only_span_1.ReadOnlySpan_1(
                    length = 56, 
                    is_empty = True, ),
                layer = civitai.models.read_only_span_1.ReadOnlySpan_1(
                    length = 56, 
                    is_empty = True, ),
                format = civitai.models.read_only_span_1.ReadOnlySpan_1(
                    length = 56, 
                    is_empty = True, )
            )
        else:
            return AIR(
        )
        """

    def testAIR(self):
        """Test AIR"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
