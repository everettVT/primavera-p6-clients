# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.timesheet_delegate_api import TimesheetDelegateApi


class TestTimesheetDelegateApi(unittest.TestCase):
    """TimesheetDelegateApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TimesheetDelegateApi()

    def tearDown(self) -> None:
        pass

    def test_get_timesheet_delegate(self) -> None:
        """Test case for get_timesheet_delegate

        Read TimesheetDelegate
        """
        pass

    def test_get_timesheet_delegate_field_length(self) -> None:
        """Test case for get_timesheet_delegate_field_length

        View TimesheetDelegate Field Length
        """
        pass

    def test_get_timesheet_delegate_fields(self) -> None:
        """Test case for get_timesheet_delegate_fields

        View TimesheetDelegate fields
        """
        pass


if __name__ == '__main__':
    unittest.main()
