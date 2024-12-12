# ActivityPeriodActual

ActivityPeriodActual Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_object_id** | **int** | The unique ID of the associated activity. | 
**actual_expense_cost** | **float** | The actual expense cost on this activity during a financial period. | [optional] 
**actual_labor_cost** | **float** | The actual labor cost on this activity during a financial period. | [optional] 
**actual_labor_units** | **float** | The actual labor units on this activity during a financial period. | [optional] 
**actual_material_cost** | **float** | The actual material cost on this activity during a financial period. | [optional] 
**actual_non_labor_cost** | **float** | The actual nonlabor cost on this activity during a financial period. | [optional] 
**actual_non_labor_units** | **float** | The actual nonlabor units on this activity during a financial period. | [optional] 
**create_date** | **datetime** | The date this activity period actual was created. | [optional] 
**create_user** | **str** | The name of the user that created this activity period actual. | [optional] 
**earned_value_cost** | **float** | The earned value cost on this activity during a financial period. | [optional] 
**earned_value_labor_units** | **float** | The earned value labor units on this activity during a financial period. | [optional] 
**financial_period_object_id** | **int** | The unique ID of the associated financial period. | 
**is_baseline** | **bool** | The boolean value indicating if this business object is related to a Project or Baseline | [optional] 
**is_template** | **bool** | The boolean value indicating if this business object is related to a template Project. | [optional] 
**last_update_date** | **datetime** | The date this activity period actual was last updated. | [optional] 
**last_update_user** | **str** | The name of the user that last updated this activity period actual. | [optional] 
**planned_value_cost** | **float** | The planned value cost on this activity during a financial period. | [optional] 
**planned_value_labor_units** | **float** | The planned value labor units on this activity during a financial period. | [optional] 
**project_object_id** | **int** | The unique ID of the associated project. | [optional] 
**wbs_object_id** | **int** | The unique ID of the WBS for the activity. | [optional] 

## Example

```python
from openapi_client.models.activity_period_actual import ActivityPeriodActual

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityPeriodActual from a JSON string
activity_period_actual_instance = ActivityPeriodActual.from_json(json)
# print the JSON string representation of the object
print(ActivityPeriodActual.to_json())

# convert the object into a dict
activity_period_actual_dict = activity_period_actual_instance.to_dict()
# create an instance of ActivityPeriodActual from a dict
activity_period_actual_from_dict = ActivityPeriodActual.from_dict(activity_period_actual_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


