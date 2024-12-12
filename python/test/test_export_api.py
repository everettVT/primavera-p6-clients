# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.export_api import ExportApi


class TestExportApi(unittest.TestCase):
    """ExportApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ExportApi()

    def tearDown(self) -> None:
        pass

    def test_download_files(self) -> None:
        """Test case for download_files

        Download Files
        """
        pass

    def test_export_impdar_project(self) -> None:
        """Test case for export_impdar_project

        Export ImpdarProject
        """
        pass

    def test_export_project(self) -> None:
        """Test case for export_project

        Export Projects
        """
        pass

    def test_export_project1(self) -> None:
        """Test case for export_project1

        Export Project
        """
        pass


if __name__ == '__main__':
    unittest.main()