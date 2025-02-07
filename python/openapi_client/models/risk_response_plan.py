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

class RiskResponsePlan(BaseModel):
    """
    RiskResponsePlan Entity
    """ # noqa: E501
    actual_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The actual cost.", alias="ActualCost")
    create_date: Optional[datetime] = Field(default=None, description="The date this risk response plan was created.", alias="CreateDate")
    create_user: Optional[StrictStr] = Field(default=None, description="The name of the user that created the risk response plan.", alias="CreateUser")
    finish_date: Optional[datetime] = Field(default=None, description="The finish date of the risk response action. If an activity is assigned, the risk response action uses the activity finish date.", alias="FinishDate")
    id: StrictStr = Field(description="The ID of the risk response plan. This must be unique within the assigned risk.", alias="Id")
    is_active: Optional[StrictBool] = Field(default=None, description="The indication of whether the response plan is currently active for the associated risk. Only one response plan can be active at a given time for a risk.", alias="IsActive")
    is_baseline: Optional[StrictBool] = Field(default=None, description="The boolean value indicating if this business object is related to a Project or Baseline.", alias="IsBaseline")
    is_template: Optional[StrictBool] = Field(default=None, description="The boolean value indicating if this business object is related to a template Project.", alias="IsTemplate")
    last_update_date: Optional[datetime] = Field(default=None, description="The date this risk response plan was last updated.", alias="LastUpdateDate")
    last_update_user: Optional[StrictStr] = Field(default=None, description="The name of the user that last updated the risk response plan.", alias="LastUpdateUser")
    name: Optional[StrictStr] = Field(default=None, description="The name of the risk response plan.", alias="Name")
    object_id: Optional[StrictInt] = Field(default=None, description="The unique ID generated by the system.", alias="ObjectId")
    planned_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The planned cost.", alias="PlannedCost")
    planned_finish_date: Optional[datetime] = Field(default=None, description="The planned finish date.", alias="PlannedFinishDate")
    planned_start_date: Optional[datetime] = Field(default=None, description="The planned start date.", alias="PlannedStartDate")
    project_id: Optional[StrictStr] = Field(default=None, description="The short name of the associated project.", alias="ProjectId")
    project_name: Optional[StrictStr] = Field(default=None, description="The name of the associated project.", alias="ProjectName")
    project_object_id: Optional[StrictInt] = Field(default=None, description="The unique ID of the associated project.", alias="ProjectObjectId")
    remaining_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The remaining cost associated with the risk response action.", alias="RemainingCost")
    response_type: Optional[StrictStr] = Field(default=None, description="The risk response plan type. If the risk is a threat, the valid types are 'Avoid', 'Transfer', 'Reduce', and 'Accept'. If the risk is a opportunity, the valid types are 'Exploit', 'Facilitate', 'Enhance', and 'Reject'.", alias="ResponseType")
    risk_id: Optional[StrictStr] = Field(default=None, description="The ID of the risk.", alias="RiskId")
    risk_name: Optional[StrictStr] = Field(default=None, description="The name of the risk.", alias="RiskName")
    risk_object_id: StrictInt = Field(description="The unique ID of the associated risk.", alias="RiskObjectId")
    score: Optional[StrictInt] = Field(default=None, description="The risk score from the numeric PID after all response actions of the response plan have been completed. The post response plan score is set from the response action with the latest finish date and the lowest score when more than one response action has the same date.", alias="Score")
    score_color: Optional[StrictStr] = Field(default=None, description="The color of the tolerance threshold for the score value.", alias="ScoreColor")
    score_text: Optional[StrictStr] = Field(default=None, description="The risk score from the alphanumeric PID after all response actions of the response plan have been completed. The post response plan score is set from the response action with the latest finish date and the lowest score when more than one response action has the same date.", alias="ScoreText")
    start_date: Optional[datetime] = Field(default=None, description="The start date of the risk response action. If an activity is assigned, the risk response action uses the activity start date.", alias="StartDate")
    __properties: ClassVar[List[str]] = ["ActualCost", "CreateDate", "CreateUser", "FinishDate", "Id", "IsActive", "IsBaseline", "IsTemplate", "LastUpdateDate", "LastUpdateUser", "Name", "ObjectId", "PlannedCost", "PlannedFinishDate", "PlannedStartDate", "ProjectId", "ProjectName", "ProjectObjectId", "RemainingCost", "ResponseType", "RiskId", "RiskName", "RiskObjectId", "Score", "ScoreColor", "ScoreText", "StartDate"]

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
        """Create an instance of RiskResponsePlan from a JSON string"""
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
        """Create an instance of RiskResponsePlan from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ActualCost": obj.get("ActualCost"),
            "CreateDate": obj.get("CreateDate"),
            "CreateUser": obj.get("CreateUser"),
            "FinishDate": obj.get("FinishDate"),
            "Id": obj.get("Id"),
            "IsActive": obj.get("IsActive"),
            "IsBaseline": obj.get("IsBaseline"),
            "IsTemplate": obj.get("IsTemplate"),
            "LastUpdateDate": obj.get("LastUpdateDate"),
            "LastUpdateUser": obj.get("LastUpdateUser"),
            "Name": obj.get("Name"),
            "ObjectId": obj.get("ObjectId"),
            "PlannedCost": obj.get("PlannedCost"),
            "PlannedFinishDate": obj.get("PlannedFinishDate"),
            "PlannedStartDate": obj.get("PlannedStartDate"),
            "ProjectId": obj.get("ProjectId"),
            "ProjectName": obj.get("ProjectName"),
            "ProjectObjectId": obj.get("ProjectObjectId"),
            "RemainingCost": obj.get("RemainingCost"),
            "ResponseType": obj.get("ResponseType"),
            "RiskId": obj.get("RiskId"),
            "RiskName": obj.get("RiskName"),
            "RiskObjectId": obj.get("RiskObjectId"),
            "Score": obj.get("Score"),
            "ScoreColor": obj.get("ScoreColor"),
            "ScoreText": obj.get("ScoreText"),
            "StartDate": obj.get("StartDate")
        })
        return _obj


