# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.resource_curve import ResourceCurve

class TestResourceCurve(unittest.TestCase):
    """ResourceCurve unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceCurve:
        """Test ResourceCurve
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceCurve`
        """
        model = ResourceCurve()
        if include_optional:
            return ResourceCurve(
                create_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                create_user = '',
                is_default = True,
                last_update_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_update_user = '',
                name = '',
                object_id = 56,
                values = openapi_client.models.values.Values(
                    value0 = 1.337, 
                    value5 = 1.337, 
                    value10 = 1.337, 
                    value15 = 1.337, 
                    value20 = 1.337, 
                    value25 = 1.337, 
                    value30 = 1.337, 
                    value35 = 1.337, 
                    value40 = 1.337, 
                    value45 = 1.337, 
                    value50 = 1.337, 
                    value55 = 1.337, 
                    value60 = 1.337, 
                    value65 = 1.337, 
                    value70 = 1.337, 
                    value75 = 1.337, 
                    value80 = 1.337, 
                    value85 = 1.337, 
                    value90 = 1.337, 
                    value95 = 1.337, 
                    value100 = 1.337, )
            )
        else:
            return ResourceCurve(
        )
        """

    def testResourceCurve(self):
        """Test ResourceCurve"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
