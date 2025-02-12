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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class Values(BaseModel):
    """
    Values
    """ # noqa: E501
    value0: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Value0")
    value5: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Value5")
    value10: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Value10")
    value15: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Value15")
    value20: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Value20")
    value25: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Value25")
    value30: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Value30")
    value35: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Value35")
    value40: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Value40")
    value45: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Value45")
    value50: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Value50")
    value55: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Value55")
    value60: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Value60")
    value65: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Value65")
    value70: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Value70")
    value75: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Value75")
    value80: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Value80")
    value85: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Value85")
    value90: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Value90")
    value95: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Value95")
    value100: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Value100")
    __properties: ClassVar[List[str]] = ["Value0", "Value5", "Value10", "Value15", "Value20", "Value25", "Value30", "Value35", "Value40", "Value45", "Value50", "Value55", "Value60", "Value65", "Value70", "Value75", "Value80", "Value85", "Value90", "Value95", "Value100"]

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
        """Create an instance of Values from a JSON string"""
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
        """Create an instance of Values from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Value0": obj.get("Value0"),
            "Value5": obj.get("Value5"),
            "Value10": obj.get("Value10"),
            "Value15": obj.get("Value15"),
            "Value20": obj.get("Value20"),
            "Value25": obj.get("Value25"),
            "Value30": obj.get("Value30"),
            "Value35": obj.get("Value35"),
            "Value40": obj.get("Value40"),
            "Value45": obj.get("Value45"),
            "Value50": obj.get("Value50"),
            "Value55": obj.get("Value55"),
            "Value60": obj.get("Value60"),
            "Value65": obj.get("Value65"),
            "Value70": obj.get("Value70"),
            "Value75": obj.get("Value75"),
            "Value80": obj.get("Value80"),
            "Value85": obj.get("Value85"),
            "Value90": obj.get("Value90"),
            "Value95": obj.get("Value95"),
            "Value100": obj.get("Value100")
        })
        return _obj


