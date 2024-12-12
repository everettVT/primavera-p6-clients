# ReadCBSExpenseSpreadResponse

ReadCBSExpenseSpreadResponse Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cbsexpense_spread** | [**List[CBSExpenseSpread]**](CBSExpenseSpread.md) |  | [optional] 
**cbs_expense_spread** | [**List[CBSExpenseSpread]**](CBSExpenseSpread.md) |  | [optional] 

## Example

```python
from openapi_client.models.read_cbs_expense_spread_response import ReadCBSExpenseSpreadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadCBSExpenseSpreadResponse from a JSON string
read_cbs_expense_spread_response_instance = ReadCBSExpenseSpreadResponse.from_json(json)
# print the JSON string representation of the object
print(ReadCBSExpenseSpreadResponse.to_json())

# convert the object into a dict
read_cbs_expense_spread_response_dict = read_cbs_expense_spread_response_instance.to_dict()
# create an instance of ReadCBSExpenseSpreadResponse from a dict
read_cbs_expense_spread_response_from_dict = ReadCBSExpenseSpreadResponse.from_dict(read_cbs_expense_spread_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


