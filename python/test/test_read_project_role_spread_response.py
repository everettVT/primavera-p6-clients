# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.read_project_role_spread_response import ReadProjectRoleSpreadResponse

class TestReadProjectRoleSpreadResponse(unittest.TestCase):
    """ReadProjectRoleSpreadResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReadProjectRoleSpreadResponse:
        """Test ReadProjectRoleSpreadResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReadProjectRoleSpreadResponse`
        """
        model = ReadProjectRoleSpreadResponse()
        if include_optional:
            return ReadProjectRoleSpreadResponse(
                project_id = '',
                project_object_id = 56,
                role_id = '',
                role_object_id = 56,
                start_date = '',
                end_date = '',
                period_type = '',
                period = [
                    openapi_client.models.resource_role_spread_period.ResourceRoleSpreadPeriod(
                        start_date = '', 
                        end_date = '', 
                        financial_period_object_id = 56, 
                        actual_cost = 1.337, 
                        actual_overtime_cost = 1.337, 
                        actual_overtime_units = 1.337, 
                        actual_regular_cost = 1.337, 
                        actual_regular_units = 1.337, 
                        actual_units = 1.337, 
                        at_completion_cost = 1.337, 
                        at_completion_units = 1.337, 
                        limit = 1.337, 
                        period_actual_cost = 1.337, 
                        period_actual_units = 1.337, 
                        period_at_completion_cost = 1.337, 
                        period_at_completion_units = 1.337, 
                        planned_cost = 1.337, 
                        planned_units = 1.337, 
                        remaining_cost = 1.337, 
                        remaining_late_cost = 1.337, 
                        remaining_late_units = 1.337, 
                        remaining_units = 1.337, 
                        staffed_actual_cost = 1.337, 
                        staffed_actual_overtime_cost = 1.337, 
                        staffed_actual_overtime_units = 1.337, 
                        staffed_actual_regular_cost = 1.337, 
                        staffed_actual_regular_units = 1.337, 
                        staffed_actual_units = 1.337, 
                        staffed_at_completion_cost = 1.337, 
                        staffed_at_completion_units = 1.337, 
                        staffed_planned_cost = 1.337, 
                        staffed_planned_units = 1.337, 
                        staffed_remaining_cost = 1.337, 
                        staffed_remaining_late_cost = 1.337, 
                        staffed_remaining_late_units = 1.337, 
                        staffed_remaining_units = 1.337, 
                        unstaffed_actual_cost = 1.337, 
                        unstaffed_actual_overtime_cost = 1.337, 
                        unstaffed_actual_overtime_units = 1.337, 
                        unstaffed_actual_regular_cost = 1.337, 
                        unstaffed_actual_regular_units = 1.337, 
                        unstaffed_actual_units = 1.337, 
                        unstaffed_at_completion_cost = 1.337, 
                        unstaffed_at_completion_units = 1.337, 
                        unstaffed_planned_cost = 1.337, 
                        unstaffed_planned_units = 1.337, 
                        unstaffed_remaining_cost = 1.337, 
                        unstaffed_remaining_late_cost = 1.337, 
                        unstaffed_remaining_late_units = 1.337, 
                        unstaffed_remaining_units = 1.337, 
                        cumulative_actual_cost = 1.337, 
                        cumulative_actual_overtime_cost = 1.337, 
                        cumulative_actual_overtime_units = 1.337, 
                        cumulative_actual_regular_cost = 1.337, 
                        cumulative_actual_regular_units = 1.337, 
                        cumulative_actual_units = 1.337, 
                        cumulative_at_completion_cost = 1.337, 
                        cumulative_at_completion_units = 1.337, 
                        cumulative_limit = 1.337, 
                        cumulative_period_actual_cost = 1.337, 
                        cumulative_period_actual_units = 1.337, 
                        cumulative_period_at_completion_cost = 1.337, 
                        cumulative_period_at_completion_units = 1.337, 
                        cumulative_planned_cost = 1.337, 
                        cumulative_planned_units = 1.337, 
                        cumulative_remaining_cost = 1.337, 
                        cumulative_remaining_late_cost = 1.337, 
                        cumulative_remaining_late_units = 1.337, 
                        cumulative_remaining_units = 1.337, 
                        cumulative_staffed_actual_cost = 1.337, 
                        cumulative_staffed_actual_overtime_cost = 1.337, 
                        cumulative_staffed_actual_overtime_units = 1.337, 
                        cumulative_staffed_actual_regular_cost = 1.337, 
                        cumulative_staffed_actual_regular_units = 1.337, 
                        cumulative_staffed_actual_units = 1.337, 
                        cumulative_staffed_at_completion_cost = 1.337, 
                        cumulative_staffed_at_completion_units = 1.337, 
                        cumulative_staffed_planned_cost = 1.337, 
                        cumulative_staffed_planned_units = 1.337, 
                        cumulative_staffed_remaining_cost = 1.337, 
                        cumulative_staffed_remaining_late_cost = 1.337, 
                        cumulative_staffed_remaining_late_units = 1.337, 
                        cumulative_staffed_remaining_units = 1.337, 
                        cumulative_unstaffed_actual_cost = 1.337, 
                        cumulative_unstaffed_actual_overtime_cost = 1.337, 
                        cumulative_unstaffed_actual_overtime_units = 1.337, 
                        cumulative_unstaffed_actual_regular_cost = 1.337, 
                        cumulative_unstaffed_actual_regular_units = 1.337, 
                        cumulative_unstaffed_actual_units = 1.337, 
                        cumulative_unstaffed_at_completion_cost = 1.337, 
                        cumulative_unstaffed_at_completion_units = 1.337, 
                        cumulative_unstaffed_planned_cost = 1.337, 
                        cumulative_unstaffed_planned_units = 1.337, 
                        cumulative_unstaffed_remaining_cost = 1.337, 
                        cumulative_unstaffed_remaining_late_cost = 1.337, 
                        cumulative_unstaffed_remaining_late_units = 1.337, 
                        cumulative_unstaffed_remaining_units = 1.337, )
                    ]
            )
        else:
            return ReadProjectRoleSpreadResponse(
        )
        """

    def testReadProjectRoleSpreadResponse(self):
        """Test ReadProjectRoleSpreadResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
