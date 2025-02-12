# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.eps_api import EPSApi


class TestEPSApi(unittest.TestCase):
    """EPSApi unit test stubs"""

    def setUp(self) -> None:
        self.api = EPSApi()

    def tearDown(self) -> None:
        pass

    def test_create_eps(self) -> None:
        """Test case for create_eps

        Create EPS
        """
        pass

    def test_delete_eps(self) -> None:
        """Test case for delete_eps

        Delete EPS
        """
        pass

    def test_get_eps(self) -> None:
        """Test case for get_eps

        Read EPS
        """
        pass

    def test_get_eps_field_length(self) -> None:
        """Test case for get_eps_field_length

        View EPS Field Length
        """
        pass

    def test_get_eps_fields(self) -> None:
        """Test case for get_eps_fields

        View EPS fields
        """
        pass

    def test_update_eps(self) -> None:
        """Test case for update_eps

        Update EPS
        """
        pass


if __name__ == '__main__':
    unittest.main()
