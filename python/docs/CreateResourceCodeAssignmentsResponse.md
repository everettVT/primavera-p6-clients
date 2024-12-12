# CreateResourceCodeAssignmentsResponse

CreateResourceCodeAssignmentsResponse Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_code_type_object_id** | **int** | The unique ID of the parent resource code type. | [optional] 
**resource_object_id** | **int** | The unique ID of the resource to which the resource code is assigned. | [optional] 

## Example

```python
from openapi_client.models.create_resource_code_assignments_response import CreateResourceCodeAssignmentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateResourceCodeAssignmentsResponse from a JSON string
create_resource_code_assignments_response_instance = CreateResourceCodeAssignmentsResponse.from_json(json)
# print the JSON string representation of the object
print(CreateResourceCodeAssignmentsResponse.to_json())

# convert the object into a dict
create_resource_code_assignments_response_dict = create_resource_code_assignments_response_instance.to_dict()
# create an instance of CreateResourceCodeAssignmentsResponse from a dict
create_resource_code_assignments_response_from_dict = CreateResourceCodeAssignmentsResponse.from_dict(create_resource_code_assignments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


