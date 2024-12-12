# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.activity_expense_api import ActivityExpenseApi


class TestActivityExpenseApi(unittest.TestCase):
    """ActivityExpenseApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ActivityExpenseApi()

    def tearDown(self) -> None:
        pass

    def test_create_activity_expense(self) -> None:
        """Test case for create_activity_expense

        Create ActivityExpenses
        """
        pass

    def test_delete_activity_expenses(self) -> None:
        """Test case for delete_activity_expenses

        Delete ActivityExpenses
        """
        pass

    def test_get_activity_expense_field_length(self) -> None:
        """Test case for get_activity_expense_field_length

        View ActivityExpense Field Length
        """
        pass

    def test_get_activity_expense_fields(self) -> None:
        """Test case for get_activity_expense_fields

        View ActivityExpense fields
        """
        pass

    def test_get_activity_expenses(self) -> None:
        """Test case for get_activity_expenses

        Read ActivityExpenses
        """
        pass

    def test_update_activity_expenses(self) -> None:
        """Test case for update_activity_expenses

        Update ActivityExpenses
        """
        pass


if __name__ == '__main__':
    unittest.main()