# coding: utf-8

"""
    Civitai Orchestration Consumer API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from civitai.models.image_embedding_job_request import ImageEmbeddingJobRequest

class TestImageEmbeddingJobRequest(unittest.TestCase):
    """ImageEmbeddingJobRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImageEmbeddingJobRequest:
        """Test ImageEmbeddingJobRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImageEmbeddingJobRequest`
        """
        model = ImageEmbeddingJobRequest()
        if include_optional:
            return ImageEmbeddingJobRequest(
                image_url = ''
            )
        else:
            return ImageEmbeddingJobRequest(
        )
        """

    def testImageEmbeddingJobRequest(self):
        """Test ImageEmbeddingJobRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
