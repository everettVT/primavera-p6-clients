# CBSRsrcExpenseSpreadPeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**actual_cost** | **float** |  | [optional] 
**actual_units** | **float** |  | [optional] 
**at_completion_cost** | **float** |  | [optional] 
**at_completion_units** | **float** |  | [optional] 
**planned_cost** | **float** |  | [optional] 
**planned_units** | **float** |  | [optional] 
**remaining_cost** | **float** |  | [optional] 
**remaining_units** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.cbs_rsrc_expense_spread_period import CBSRsrcExpenseSpreadPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of CBSRsrcExpenseSpreadPeriod from a JSON string
cbs_rsrc_expense_spread_period_instance = CBSRsrcExpenseSpreadPeriod.from_json(json)
# print the JSON string representation of the object
print(CBSRsrcExpenseSpreadPeriod.to_json())

# convert the object into a dict
cbs_rsrc_expense_spread_period_dict = cbs_rsrc_expense_spread_period_instance.to_dict()
# create an instance of CBSRsrcExpenseSpreadPeriod from a dict
cbs_rsrc_expense_spread_period_from_dict = CBSRsrcExpenseSpreadPeriod.from_dict(cbs_rsrc_expense_spread_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


