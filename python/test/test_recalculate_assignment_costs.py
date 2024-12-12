# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.recalculate_assignment_costs import RecalculateAssignmentCosts

class TestRecalculateAssignmentCosts(unittest.TestCase):
    """RecalculateAssignmentCosts unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RecalculateAssignmentCosts:
        """Test RecalculateAssignmentCosts
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RecalculateAssignmentCosts`
        """
        model = RecalculateAssignmentCosts()
        if include_optional:
            return RecalculateAssignmentCosts(
                project_object_id = 56,
                synchronize_overtime_factor = True,
                timeout = 56
            )
        else:
            return RecalculateAssignmentCosts(
        )
        """

    def testRecalculateAssignmentCosts(self):
        """Test RecalculateAssignmentCosts"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
