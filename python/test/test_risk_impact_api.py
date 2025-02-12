# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.risk_impact_api import RiskImpactApi


class TestRiskImpactApi(unittest.TestCase):
    """RiskImpactApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RiskImpactApi()

    def tearDown(self) -> None:
        pass

    def test_create_risk_impact(self) -> None:
        """Test case for create_risk_impact

        Create RiskImpacts
        """
        pass

    def test_delete_risk_impact(self) -> None:
        """Test case for delete_risk_impact

        Delete RiskImpacts
        """
        pass

    def test_get_risk_impact(self) -> None:
        """Test case for get_risk_impact

        Read RiskImpacts
        """
        pass

    def test_get_risk_impact_field_length(self) -> None:
        """Test case for get_risk_impact_field_length

        View RiskImpact Field Length
        """
        pass

    def test_get_risk_impact_fields(self) -> None:
        """Test case for get_risk_impact_fields

        View RiskImpact fields
        """
        pass

    def test_update_risk_impact(self) -> None:
        """Test case for update_risk_impact

        Update RiskImpacts
        """
        pass


if __name__ == '__main__':
    unittest.main()
