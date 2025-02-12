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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class ResourceAssignmentSpreadPeriod(BaseModel):
    """
    ResourceAssignmentSpreadPeriod
    """ # noqa: E501
    start_date: Optional[StrictStr] = Field(default=None, alias="StartDate")
    end_date: Optional[StrictStr] = Field(default=None, alias="EndDate")
    actual_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="ActualCost")
    actual_overtime_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="ActualOvertimeCost")
    actual_overtime_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="ActualOvertimeUnits")
    actual_regular_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="ActualRegularCost")
    actual_regular_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="ActualRegularUnits")
    actual_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="ActualUnits")
    at_completion_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="AtCompletionCost")
    at_completion_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="AtCompletionUnits")
    planned_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PlannedCost")
    planned_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PlannedUnits")
    remaining_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="RemainingCost")
    remaining_late_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="RemainingLateCost")
    remaining_late_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="RemainingLateUnits")
    remaining_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="RemainingUnits")
    staffed_remaining_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="StaffedRemainingCost")
    staffed_remaining_late_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="StaffedRemainingLateCost")
    staffed_remaining_late_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="StaffedRemainingLateUnits")
    staffed_remaining_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="StaffedRemainingUnits")
    unstaffed_remaining_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="UnstaffedRemainingCost")
    unstaffed_remaining_late_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="UnstaffedRemainingLateCost")
    unstaffed_remaining_late_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="UnstaffedRemainingLateUnits")
    unstaffed_remaining_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="UnstaffedRemainingUnits")
    cumulative_actual_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeActualCost")
    cumulative_actual_overtime_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeActualOvertimeCost")
    cumulative_actual_overtime_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeActualOvertimeUnits")
    cumulative_actual_regular_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeActualRegularCost")
    cumulative_actual_regular_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeActualRegularUnits")
    cumulative_actual_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeActualUnits")
    cumulative_at_completion_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeAtCompletionCost")
    cumulative_at_completion_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeAtCompletionUnits")
    cumulative_planned_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePlannedCost")
    cumulative_planned_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePlannedUnits")
    cumulative_remaining_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeRemainingCost")
    cumulative_remaining_late_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeRemainingLateCost")
    cumulative_remaining_late_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeRemainingLateUnits")
    cumulative_remaining_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeRemainingUnits")
    cumulative_staffed_remaining_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeStaffedRemainingCost")
    cumulative_staffed_remaining_late_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeStaffedRemainingLateCost")
    cumulative_staffed_remaining_late_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeStaffedRemainingLateUnits")
    cumulative_staffed_remaining_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeStaffedRemainingUnits")
    cumulative_unstaffed_remaining_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeUnstaffedRemainingCost")
    cumulative_unstaffed_remaining_late_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeUnstaffedRemainingLateCost")
    cumulative_unstaffed_remaining_late_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeUnstaffedRemainingLateUnits")
    cumulative_unstaffed_remaining_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeUnstaffedRemainingUnits")
    period_actual_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PeriodActualCost")
    period_actual_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PeriodActualUnits")
    period_at_completion_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PeriodAtCompletionCost")
    period_at_completion_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PeriodAtCompletionUnits")
    __properties: ClassVar[List[str]] = ["StartDate", "EndDate", "ActualCost", "ActualOvertimeCost", "ActualOvertimeUnits", "ActualRegularCost", "ActualRegularUnits", "ActualUnits", "AtCompletionCost", "AtCompletionUnits", "PlannedCost", "PlannedUnits", "RemainingCost", "RemainingLateCost", "RemainingLateUnits", "RemainingUnits", "StaffedRemainingCost", "StaffedRemainingLateCost", "StaffedRemainingLateUnits", "StaffedRemainingUnits", "UnstaffedRemainingCost", "UnstaffedRemainingLateCost", "UnstaffedRemainingLateUnits", "UnstaffedRemainingUnits", "CumulativeActualCost", "CumulativeActualOvertimeCost", "CumulativeActualOvertimeUnits", "CumulativeActualRegularCost", "CumulativeActualRegularUnits", "CumulativeActualUnits", "CumulativeAtCompletionCost", "CumulativeAtCompletionUnits", "CumulativePlannedCost", "CumulativePlannedUnits", "CumulativeRemainingCost", "CumulativeRemainingLateCost", "CumulativeRemainingLateUnits", "CumulativeRemainingUnits", "CumulativeStaffedRemainingCost", "CumulativeStaffedRemainingLateCost", "CumulativeStaffedRemainingLateUnits", "CumulativeStaffedRemainingUnits", "CumulativeUnstaffedRemainingCost", "CumulativeUnstaffedRemainingLateCost", "CumulativeUnstaffedRemainingLateUnits", "CumulativeUnstaffedRemainingUnits", "PeriodActualCost", "PeriodActualUnits", "PeriodAtCompletionCost", "PeriodAtCompletionUnits"]

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
        """Create an instance of ResourceAssignmentSpreadPeriod from a JSON string"""
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
        """Create an instance of ResourceAssignmentSpreadPeriod from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "StartDate": obj.get("StartDate"),
            "EndDate": obj.get("EndDate"),
            "ActualCost": obj.get("ActualCost"),
            "ActualOvertimeCost": obj.get("ActualOvertimeCost"),
            "ActualOvertimeUnits": obj.get("ActualOvertimeUnits"),
            "ActualRegularCost": obj.get("ActualRegularCost"),
            "ActualRegularUnits": obj.get("ActualRegularUnits"),
            "ActualUnits": obj.get("ActualUnits"),
            "AtCompletionCost": obj.get("AtCompletionCost"),
            "AtCompletionUnits": obj.get("AtCompletionUnits"),
            "PlannedCost": obj.get("PlannedCost"),
            "PlannedUnits": obj.get("PlannedUnits"),
            "RemainingCost": obj.get("RemainingCost"),
            "RemainingLateCost": obj.get("RemainingLateCost"),
            "RemainingLateUnits": obj.get("RemainingLateUnits"),
            "RemainingUnits": obj.get("RemainingUnits"),
            "StaffedRemainingCost": obj.get("StaffedRemainingCost"),
            "StaffedRemainingLateCost": obj.get("StaffedRemainingLateCost"),
            "StaffedRemainingLateUnits": obj.get("StaffedRemainingLateUnits"),
            "StaffedRemainingUnits": obj.get("StaffedRemainingUnits"),
            "UnstaffedRemainingCost": obj.get("UnstaffedRemainingCost"),
            "UnstaffedRemainingLateCost": obj.get("UnstaffedRemainingLateCost"),
            "UnstaffedRemainingLateUnits": obj.get("UnstaffedRemainingLateUnits"),
            "UnstaffedRemainingUnits": obj.get("UnstaffedRemainingUnits"),
            "CumulativeActualCost": obj.get("CumulativeActualCost"),
            "CumulativeActualOvertimeCost": obj.get("CumulativeActualOvertimeCost"),
            "CumulativeActualOvertimeUnits": obj.get("CumulativeActualOvertimeUnits"),
            "CumulativeActualRegularCost": obj.get("CumulativeActualRegularCost"),
            "CumulativeActualRegularUnits": obj.get("CumulativeActualRegularUnits"),
            "CumulativeActualUnits": obj.get("CumulativeActualUnits"),
            "CumulativeAtCompletionCost": obj.get("CumulativeAtCompletionCost"),
            "CumulativeAtCompletionUnits": obj.get("CumulativeAtCompletionUnits"),
            "CumulativePlannedCost": obj.get("CumulativePlannedCost"),
            "CumulativePlannedUnits": obj.get("CumulativePlannedUnits"),
            "CumulativeRemainingCost": obj.get("CumulativeRemainingCost"),
            "CumulativeRemainingLateCost": obj.get("CumulativeRemainingLateCost"),
            "CumulativeRemainingLateUnits": obj.get("CumulativeRemainingLateUnits"),
            "CumulativeRemainingUnits": obj.get("CumulativeRemainingUnits"),
            "CumulativeStaffedRemainingCost": obj.get("CumulativeStaffedRemainingCost"),
            "CumulativeStaffedRemainingLateCost": obj.get("CumulativeStaffedRemainingLateCost"),
            "CumulativeStaffedRemainingLateUnits": obj.get("CumulativeStaffedRemainingLateUnits"),
            "CumulativeStaffedRemainingUnits": obj.get("CumulativeStaffedRemainingUnits"),
            "CumulativeUnstaffedRemainingCost": obj.get("CumulativeUnstaffedRemainingCost"),
            "CumulativeUnstaffedRemainingLateCost": obj.get("CumulativeUnstaffedRemainingLateCost"),
            "CumulativeUnstaffedRemainingLateUnits": obj.get("CumulativeUnstaffedRemainingLateUnits"),
            "CumulativeUnstaffedRemainingUnits": obj.get("CumulativeUnstaffedRemainingUnits"),
            "PeriodActualCost": obj.get("PeriodActualCost"),
            "PeriodActualUnits": obj.get("PeriodActualUnits"),
            "PeriodAtCompletionCost": obj.get("PeriodAtCompletionCost"),
            "PeriodAtCompletionUnits": obj.get("PeriodAtCompletionUnits")
        })
        return _obj


