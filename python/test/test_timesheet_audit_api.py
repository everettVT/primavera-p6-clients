# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.timesheet_audit_api import TimesheetAuditApi


class TestTimesheetAuditApi(unittest.TestCase):
    """TimesheetAuditApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TimesheetAuditApi()

    def tearDown(self) -> None:
        pass

    def test_get_timesheet_audit(self) -> None:
        """Test case for get_timesheet_audit

        Read TimesheetAudit
        """
        pass

    def test_get_timesheet_audit_field_length(self) -> None:
        """Test case for get_timesheet_audit_field_length

        View TimesheetAudit Field Length
        """
        pass

    def test_get_timesheet_audit_fields(self) -> None:
        """Test case for get_timesheet_audit_fields

        View TimesheetAudit fields
        """
        pass


if __name__ == '__main__':
    unittest.main()