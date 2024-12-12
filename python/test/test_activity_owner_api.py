# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.activity_owner_api import ActivityOwnerApi


class TestActivityOwnerApi(unittest.TestCase):
    """ActivityOwnerApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ActivityOwnerApi()

    def tearDown(self) -> None:
        pass

    def test_create_activity_owners(self) -> None:
        """Test case for create_activity_owners

        Create ActivityOwners
        """
        pass

    def test_delete_activity_owners(self) -> None:
        """Test case for delete_activity_owners

        Delete ActivityOwners
        """
        pass

    def test_get_activity_owners(self) -> None:
        """Test case for get_activity_owners

        Read ActivityOwners
        """
        pass

    def test_get_activity_owners_field_length(self) -> None:
        """Test case for get_activity_owners_field_length

        View ActivityOwner Field Length
        """
        pass

    def test_get_activity_owners_fields(self) -> None:
        """Test case for get_activity_owners_fields

        View ActivityOwner fields
        """
        pass

    def test_update_activity_owners(self) -> None:
        """Test case for update_activity_owners

        Update ActivityOwners
        """
        pass


if __name__ == '__main__':
    unittest.main()
