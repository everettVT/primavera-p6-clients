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

class ResourceAssignmentCreate(BaseModel):
    """
    ResourceAssignmentCreate Entity
    """ # noqa: E501
    activity_object_id: StrictInt = Field(description="The unique ID of the activity to which the associated assignment is assigned.", alias="ActivityObjectId")
    actual_finish_date: Optional[datetime] = Field(default=None, description="The date the resource actually finished working on the activity.", alias="ActualFinishDate")
    actual_start_date: Optional[datetime] = Field(default=None, description="The date the resource actually started working on the activity.", alias="ActualStartDate")
    actual_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The actual units worked by the resource on this activity.", alias="ActualUnits")
    assignment_is_read: Optional[StrictStr] = Field(default=None, description="To determine whether or not the newly created assignment from P6 Team Member Web is viewed by the manager in the Control Status Update.", alias="AssignmentIsRead")
    change_set_object_id: Optional[StrictInt] = Field(default=None, description="The unique ID of the associated Changeset.", alias="ChangeSetObjectId")
    var_date: Optional[datetime] = Field(default=None, description="The date of the transaction.", alias="Date")
    project_object_id: Optional[StrictInt] = Field(default=None, description="The unique identifier of the project that is associated with the ResourceAssignmentCreate object.", alias="ProjectObjectId")
    remaining_duration: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The remaining finish date for the resource working on the activity.", alias="RemainingDuration")
    remaining_finish_date: Optional[datetime] = Field(default=None, description="The remaining finish date for the resource working on the activity.", alias="RemainingFinishDate")
    remaining_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The remaining units of work to be performed by this resource on this activity.", alias="RemainingUnits")
    request_user_object_id: Optional[StrictInt] = Field(default=None, description="The unique ID of the user modifying the task, assignment or step.", alias="RequestUserObjectId")
    resource_assignment_create_object_id: Optional[StrictInt] = Field(default=None, description="The unique identifier of the ResourceAssignment that is associated to the ResourceAssignmentCreate.", alias="ResourceAssignmentCreateObjectId")
    resource_assignment_object_id: Optional[StrictInt] = Field(default=None, description="The unique identifier of the ResourceAssignment that is associated with ResourceAssignmentCreate object.", alias="ResourceAssignmentObjectId")
    resource_object_id: StrictInt = Field(description="The unique identifier of the associated resource.", alias="ResourceObjectId")
    status: Optional[StrictStr] = Field(default=None, description="The status of the resource assignment. [not sure about the filter orderable or read only]", alias="Status")
    __properties: ClassVar[List[str]] = ["ActivityObjectId", "ActualFinishDate", "ActualStartDate", "ActualUnits", "AssignmentIsRead", "ChangeSetObjectId", "Date", "ProjectObjectId", "RemainingDuration", "RemainingFinishDate", "RemainingUnits", "RequestUserObjectId", "ResourceAssignmentCreateObjectId", "ResourceAssignmentObjectId", "ResourceObjectId", "Status"]

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
        """Create an instance of ResourceAssignmentCreate from a JSON string"""
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
        """Create an instance of ResourceAssignmentCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ActivityObjectId": obj.get("ActivityObjectId"),
            "ActualFinishDate": obj.get("ActualFinishDate"),
            "ActualStartDate": obj.get("ActualStartDate"),
            "ActualUnits": obj.get("ActualUnits"),
            "AssignmentIsRead": obj.get("AssignmentIsRead"),
            "ChangeSetObjectId": obj.get("ChangeSetObjectId"),
            "Date": obj.get("Date"),
            "ProjectObjectId": obj.get("ProjectObjectId"),
            "RemainingDuration": obj.get("RemainingDuration"),
            "RemainingFinishDate": obj.get("RemainingFinishDate"),
            "RemainingUnits": obj.get("RemainingUnits"),
            "RequestUserObjectId": obj.get("RequestUserObjectId"),
            "ResourceAssignmentCreateObjectId": obj.get("ResourceAssignmentCreateObjectId"),
            "ResourceAssignmentObjectId": obj.get("ResourceAssignmentObjectId"),
            "ResourceObjectId": obj.get("ResourceObjectId"),
            "Status": obj.get("Status")
        })
        return _obj


