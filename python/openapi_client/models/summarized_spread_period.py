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

class SummarizedSpreadPeriod(BaseModel):
    """
    SummarizedSpreadPeriod
    """ # noqa: E501
    start_date: Optional[StrictStr] = Field(default=None, alias="StartDate")
    end_date: Optional[StrictStr] = Field(default=None, alias="EndDate")
    actual_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="ActualCost")
    actual_expense_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="ActualExpenseCost")
    actual_labor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="ActualLaborCost")
    actual_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="ActualLaborUnits")
    actual_material_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="ActualMaterialCost")
    actual_nonlabor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="ActualNonlaborCost")
    actual_nonlabor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="ActualNonlaborUnits")
    actual_total_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="ActualTotalCost")
    at_completion_expense_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="AtCompletionExpenseCost")
    at_completion_labor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="AtCompletionLaborCost")
    at_completion_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="AtCompletionLaborUnits")
    at_completion_material_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="AtCompletionMaterialCost")
    at_completion_nonlabor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="AtCompletionNonlaborCost")
    at_completion_nonlabor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="AtCompletionNonlaborUnits")
    at_completion_total_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="AtCompletionTotalCost")
    baseline_planned_expense_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="BaselinePlannedExpenseCost")
    baseline_planned_labor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="BaselinePlannedLaborCost")
    baseline_planned_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="BaselinePlannedLaborUnits")
    baseline_planned_material_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="BaselinePlannedMaterialCost")
    baseline_planned_nonlabor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="BaselinePlannedNonlaborCost")
    baseline_planned_nonlabor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="BaselinePlannedNonlaborUnits")
    baseline_planned_total_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="BaselinePlannedTotalCost")
    earned_value_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="EarnedValueCost")
    earned_value_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="EarnedValueLaborUnits")
    estimate_at_completion_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="EstimateAtCompletionCost")
    estimate_at_completion_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="EstimateAtCompletionLaborUnits")
    estimate_to_complete_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="EstimateToCompleteCost")
    estimate_to_complete_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="EstimateToCompleteLaborUnits")
    period_actual_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PeriodActualCost")
    period_actual_expense_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PeriodActualExpenseCost")
    period_actual_labor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PeriodActualLaborCost")
    period_actual_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PeriodActualLaborUnits")
    period_actual_material_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PeriodActualMaterialCost")
    period_actual_non_labor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PeriodActualNonLaborCost")
    period_actual_non_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PeriodActualNonLaborUnits")
    period_at_completion_expense_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PeriodAtCompletionExpenseCost")
    period_at_completion_labor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PeriodAtCompletionLaborCost")
    period_at_completion_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PeriodAtCompletionLaborUnits")
    period_at_completion_material_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PeriodAtCompletionMaterialCost")
    period_at_completion_non_labor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PeriodAtCompletionNonLaborCost")
    period_at_completion_non_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PeriodAtCompletionNonLaborUnits")
    period_at_completion_total_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PeriodAtCompletionTotalCost")
    period_earned_value_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PeriodEarnedValueCost")
    period_earned_value_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PeriodEarnedValueLaborUnits")
    period_estimate_at_completion_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PeriodEstimateAtCompletionCost")
    period_estimate_at_completion_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PeriodEstimateAtCompletionLaborUnits")
    period_planned_value_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PeriodPlannedValueCost")
    period_planned_value_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PeriodPlannedValueLaborUnits")
    planned_expense_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PlannedExpenseCost")
    planned_labor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PlannedLaborCost")
    planned_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PlannedLaborUnits")
    planned_material_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PlannedMaterialCost")
    planned_nonlabor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PlannedNonlaborCost")
    planned_nonlabor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PlannedNonlaborUnits")
    planned_total_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PlannedTotalCost")
    planned_value_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PlannedValueCost")
    planned_value_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PlannedValueLaborUnits")
    remaining_expense_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="RemainingExpenseCost")
    remaining_labor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="RemainingLaborCost")
    remaining_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="RemainingLaborUnits")
    remaining_late_expense_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="RemainingLateExpenseCost")
    remaining_late_labor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="RemainingLateLaborCost")
    remaining_late_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="RemainingLateLaborUnits")
    remaining_late_material_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="RemainingLateMaterialCost")
    remaining_late_nonlabor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="RemainingLateNonlaborCost")
    remaining_late_nonlabor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="RemainingLateNonlaborUnits")
    remaining_late_total_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="RemainingLateTotalCost")
    remaining_material_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="RemainingMaterialCost")
    remaining_nonlabor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="RemainingNonlaborCost")
    remaining_nonlabor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="RemainingNonlaborUnits")
    remaining_total_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="RemainingTotalCost")
    cumulative_actual_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeActualCost")
    cumulative_actual_expense_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeActualExpenseCost")
    cumulative_actual_labor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeActualLaborCost")
    cumulative_actual_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeActualLaborUnits")
    cumulative_actual_material_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeActualMaterialCost")
    cumulative_actual_nonlabor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeActualNonlaborCost")
    cumulative_actual_nonlabor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeActualNonlaborUnits")
    cumulative_actual_total_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeActualTotalCost")
    cumulative_at_completion_expense_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeAtCompletionExpenseCost")
    cumulative_at_completion_labor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeAtCompletionLaborCost")
    cumulative_at_completion_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeAtCompletionLaborUnits")
    cumulative_at_completion_material_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeAtCompletionMaterialCost")
    cumulative_at_completion_nonlabor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeAtCompletionNonlaborCost")
    cumulative_at_completion_nonlabor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeAtCompletionNonlaborUnits")
    cumulative_at_completion_total_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeAtCompletionTotalCost")
    cumulative_baseline_planned_expense_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeBaselinePlannedExpenseCost")
    cumulative_baseline_planned_labor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeBaselinePlannedLaborCost")
    cumulative_baseline_planned_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeBaselinePlannedLaborUnits")
    cumulative_baseline_planned_material_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeBaselinePlannedMaterialCost")
    cumulative_baseline_planned_nonlabor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeBaselinePlannedNonlaborCost")
    cumulative_baseline_planned_nonlabor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeBaselinePlannedNonlaborUnits")
    cumulative_baseline_planned_total_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeBaselinePlannedTotalCost")
    cumulative_earned_value_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeEarnedValueCost")
    cumulative_earned_value_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeEarnedValueLaborUnits")
    cumulative_estimate_at_completion_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeEstimateAtCompletionCost")
    cumulative_estimate_at_completion_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeEstimateAtCompletionLaborUnits")
    cumulative_estimate_to_complete_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeEstimateToCompleteCost")
    cumulative_estimate_to_complete_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeEstimateToCompleteLaborUnits")
    cumulative_limit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeLimit")
    cumulative_planned_expense_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePlannedExpenseCost")
    cumulative_planned_labor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePlannedLaborCost")
    cumulative_planned_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePlannedLaborUnits")
    cumulative_planned_material_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePlannedMaterialCost")
    cumulative_planned_nonlabor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePlannedNonlaborCost")
    cumulative_planned_nonlabor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePlannedNonlaborUnits")
    cumulative_planned_total_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePlannedTotalCost")
    cumulative_planned_value_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePlannedValueCost")
    cumulative_planned_value_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePlannedValueLaborUnits")
    cumulative_period_actual_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePeriodActualCost")
    cumulative_period_actual_expense_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePeriodActualExpenseCost")
    cumulative_period_actual_labor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePeriodActualLaborCost")
    cumulative_period_actual_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePeriodActualLaborUnits")
    cumulative_period_actual_material_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePeriodActualMaterialCost")
    cumulative_period_actual_non_labor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePeriodActualNonLaborCost")
    cumulative_period_actual_non_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePeriodActualNonLaborUnits")
    cumulative_period_at_completion_expense_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePeriodAtCompletionExpenseCost")
    cumulative_period_at_completion_labor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePeriodAtCompletionLaborCost")
    cumulative_period_at_completion_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePeriodAtCompletionLaborUnits")
    cumulative_period_at_completion_material_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePeriodAtCompletionMaterialCost")
    cumulative_period_at_completion_non_labor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePeriodAtCompletionNonLaborCost")
    cumulative_period_at_completion_non_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePeriodAtCompletionNonLaborUnits")
    cumulative_period_at_completion_total_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePeriodAtCompletionTotalCost")
    cumulative_period_earned_value_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePeriodEarnedValueCost")
    cumulative_period_earned_value_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePeriodEarnedValueLaborUnits")
    cumulative_period_estimate_at_completion_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePeriodEstimateAtCompletionCost")
    cumulative_period_estimate_at_completion_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePeriodEstimateAtCompletionLaborUnits")
    cumulative_period_planned_value_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePeriodPlannedValueCost")
    cumulative_period_planned_value_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativePeriodPlannedValueLaborUnits")
    cumulative_remaining_expense_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeRemainingExpenseCost")
    cumulative_remaining_labor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeRemainingLaborCost")
    cumulative_remaining_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeRemainingLaborUnits")
    cumulative_remaining_late_expense_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeRemainingLateExpenseCost")
    cumulative_remaining_late_labor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeRemainingLateLaborCost")
    cumulative_remaining_late_labor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeRemainingLateLaborUnits")
    cumulative_remaining_late_material_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeRemainingLateMaterialCost")
    cumulative_remaining_late_nonlabor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeRemainingLateNonlaborCost")
    cumulative_remaining_late_nonlabor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeRemainingLateNonlaborUnits")
    cumulative_remaining_late_total_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeRemainingLateTotalCost")
    cumulative_remaining_material_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeRemainingMaterialCost")
    cumulative_remaining_nonlabor_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeRemainingNonlaborCost")
    cumulative_remaining_nonlabor_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeRemainingNonlaborUnits")
    cumulative_remaining_total_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CumulativeRemainingTotalCost")
    __properties: ClassVar[List[str]] = ["StartDate", "EndDate", "ActualCost", "ActualExpenseCost", "ActualLaborCost", "ActualLaborUnits", "ActualMaterialCost", "ActualNonlaborCost", "ActualNonlaborUnits", "ActualTotalCost", "AtCompletionExpenseCost", "AtCompletionLaborCost", "AtCompletionLaborUnits", "AtCompletionMaterialCost", "AtCompletionNonlaborCost", "AtCompletionNonlaborUnits", "AtCompletionTotalCost", "BaselinePlannedExpenseCost", "BaselinePlannedLaborCost", "BaselinePlannedLaborUnits", "BaselinePlannedMaterialCost", "BaselinePlannedNonlaborCost", "BaselinePlannedNonlaborUnits", "BaselinePlannedTotalCost", "EarnedValueCost", "EarnedValueLaborUnits", "EstimateAtCompletionCost", "EstimateAtCompletionLaborUnits", "EstimateToCompleteCost", "EstimateToCompleteLaborUnits", "PeriodActualCost", "PeriodActualExpenseCost", "PeriodActualLaborCost", "PeriodActualLaborUnits", "PeriodActualMaterialCost", "PeriodActualNonLaborCost", "PeriodActualNonLaborUnits", "PeriodAtCompletionExpenseCost", "PeriodAtCompletionLaborCost", "PeriodAtCompletionLaborUnits", "PeriodAtCompletionMaterialCost", "PeriodAtCompletionNonLaborCost", "PeriodAtCompletionNonLaborUnits", "PeriodAtCompletionTotalCost", "PeriodEarnedValueCost", "PeriodEarnedValueLaborUnits", "PeriodEstimateAtCompletionCost", "PeriodEstimateAtCompletionLaborUnits", "PeriodPlannedValueCost", "PeriodPlannedValueLaborUnits", "PlannedExpenseCost", "PlannedLaborCost", "PlannedLaborUnits", "PlannedMaterialCost", "PlannedNonlaborCost", "PlannedNonlaborUnits", "PlannedTotalCost", "PlannedValueCost", "PlannedValueLaborUnits", "RemainingExpenseCost", "RemainingLaborCost", "RemainingLaborUnits", "RemainingLateExpenseCost", "RemainingLateLaborCost", "RemainingLateLaborUnits", "RemainingLateMaterialCost", "RemainingLateNonlaborCost", "RemainingLateNonlaborUnits", "RemainingLateTotalCost", "RemainingMaterialCost", "RemainingNonlaborCost", "RemainingNonlaborUnits", "RemainingTotalCost", "CumulativeActualCost", "CumulativeActualExpenseCost", "CumulativeActualLaborCost", "CumulativeActualLaborUnits", "CumulativeActualMaterialCost", "CumulativeActualNonlaborCost", "CumulativeActualNonlaborUnits", "CumulativeActualTotalCost", "CumulativeAtCompletionExpenseCost", "CumulativeAtCompletionLaborCost", "CumulativeAtCompletionLaborUnits", "CumulativeAtCompletionMaterialCost", "CumulativeAtCompletionNonlaborCost", "CumulativeAtCompletionNonlaborUnits", "CumulativeAtCompletionTotalCost", "CumulativeBaselinePlannedExpenseCost", "CumulativeBaselinePlannedLaborCost", "CumulativeBaselinePlannedLaborUnits", "CumulativeBaselinePlannedMaterialCost", "CumulativeBaselinePlannedNonlaborCost", "CumulativeBaselinePlannedNonlaborUnits", "CumulativeBaselinePlannedTotalCost", "CumulativeEarnedValueCost", "CumulativeEarnedValueLaborUnits", "CumulativeEstimateAtCompletionCost", "CumulativeEstimateAtCompletionLaborUnits", "CumulativeEstimateToCompleteCost", "CumulativeEstimateToCompleteLaborUnits", "CumulativeLimit", "CumulativePlannedExpenseCost", "CumulativePlannedLaborCost", "CumulativePlannedLaborUnits", "CumulativePlannedMaterialCost", "CumulativePlannedNonlaborCost", "CumulativePlannedNonlaborUnits", "CumulativePlannedTotalCost", "CumulativePlannedValueCost", "CumulativePlannedValueLaborUnits", "CumulativePeriodActualCost", "CumulativePeriodActualExpenseCost", "CumulativePeriodActualLaborCost", "CumulativePeriodActualLaborUnits", "CumulativePeriodActualMaterialCost", "CumulativePeriodActualNonLaborCost", "CumulativePeriodActualNonLaborUnits", "CumulativePeriodAtCompletionExpenseCost", "CumulativePeriodAtCompletionLaborCost", "CumulativePeriodAtCompletionLaborUnits", "CumulativePeriodAtCompletionMaterialCost", "CumulativePeriodAtCompletionNonLaborCost", "CumulativePeriodAtCompletionNonLaborUnits", "CumulativePeriodAtCompletionTotalCost", "CumulativePeriodEarnedValueCost", "CumulativePeriodEarnedValueLaborUnits", "CumulativePeriodEstimateAtCompletionCost", "CumulativePeriodEstimateAtCompletionLaborUnits", "CumulativePeriodPlannedValueCost", "CumulativePeriodPlannedValueLaborUnits", "CumulativeRemainingExpenseCost", "CumulativeRemainingLaborCost", "CumulativeRemainingLaborUnits", "CumulativeRemainingLateExpenseCost", "CumulativeRemainingLateLaborCost", "CumulativeRemainingLateLaborUnits", "CumulativeRemainingLateMaterialCost", "CumulativeRemainingLateNonlaborCost", "CumulativeRemainingLateNonlaborUnits", "CumulativeRemainingLateTotalCost", "CumulativeRemainingMaterialCost", "CumulativeRemainingNonlaborCost", "CumulativeRemainingNonlaborUnits", "CumulativeRemainingTotalCost"]

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
        """Create an instance of SummarizedSpreadPeriod from a JSON string"""
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
        """Create an instance of SummarizedSpreadPeriod from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "StartDate": obj.get("StartDate"),
            "EndDate": obj.get("EndDate"),
            "ActualCost": obj.get("ActualCost"),
            "ActualExpenseCost": obj.get("ActualExpenseCost"),
            "ActualLaborCost": obj.get("ActualLaborCost"),
            "ActualLaborUnits": obj.get("ActualLaborUnits"),
            "ActualMaterialCost": obj.get("ActualMaterialCost"),
            "ActualNonlaborCost": obj.get("ActualNonlaborCost"),
            "ActualNonlaborUnits": obj.get("ActualNonlaborUnits"),
            "ActualTotalCost": obj.get("ActualTotalCost"),
            "AtCompletionExpenseCost": obj.get("AtCompletionExpenseCost"),
            "AtCompletionLaborCost": obj.get("AtCompletionLaborCost"),
            "AtCompletionLaborUnits": obj.get("AtCompletionLaborUnits"),
            "AtCompletionMaterialCost": obj.get("AtCompletionMaterialCost"),
            "AtCompletionNonlaborCost": obj.get("AtCompletionNonlaborCost"),
            "AtCompletionNonlaborUnits": obj.get("AtCompletionNonlaborUnits"),
            "AtCompletionTotalCost": obj.get("AtCompletionTotalCost"),
            "BaselinePlannedExpenseCost": obj.get("BaselinePlannedExpenseCost"),
            "BaselinePlannedLaborCost": obj.get("BaselinePlannedLaborCost"),
            "BaselinePlannedLaborUnits": obj.get("BaselinePlannedLaborUnits"),
            "BaselinePlannedMaterialCost": obj.get("BaselinePlannedMaterialCost"),
            "BaselinePlannedNonlaborCost": obj.get("BaselinePlannedNonlaborCost"),
            "BaselinePlannedNonlaborUnits": obj.get("BaselinePlannedNonlaborUnits"),
            "BaselinePlannedTotalCost": obj.get("BaselinePlannedTotalCost"),
            "EarnedValueCost": obj.get("EarnedValueCost"),
            "EarnedValueLaborUnits": obj.get("EarnedValueLaborUnits"),
            "EstimateAtCompletionCost": obj.get("EstimateAtCompletionCost"),
            "EstimateAtCompletionLaborUnits": obj.get("EstimateAtCompletionLaborUnits"),
            "EstimateToCompleteCost": obj.get("EstimateToCompleteCost"),
            "EstimateToCompleteLaborUnits": obj.get("EstimateToCompleteLaborUnits"),
            "PeriodActualCost": obj.get("PeriodActualCost"),
            "PeriodActualExpenseCost": obj.get("PeriodActualExpenseCost"),
            "PeriodActualLaborCost": obj.get("PeriodActualLaborCost"),
            "PeriodActualLaborUnits": obj.get("PeriodActualLaborUnits"),
            "PeriodActualMaterialCost": obj.get("PeriodActualMaterialCost"),
            "PeriodActualNonLaborCost": obj.get("PeriodActualNonLaborCost"),
            "PeriodActualNonLaborUnits": obj.get("PeriodActualNonLaborUnits"),
            "PeriodAtCompletionExpenseCost": obj.get("PeriodAtCompletionExpenseCost"),
            "PeriodAtCompletionLaborCost": obj.get("PeriodAtCompletionLaborCost"),
            "PeriodAtCompletionLaborUnits": obj.get("PeriodAtCompletionLaborUnits"),
            "PeriodAtCompletionMaterialCost": obj.get("PeriodAtCompletionMaterialCost"),
            "PeriodAtCompletionNonLaborCost": obj.get("PeriodAtCompletionNonLaborCost"),
            "PeriodAtCompletionNonLaborUnits": obj.get("PeriodAtCompletionNonLaborUnits"),
            "PeriodAtCompletionTotalCost": obj.get("PeriodAtCompletionTotalCost"),
            "PeriodEarnedValueCost": obj.get("PeriodEarnedValueCost"),
            "PeriodEarnedValueLaborUnits": obj.get("PeriodEarnedValueLaborUnits"),
            "PeriodEstimateAtCompletionCost": obj.get("PeriodEstimateAtCompletionCost"),
            "PeriodEstimateAtCompletionLaborUnits": obj.get("PeriodEstimateAtCompletionLaborUnits"),
            "PeriodPlannedValueCost": obj.get("PeriodPlannedValueCost"),
            "PeriodPlannedValueLaborUnits": obj.get("PeriodPlannedValueLaborUnits"),
            "PlannedExpenseCost": obj.get("PlannedExpenseCost"),
            "PlannedLaborCost": obj.get("PlannedLaborCost"),
            "PlannedLaborUnits": obj.get("PlannedLaborUnits"),
            "PlannedMaterialCost": obj.get("PlannedMaterialCost"),
            "PlannedNonlaborCost": obj.get("PlannedNonlaborCost"),
            "PlannedNonlaborUnits": obj.get("PlannedNonlaborUnits"),
            "PlannedTotalCost": obj.get("PlannedTotalCost"),
            "PlannedValueCost": obj.get("PlannedValueCost"),
            "PlannedValueLaborUnits": obj.get("PlannedValueLaborUnits"),
            "RemainingExpenseCost": obj.get("RemainingExpenseCost"),
            "RemainingLaborCost": obj.get("RemainingLaborCost"),
            "RemainingLaborUnits": obj.get("RemainingLaborUnits"),
            "RemainingLateExpenseCost": obj.get("RemainingLateExpenseCost"),
            "RemainingLateLaborCost": obj.get("RemainingLateLaborCost"),
            "RemainingLateLaborUnits": obj.get("RemainingLateLaborUnits"),
            "RemainingLateMaterialCost": obj.get("RemainingLateMaterialCost"),
            "RemainingLateNonlaborCost": obj.get("RemainingLateNonlaborCost"),
            "RemainingLateNonlaborUnits": obj.get("RemainingLateNonlaborUnits"),
            "RemainingLateTotalCost": obj.get("RemainingLateTotalCost"),
            "RemainingMaterialCost": obj.get("RemainingMaterialCost"),
            "RemainingNonlaborCost": obj.get("RemainingNonlaborCost"),
            "RemainingNonlaborUnits": obj.get("RemainingNonlaborUnits"),
            "RemainingTotalCost": obj.get("RemainingTotalCost"),
            "CumulativeActualCost": obj.get("CumulativeActualCost"),
            "CumulativeActualExpenseCost": obj.get("CumulativeActualExpenseCost"),
            "CumulativeActualLaborCost": obj.get("CumulativeActualLaborCost"),
            "CumulativeActualLaborUnits": obj.get("CumulativeActualLaborUnits"),
            "CumulativeActualMaterialCost": obj.get("CumulativeActualMaterialCost"),
            "CumulativeActualNonlaborCost": obj.get("CumulativeActualNonlaborCost"),
            "CumulativeActualNonlaborUnits": obj.get("CumulativeActualNonlaborUnits"),
            "CumulativeActualTotalCost": obj.get("CumulativeActualTotalCost"),
            "CumulativeAtCompletionExpenseCost": obj.get("CumulativeAtCompletionExpenseCost"),
            "CumulativeAtCompletionLaborCost": obj.get("CumulativeAtCompletionLaborCost"),
            "CumulativeAtCompletionLaborUnits": obj.get("CumulativeAtCompletionLaborUnits"),
            "CumulativeAtCompletionMaterialCost": obj.get("CumulativeAtCompletionMaterialCost"),
            "CumulativeAtCompletionNonlaborCost": obj.get("CumulativeAtCompletionNonlaborCost"),
            "CumulativeAtCompletionNonlaborUnits": obj.get("CumulativeAtCompletionNonlaborUnits"),
            "CumulativeAtCompletionTotalCost": obj.get("CumulativeAtCompletionTotalCost"),
            "CumulativeBaselinePlannedExpenseCost": obj.get("CumulativeBaselinePlannedExpenseCost"),
            "CumulativeBaselinePlannedLaborCost": obj.get("CumulativeBaselinePlannedLaborCost"),
            "CumulativeBaselinePlannedLaborUnits": obj.get("CumulativeBaselinePlannedLaborUnits"),
            "CumulativeBaselinePlannedMaterialCost": obj.get("CumulativeBaselinePlannedMaterialCost"),
            "CumulativeBaselinePlannedNonlaborCost": obj.get("CumulativeBaselinePlannedNonlaborCost"),
            "CumulativeBaselinePlannedNonlaborUnits": obj.get("CumulativeBaselinePlannedNonlaborUnits"),
            "CumulativeBaselinePlannedTotalCost": obj.get("CumulativeBaselinePlannedTotalCost"),
            "CumulativeEarnedValueCost": obj.get("CumulativeEarnedValueCost"),
            "CumulativeEarnedValueLaborUnits": obj.get("CumulativeEarnedValueLaborUnits"),
            "CumulativeEstimateAtCompletionCost": obj.get("CumulativeEstimateAtCompletionCost"),
            "CumulativeEstimateAtCompletionLaborUnits": obj.get("CumulativeEstimateAtCompletionLaborUnits"),
            "CumulativeEstimateToCompleteCost": obj.get("CumulativeEstimateToCompleteCost"),
            "CumulativeEstimateToCompleteLaborUnits": obj.get("CumulativeEstimateToCompleteLaborUnits"),
            "CumulativeLimit": obj.get("CumulativeLimit"),
            "CumulativePlannedExpenseCost": obj.get("CumulativePlannedExpenseCost"),
            "CumulativePlannedLaborCost": obj.get("CumulativePlannedLaborCost"),
            "CumulativePlannedLaborUnits": obj.get("CumulativePlannedLaborUnits"),
            "CumulativePlannedMaterialCost": obj.get("CumulativePlannedMaterialCost"),
            "CumulativePlannedNonlaborCost": obj.get("CumulativePlannedNonlaborCost"),
            "CumulativePlannedNonlaborUnits": obj.get("CumulativePlannedNonlaborUnits"),
            "CumulativePlannedTotalCost": obj.get("CumulativePlannedTotalCost"),
            "CumulativePlannedValueCost": obj.get("CumulativePlannedValueCost"),
            "CumulativePlannedValueLaborUnits": obj.get("CumulativePlannedValueLaborUnits"),
            "CumulativePeriodActualCost": obj.get("CumulativePeriodActualCost"),
            "CumulativePeriodActualExpenseCost": obj.get("CumulativePeriodActualExpenseCost"),
            "CumulativePeriodActualLaborCost": obj.get("CumulativePeriodActualLaborCost"),
            "CumulativePeriodActualLaborUnits": obj.get("CumulativePeriodActualLaborUnits"),
            "CumulativePeriodActualMaterialCost": obj.get("CumulativePeriodActualMaterialCost"),
            "CumulativePeriodActualNonLaborCost": obj.get("CumulativePeriodActualNonLaborCost"),
            "CumulativePeriodActualNonLaborUnits": obj.get("CumulativePeriodActualNonLaborUnits"),
            "CumulativePeriodAtCompletionExpenseCost": obj.get("CumulativePeriodAtCompletionExpenseCost"),
            "CumulativePeriodAtCompletionLaborCost": obj.get("CumulativePeriodAtCompletionLaborCost"),
            "CumulativePeriodAtCompletionLaborUnits": obj.get("CumulativePeriodAtCompletionLaborUnits"),
            "CumulativePeriodAtCompletionMaterialCost": obj.get("CumulativePeriodAtCompletionMaterialCost"),
            "CumulativePeriodAtCompletionNonLaborCost": obj.get("CumulativePeriodAtCompletionNonLaborCost"),
            "CumulativePeriodAtCompletionNonLaborUnits": obj.get("CumulativePeriodAtCompletionNonLaborUnits"),
            "CumulativePeriodAtCompletionTotalCost": obj.get("CumulativePeriodAtCompletionTotalCost"),
            "CumulativePeriodEarnedValueCost": obj.get("CumulativePeriodEarnedValueCost"),
            "CumulativePeriodEarnedValueLaborUnits": obj.get("CumulativePeriodEarnedValueLaborUnits"),
            "CumulativePeriodEstimateAtCompletionCost": obj.get("CumulativePeriodEstimateAtCompletionCost"),
            "CumulativePeriodEstimateAtCompletionLaborUnits": obj.get("CumulativePeriodEstimateAtCompletionLaborUnits"),
            "CumulativePeriodPlannedValueCost": obj.get("CumulativePeriodPlannedValueCost"),
            "CumulativePeriodPlannedValueLaborUnits": obj.get("CumulativePeriodPlannedValueLaborUnits"),
            "CumulativeRemainingExpenseCost": obj.get("CumulativeRemainingExpenseCost"),
            "CumulativeRemainingLaborCost": obj.get("CumulativeRemainingLaborCost"),
            "CumulativeRemainingLaborUnits": obj.get("CumulativeRemainingLaborUnits"),
            "CumulativeRemainingLateExpenseCost": obj.get("CumulativeRemainingLateExpenseCost"),
            "CumulativeRemainingLateLaborCost": obj.get("CumulativeRemainingLateLaborCost"),
            "CumulativeRemainingLateLaborUnits": obj.get("CumulativeRemainingLateLaborUnits"),
            "CumulativeRemainingLateMaterialCost": obj.get("CumulativeRemainingLateMaterialCost"),
            "CumulativeRemainingLateNonlaborCost": obj.get("CumulativeRemainingLateNonlaborCost"),
            "CumulativeRemainingLateNonlaborUnits": obj.get("CumulativeRemainingLateNonlaborUnits"),
            "CumulativeRemainingLateTotalCost": obj.get("CumulativeRemainingLateTotalCost"),
            "CumulativeRemainingMaterialCost": obj.get("CumulativeRemainingMaterialCost"),
            "CumulativeRemainingNonlaborCost": obj.get("CumulativeRemainingNonlaborCost"),
            "CumulativeRemainingNonlaborUnits": obj.get("CumulativeRemainingNonlaborUnits"),
            "CumulativeRemainingTotalCost": obj.get("CumulativeRemainingTotalCost")
        })
        return _obj

