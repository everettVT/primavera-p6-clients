# ReadEPSSpreadResponse

ReadEPSSpreadResponse Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**epsid** | **str** |  | [optional] 
**eps_object_id** | **int** |  | [optional] 
**start_date** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**period_type** | **str** |  | [optional] 
**period** | [**List[SummarizedSpreadPeriod]**](SummarizedSpreadPeriod.md) |  | [optional] 

## Example

```python
from openapi_client.models.read_eps_spread_response import ReadEPSSpreadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadEPSSpreadResponse from a JSON string
read_eps_spread_response_instance = ReadEPSSpreadResponse.from_json(json)
# print the JSON string representation of the object
print(ReadEPSSpreadResponse.to_json())

# convert the object into a dict
read_eps_spread_response_dict = read_eps_spread_response_instance.to_dict()
# create an instance of ReadEPSSpreadResponse from a dict
read_eps_spread_response_from_dict = ReadEPSSpreadResponse.from_dict(read_eps_spread_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


