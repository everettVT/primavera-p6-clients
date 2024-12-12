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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ResourceAssignmentExport(BaseModel):
    """
    ResourceAssignment Entity
    """ # noqa: E501
    include: Optional[StrictBool] = Field(default=None, description="Boolean flag that indicates whether the associated object is to be exported. The default value of the Include element is true. To exclude a business object from the XML export file, specify false in the Include element for that business object.", alias="Include")
    var_field: Optional[List[StrictStr]] = Field(default=None, description="List of Fields for ResourceAssignment Business Object", alias="Field")
    __properties: ClassVar[List[str]] = ["Include", "Field"]

    @field_validator('var_field')
    def var_field_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['ACTIVITY_ACTUAL_FINISH', 'ACTIVITY_ID', 'ACTIVITY_NAME', 'ACTIVITY_OBJECT_ID', 'ACTIVITY_TYPE', 'ACTUAL_COST', 'ACTUAL_CURVE', 'ACTUAL_DURATION', 'ACTUAL_FINISH_DATE', 'ACTUAL_OVERTIME_COST', 'ACTUAL_OVERTIME_UNITS', 'ACTUAL_REGULAR_COST', 'ACTUAL_REGULAR_UNITS', 'ACTUAL_START_DATE', 'ACTUAL_THIS_PERIOD_COST', 'ACTUAL_THIS_PERIOD_UNITS', 'ACTUAL_UNITS', 'ASSIGNMENT_PERCENT_COMPLETE', 'AT_COMPLETION_COST', 'AT_COMPLETION_DURATION', 'AT_COMPLETION_UNITS', 'AUTO_COMPUTE_ACTUALS', 'BUDGET_AT_COMPLETION_COSTS', 'BUDGET_AT_COMPLETION_UNITS', 'CBS_CODE', 'CBS_ID', 'CALENDAR_NAME', 'CALENDAR_OBJECT_ID', 'COST_ACCOUNT_ID', 'COST_ACCOUNT_NAME', 'COST_ACCOUNT_OBJECT_ID', 'CREATE_DATE', 'CREATE_USER', 'DRIVING_ACTIVITY_DATES_FLAG', 'DURATION_PERCENT_COMPLETE', 'ESTIMATE_TO_COMPLETION_COSTS', 'ESTIMATE_TO_COMPLETION_UNITS', 'FINANCIAL_PERIOD_TMPL_ID', 'FINISH_DATE', 'GUID', 'HAS_FUTURE_BUCKET_DATA', 'IS_ACTIVE', 'IS_ACTIVITY_FLAGGED', 'IS_BASELINE', 'IS_COST_UNITS_LINKED', 'IS_OVERTIME_ALLOWED', 'IS_PRIMARY_RESOURCE', 'IS_TEMPLATE', 'LAST_UPDATE_DATE', 'LAST_UPDATE_USER', 'OBJECT_ID', 'OVERTIME_FACTOR', 'PENDING_ACTUAL_OVERTIME_UNITS', 'PENDING_ACTUAL_REGULAR_UNITS', 'PENDING_PERCENT_COMPLETE', 'PENDING_REMAINING_UNITS', 'PERCENT_COMPLETE', 'PERCENT_COMPLETE_TYPE', 'PLANNED_COST', 'PLANNED_CURVE', 'PLANNED_DURATION', 'PLANNED_FINISH_DATE', 'PLANNED_LAG', 'PLANNED_START_DATE', 'PLANNED_UNITS', 'PLANNED_UNITS_PER_TIME', 'PRICE_PER_UNIT', 'PRIOR_ACTUAL_OVERTIME_UNITS', 'PRIOR_ACTUAL_REGULAR_UNITS', 'PROFICIENCY', 'PROJECT_FLAG', 'PROJECT_ID', 'PROJECT_NAME', 'PROJECT_OBJECT_ID', 'PROJECT_PROJECT_FLAG', 'RATE_SOURCE', 'RATE_TYPE', 'REMAINING_COST', 'REMAINING_CURVE', 'REMAINING_DURATION', 'REMAINING_FINISH_DATE', 'REMAINING_LAG', 'REMAINING_LATE_FINISH_DATE', 'REMAINING_LATE_START_DATE', 'REMAINING_START_DATE', 'REMAINING_UNITS', 'REMAINING_UNITS_PER_TIME', 'RESOURCE_CALENDAR_NAME', 'RESOURCE_CURVE_NAME', 'RESOURCE_CURVE_OBJECT_ID', 'RESOURCE_ID', 'RESOURCE_NAME', 'RESOURCE_OBJECT_ID', 'RESOURCE_REQUEST', 'RESOURCE_TYPE', 'REVIEW_REQUIRED', 'ROLE_ID', 'ROLE_NAME', 'ROLE_OBJECT_ID', 'ROLE_SHORT_NAME', 'STAFFED_REMAINING_COST', 'STAFFED_REMAINING_UNITS', 'START_DATE', 'STATUS_CODE', 'TOTAL_PAST_PERIOD_COST', 'TOTAL_PAST_PERIOD_UNITS', 'UNITS_PERCENT_COMPLETE', 'UNREAD_COMMENT_COUNT', 'UNSTAFFED_REMAINING_COST', 'UNSTAFFED_REMAINING_UNITS', 'WBS_NAME_PATH', 'WBS_OBJECT_ID']):
                raise ValueError("each list item must be one of ('ACTIVITY_ACTUAL_FINISH', 'ACTIVITY_ID', 'ACTIVITY_NAME', 'ACTIVITY_OBJECT_ID', 'ACTIVITY_TYPE', 'ACTUAL_COST', 'ACTUAL_CURVE', 'ACTUAL_DURATION', 'ACTUAL_FINISH_DATE', 'ACTUAL_OVERTIME_COST', 'ACTUAL_OVERTIME_UNITS', 'ACTUAL_REGULAR_COST', 'ACTUAL_REGULAR_UNITS', 'ACTUAL_START_DATE', 'ACTUAL_THIS_PERIOD_COST', 'ACTUAL_THIS_PERIOD_UNITS', 'ACTUAL_UNITS', 'ASSIGNMENT_PERCENT_COMPLETE', 'AT_COMPLETION_COST', 'AT_COMPLETION_DURATION', 'AT_COMPLETION_UNITS', 'AUTO_COMPUTE_ACTUALS', 'BUDGET_AT_COMPLETION_COSTS', 'BUDGET_AT_COMPLETION_UNITS', 'CBS_CODE', 'CBS_ID', 'CALENDAR_NAME', 'CALENDAR_OBJECT_ID', 'COST_ACCOUNT_ID', 'COST_ACCOUNT_NAME', 'COST_ACCOUNT_OBJECT_ID', 'CREATE_DATE', 'CREATE_USER', 'DRIVING_ACTIVITY_DATES_FLAG', 'DURATION_PERCENT_COMPLETE', 'ESTIMATE_TO_COMPLETION_COSTS', 'ESTIMATE_TO_COMPLETION_UNITS', 'FINANCIAL_PERIOD_TMPL_ID', 'FINISH_DATE', 'GUID', 'HAS_FUTURE_BUCKET_DATA', 'IS_ACTIVE', 'IS_ACTIVITY_FLAGGED', 'IS_BASELINE', 'IS_COST_UNITS_LINKED', 'IS_OVERTIME_ALLOWED', 'IS_PRIMARY_RESOURCE', 'IS_TEMPLATE', 'LAST_UPDATE_DATE', 'LAST_UPDATE_USER', 'OBJECT_ID', 'OVERTIME_FACTOR', 'PENDING_ACTUAL_OVERTIME_UNITS', 'PENDING_ACTUAL_REGULAR_UNITS', 'PENDING_PERCENT_COMPLETE', 'PENDING_REMAINING_UNITS', 'PERCENT_COMPLETE', 'PERCENT_COMPLETE_TYPE', 'PLANNED_COST', 'PLANNED_CURVE', 'PLANNED_DURATION', 'PLANNED_FINISH_DATE', 'PLANNED_LAG', 'PLANNED_START_DATE', 'PLANNED_UNITS', 'PLANNED_UNITS_PER_TIME', 'PRICE_PER_UNIT', 'PRIOR_ACTUAL_OVERTIME_UNITS', 'PRIOR_ACTUAL_REGULAR_UNITS', 'PROFICIENCY', 'PROJECT_FLAG', 'PROJECT_ID', 'PROJECT_NAME', 'PROJECT_OBJECT_ID', 'PROJECT_PROJECT_FLAG', 'RATE_SOURCE', 'RATE_TYPE', 'REMAINING_COST', 'REMAINING_CURVE', 'REMAINING_DURATION', 'REMAINING_FINISH_DATE', 'REMAINING_LAG', 'REMAINING_LATE_FINISH_DATE', 'REMAINING_LATE_START_DATE', 'REMAINING_START_DATE', 'REMAINING_UNITS', 'REMAINING_UNITS_PER_TIME', 'RESOURCE_CALENDAR_NAME', 'RESOURCE_CURVE_NAME', 'RESOURCE_CURVE_OBJECT_ID', 'RESOURCE_ID', 'RESOURCE_NAME', 'RESOURCE_OBJECT_ID', 'RESOURCE_REQUEST', 'RESOURCE_TYPE', 'REVIEW_REQUIRED', 'ROLE_ID', 'ROLE_NAME', 'ROLE_OBJECT_ID', 'ROLE_SHORT_NAME', 'STAFFED_REMAINING_COST', 'STAFFED_REMAINING_UNITS', 'START_DATE', 'STATUS_CODE', 'TOTAL_PAST_PERIOD_COST', 'TOTAL_PAST_PERIOD_UNITS', 'UNITS_PERCENT_COMPLETE', 'UNREAD_COMMENT_COUNT', 'UNSTAFFED_REMAINING_COST', 'UNSTAFFED_REMAINING_UNITS', 'WBS_NAME_PATH', 'WBS_OBJECT_ID')")
        return value

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
        """Create an instance of ResourceAssignmentExport from a JSON string"""
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
        """Create an instance of ResourceAssignmentExport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Include": obj.get("Include"),
            "Field": obj.get("Field")
        })
        return _obj


