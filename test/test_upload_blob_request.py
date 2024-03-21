# coding: utf-8

"""
    Civitai Orchestration Consumer API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from civitai.models.upload_blob_request import UploadBlobRequest

class TestUploadBlobRequest(unittest.TestCase):
    """UploadBlobRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UploadBlobRequest:
        """Test UploadBlobRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UploadBlobRequest`
        """
        model = UploadBlobRequest()
        if include_optional:
            return UploadBlobRequest(
                key = '',
                replace = True,
                duration = civitai.models.time_span.TimeSpan(
                    ticks = 56, 
                    days = 56, 
                    hours = 56, 
                    milliseconds = 56, 
                    microseconds = 56, 
                    nanoseconds = 56, 
                    minutes = 56, 
                    seconds = 56, 
                    total_days = 1.337, 
                    total_hours = 1.337, 
                    total_milliseconds = 1.337, 
                    total_microseconds = 1.337, 
                    total_nanoseconds = 1.337, 
                    total_minutes = 1.337, 
                    total_seconds = 1.337, )
            )
        else:
            return UploadBlobRequest(
        )
        """

    def testUploadBlobRequest(self):
        """Test UploadBlobRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
