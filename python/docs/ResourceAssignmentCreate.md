# ResourceAssignmentCreate

ResourceAssignmentCreate Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_object_id** | **int** | The unique ID of the activity to which the associated assignment is assigned. | 
**actual_finish_date** | **datetime** | The date the resource actually finished working on the activity. | [optional] 
**actual_start_date** | **datetime** | The date the resource actually started working on the activity. | [optional] 
**actual_units** | **float** | The actual units worked by the resource on this activity. | [optional] 
**assignment_is_read** | **str** | To determine whether or not the newly created assignment from P6 Team Member Web is viewed by the manager in the Control Status Update. | [optional] 
**change_set_object_id** | **int** | The unique ID of the associated Changeset. | [optional] 
**var_date** | **datetime** | The date of the transaction. | [optional] 
**project_object_id** | **int** | The unique identifier of the project that is associated with the ResourceAssignmentCreate object. | [optional] 
**remaining_duration** | **float** | The remaining finish date for the resource working on the activity. | [optional] 
**remaining_finish_date** | **datetime** | The remaining finish date for the resource working on the activity. | [optional] 
**remaining_units** | **float** | The remaining units of work to be performed by this resource on this activity. | [optional] 
**request_user_object_id** | **int** | The unique ID of the user modifying the task, assignment or step. | [optional] 
**resource_assignment_create_object_id** | **int** | The unique identifier of the ResourceAssignment that is associated to the ResourceAssignmentCreate. | [optional] 
**resource_assignment_object_id** | **int** | The unique identifier of the ResourceAssignment that is associated with ResourceAssignmentCreate object. | [optional] 
**resource_object_id** | **int** | The unique identifier of the associated resource. | 
**status** | **str** | The status of the resource assignment. [not sure about the filter orderable or read only] | [optional] 

## Example

```python
from openapi_client.models.resource_assignment_create import ResourceAssignmentCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceAssignmentCreate from a JSON string
resource_assignment_create_instance = ResourceAssignmentCreate.from_json(json)
# print the JSON string representation of the object
print(ResourceAssignmentCreate.to_json())

# convert the object into a dict
resource_assignment_create_dict = resource_assignment_create_instance.to_dict()
# create an instance of ResourceAssignmentCreate from a dict
resource_assignment_create_from_dict = ResourceAssignmentCreate.from_dict(resource_assignment_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


