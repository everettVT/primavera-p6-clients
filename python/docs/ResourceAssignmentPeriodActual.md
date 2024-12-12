# ResourceAssignmentPeriodActual

ResourceAssignmentPeriodActual Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_object_id** | **int** | The unique ID of the associated activity. | [optional] 
**actual_cost** | **float** | The actual cost on this resource assignment during a financial period. | 
**actual_units** | **float** | The actual units on this resource assignment during a financial period. | 
**create_date** | **datetime** | The date this resource assignment period actual was created. | [optional] 
**create_user** | **str** | The name of the user that created this resource assignment period actual. | [optional] 
**financial_period_object_id** | **int** | The unique ID of the associated financial period. | 
**is_baseline** | **bool** | The boolean value indicating if this business object is related to a Project or Baseline | [optional] 
**is_template** | **bool** | The boolean value indicating if this business object is related to a template Project. | [optional] 
**last_update_date** | **datetime** | The date this resource assignment period actual was last updated. | [optional] 
**last_update_user** | **str** | The name of the user that last updated this resource assignment period actual. | [optional] 
**project_object_id** | **int** | The unique ID of the associated project. | [optional] 
**resource_assignment_object_id** | **int** | The unique ID of the associated resource assignment. | 
**resource_type** | **str** | The resource type: \&quot;Labor\&quot;, \&quot;Nonlabor\&quot;, or \&quot;Material\&quot;. | [optional] 
**wbs_object_id** | **int** | The unique ID of the WBS for the associated activity. | [optional] 

## Example

```python
from openapi_client.models.resource_assignment_period_actual import ResourceAssignmentPeriodActual

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceAssignmentPeriodActual from a JSON string
resource_assignment_period_actual_instance = ResourceAssignmentPeriodActual.from_json(json)
# print the JSON string representation of the object
print(ResourceAssignmentPeriodActual.to_json())

# convert the object into a dict
resource_assignment_period_actual_dict = resource_assignment_period_actual_instance.to_dict()
# create an instance of ResourceAssignmentPeriodActual from a dict
resource_assignment_period_actual_from_dict = ResourceAssignmentPeriodActual.from_dict(resource_assignment_period_actual_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


