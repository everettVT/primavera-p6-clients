# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.project_spending_plan import ProjectSpendingPlan

class TestProjectSpendingPlan(unittest.TestCase):
    """ProjectSpendingPlan unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectSpendingPlan:
        """Test ProjectSpendingPlan
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectSpendingPlan`
        """
        model = ProjectSpendingPlan()
        if include_optional:
            return ProjectSpendingPlan(
                benefit_plan = 1.337,
                create_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                create_user = '',
                var_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                is_baseline = True,
                is_template = True,
                last_update_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_update_user = '',
                object_id = 56,
                project_id = '',
                project_object_id = 56,
                spending_plan = 1.337,
                wbs_code = '',
                wbs_name = '',
                wbs_object_id = 56
            )
        else:
            return ProjectSpendingPlan(
                var_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                project_object_id = 56,
                wbs_object_id = 56,
        )
        """

    def testProjectSpendingPlan(self):
        """Test ProjectSpendingPlan"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
