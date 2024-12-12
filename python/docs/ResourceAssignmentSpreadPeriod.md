# ResourceAssignmentSpreadPeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**actual_cost** | **float** |  | [optional] 
**actual_overtime_cost** | **float** |  | [optional] 
**actual_overtime_units** | **float** |  | [optional] 
**actual_regular_cost** | **float** |  | [optional] 
**actual_regular_units** | **float** |  | [optional] 
**actual_units** | **float** |  | [optional] 
**at_completion_cost** | **float** |  | [optional] 
**at_completion_units** | **float** |  | [optional] 
**planned_cost** | **float** |  | [optional] 
**planned_units** | **float** |  | [optional] 
**remaining_cost** | **float** |  | [optional] 
**remaining_late_cost** | **float** |  | [optional] 
**remaining_late_units** | **float** |  | [optional] 
**remaining_units** | **float** |  | [optional] 
**staffed_remaining_cost** | **float** |  | [optional] 
**staffed_remaining_late_cost** | **float** |  | [optional] 
**staffed_remaining_late_units** | **float** |  | [optional] 
**staffed_remaining_units** | **float** |  | [optional] 
**unstaffed_remaining_cost** | **float** |  | [optional] 
**unstaffed_remaining_late_cost** | **float** |  | [optional] 
**unstaffed_remaining_late_units** | **float** |  | [optional] 
**unstaffed_remaining_units** | **float** |  | [optional] 
**cumulative_actual_cost** | **float** |  | [optional] 
**cumulative_actual_overtime_cost** | **float** |  | [optional] 
**cumulative_actual_overtime_units** | **float** |  | [optional] 
**cumulative_actual_regular_cost** | **float** |  | [optional] 
**cumulative_actual_regular_units** | **float** |  | [optional] 
**cumulative_actual_units** | **float** |  | [optional] 
**cumulative_at_completion_cost** | **float** |  | [optional] 
**cumulative_at_completion_units** | **float** |  | [optional] 
**cumulative_planned_cost** | **float** |  | [optional] 
**cumulative_planned_units** | **float** |  | [optional] 
**cumulative_remaining_cost** | **float** |  | [optional] 
**cumulative_remaining_late_cost** | **float** |  | [optional] 
**cumulative_remaining_late_units** | **float** |  | [optional] 
**cumulative_remaining_units** | **float** |  | [optional] 
**cumulative_staffed_remaining_cost** | **float** |  | [optional] 
**cumulative_staffed_remaining_late_cost** | **float** |  | [optional] 
**cumulative_staffed_remaining_late_units** | **float** |  | [optional] 
**cumulative_staffed_remaining_units** | **float** |  | [optional] 
**cumulative_unstaffed_remaining_cost** | **float** |  | [optional] 
**cumulative_unstaffed_remaining_late_cost** | **float** |  | [optional] 
**cumulative_unstaffed_remaining_late_units** | **float** |  | [optional] 
**cumulative_unstaffed_remaining_units** | **float** |  | [optional] 
**period_actual_cost** | **float** |  | [optional] 
**period_actual_units** | **float** |  | [optional] 
**period_at_completion_cost** | **float** |  | [optional] 
**period_at_completion_units** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.resource_assignment_spread_period import ResourceAssignmentSpreadPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceAssignmentSpreadPeriod from a JSON string
resource_assignment_spread_period_instance = ResourceAssignmentSpreadPeriod.from_json(json)
# print the JSON string representation of the object
print(ResourceAssignmentSpreadPeriod.to_json())

# convert the object into a dict
resource_assignment_spread_period_dict = resource_assignment_spread_period_instance.to_dict()
# create an instance of ResourceAssignmentSpreadPeriod from a dict
resource_assignment_spread_period_from_dict = ResourceAssignmentSpreadPeriod.from_dict(resource_assignment_spread_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


