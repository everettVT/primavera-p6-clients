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

class Currency(BaseModel):
    """
    Currency Entity
    """ # noqa: E501
    create_date: Optional[datetime] = Field(default=None, description="The date this currency was created.", alias="CreateDate")
    create_user: Optional[StrictStr] = Field(default=None, description="The name of the user that created this currency.", alias="CreateUser")
    decimal_places: Optional[StrictInt] = Field(default=None, description="The number of decimal places displayed.", alias="DecimalPlaces")
    decimal_symbol: Optional[StrictStr] = Field(default=None, description="The decimal symbol displayed.", alias="DecimalSymbol")
    digit_grouping_symbol: Optional[StrictStr] = Field(default=None, description="The symbol used to group the numbers.", alias="DigitGroupingSymbol")
    exchange_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The exchange rate against the base currency.", alias="ExchangeRate")
    id: StrictStr = Field(description="The unique currency abbreviation for each currency.", alias="Id")
    is_base_currency: Optional[StrictBool] = Field(default=None, description="The currency used to store cost in the Project Management database. The exchange rate for the base currency is always 1.0. The base currency ID, name, and symbol default to U.S. dollars and can be edited but never deleted.", alias="IsBaseCurrency")
    last_update_date: Optional[datetime] = Field(default=None, description="The date this currency was last updated.", alias="LastUpdateDate")
    last_update_user: Optional[StrictStr] = Field(default=None, description="The name of the user that last updated this currency.", alias="LastUpdateUser")
    name: StrictStr = Field(description="The name of the currency.", alias="Name")
    negative_symbol: Optional[StrictStr] = Field(default=None, description="The symbol used to display a negative currency.", alias="NegativeSymbol")
    object_id: Optional[StrictInt] = Field(default=None, description="The unique ID generated by the system.", alias="ObjectId")
    positive_symbol: Optional[StrictStr] = Field(default=None, description="The symbol used to display a positive currency.", alias="PositiveSymbol")
    symbol: StrictStr = Field(description="The currency symbol displayed.", alias="Symbol")
    __properties: ClassVar[List[str]] = ["CreateDate", "CreateUser", "DecimalPlaces", "DecimalSymbol", "DigitGroupingSymbol", "ExchangeRate", "Id", "IsBaseCurrency", "LastUpdateDate", "LastUpdateUser", "Name", "NegativeSymbol", "ObjectId", "PositiveSymbol", "Symbol"]

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
        """Create an instance of Currency from a JSON string"""
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
        """Create an instance of Currency from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "CreateDate": obj.get("CreateDate"),
            "CreateUser": obj.get("CreateUser"),
            "DecimalPlaces": obj.get("DecimalPlaces"),
            "DecimalSymbol": obj.get("DecimalSymbol"),
            "DigitGroupingSymbol": obj.get("DigitGroupingSymbol"),
            "ExchangeRate": obj.get("ExchangeRate"),
            "Id": obj.get("Id"),
            "IsBaseCurrency": obj.get("IsBaseCurrency"),
            "LastUpdateDate": obj.get("LastUpdateDate"),
            "LastUpdateUser": obj.get("LastUpdateUser"),
            "Name": obj.get("Name"),
            "NegativeSymbol": obj.get("NegativeSymbol"),
            "ObjectId": obj.get("ObjectId"),
            "PositiveSymbol": obj.get("PositiveSymbol"),
            "Symbol": obj.get("Symbol")
        })
        return _obj


