# ReadWBSSpreadResponse

ReadWBSSpreadResponse Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wbs_code** | **str** |  | [optional] 
**wbs_object_id** | **int** |  | [optional] 
**start_date** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**period_type** | **str** |  | [optional] 
**period** | [**List[SummarizedSpreadPeriod]**](SummarizedSpreadPeriod.md) |  | [optional] 

## Example

```python
from openapi_client.models.read_wbs_spread_response import ReadWBSSpreadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadWBSSpreadResponse from a JSON string
read_wbs_spread_response_instance = ReadWBSSpreadResponse.from_json(json)
# print the JSON string representation of the object
print(ReadWBSSpreadResponse.to_json())

# convert the object into a dict
read_wbs_spread_response_dict = read_wbs_spread_response_instance.to_dict()
# create an instance of ReadWBSSpreadResponse from a dict
read_wbs_spread_response_from_dict = ReadWBSSpreadResponse.from_dict(read_wbs_spread_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


