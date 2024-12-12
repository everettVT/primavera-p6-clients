# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.resource_assignment_create import ResourceAssignmentCreate

class TestResourceAssignmentCreate(unittest.TestCase):
    """ResourceAssignmentCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceAssignmentCreate:
        """Test ResourceAssignmentCreate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceAssignmentCreate`
        """
        model = ResourceAssignmentCreate()
        if include_optional:
            return ResourceAssignmentCreate(
                activity_object_id = 56,
                actual_finish_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                actual_start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                actual_units = 1.337,
                assignment_is_read = '',
                change_set_object_id = 56,
                var_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                project_object_id = 56,
                remaining_duration = 1.337,
                remaining_finish_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                remaining_units = 1.337,
                request_user_object_id = 56,
                resource_assignment_create_object_id = 56,
                resource_assignment_object_id = 56,
                resource_object_id = 56,
                status = ''
            )
        else:
            return ResourceAssignmentCreate(
                activity_object_id = 56,
                resource_object_id = 56,
        )
        """

    def testResourceAssignmentCreate(self):
        """Test ResourceAssignmentCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()