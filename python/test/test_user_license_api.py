# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.user_license_api import UserLicenseApi


class TestUserLicenseApi(unittest.TestCase):
    """UserLicenseApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UserLicenseApi()

    def tearDown(self) -> None:
        pass

    def test_create_user_license(self) -> None:
        """Test case for create_user_license

        Create UserLicense
        """
        pass

    def test_delete_user_license(self) -> None:
        """Test case for delete_user_license

        Delete UserLicense
        """
        pass

    def test_get_user_license(self) -> None:
        """Test case for get_user_license

        Read UserLicense
        """
        pass

    def test_get_user_license_field_length(self) -> None:
        """Test case for get_user_license_field_length

        View UserLicense Field Length
        """
        pass

    def test_get_user_license_fields(self) -> None:
        """Test case for get_user_license_fields

        View UserLicense fields
        """
        pass


if __name__ == '__main__':
    unittest.main()
