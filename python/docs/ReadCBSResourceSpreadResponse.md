# ReadCBSResourceSpreadResponse

ReadCBSResourceSpreadResponse Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cbsresource_spread** | [**List[CBSResourceSpread]**](CBSResourceSpread.md) |  | [optional] 
**cbs_resource_spread** | [**List[CBSResourceSpread]**](CBSResourceSpread.md) |  | [optional] 

## Example

```python
from openapi_client.models.read_cbs_resource_spread_response import ReadCBSResourceSpreadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadCBSResourceSpreadResponse from a JSON string
read_cbs_resource_spread_response_instance = ReadCBSResourceSpreadResponse.from_json(json)
# print the JSON string representation of the object
print(ReadCBSResourceSpreadResponse.to_json())

# convert the object into a dict
read_cbs_resource_spread_response_dict = read_cbs_resource_spread_response_instance.to_dict()
# create an instance of ReadCBSResourceSpreadResponse from a dict
read_cbs_resource_spread_response_from_dict = ReadCBSResourceSpreadResponse.from_dict(read_cbs_resource_spread_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


