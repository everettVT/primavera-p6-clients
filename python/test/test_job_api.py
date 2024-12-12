# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.job_api import JobApi


class TestJobApi(unittest.TestCase):
    """JobApi unit test stubs"""

    def setUp(self) -> None:
        self.api = JobApi()

    def tearDown(self) -> None:
        pass

    def test_apply_actual(self) -> None:
        """Test case for apply_actual

        Apply Actual
        """
        pass

    def test_cancel_job(self) -> None:
        """Test case for cancel_job

        CancelJob
        """
        pass

    def test_get_current_jobs(self) -> None:
        """Test case for get_current_jobs

        GetCurrentJobs
        """
        pass

    def test_level(self) -> None:
        """Test case for level

        Leveling Project
        """
        pass

    def test_read_job_log(self) -> None:
        """Test case for read_job_log

        ReadJobLog
        """
        pass

    def test_read_job_status(self) -> None:
        """Test case for read_job_status

        ReadJobStatus
        """
        pass

    def test_recalculate_assignment_costs(self) -> None:
        """Test case for recalculate_assignment_costs

        RecalculateAssignmentCosts
        """
        pass

    def test_schedule(self) -> None:
        """Test case for schedule

        Schedule Project
        """
        pass

    def test_schedule1(self) -> None:
        """Test case for schedule1

        Update Baseline
        """
        pass

    def test_send_to_unifier(self) -> None:
        """Test case for send_to_unifier

        ScheduleCheck
        """
        pass

    def test_send_to_unifier1(self) -> None:
        """Test case for send_to_unifier1

        SendToUnifier
        """
        pass

    def test_store_period_performance(self) -> None:
        """Test case for store_period_performance

        StorePeriodPerformance
        """
        pass

    def test_summarize_eps(self) -> None:
        """Test case for summarize_eps

        Summarize CBS
        """
        pass

    def test_summarize_eps1(self) -> None:
        """Test case for summarize_eps1

        Summarize EPS
        """
        pass

    def test_summarize_project(self) -> None:
        """Test case for summarize_project

        Summarize Project
        """
        pass


if __name__ == '__main__':
    unittest.main()