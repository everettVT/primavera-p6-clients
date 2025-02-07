# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.user_obs_api import UserOBSApi


class TestUserOBSApi(unittest.TestCase):
    """UserOBSApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UserOBSApi()

    def tearDown(self) -> None:
        pass

    def test_create_user_obs(self) -> None:
        """Test case for create_user_obs

        Create UserOBS
        """
        pass

    def test_delete_user_obs(self) -> None:
        """Test case for delete_user_obs

        Delete UserOBS
        """
        pass

    def test_get_user_obs(self) -> None:
        """Test case for get_user_obs

        Read UserOBS
        """
        pass

    def test_get_user_obs_field_length(self) -> None:
        """Test case for get_user_obs_field_length

        View UserOBS Field Length
        """
        pass

    def test_get_user_obs_fields(self) -> None:
        """Test case for get_user_obs_fields

        View UserOBS fields
        """
        pass

    def test_update_user_obs(self) -> None:
        """Test case for update_user_obs

        Update UserOBS
        """
        pass


if __name__ == '__main__':
    unittest.main()
