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
from openapi_client.models.member_project import MemberProject
from typing import Optional, Set
from typing_extensions import Self

class ProjectPortfolio(BaseModel):
    """
    ProjectPortfolio Entity
    """ # noqa: E501
    create_date: Optional[datetime] = Field(default=None, description="The date this project portfolio was created.", alias="CreateDate")
    create_user: Optional[StrictStr] = Field(default=None, description="The name of the user that created this project portfolio.", alias="CreateUser")
    description: Optional[StrictStr] = Field(default=None, description="The description of the project portfolio.", alias="Description")
    include_closed_projects: Optional[StrictBool] = Field(default=None, description="The flag that indicates whether closed projects are included in the portfolio.", alias="IncludeClosedProjects")
    include_what_if_projects: Optional[StrictBool] = Field(default=None, description="The flag that indicates whether what-if projects are included in the portfolio.", alias="IncludeWhatIfProjects")
    last_update_date: Optional[datetime] = Field(default=None, description="The date this project portfolio was last updated.", alias="LastUpdateDate")
    last_update_user: Optional[StrictStr] = Field(default=None, description="The name of the user that last updated this project portfolio.", alias="LastUpdateUser")
    name: StrictStr = Field(description="The name of the project portfolio.", alias="Name")
    object_id: Optional[StrictInt] = Field(default=None, description="The unique ID generated by the system.", alias="ObjectId")
    portfolio_user_id_array: Optional[StrictStr] = Field(default=None, alias="PortfolioUserIdArray")
    portfolio_user_name_array: Optional[StrictStr] = Field(default=None, alias="PortfolioUserNameArray")
    type: Optional[StrictStr] = Field(default=None, description="The type of the project portfolio: \"Manual\", \"Auto-Maintained\", or \"Filtered\".", alias="Type")
    user_name: Optional[StrictStr] = Field(default=None, description="The user's login name.", alias="UserName")
    user_object_id: Optional[StrictInt] = Field(default=None, description="The unique ID of a specific user who has access to the selected project portfolio.", alias="UserObjectId")
    member_project: Optional[List[MemberProject]] = Field(default=None, description="MemberProject", alias="MemberProject")
    __properties: ClassVar[List[str]] = ["CreateDate", "CreateUser", "Description", "IncludeClosedProjects", "IncludeWhatIfProjects", "LastUpdateDate", "LastUpdateUser", "Name", "ObjectId", "PortfolioUserIdArray", "PortfolioUserNameArray", "Type", "UserName", "UserObjectId", "MemberProject"]

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
        """Create an instance of ProjectPortfolio from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in member_project (list)
        _items = []
        if self.member_project:
            for _item_member_project in self.member_project:
                if _item_member_project:
                    _items.append(_item_member_project.to_dict())
            _dict['MemberProject'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProjectPortfolio from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "CreateDate": obj.get("CreateDate"),
            "CreateUser": obj.get("CreateUser"),
            "Description": obj.get("Description"),
            "IncludeClosedProjects": obj.get("IncludeClosedProjects"),
            "IncludeWhatIfProjects": obj.get("IncludeWhatIfProjects"),
            "LastUpdateDate": obj.get("LastUpdateDate"),
            "LastUpdateUser": obj.get("LastUpdateUser"),
            "Name": obj.get("Name"),
            "ObjectId": obj.get("ObjectId"),
            "PortfolioUserIdArray": obj.get("PortfolioUserIdArray"),
            "PortfolioUserNameArray": obj.get("PortfolioUserNameArray"),
            "Type": obj.get("Type"),
            "UserName": obj.get("UserName"),
            "UserObjectId": obj.get("UserObjectId"),
            "MemberProject": [MemberProject.from_dict(_item) for _item in obj["MemberProject"]] if obj.get("MemberProject") is not None else None
        })
        return _obj


