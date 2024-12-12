# CreateActivityCodeAssignmentsResponse

CreateActivityCodeAssignmentsResponse Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_code_type_object_id** | **int** | The unique ID of the parent activity code type. | [optional] 
**activity_object_id** | **int** | The unique ID of the activity to which the activity code is assigned. | [optional] 

## Example

```python
from openapi_client.models.create_activity_code_assignments_response import CreateActivityCodeAssignmentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateActivityCodeAssignmentsResponse from a JSON string
create_activity_code_assignments_response_instance = CreateActivityCodeAssignmentsResponse.from_json(json)
# print the JSON string representation of the object
print(CreateActivityCodeAssignmentsResponse.to_json())

# convert the object into a dict
create_activity_code_assignments_response_dict = create_activity_code_assignments_response_instance.to_dict()
# create an instance of CreateActivityCodeAssignmentsResponse from a dict
create_activity_code_assignments_response_from_dict = CreateActivityCodeAssignmentsResponse.from_dict(create_activity_code_assignments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


