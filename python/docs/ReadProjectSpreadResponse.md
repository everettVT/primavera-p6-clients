# ReadProjectSpreadResponse

ReadProjectSpreadResponse Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | [optional] 
**project_object_id** | **int** |  | [optional] 
**start_date** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**period_type** | **str** |  | [optional] 
**period** | [**List[SummarizedSpreadPeriod]**](SummarizedSpreadPeriod.md) |  | [optional] 

## Example

```python
from openapi_client.models.read_project_spread_response import ReadProjectSpreadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadProjectSpreadResponse from a JSON string
read_project_spread_response_instance = ReadProjectSpreadResponse.from_json(json)
# print the JSON string representation of the object
print(ReadProjectSpreadResponse.to_json())

# convert the object into a dict
read_project_spread_response_dict = read_project_spread_response_instance.to_dict()
# create an instance of ReadProjectSpreadResponse from a dict
read_project_spread_response_from_dict = ReadProjectSpreadResponse.from_dict(read_project_spread_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


