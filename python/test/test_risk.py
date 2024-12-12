# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.risk import Risk

class TestRisk(unittest.TestCase):
    """Risk unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Risk:
        """Test Risk
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Risk`
        """
        model = Risk()
        if include_optional:
            return Risk(
                cause = '',
                cost_threshold_id = 56,
                create_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                create_user = '',
                description = '',
                effect = '',
                exposure = 1.337,
                exposure_finish_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                exposure_start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                identified_by_resource_id = '',
                identified_by_resource_name = '',
                identified_by_resource_object_id = 56,
                identified_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                impact_threshold_values = 56,
                is_baseline = True,
                is_template = True,
                last_update_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_update_user = '',
                name = '',
                note = '',
                object_id = 56,
                probability_threshold_id = 56,
                project_id = '',
                project_name = '',
                project_object_id = 56,
                resource_id = '',
                resource_name = '',
                resource_object_id = 56,
                response_total_cost = 1.337,
                risk_category_name = '',
                risk_category_object_id = 56,
                schedule_threshold_id = 56,
                score = 56,
                score_color = '',
                score_text = '',
                status = '',
                type = ''
            )
        else:
            return Risk(
                id = '',
                project_object_id = 56,
        )
        """

    def testRisk(self):
        """Test Risk"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()