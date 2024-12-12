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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class TimesheetDelegate(BaseModel):
    """
    TimesheetDelegate Entity
    """ # noqa: E501
    active_flag: Optional[StrictBool] = Field(default=None, description="The flag indicating whether this delegate is active.", alias="ActiveFlag")
    approver_user_name: Optional[StrictStr] = Field(default=None, description="The approver user's login name.", alias="ApproverUserName")
    approver_user_object_id: Optional[StrictInt] = Field(default=None, description="The unique ID of the approver user.", alias="ApproverUserObjectId")
    create_date: Optional[datetime] = Field(default=None, description="The date this timesheet delegate was created.", alias="CreateDate")
    create_user: Optional[StrictStr] = Field(default=None, description="The name of the user that created this timesheet delegate.", alias="CreateUser")
    delegate_user_email_address: Optional[StrictStr] = Field(default=None, description="The delegate user's email address.", alias="DelegateUserEmailAddress")
    delegate_user_name: Optional[StrictStr] = Field(default=None, description="The delegate user's login name.", alias="DelegateUserName")
    delegate_user_object_id: Optional[StrictInt] = Field(default=None, description="The unique ID of the delegate user.", alias="DelegateUserObjectId")
    last_update_date: Optional[datetime] = Field(default=None, description="The date this timesheet delegate was last updated.", alias="LastUpdateDate")
    last_update_user: Optional[StrictStr] = Field(default=None, description="The name of the user that last updated this timesheet delegate.", alias="LastUpdateUser")
    object_id: Optional[StrictInt] = Field(default=None, description="The unique ID generated by the system.", alias="ObjectId")
    project_object_id: Optional[StrictInt] = Field(default=None, description="The unique ID of the associated project.", alias="ProjectObjectId")
    __properties: ClassVar[List[str]] = ["ActiveFlag", "ApproverUserName", "ApproverUserObjectId", "CreateDate", "CreateUser", "DelegateUserEmailAddress", "DelegateUserName", "DelegateUserObjectId", "LastUpdateDate", "LastUpdateUser", "ObjectId", "ProjectObjectId"]

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
        """Create an instance of TimesheetDelegate from a JSON string"""
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
        """Create an instance of TimesheetDelegate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ActiveFlag": obj.get("ActiveFlag"),
            "ApproverUserName": obj.get("ApproverUserName"),
            "ApproverUserObjectId": obj.get("ApproverUserObjectId"),
            "CreateDate": obj.get("CreateDate"),
            "CreateUser": obj.get("CreateUser"),
            "DelegateUserEmailAddress": obj.get("DelegateUserEmailAddress"),
            "DelegateUserName": obj.get("DelegateUserName"),
            "DelegateUserObjectId": obj.get("DelegateUserObjectId"),
            "LastUpdateDate": obj.get("LastUpdateDate"),
            "LastUpdateUser": obj.get("LastUpdateUser"),
            "ObjectId": obj.get("ObjectId"),
            "ProjectObjectId": obj.get("ProjectObjectId")
        })
        return _obj

