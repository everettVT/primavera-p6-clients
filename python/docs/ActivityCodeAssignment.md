# ActivityCodeAssignment

ActivityCodeAssignment Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_code_description** | **str** | The description of the associated activity code. | [optional] 
**activity_code_object_id** | **int** | The unique ID of the associated activity code. | 
**activity_code_type_name** | **str** | The name of the parent activity code type. | [optional] 
**activity_code_type_object_id** | **int** | The unique ID of the parent activity code type. | [optional] 
**activity_code_type_scope** | **str** | The scope of the associated activity code type: Global, EPS, or Project. An activity code with Global scope can be assigned to any activity. An activity code with EPS scope can be assigned only to an activity within a project under that particular EPS. Similarly, an activity code with Project scope can be assigned only to an activity within that particular project. | [optional] 
**activity_code_value** | **str** | The value of the associated activity code. | [optional] 
**activity_id** | **str** | The short ID that uniquely identifies the activity to which the activity code is assigned. | [optional] 
**activity_name** | **str** | The name of the activity to which the activity code is assigned. | [optional] 
**activity_object_id** | **int** | The unique ID of the activity to which the activity code is assigned. | 
**create_date** | **datetime** | The date this code assignment was created. | [optional] 
**create_user** | **str** | The name of the user that created this code assignment. | [optional] 
**is_baseline** | **bool** | The boolean value indicating if this business object is related to a Project or Baseline. | [optional] 
**is_template** | **bool** | The boolean value indicating if this business object is related to a template Project. | [optional] 
**last_update_date** | **datetime** | The date this code assignment was last updated. | [optional] 
**last_update_user** | **str** | The name of the user that last updated this code assignment. | [optional] 
**project_id** | **str** | The short code of the associated project. | [optional] 
**project_object_id** | **int** | The unique ID of the associated project. | [optional] 
**wbs_object_id** | **int** | The unique ID of the WBS for the associated activity. | [optional] 

## Example

```python
from openapi_client.models.activity_code_assignment import ActivityCodeAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityCodeAssignment from a JSON string
activity_code_assignment_instance = ActivityCodeAssignment.from_json(json)
# print the JSON string representation of the object
print(ActivityCodeAssignment.to_json())

# convert the object into a dict
activity_code_assignment_dict = activity_code_assignment_instance.to_dict()
# create an instance of ActivityCodeAssignment from a dict
activity_code_assignment_from_dict = ActivityCodeAssignment.from_dict(activity_code_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


