# ExpenseSpreadPeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**financial_period_object_id** | **int** |  | [optional] 
**actual_cost** | **float** |  | [optional] 
**at_completion_cost** | **float** |  | [optional] 
**planned_cost** | **float** |  | [optional] 
**remaining_cost** | **float** |  | [optional] 
**cumulative_actual_cost** | **float** |  | [optional] 
**cumulative_at_completion_cost** | **float** |  | [optional] 
**cumulative_planned_cost** | **float** |  | [optional] 
**cumulative_remaining_cost** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.expense_spread_period import ExpenseSpreadPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseSpreadPeriod from a JSON string
expense_spread_period_instance = ExpenseSpreadPeriod.from_json(json)
# print the JSON string representation of the object
print(ExpenseSpreadPeriod.to_json())

# convert the object into a dict
expense_spread_period_dict = expense_spread_period_instance.to_dict()
# create an instance of ExpenseSpreadPeriod from a dict
expense_spread_period_from_dict = ExpenseSpreadPeriod.from_dict(expense_spread_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


