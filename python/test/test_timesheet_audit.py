# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.timesheet_audit import TimesheetAudit

class TestTimesheetAudit(unittest.TestCase):
    """TimesheetAudit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimesheetAudit:
        """Test TimesheetAudit
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimesheetAudit`
        """
        model = TimesheetAudit()
        if include_optional:
            return TimesheetAudit(
                approver_user_name = '',
                approver_user_object_id = 56,
                audit_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                object_id = 56,
                overhead_hours = 1.337,
                overhead_overtime_hours = 1.337,
                pending_overhead_hours = 1.337,
                pending_overhead_overtime_hours = 1.337,
                pending_project_hours = 1.337,
                pending_project_overtime_hours = 1.337,
                project_hours = 1.337,
                project_id = '',
                project_object_id = 56,
                project_overtime_hours = 1.337,
                resource_id = '',
                resource_name = '',
                resource_object_id = 56,
                timesheet_activity_status = '',
                timesheet_approving_as = '',
                timesheet_period_end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                timesheet_period_object_id = 56,
                timesheet_period_start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                timesheet_status = ''
            )
        else:
            return TimesheetAudit(
        )
        """

    def testTimesheetAudit(self):
        """Test TimesheetAudit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
