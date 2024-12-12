# ScheduleCheckOption

ScheduleCheckOption Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_bei_tripwire** | **bool** | The baseline execution index. | [optional] 
**check_hard_constraints** | **bool** | Checks for the constraints that prevent activities from being moved. | [optional] 
**check_invalid_progress** | **bool** | Checks for activities that have invalid progress dates. | [optional] 
**check_lags** | **bool** | Checks for relationships that have a positive lag duration. | [optional] 
**check_large_durations** | **bool** | Checks for activities that have a remaining duration that is greater than the specified LargeDurationCriteria value.. | [optional] 
**check_large_float** | **bool** | Checks for activities that have a float value greater than the specified LargeFloatCriteria value. | [optional] 
**check_late_activities** | **bool** | Checks for activities that are scheduled to finish later than the project baseline. | [optional] 
**check_logic** | **bool** | Checks for activities with missing predecessors or successors. | [optional] 
**check_long_lags** | **bool** | Checks for relationships that have a lag duration that is greater than the specified LongLagsCriteria value. | [optional] 
**check_negative_float** | **bool** | Checks for activities that have a total float less than 0. | [optional] 
**check_negative_lags** | **bool** | Checks for relationships that have a lag duration less than 0. | [optional] 
**check_relation_ships** | **bool** | Checks for the relationships that are set | [optional] 
**check_resources** | **bool** | Checks for activities that do not have an expense or an assigned resource. | [optional] 
**check_soft_constraints** | **bool** | Checks for constraints that do not prevent activities from being moved. | [optional] 
**hard_constraint_target** | **int** | Checks for constraints that prevent activities from being moved. | [optional] 
**lags_target** | **int** | Relationships that have a positive lag duration. | [optional] 
**large_duration_criteria** | **int** | The value of the Large Duration Criteria. | [optional] 
**large_duration_target** | **int** | Activities that have a remaining duration greater than the Large Duration Criteria. | [optional] 
**large_float_criteria** | **int** | The value of the Large Float Criteria. | [optional] 
**large_float_target** | **int** | Activities that have a total float greater than the Large Float Criteria. | [optional] 
**late_activities_target** | **int** | Activities that are scheduled to finish later than the project baseline. | [optional] 
**logic_target** | **int** | Activities that are missing predecessors or successors. | [optional] 
**long_lags_criteria** | **int** | The value of the Long Lags Criteria. | [optional] 
**long_lags_target** | **int** | Relationships that have a lag duration greater than the Long Lags Criteria. | [optional] 
**negative_float_target** | **int** | Activities that have a total float less than 0. | [optional] 
**negative_lags_target** | **int** | Relationships that have a lag duration less than 0. | [optional] 
**progress_date_target** | **int** | Activities that have invalid progress dates. | [optional] 
**proj_prop_type_int** | **int** | The enum values that are associated with the Project Property Type. | [optional] 
**project_object_id** | **int** | The unique identifier of the project which has a schedule you want to check. | [optional] 
**prop_value** | **str** | The Project Property Type value. | [optional] 
**relationship_target** | **int** | The relationships that are finish to start. | [optional] 
**resources_target** | **int** | Activities that do not have an expense or an assigned resource. | [optional] 
**schedule_check_data** | **str** | The ScheduleCheck data. | [optional] 
**schedule_check_options_id** | **int** | The unique id for ScheduleCheckOptions. | [optional] 
**soft_constraint_target** | **int** | Constraints that do not prevent activities from being moved. | [optional] 
**bei_tripwire_target** | **float** | The baseline execution index. | [optional] 

## Example

```python
from openapi_client.models.schedule_check_option import ScheduleCheckOption

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleCheckOption from a JSON string
schedule_check_option_instance = ScheduleCheckOption.from_json(json)
# print the JSON string representation of the object
print(ScheduleCheckOption.to_json())

# convert the object into a dict
schedule_check_option_dict = schedule_check_option_instance.to_dict()
# create an instance of ScheduleCheckOption from a dict
schedule_check_option_from_dict = ScheduleCheckOption.from_dict(schedule_check_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


