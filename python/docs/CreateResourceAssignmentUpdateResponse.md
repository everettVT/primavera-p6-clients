# CreateResourceAssignmentUpdateResponse

CreateResourceAssignmentUpdateResponse Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_assignment_object_id** | **int** | The unique identifier for the ResourceAssignment. You can specify one or more ResourceAssignmentObjectID. | [optional] 
**change_set_object_id** | **str** | The unique ID generated by the system for the change set object. | [optional] 

## Example

```python
from openapi_client.models.create_resource_assignment_update_response import CreateResourceAssignmentUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateResourceAssignmentUpdateResponse from a JSON string
create_resource_assignment_update_response_instance = CreateResourceAssignmentUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(CreateResourceAssignmentUpdateResponse.to_json())

# convert the object into a dict
create_resource_assignment_update_response_dict = create_resource_assignment_update_response_instance.to_dict()
# create an instance of CreateResourceAssignmentUpdateResponse from a dict
create_resource_assignment_update_response_from_dict = CreateResourceAssignmentUpdateResponse.from_dict(create_resource_assignment_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

