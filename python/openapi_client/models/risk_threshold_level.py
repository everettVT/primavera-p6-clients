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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class RiskThresholdLevel(BaseModel):
    """
    RiskThresholdLevel Entity
    """ # noqa: E501
    code: StrictStr = Field(description="The 10 character code for the threshold level. Must be unique.", alias="Code")
    color: Optional[StrictStr] = Field(default=None, description="The Hex representation for the color e.g. 0xFFFFFF.", alias="Color")
    cost_range: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The cost range of the threshold level.", alias="CostRange")
    create_date: Optional[datetime] = Field(default=None, description="The date this threshold level was created.", alias="CreateDate")
    create_user: Optional[StrictStr] = Field(default=None, description="The name of the user that created the threshold level.", alias="CreateUser")
    last_update_date: Optional[datetime] = Field(default=None, description="The date this threshold level was last updated.", alias="LastUpdateDate")
    last_update_user: Optional[StrictStr] = Field(default=None, description="The name of the user that last updated the threshold level.", alias="LastUpdateUser")
    level: Optional[StrictInt] = Field(default=None, description="The valid values are between 0 and 9. Defines a level for the Risk Threshold.", alias="Level")
    name: Optional[StrictStr] = Field(default=None, description="The 40 character name for the threshold level. Does not need to be unique.", alias="Name")
    object_id: Optional[StrictInt] = Field(default=None, description="The unique ID generated by the system.", alias="ObjectId")
    probability_range: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The probability range of the threshold level.", alias="ProbabilityRange")
    range: Optional[StrictStr] = Field(default=None, description="The user defined range.", alias="Range")
    risk_threshold_name: Optional[StrictStr] = Field(default=None, description="The name of the associated risk score type.", alias="RiskThresholdName")
    risk_threshold_object_id: StrictInt = Field(description="The unique ID of the associated Risk Threshold.", alias="RiskThresholdObjectId")
    schedule_range: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The schedule range of the threshold level.", alias="ScheduleRange")
    threshold_type: Optional[StrictStr] = Field(default=None, description="The type of Risk Threshold. Valid types are 'Probability', 'Tolerance', 'Schedule', 'Cost', 'Relative Schedule', 'Relative Cost' and 'User Defined'.", alias="ThresholdType")
    tolerance_range: Optional[StrictInt] = Field(default=None, description="The tolerance range of the threshold level.", alias="ToleranceRange")
    __properties: ClassVar[List[str]] = ["Code", "Color", "CostRange", "CreateDate", "CreateUser", "LastUpdateDate", "LastUpdateUser", "Level", "Name", "ObjectId", "ProbabilityRange", "Range", "RiskThresholdName", "RiskThresholdObjectId", "ScheduleRange", "ThresholdType", "ToleranceRange"]

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
        """Create an instance of RiskThresholdLevel from a JSON string"""
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
        """Create an instance of RiskThresholdLevel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Code": obj.get("Code"),
            "Color": obj.get("Color"),
            "CostRange": obj.get("CostRange"),
            "CreateDate": obj.get("CreateDate"),
            "CreateUser": obj.get("CreateUser"),
            "LastUpdateDate": obj.get("LastUpdateDate"),
            "LastUpdateUser": obj.get("LastUpdateUser"),
            "Level": obj.get("Level"),
            "Name": obj.get("Name"),
            "ObjectId": obj.get("ObjectId"),
            "ProbabilityRange": obj.get("ProbabilityRange"),
            "Range": obj.get("Range"),
            "RiskThresholdName": obj.get("RiskThresholdName"),
            "RiskThresholdObjectId": obj.get("RiskThresholdObjectId"),
            "ScheduleRange": obj.get("ScheduleRange"),
            "ThresholdType": obj.get("ThresholdType"),
            "ToleranceRange": obj.get("ToleranceRange")
        })
        return _obj

