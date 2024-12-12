# ProjectCodeAssignment

ProjectCodeAssignment Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_date** | **datetime** | The date this code assignment was created. | [optional] 
**create_user** | **str** | The name of the user that created this code assignment. | [optional] 
**is_baseline** | **bool** | The boolean value indicating if this business object is related to a Project or Baseline | [optional] 
**is_template** | **bool** | The boolean value indicating if this business object is related to a template Project. | [optional] 
**last_update_date** | **datetime** | The date this code assignment was last updated. | [optional] 
**last_update_user** | **str** | The name of the user that last updated this code assignment. | [optional] 
**project_code_description** | **str** | The description of the associated project code. | [optional] 
**project_code_object_id** | **int** | The unique ID of the associated project code. | 
**project_code_type_name** | **str** | The name of the parent project code type. | [optional] 
**project_code_type_object_id** | **int** | The unique ID of the parent project code type. | [optional] 
**project_code_value** | **str** | The value of the associated project code. | [optional] 
**project_id** | **str** | The short code that uniquely identifies the associated project. | [optional] 
**project_name** | **str** | The name of the project to which the project code is assigned. | [optional] 
**project_object_id** | **int** | The unique ID of the project to which the project code is assigned. | 
**wbs_object_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.project_code_assignment import ProjectCodeAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCodeAssignment from a JSON string
project_code_assignment_instance = ProjectCodeAssignment.from_json(json)
# print the JSON string representation of the object
print(ProjectCodeAssignment.to_json())

# convert the object into a dict
project_code_assignment_dict = project_code_assignment_instance.to_dict()
# create an instance of ProjectCodeAssignment from a dict
project_code_assignment_from_dict = ProjectCodeAssignment.from_dict(project_code_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


