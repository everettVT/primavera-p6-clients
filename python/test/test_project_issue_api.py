# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.project_issue_api import ProjectIssueApi


class TestProjectIssueApi(unittest.TestCase):
    """ProjectIssueApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProjectIssueApi()

    def tearDown(self) -> None:
        pass

    def test_create_project_issue(self) -> None:
        """Test case for create_project_issue

        Create ProjectIssue
        """
        pass

    def test_delete_project_issue(self) -> None:
        """Test case for delete_project_issue

        Delete ProjectIssue
        """
        pass

    def test_get_project_issue(self) -> None:
        """Test case for get_project_issue

        Reads ProjectIssue
        """
        pass

    def test_get_project_issue_field_length(self) -> None:
        """Test case for get_project_issue_field_length

        View ProjectIssue Field Length
        """
        pass

    def test_get_project_issue_fields(self) -> None:
        """Test case for get_project_issue_fields

        View Project fields
        """
        pass

    def test_update_project_issue(self) -> None:
        """Test case for update_project_issue

        Update ProjectIssue
        """
        pass


if __name__ == '__main__':
    unittest.main()
