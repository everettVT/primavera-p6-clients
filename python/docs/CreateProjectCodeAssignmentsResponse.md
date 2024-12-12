# CreateProjectCodeAssignmentsResponse

CreateProjectCodeAssignmentsResponse Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_object_id** | **int** | The unique ID of the project to which the project code is assigned. | [optional] 
**project_code_type_object_id** | **int** | The unique ID of the parent project code type. | [optional] 

## Example

```python
from openapi_client.models.create_project_code_assignments_response import CreateProjectCodeAssignmentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectCodeAssignmentsResponse from a JSON string
create_project_code_assignments_response_instance = CreateProjectCodeAssignmentsResponse.from_json(json)
# print the JSON string representation of the object
print(CreateProjectCodeAssignmentsResponse.to_json())

# convert the object into a dict
create_project_code_assignments_response_dict = create_project_code_assignments_response_instance.to_dict()
# create an instance of CreateProjectCodeAssignmentsResponse from a dict
create_project_code_assignments_response_from_dict = CreateProjectCodeAssignmentsResponse.from_dict(create_project_code_assignments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


