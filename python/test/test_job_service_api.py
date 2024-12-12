# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.job_service_api import JobServiceApi


class TestJobServiceApi(unittest.TestCase):
    """JobServiceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = JobServiceApi()

    def tearDown(self) -> None:
        pass

    def test_create_global_profile(self) -> None:
        """Test case for create_global_profile

        Create JobService
        """
        pass

    def test_delete_job_service(self) -> None:
        """Test case for delete_job_service

        Delete JobService
        """
        pass

    def test_get_job_service(self) -> None:
        """Test case for get_job_service

        Read JobService
        """
        pass

    def test_get_schedule_options_field_length(self) -> None:
        """Test case for get_schedule_options_field_length

        View JobService Field Length
        """
        pass

    def test_get_schedule_options_fields(self) -> None:
        """Test case for get_schedule_options_fields

        View ScheduleOptions fields
        """
        pass

    def test_update_job_service(self) -> None:
        """Test case for update_job_service

        Update JobService
        """
        pass


if __name__ == '__main__':
    unittest.main()
