# coding: utf-8

"""
    Civitai Orchestration Consumer API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from civitai.models.pin_blob_request import PinBlobRequest

class TestPinBlobRequest(unittest.TestCase):
    """PinBlobRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PinBlobRequest:
        """Test PinBlobRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PinBlobRequest`
        """
        model = PinBlobRequest()
        if include_optional:
            return PinBlobRequest(
                key = ''
            )
        else:
            return PinBlobRequest(
        )
        """

    def testPinBlobRequest(self):
        """Test PinBlobRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
