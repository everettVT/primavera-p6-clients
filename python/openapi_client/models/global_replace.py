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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class GlobalReplace(BaseModel):
    """
    GlobalReplace Entity
    """ # noqa: E501
    all_projects: Optional[StrictBool] = Field(default=None, description="The option used to set all of projects to which a user has access.", alias="AllProjects")
    global_replace_data: Optional[StrictStr] = Field(default=None, description="The Global Replace template.", alias="GlobalReplaceData")
    global_replace_name: Optional[StrictStr] = Field(default=None, description="The Global Replace template name.", alias="GlobalReplaceName")
    greplace_object_id: Optional[StrictInt] = Field(default=None, description="The unique id of the Global Replace template.", alias="GreplaceObjectId")
    project_id_name: Optional[StrictStr] = Field(default=None, description="Project ids and names that are separated by commas.", alias="ProjectIdName")
    project_ids: Optional[StrictStr] = Field(default=None, description="TProject ids that are separated by commas.", alias="ProjectIds")
    replace_field_name_one: Optional[StrictStr] = Field(default=None, description="First field name the user has selected to replace.", alias="ReplaceFieldNameOne")
    search_criteria: Optional[StrictStr] = Field(default=None, description="The criteria that is used to search and load business objects.", alias="SearchCriteria")
    subject_area_type: Optional[StrictStr] = Field(default=None, description="The name of the object to be updated.", alias="SubjectAreaType")
    user_object_id: Optional[StrictInt] = Field(default=None, description="The unique id of the associated user.", alias="UserObjectId")
    __properties: ClassVar[List[str]] = ["AllProjects", "GlobalReplaceData", "GlobalReplaceName", "GreplaceObjectId", "ProjectIdName", "ProjectIds", "ReplaceFieldNameOne", "SearchCriteria", "SubjectAreaType", "UserObjectId"]

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
        """Create an instance of GlobalReplace from a JSON string"""
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
        """Create an instance of GlobalReplace from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "AllProjects": obj.get("AllProjects"),
            "GlobalReplaceData": obj.get("GlobalReplaceData"),
            "GlobalReplaceName": obj.get("GlobalReplaceName"),
            "GreplaceObjectId": obj.get("GreplaceObjectId"),
            "ProjectIdName": obj.get("ProjectIdName"),
            "ProjectIds": obj.get("ProjectIds"),
            "ReplaceFieldNameOne": obj.get("ReplaceFieldNameOne"),
            "SearchCriteria": obj.get("SearchCriteria"),
            "SubjectAreaType": obj.get("SubjectAreaType"),
            "UserObjectId": obj.get("UserObjectId")
        })
        return _obj


