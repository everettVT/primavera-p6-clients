# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.activity_code_assignment_api import ActivityCodeAssignmentApi


class TestActivityCodeAssignmentApi(unittest.TestCase):
    """ActivityCodeAssignmentApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ActivityCodeAssignmentApi()

    def tearDown(self) -> None:
        pass

    def test_create_activity_code_assignment(self) -> None:
        """Test case for create_activity_code_assignment

        Create ActivityCodeAssignments
        """
        pass

    def test_delete_activity_code_assignment(self) -> None:
        """Test case for delete_activity_code_assignment

        Delete ActivityCodeAssignments
        """
        pass

    def test_get_activity_code_assignment_field_length(self) -> None:
        """Test case for get_activity_code_assignment_field_length

        View ActivityCodeAssignment Field Length
        """
        pass

    def test_get_activity_code_assignment_fields(self) -> None:
        """Test case for get_activity_code_assignment_fields

        View ActivityCodeAssignment fields
        """
        pass

    def test_get_activity_code_assignments(self) -> None:
        """Test case for get_activity_code_assignments

        Read ActivityCodeAssignments
        """
        pass

    def test_update_activity_code_assignment(self) -> None:
        """Test case for update_activity_code_assignment

        Update ActivityCodeAssignments
        """
        pass


if __name__ == '__main__':
    unittest.main()
