# coding: utf-8

"""
    Civitai Orchestration Consumer API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from civitai.models.clear_asset_request import ClearAssetRequest

class TestClearAssetRequest(unittest.TestCase):
    """ClearAssetRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClearAssetRequest:
        """Test ClearAssetRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClearAssetRequest`
        """
        model = ClearAssetRequest()
        if include_optional:
            return ClearAssetRequest(
                job_id = ''
            )
        else:
            return ClearAssetRequest(
        )
        """

    def testClearAssetRequest(self):
        """Test ClearAssetRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
