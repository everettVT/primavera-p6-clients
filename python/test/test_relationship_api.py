# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.relationship_api import RelationshipApi


class TestRelationshipApi(unittest.TestCase):
    """RelationshipApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RelationshipApi()

    def tearDown(self) -> None:
        pass

    def test_create_relationship(self) -> None:
        """Test case for create_relationship

        Create Relationship
        """
        pass

    def test_delete_relationship(self) -> None:
        """Test case for delete_relationship

        Delete Relationship
        """
        pass

    def test_get_relationship(self) -> None:
        """Test case for get_relationship

        Read Relationship
        """
        pass

    def test_get_relationship_field_length(self) -> None:
        """Test case for get_relationship_field_length

        View Relationship Field Length
        """
        pass

    def test_get_relationship_fields(self) -> None:
        """Test case for get_relationship_fields

        View Relationship fields
        """
        pass

    def test_update_relationship(self) -> None:
        """Test case for update_relationship

        Update Relationship
        """
        pass


if __name__ == '__main__':
    unittest.main()