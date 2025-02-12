# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.wbs_api import WBSApi


class TestWBSApi(unittest.TestCase):
    """WBSApi unit test stubs"""

    def setUp(self) -> None:
        self.api = WBSApi()

    def tearDown(self) -> None:
        pass

    def test_create_wbs(self) -> None:
        """Test case for create_wbs

        Create WBS
        """
        pass

    def test_delete_wbs(self) -> None:
        """Test case for delete_wbs

        Delete WBS
        """
        pass

    def test_get_eps_fields1(self) -> None:
        """Test case for get_eps_fields1

        View WBS fields
        """
        pass

    def test_get_wbs(self) -> None:
        """Test case for get_wbs

        Read WBS
        """
        pass

    def test_get_wbs_field_length(self) -> None:
        """Test case for get_wbs_field_length

        View WBS Field Length
        """
        pass

    def test_update_wbs(self) -> None:
        """Test case for update_wbs

        Update WBS
        """
        pass


if __name__ == '__main__':
    unittest.main()
