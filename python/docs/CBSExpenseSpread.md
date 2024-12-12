# CBSExpenseSpread


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
**expense_category_object_id** | **int** |  | [optional] 
**expense_category_name** | **str** |  | [optional] 
**baseline_type** | **str** |  | [optional] 
**data_date** | **datetime** |  | [optional] 
**summary_actual_cost** | **float** |  | [optional] 
**summary_actual_units** | **float** |  | [optional] 
**summary_at_completion_cost** | **float** |  | [optional] 
**summary_at_completion_units** | **float** |  | [optional] 
**summary_planned_cost** | **float** |  | [optional] 
**summary_planned_units** | **float** |  | [optional] 
**summary_remaining_cost** | **float** |  | [optional] 
**summary_remaining_units** | **float** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**period_type** | **str** |  | [optional] 
**period** | [**List[CBSRsrcExpenseSpreadPeriod]**](CBSRsrcExpenseSpreadPeriod.md) |  | [optional] 

## Example

```python
from openapi_client.models.cbs_expense_spread import CBSExpenseSpread

# TODO update the JSON string below
json = "{}"
# create an instance of CBSExpenseSpread from a JSON string
cbs_expense_spread_instance = CBSExpenseSpread.from_json(json)
# print the JSON string representation of the object
print(CBSExpenseSpread.to_json())

# convert the object into a dict
cbs_expense_spread_dict = cbs_expense_spread_instance.to_dict()
# create an instance of CBSExpenseSpread from a dict
cbs_expense_spread_from_dict = CBSExpenseSpread.from_dict(cbs_expense_spread_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


