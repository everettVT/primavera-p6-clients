# ReadResourceAssignmentSpreadResponse

ReadResourceAssignmentSpreadResponse Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_assignment_object_id** | **int** |  | [optional] 
**start_date** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**period_type** | **str** |  | [optional] 
**period** | [**List[ResourceAssignmentSpreadPeriod]**](ResourceAssignmentSpreadPeriod.md) |  | [optional] 

## Example

```python
from openapi_client.models.read_resource_assignment_spread_response import ReadResourceAssignmentSpreadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadResourceAssignmentSpreadResponse from a JSON string
read_resource_assignment_spread_response_instance = ReadResourceAssignmentSpreadResponse.from_json(json)
# print the JSON string representation of the object
print(ReadResourceAssignmentSpreadResponse.to_json())

# convert the object into a dict
read_resource_assignment_spread_response_dict = read_resource_assignment_spread_response_instance.to_dict()
# create an instance of ReadResourceAssignmentSpreadResponse from a dict
read_resource_assignment_spread_response_from_dict = ReadResourceAssignmentSpreadResponse.from_dict(read_resource_assignment_spread_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


