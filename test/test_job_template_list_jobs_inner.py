# coding: utf-8

"""
    Civitai Orchestration Consumer API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from civitai.models.job_template_list_jobs_inner import JobTemplateListJobsInner

class TestJobTemplateListJobsInner(unittest.TestCase):
    """JobTemplateListJobsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JobTemplateListJobsInner:
        """Test JobTemplateListJobsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JobTemplateListJobsInner`
        """
        model = JobTemplateListJobsInner()
        if include_optional:
            return JobTemplateListJobsInner(
                model = '',
                training_data = '',
                params = {
                    'key' : None
                    },
                type = '',
                name = '',
                priority = None,
                providers = [
                    'Civitai'
                    ],
                expire_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                properties = {
                    'key' : None
                    },
                callback_url = '',
                timeout = civitai.models.time_span.TimeSpan(
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
                    total_seconds = 1.337, ),
                retries = 56,
                dependencies = [
                    ''
                    ],
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
                    total_seconds = 1.337, ),
                image_url = '',
                blob_key = '',
                transformer = 'Canny',
                destination_url = '',
                job_id = '',
                asset_name = '',
                destination_uri = '',
                media_url = '',
                threshold = 1.337,
                model_id = 56,
                base_model = 'SD_1_5',
                action = 'Upload'
            )
        else:
            return JobTemplateListJobsInner(
                model = '',
                type = '',
                media_url = '',
                model_id = 56,
        )
        """

    def testJobTemplateListJobsInner(self):
        """Test JobTemplateListJobsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
