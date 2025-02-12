# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class ActivityPeriodActual(BaseModel):
    """
    ActivityPeriodActual Entity
    """ # noqa: E501
    activity_object_id: StrictInt = Field(description="The unique ID of the associated activity.", alias="ActivityObjectId")
    actual_expense_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The actual expense cost on this activity during a financial period.", alias="ActualExpenseCost")
    actual_labor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The actual labor cost on this activity during a financial period.", alias="ActualLaborCost")
    actual_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The actual labor units on this activity during a financial period.", alias="ActualLaborUnits")
    actual_material_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The actual material cost on this activity during a financial period.", alias="ActualMaterialCost")
    actual_non_labor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The actual nonlabor cost on this activity during a financial period.", alias="ActualNonLaborCost")
    actual_non_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The actual nonlabor units on this activity during a financial period.", alias="ActualNonLaborUnits")
    create_date: Optional[datetime] = Field(default=None, description="The date this activity period actual was created.", alias="CreateDate")
    create_user: Optional[StrictStr] = Field(default=None, description="The name of the user that created this activity period actual.", alias="CreateUser")
    earned_value_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The earned value cost on this activity during a financial period.", alias="EarnedValueCost")
    earned_value_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The earned value labor units on this activity during a financial period.", alias="EarnedValueLaborUnits")
    financial_period_object_id: StrictInt = Field(description="The unique ID of the associated financial period.", alias="FinancialPeriodObjectId")
    is_baseline: Optional[StrictBool] = Field(default=None, description="The boolean value indicating if this business object is related to a Project or Baseline", alias="IsBaseline")
    is_template: Optional[StrictBool] = Field(default=None, description="The boolean value indicating if this business object is related to a template Project.", alias="IsTemplate")
    last_update_date: Optional[datetime] = Field(default=None, description="The date this activity period actual was last updated.", alias="LastUpdateDate")
    last_update_user: Optional[StrictStr] = Field(default=None, description="The name of the user that last updated this activity period actual.", alias="LastUpdateUser")
    planned_value_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The planned value cost on this activity during a financial period.", alias="PlannedValueCost")
    planned_value_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The planned value labor units on this activity during a financial period.", alias="PlannedValueLaborUnits")
    project_object_id: Optional[StrictInt] = Field(default=None, description="The unique ID of the associated project.", alias="ProjectObjectId")
    wbs_object_id: Optional[StrictInt] = Field(default=None, description="The unique ID of the WBS for the activity.", alias="WBSObjectId")
    __properties: ClassVar[List[str]] = ["ActivityObjectId", "ActualExpenseCost", "ActualLaborCost", "ActualLaborUnits", "ActualMaterialCost", "ActualNonLaborCost", "ActualNonLaborUnits", "CreateDate", "CreateUser", "EarnedValueCost", "EarnedValueLaborUnits", "FinancialPeriodObjectId", "IsBaseline", "IsTemplate", "LastUpdateDate", "LastUpdateUser", "PlannedValueCost", "PlannedValueLaborUnits", "ProjectObjectId", "WBSObjectId"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ActivityPeriodActual from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ActivityPeriodActual from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ActivityObjectId": obj.get("ActivityObjectId"),
            "ActualExpenseCost": obj.get("ActualExpenseCost"),
            "ActualLaborCost": obj.get("ActualLaborCost"),
            "ActualLaborUnits": obj.get("ActualLaborUnits"),
            "ActualMaterialCost": obj.get("ActualMaterialCost"),
            "ActualNonLaborCost": obj.get("ActualNonLaborCost"),
            "ActualNonLaborUnits": obj.get("ActualNonLaborUnits"),
            "CreateDate": obj.get("CreateDate"),
            "CreateUser": obj.get("CreateUser"),
            "EarnedValueCost": obj.get("EarnedValueCost"),
            "EarnedValueLaborUnits": obj.get("EarnedValueLaborUnits"),
            "FinancialPeriodObjectId": obj.get("FinancialPeriodObjectId"),
            "IsBaseline": obj.get("IsBaseline"),
            "IsTemplate": obj.get("IsTemplate"),
            "LastUpdateDate": obj.get("LastUpdateDate"),
            "LastUpdateUser": obj.get("LastUpdateUser"),
            "PlannedValueCost": obj.get("PlannedValueCost"),
            "PlannedValueLaborUnits": obj.get("PlannedValueLaborUnits"),
            "ProjectObjectId": obj.get("ProjectObjectId"),
            "WBSObjectId": obj.get("WBSObjectId")
        })
        return _obj


