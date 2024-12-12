# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.risk_response_action_impact import RiskResponseActionImpact

class TestRiskResponseActionImpact(unittest.TestCase):
    """RiskResponseActionImpact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RiskResponseActionImpact:
        """Test RiskResponseActionImpact
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RiskResponseActionImpact`
        """
        model = RiskResponseActionImpact()
        if include_optional:
            return RiskResponseActionImpact(
                create_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                create_user = '',
                is_baseline = True,
                is_template = True,
                last_update_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_update_user = '',
                project_id = '',
                project_name = '',
                project_object_id = 56,
                risk_id = '',
                risk_object_id = 56,
                risk_response_action_id = '',
                risk_response_action_name = '',
                risk_response_action_object_id = 56,
                risk_threshold_level_code = '',
                risk_threshold_level_name = '',
                risk_threshold_level_object_id = 56,
                risk_threshold_name = '',
                risk_threshold_object_id = 56
            )
        else:
            return RiskResponseActionImpact(
                risk_response_action_object_id = 56,
                risk_threshold_level_object_id = 56,
        )
        """

    def testRiskResponseActionImpact(self):
        """Test RiskResponseActionImpact"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
