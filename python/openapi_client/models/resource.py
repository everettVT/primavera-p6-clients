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

class Resource(BaseModel):
    """
    Resource Entity
    """ # noqa: E501
    auto_compute_actuals: Optional[StrictBool] = Field(default=None, alias="AutoComputeActuals")
    calculate_cost_from_units: Optional[StrictBool] = Field(default=None, alias="CalculateCostFromUnits")
    calendar_name: Optional[StrictStr] = Field(default=None, alias="CalendarName")
    calendar_object_id: Optional[StrictInt] = Field(default=None, alias="CalendarObjectId")
    create_date: Optional[datetime] = Field(default=None, alias="CreateDate")
    create_user: Optional[StrictStr] = Field(default=None, alias="CreateUser")
    currency_id: Optional[StrictStr] = Field(default=None, alias="CurrencyId")
    currency_name: Optional[StrictStr] = Field(default=None, alias="CurrencyName")
    currency_object_id: Optional[StrictInt] = Field(default=None, alias="CurrencyObjectId")
    default_units_per_time: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="DefaultUnitsPerTime")
    effective_date: Optional[datetime] = Field(default=None, alias="EffectiveDate")
    email_address: Optional[StrictStr] = Field(default=None, alias="EmailAddress")
    employee_id: Optional[StrictStr] = Field(default=None, alias="EmployeeId")
    guid: Optional[StrictStr] = Field(default=None, alias="GUID")
    id: Optional[StrictStr] = Field(default=None, alias="Id")
    integrated_type: Optional[StrictStr] = Field(default=None, alias="IntegratedType")
    is_active: Optional[StrictBool] = Field(default=None, alias="IsActive")
    is_over_time_allowed: Optional[StrictBool] = Field(default=None, alias="IsOverTimeAllowed")
    last_update_date: Optional[datetime] = Field(default=None, alias="LastUpdateDate")
    last_update_user: Optional[StrictStr] = Field(default=None, alias="LastUpdateUser")
    latitude: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Latitude")
    location_name: Optional[StrictStr] = Field(default=None, alias="LocationName")
    location_object_id: Optional[StrictInt] = Field(default=None, alias="LocationObjectId")
    longitude: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Longitude")
    max_units_per_time: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="MaxUnitsPerTime")
    name: Optional[StrictStr] = Field(default=None, alias="Name")
    object_id: Optional[StrictInt] = Field(default=None, alias="ObjectId")
    office_phone: Optional[StrictStr] = Field(default=None, alias="OfficePhone")
    other_phone: Optional[StrictStr] = Field(default=None, alias="OtherPhone")
    overtime_factor: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="OvertimeFactor")
    parent_object_id: Optional[StrictInt] = Field(default=None, alias="ParentObjectId")
    price_per_unit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PricePerUnit")
    primary_role_id: Optional[StrictStr] = Field(default=None, alias="PrimaryRoleId")
    primary_role_name: Optional[StrictStr] = Field(default=None, alias="PrimaryRoleName")
    primary_role_object_id: Optional[StrictInt] = Field(default=None, alias="PrimaryRoleObjectId")
    resource_notes: Optional[StrictStr] = Field(default=None, alias="ResourceNotes")
    resource_type: Optional[StrictStr] = Field(default=None, alias="ResourceType")
    sequence_number: Optional[StrictInt] = Field(default=None, alias="SequenceNumber")
    shift_object_id: Optional[StrictInt] = Field(default=None, alias="ShiftObjectId")
    timesheet_approval_manager: Optional[StrictStr] = Field(default=None, alias="TimesheetApprovalManager")
    timesheet_approval_manager_object_id: Optional[StrictInt] = Field(default=None, alias="TimesheetApprovalManagerObjectId")
    title: Optional[StrictStr] = Field(default=None, alias="Title")
    unit_of_measure_abbreviation: Optional[StrictStr] = Field(default=None, alias="UnitOfMeasureAbbreviation")
    unit_of_measure_name: Optional[StrictStr] = Field(default=None, alias="UnitOfMeasureName")
    unit_of_measure_object_id: Optional[StrictInt] = Field(default=None, alias="UnitOfMeasureObjectId")
    use_timesheets: Optional[StrictBool] = Field(default=None, alias="UseTimesheets")
    user_name: Optional[StrictStr] = Field(default=None, alias="UserName")
    user_object_id: Optional[StrictInt] = Field(default=None, alias="UserObjectId")
    __properties: ClassVar[List[str]] = ["AutoComputeActuals", "CalculateCostFromUnits", "CalendarName", "CalendarObjectId", "CreateDate", "CreateUser", "CurrencyId", "CurrencyName", "CurrencyObjectId", "DefaultUnitsPerTime", "EffectiveDate", "EmailAddress", "EmployeeId", "GUID", "Id", "IntegratedType", "IsActive", "IsOverTimeAllowed", "LastUpdateDate", "LastUpdateUser", "Latitude", "LocationName", "LocationObjectId", "Longitude", "MaxUnitsPerTime", "Name", "ObjectId", "OfficePhone", "OtherPhone", "OvertimeFactor", "ParentObjectId", "PricePerUnit", "PrimaryRoleId", "PrimaryRoleName", "PrimaryRoleObjectId", "ResourceNotes", "ResourceType", "SequenceNumber", "ShiftObjectId", "TimesheetApprovalManager", "TimesheetApprovalManagerObjectId", "Title", "UnitOfMeasureAbbreviation", "UnitOfMeasureName", "UnitOfMeasureObjectId", "UseTimesheets", "UserName", "UserObjectId"]

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
        """Create an instance of Resource from a JSON string"""
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
        """Create an instance of Resource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "AutoComputeActuals": obj.get("AutoComputeActuals"),
            "CalculateCostFromUnits": obj.get("CalculateCostFromUnits"),
            "CalendarName": obj.get("CalendarName"),
            "CalendarObjectId": obj.get("CalendarObjectId"),
            "CreateDate": obj.get("CreateDate"),
            "CreateUser": obj.get("CreateUser"),
            "CurrencyId": obj.get("CurrencyId"),
            "CurrencyName": obj.get("CurrencyName"),
            "CurrencyObjectId": obj.get("CurrencyObjectId"),
            "DefaultUnitsPerTime": obj.get("DefaultUnitsPerTime"),
            "EffectiveDate": obj.get("EffectiveDate"),
            "EmailAddress": obj.get("EmailAddress"),
            "EmployeeId": obj.get("EmployeeId"),
            "GUID": obj.get("GUID"),
            "Id": obj.get("Id"),
            "IntegratedType": obj.get("IntegratedType"),
            "IsActive": obj.get("IsActive"),
            "IsOverTimeAllowed": obj.get("IsOverTimeAllowed"),
            "LastUpdateDate": obj.get("LastUpdateDate"),
            "LastUpdateUser": obj.get("LastUpdateUser"),
            "Latitude": obj.get("Latitude"),
            "LocationName": obj.get("LocationName"),
            "LocationObjectId": obj.get("LocationObjectId"),
            "Longitude": obj.get("Longitude"),
            "MaxUnitsPerTime": obj.get("MaxUnitsPerTime"),
            "Name": obj.get("Name"),
            "ObjectId": obj.get("ObjectId"),
            "OfficePhone": obj.get("OfficePhone"),
            "OtherPhone": obj.get("OtherPhone"),
            "OvertimeFactor": obj.get("OvertimeFactor"),
            "ParentObjectId": obj.get("ParentObjectId"),
            "PricePerUnit": obj.get("PricePerUnit"),
            "PrimaryRoleId": obj.get("PrimaryRoleId"),
            "PrimaryRoleName": obj.get("PrimaryRoleName"),
            "PrimaryRoleObjectId": obj.get("PrimaryRoleObjectId"),
            "ResourceNotes": obj.get("ResourceNotes"),
            "ResourceType": obj.get("ResourceType"),
            "SequenceNumber": obj.get("SequenceNumber"),
            "ShiftObjectId": obj.get("ShiftObjectId"),
            "TimesheetApprovalManager": obj.get("TimesheetApprovalManager"),
            "TimesheetApprovalManagerObjectId": obj.get("TimesheetApprovalManagerObjectId"),
            "Title": obj.get("Title"),
            "UnitOfMeasureAbbreviation": obj.get("UnitOfMeasureAbbreviation"),
            "UnitOfMeasureName": obj.get("UnitOfMeasureName"),
            "UnitOfMeasureObjectId": obj.get("UnitOfMeasureObjectId"),
            "UseTimesheets": obj.get("UseTimesheets"),
            "UserName": obj.get("UserName"),
            "UserObjectId": obj.get("UserObjectId")
        })
        return _obj


