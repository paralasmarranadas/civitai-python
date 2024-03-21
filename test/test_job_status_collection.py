# coding: utf-8

"""
    Civitai Orchestration Consumer API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from civitai.models.job_status_collection import JobStatusCollection

class TestJobStatusCollection(unittest.TestCase):
    """JobStatusCollection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JobStatusCollection:
        """Test JobStatusCollection
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JobStatusCollection`
        """
        model = JobStatusCollection()
        if include_optional:
            return JobStatusCollection(
                token = '',
                jobs = [
                    civitai.models.job_status.JobStatus(
                        job = null, 
                        job_id = '', 
                        cost = 1.337, 
                        properties = {
                            'key' : null
                            }, 
                        result = null, 
                        last_event = civitai.models.job_event.JobEvent(
                            job_id = '', 
                            type = 'Initialized', 
                            date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            provider = 'Civitai', 
                            worker_id = '', 
                            context = {
                                'key' : null
                                }, 
                            claim_duration = civitai.models.time_span.TimeSpan(
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
                            job_duration = civitai.models.time_span.TimeSpan(
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
                            retry_attempt = 56, 
                            cost = 1.337, 
                            job_properties = {
                                'key' : null
                                }, 
                            job_type = '', 
                            job_priority = 56, 
                            claim_has_completed = True, 
                            job_has_completed = True, ), 
                        service_providers = {
                            'key' : civitai.models.provider_job_status.ProviderJobStatus(
                                support = 'Unsupported', 
                                queue_position = civitai.models.provider_job_queue_position.ProviderJobQueuePosition(
                                    preceding_jobs = 56, 
                                    preceding_cost = 1.337, 
                                    throughput_rate = 1.337, 
                                    worker_id = '', 
                                    estimated_start_duration = , 
                                    estimated_start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), )
                            }, 
                        scheduled = True, )
                    ]
            )
        else:
            return JobStatusCollection(
        )
        """

    def testJobStatusCollection(self):
        """Test JobStatusCollection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
