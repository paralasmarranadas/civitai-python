# coding: utf-8

"""
    Civitai Orchestration Consumer API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from civitai.models.image_job_control_net import ImageJobControlNet

class TestImageJobControlNet(unittest.TestCase):
    """ImageJobControlNet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImageJobControlNet:
        """Test ImageJobControlNet
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImageJobControlNet`
        """
        model = ImageJobControlNet()
        if include_optional:
            return ImageJobControlNet(
                preprocessor = 'Canny',
                weight = 1.337,
                start_step = 1.337,
                end_step = 1.337,
                blob_key = '',
                image_url = ''
            )
        else:
            return ImageJobControlNet(
        )
        """

    def testImageJobControlNet(self):
        """Test ImageJobControlNet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
