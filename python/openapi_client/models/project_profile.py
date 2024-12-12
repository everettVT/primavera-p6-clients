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
from openapi_client.models.privilege import Privilege
from typing import Optional, Set
from typing_extensions import Self

class ProjectProfile(BaseModel):
    """
    ProjectProfile Entity
    """ # noqa: E501
    create_date: Optional[datetime] = Field(default=None, description="The date this project profile was created.", alias="CreateDate")
    create_user: Optional[StrictStr] = Field(default=None, description="The name of the user that created this project profile.", alias="CreateUser")
    is_default: Optional[StrictBool] = Field(default=None, description="The flag that indicates this security profile is the default profile assigned to UserOBS objects. When a ProjectProfile object is deleted from the database, all UserOBS objects assigned to that profile are reassigned to the default profile. You cannot not delete the default profile.", alias="IsDefault")
    is_super_user: Optional[StrictBool] = Field(default=None, description="The flag that indicates this is the project superuser profile, which gives a user read/write privileges for all project and OBS specific information and features", alias="IsSuperUser")
    last_update_date: Optional[datetime] = Field(default=None, description="The date this project profile was last updated.", alias="LastUpdateDate")
    last_update_user: Optional[StrictStr] = Field(default=None, description="The name of the user that last updated this project profile.", alias="LastUpdateUser")
    name: StrictStr = Field(description="The unique name of this project profile", alias="Name")
    object_id: Optional[StrictInt] = Field(default=None, description="The unique ID generated by the system.", alias="ObjectId")
    privilege: Optional[List[Privilege]] = Field(default=None, description="Privilege", alias="Privilege")
    __properties: ClassVar[List[str]] = ["CreateDate", "CreateUser", "IsDefault", "IsSuperUser", "LastUpdateDate", "LastUpdateUser", "Name", "ObjectId", "Privilege"]

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
        """Create an instance of ProjectProfile from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in privilege (list)
        _items = []
        if self.privilege:
            for _item_privilege in self.privilege:
                if _item_privilege:
                    _items.append(_item_privilege.to_dict())
            _dict['Privilege'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProjectProfile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "CreateDate": obj.get("CreateDate"),
            "CreateUser": obj.get("CreateUser"),
            "IsDefault": obj.get("IsDefault"),
            "IsSuperUser": obj.get("IsSuperUser"),
            "LastUpdateDate": obj.get("LastUpdateDate"),
            "LastUpdateUser": obj.get("LastUpdateUser"),
            "Name": obj.get("Name"),
            "ObjectId": obj.get("ObjectId"),
            "Privilege": [Privilege.from_dict(_item) for _item in obj["Privilege"]] if obj.get("Privilege") is not None else None
        })
        return _obj


