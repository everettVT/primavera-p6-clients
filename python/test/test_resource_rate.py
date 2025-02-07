# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.resource_rate import ResourceRate

class TestResourceRate(unittest.TestCase):
    """ResourceRate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceRate:
        """Test ResourceRate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceRate`
        """
        model = ResourceRate()
        if include_optional:
            return ResourceRate(
                create_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                create_user = '',
                effective_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_update_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_update_user = '',
                max_units_per_time = 1.337,
                object_id = 56,
                price_per_unit = 1.337,
                price_per_unit2 = 1.337,
                price_per_unit3 = 1.337,
                price_per_unit4 = 1.337,
                price_per_unit5 = 1.337,
                resource_id = '',
                resource_name = '',
                resource_object_id = 56,
                shift_period_object_id = 56
            )
        else:
            return ResourceRate(
        )
        """

    def testResourceRate(self):
        """Test ResourceRate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
