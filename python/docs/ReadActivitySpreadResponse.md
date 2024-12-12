# ReadActivitySpreadResponse

ReadWBSSpreadResponse Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_id** | **str** |  | [optional] 
**activity_object_id** | **int** |  | [optional] 
**start_date** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**period_type** | **str** |  | [optional] 
**period** | [**List[ActivitySpreadPeriod]**](ActivitySpreadPeriod.md) |  | [optional] 

## Example

```python
from openapi_client.models.read_activity_spread_response import ReadActivitySpreadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadActivitySpreadResponse from a JSON string
read_activity_spread_response_instance = ReadActivitySpreadResponse.from_json(json)
# print the JSON string representation of the object
print(ReadActivitySpreadResponse.to_json())

# convert the object into a dict
read_activity_spread_response_dict = read_activity_spread_response_instance.to_dict()
# create an instance of ReadActivitySpreadResponse from a dict
read_activity_spread_response_from_dict = ReadActivitySpreadResponse.from_dict(read_activity_spread_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


