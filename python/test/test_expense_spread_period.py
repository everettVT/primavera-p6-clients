# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.expense_spread_period import ExpenseSpreadPeriod

class TestExpenseSpreadPeriod(unittest.TestCase):
    """ExpenseSpreadPeriod unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExpenseSpreadPeriod:
        """Test ExpenseSpreadPeriod
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExpenseSpreadPeriod`
        """
        model = ExpenseSpreadPeriod()
        if include_optional:
            return ExpenseSpreadPeriod(
                start_date = '',
                end_date = '',
                financial_period_object_id = 56,
                actual_cost = 1.337,
                at_completion_cost = 1.337,
                planned_cost = 1.337,
                remaining_cost = 1.337,
                cumulative_actual_cost = 1.337,
                cumulative_at_completion_cost = 1.337,
                cumulative_planned_cost = 1.337,
                cumulative_remaining_cost = 1.337
            )
        else:
            return ExpenseSpreadPeriod(
        )
        """

    def testExpenseSpreadPeriod(self):
        """Test ExpenseSpreadPeriod"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
