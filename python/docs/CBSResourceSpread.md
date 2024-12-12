# CBSResourceSpread


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cbsobject_id** | **int** |  | [optional] 
**baseline_project_object_id** | **int** |  | [optional] 
**project_object_id** | **int** |  | [optional] 
**project_id** | **str** |  | [optional] 
**project_name** | **str** |  | [optional] 
**original_project_object_id** | **int** |  | [optional] 
**cbs_object_id** | **int** |  | [optional] 
**resource_object_id** | **int** |  | [optional] 
**baseline_type** | **str** |  | [optional] 
**data_date** | **str** |  | [optional] 
**resource_id** | **str** |  | [optional] 
**resource_name** | **str** |  | [optional] 
**resource_type** | **str** |  | [optional] 
**unit_name** | **str** |  | [optional] 
**unit_abbreviation** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**currency_name** | **str** |  | [optional] 
**summary_actual_cost** | **float** |  | [optional] 
**summary_actual_units** | **float** |  | [optional] 
**summary_at_completion_cost** | **float** |  | [optional] 
**summary_at_completion_units** | **float** |  | [optional] 
**summary_planned_cost** | **float** |  | [optional] 
**summary_planned_units** | **float** |  | [optional] 
**summary_remaining_cost** | **float** |  | [optional] 
**summary_remaining_units** | **float** |  | [optional] 
**summary_actual_finish** | **datetime** |  | [optional] 
**summary_actual_start** | **datetime** |  | [optional] 
**summary_planned_finish** | **datetime** |  | [optional] 
**summary_planned_start** | **datetime** |  | [optional] 
**summary_remaining_finish** | **datetime** |  | [optional] 
**summary_remaining_start** | **datetime** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**period_type** | **str** |  | [optional] 
**period** | [**List[CBSRsrcExpenseSpreadPeriod]**](CBSRsrcExpenseSpreadPeriod.md) |  | [optional] 

## Example

```python
from openapi_client.models.cbs_resource_spread import CBSResourceSpread

# TODO update the JSON string below
json = "{}"
# create an instance of CBSResourceSpread from a JSON string
cbs_resource_spread_instance = CBSResourceSpread.from_json(json)
# print the JSON string representation of the object
print(CBSResourceSpread.to_json())

# convert the object into a dict
cbs_resource_spread_dict = cbs_resource_spread_instance.to_dict()
# create an instance of CBSResourceSpread from a dict
cbs_resource_spread_from_dict = CBSResourceSpread.from_dict(cbs_resource_spread_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


