# ReadWBSRoleSpreadResponse

ReadWBSRoleSpreadResponse Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wbs_code** | **str** |  | [optional] 
**wbs_object_id** | **int** |  | [optional] 
**role_id** | **str** |  | [optional] 
**role_object_id** | **int** |  | [optional] 
**start_date** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**period_type** | **str** |  | [optional] 
**period** | [**List[ResourceRoleSpreadPeriod]**](ResourceRoleSpreadPeriod.md) |  | [optional] 

## Example

```python
from openapi_client.models.read_wbs_role_spread_response import ReadWBSRoleSpreadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadWBSRoleSpreadResponse from a JSON string
read_wbs_role_spread_response_instance = ReadWBSRoleSpreadResponse.from_json(json)
# print the JSON string representation of the object
print(ReadWBSRoleSpreadResponse.to_json())

# convert the object into a dict
read_wbs_role_spread_response_dict = read_wbs_role_spread_response_instance.to_dict()
# create an instance of ReadWBSRoleSpreadResponse from a dict
read_wbs_role_spread_response_from_dict = ReadWBSRoleSpreadResponse.from_dict(read_wbs_role_spread_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


