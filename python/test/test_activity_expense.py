# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.activity_expense import ActivityExpense

class TestActivityExpense(unittest.TestCase):
    """ActivityExpense unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActivityExpense:
        """Test ActivityExpense
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActivityExpense`
        """
        model = ActivityExpense()
        if include_optional:
            return ActivityExpense(
                accrual_type = '',
                activity_id = '',
                activity_name = '',
                activity_object_id = 56,
                actual_cost = 1.337,
                actual_units = 1.337,
                at_completion_cost = 1.337,
                at_completion_units = 1.337,
                auto_compute_actuals = True,
                cbs_code = '',
                cbsid = 56,
                cost_account_id = '',
                cost_account_name = '',
                cost_account_object_id = 56,
                create_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                create_user = '',
                document_number = '',
                expense_category_name = '',
                expense_category_object_id = 56,
                expense_description = '',
                expense_item = '',
                expense_percent_complete = 1.337,
                is_baseline = True,
                is_template = True,
                last_update_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_update_user = '',
                object_id = 56,
                over_budget = True,
                planned_cost = 1.337,
                planned_units = 1.337,
                price_per_unit = 1.337,
                project_id = '',
                project_object_id = 56,
                remaining_cost = 1.337,
                remaining_units = 1.337,
                unit_of_measure = '',
                vendor = '',
                wbs_object_id = 56
            )
        else:
            return ActivityExpense(
                activity_object_id = 56,
                expense_item = '',
        )
        """

    def testActivityExpense(self):
        """Test ActivityExpense"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()