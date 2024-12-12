# ReadWBSExpenseSpreadResponse

ReadWBSExpenseSpreadResponse Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wbs_code** | **str** |  | [optional] 
**wbs_object_id** | **int** |  | [optional] 
**expense_category_name** | **str** |  | [optional] 
**expense_category_object_id** | **int** |  | [optional] 
**start_date** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**period_type** | **str** |  | [optional] 
**period** | [**List[ExpenseSpreadPeriod]**](ExpenseSpreadPeriod.md) |  | [optional] 

## Example

```python
from openapi_client.models.read_wbs_expense_spread_response import ReadWBSExpenseSpreadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadWBSExpenseSpreadResponse from a JSON string
read_wbs_expense_spread_response_instance = ReadWBSExpenseSpreadResponse.from_json(json)
# print the JSON string representation of the object
print(ReadWBSExpenseSpreadResponse.to_json())

# convert the object into a dict
read_wbs_expense_spread_response_dict = read_wbs_expense_spread_response_instance.to_dict()
# create an instance of ReadWBSExpenseSpreadResponse from a dict
read_wbs_expense_spread_response_from_dict = ReadWBSExpenseSpreadResponse.from_dict(read_wbs_expense_spread_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


