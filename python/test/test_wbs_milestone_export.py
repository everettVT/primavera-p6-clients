# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.wbs_milestone_export import WBSMilestoneExport

class TestWBSMilestoneExport(unittest.TestCase):
    """WBSMilestoneExport unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WBSMilestoneExport:
        """Test WBSMilestoneExport
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WBSMilestoneExport`
        """
        model = WBSMilestoneExport()
        if include_optional:
            return WBSMilestoneExport(
                include = True,
                var_field = [
                    'CREATE_DATE'
                    ]
            )
        else:
            return WBSMilestoneExport(
        )
        """

    def testWBSMilestoneExport(self):
        """Test WBSMilestoneExport"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
