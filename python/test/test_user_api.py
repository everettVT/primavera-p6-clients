# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.user_api import UserApi


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UserApi()

    def tearDown(self) -> None:
        pass

    def test_create_user(self) -> None:
        """Test case for create_user

        Create Users
        """
        pass

    def test_delete_user(self) -> None:
        """Test case for delete_user

        Delete Users
        """
        pass

    def test_get_user_field_length(self) -> None:
        """Test case for get_user_field_length

        View User Field Length
        """
        pass

    def test_get_user_fields(self) -> None:
        """Test case for get_user_fields

        View User fields
        """
        pass

    def test_get_users(self) -> None:
        """Test case for get_users

        Read Users
        """
        pass

    def test_update_user(self) -> None:
        """Test case for update_user

        Update Users
        """
        pass


if __name__ == '__main__':
    unittest.main()
