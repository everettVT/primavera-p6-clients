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

class ProjectIssue(BaseModel):
    """
    ProjectIssue Entity
    """ # noqa: E501
    activity_id: Optional[StrictStr] = Field(default=None, description="The short ID that uniquely identifies the activity within the project.", alias="ActivityId")
    activity_name: Optional[StrictStr] = Field(default=None, description="The name of the activity. The activity name does not have to be unique.", alias="ActivityName")
    activity_object_id: StrictInt = Field(description="The unique ID of the activity to which the project issue applies.", alias="ActivityObjectId")
    actual_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The actual value of the threshold parameter for the project issue. Issues are automatically generated by the threshold monitor when actual values of threshold parameters exceed target values.", alias="ActualValue")
    create_date: Optional[datetime] = Field(default=None, description="The date this project issue was created.", alias="CreateDate")
    create_user: Optional[StrictStr] = Field(default=None, description="The name of the user that created this project issue.", alias="CreateUser")
    date_identified: Optional[datetime] = Field(default=None, description="The date the project issue was identified.", alias="DateIdentified")
    identified_by: Optional[StrictStr] = Field(default=None, description="The identifier of the project issue. This may be the name of the user who created the project issue or Monitor, if the project issue was automatically generated by the threshold monitor.", alias="IdentifiedBy")
    is_baseline: Optional[StrictBool] = Field(default=None, description="The boolean value indicating if this business object is related to a Project or Baseline", alias="IsBaseline")
    is_template: Optional[StrictBool] = Field(default=None, description="The boolean value indicating if this business object is related to a template Project.", alias="IsTemplate")
    last_update_date: Optional[datetime] = Field(default=None, description="The date this project issue was last updated.", alias="LastUpdateDate")
    last_update_user: Optional[StrictStr] = Field(default=None, description="The name of the user that last updated this project issue.", alias="LastUpdateUser")
    lower_threshold: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The lower value of the threshold parameter that triggered the project issue. Issues are triggered when the actual/observed parameters values are less than or equal to the lower threshold.", alias="LowerThreshold")
    name: StrictStr = Field(description="The name of the project issue. Issues which are automatically generated by the threshold monitor are named after the threshold parameter that triggered the project issue.", alias="Name")
    notes: Optional[StrictStr] = Field(default=None, description="The notes associated with the project issue.", alias="Notes")
    obs_name: Optional[StrictStr] = Field(default=None, description="The name of the person/role in the organization, sometimes referred to as the \"responsible manager\".", alias="OBSName")
    obs_object_id: Optional[StrictInt] = Field(default=None, description="The unique ID of the project manager from the project's OBS tree who is responsible for the project issue.", alias="OBSObjectId")
    object_id: Optional[StrictInt] = Field(default=None, description="The unique ID generated by the system.", alias="ObjectId")
    priority: Optional[StrictStr] = Field(default=None, description="The priority of the project issue. Valid values are 'Top', 'High', 'Normal', 'Low', and 'Lowest'.", alias="Priority")
    project_id: Optional[StrictStr] = Field(default=None, description="The short code that uniquely identifies the project.", alias="ProjectId")
    project_name: Optional[StrictStr] = Field(default=None, description="The name of the associated project.", alias="ProjectName")
    project_object_id: StrictInt = Field(description="The unique ID of the associated project.", alias="ProjectObjectId")
    project_threshold_object_id: Optional[StrictInt] = Field(default=None, description="The unique ID of the associated project threshold for the project issue.", alias="ProjectThresholdObjectId")
    raw_text_note: Optional[StrictStr] = Field(default=None, description="The notes associated with the project issue.", alias="RawTextNote")
    resolution_date: Optional[datetime] = Field(default=None, description="The date the project issue was resolved.", alias="ResolutionDate")
    resource_id: Optional[StrictStr] = Field(default=None, description="The short code that uniquely identifies the resource.", alias="ResourceId")
    resource_name: Optional[StrictStr] = Field(default=None, description="The name of the resource.", alias="ResourceName")
    resource_object_id: Optional[StrictInt] = Field(default=None, description="The unique ID of the associated resource for this project issue. If a parent resource is selected, the issue applies to all child resources as well.", alias="ResourceObjectId")
    status: Optional[StrictStr] = Field(default=None, description="The current status of the project issue. Valid values are 'Open', 'On Hold', and 'Closed'.", alias="Status")
    threshold_parameter_object_id: Optional[StrictInt] = Field(default=None, description="The unique ID of the associated threshold parameter for the project issue.", alias="ThresholdParameterObjectId")
    upper_threshold: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The upper value of the threshold parameter which triggered the project issue. Issues are triggered when the actual/observed parameters values are greater than or equal to the upper threshold.", alias="UpperThreshold")
    wbs_code: Optional[StrictStr] = Field(default=None, description="The short code assigned to each WBS element for identification. Each WBS element is uniquely identified by concatenating its own code together with its parents' codes.", alias="WBSCode")
    wbs_name: Optional[StrictStr] = Field(default=None, description="The name of the WBS element.", alias="WBSName")
    wbs_object_id: StrictInt = Field(description="The unique ID of the WBS to which the project issue applies. If a parent WBS is selected, the project issue applies to all child elements as well. If the top WBS is selected, the project issue applies to the entire project.", alias="WBSObjectId")
    __properties: ClassVar[List[str]] = ["ActivityId", "ActivityName", "ActivityObjectId", "ActualValue", "CreateDate", "CreateUser", "DateIdentified", "IdentifiedBy", "IsBaseline", "IsTemplate", "LastUpdateDate", "LastUpdateUser", "LowerThreshold", "Name", "Notes", "OBSName", "OBSObjectId", "ObjectId", "Priority", "ProjectId", "ProjectName", "ProjectObjectId", "ProjectThresholdObjectId", "RawTextNote", "ResolutionDate", "ResourceId", "ResourceName", "ResourceObjectId", "Status", "ThresholdParameterObjectId", "UpperThreshold", "WBSCode", "WBSName", "WBSObjectId"]

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
        """Create an instance of ProjectIssue from a JSON string"""
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
        """Create an instance of ProjectIssue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ActivityId": obj.get("ActivityId"),
            "ActivityName": obj.get("ActivityName"),
            "ActivityObjectId": obj.get("ActivityObjectId"),
            "ActualValue": obj.get("ActualValue"),
            "CreateDate": obj.get("CreateDate"),
            "CreateUser": obj.get("CreateUser"),
            "DateIdentified": obj.get("DateIdentified"),
            "IdentifiedBy": obj.get("IdentifiedBy"),
            "IsBaseline": obj.get("IsBaseline"),
            "IsTemplate": obj.get("IsTemplate"),
            "LastUpdateDate": obj.get("LastUpdateDate"),
            "LastUpdateUser": obj.get("LastUpdateUser"),
            "LowerThreshold": obj.get("LowerThreshold"),
            "Name": obj.get("Name"),
            "Notes": obj.get("Notes"),
            "OBSName": obj.get("OBSName"),
            "OBSObjectId": obj.get("OBSObjectId"),
            "ObjectId": obj.get("ObjectId"),
            "Priority": obj.get("Priority"),
            "ProjectId": obj.get("ProjectId"),
            "ProjectName": obj.get("ProjectName"),
            "ProjectObjectId": obj.get("ProjectObjectId"),
            "ProjectThresholdObjectId": obj.get("ProjectThresholdObjectId"),
            "RawTextNote": obj.get("RawTextNote"),
            "ResolutionDate": obj.get("ResolutionDate"),
            "ResourceId": obj.get("ResourceId"),
            "ResourceName": obj.get("ResourceName"),
            "ResourceObjectId": obj.get("ResourceObjectId"),
            "Status": obj.get("Status"),
            "ThresholdParameterObjectId": obj.get("ThresholdParameterObjectId"),
            "UpperThreshold": obj.get("UpperThreshold"),
            "WBSCode": obj.get("WBSCode"),
            "WBSName": obj.get("WBSName"),
            "WBSObjectId": obj.get("WBSObjectId")
        })
        return _obj


