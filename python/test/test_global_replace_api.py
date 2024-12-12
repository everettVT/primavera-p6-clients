# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.global_replace_api import GlobalReplaceApi


class TestGlobalReplaceApi(unittest.TestCase):
    """GlobalReplaceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = GlobalReplaceApi()

    def tearDown(self) -> None:
        pass

    def test_get_global_replace(self) -> None:
        """Test case for get_global_replace

        Read GlobalReplace
        """
        pass

    def test_get_global_replace_field_length(self) -> None:
        """Test case for get_global_replace_field_length

        View GlobalReplace Field Length
        """
        pass

    def test_get_global_replace_fields(self) -> None:
        """Test case for get_global_replace_fields

        View GlobalReplace fields
        """
        pass

    def test_update_global_replace(self) -> None:
        """Test case for update_global_replace

        Update GlobalReplace
        """
        pass


if __name__ == '__main__':
    unittest.main()
