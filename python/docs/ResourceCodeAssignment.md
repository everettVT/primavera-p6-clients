# ResourceCodeAssignment

ResourceCodeAssignment Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_date** | **datetime** | The date this code assignment was created. | [optional] 
**create_user** | **str** | The name of the user that created this code assignment. | [optional] 
**last_update_date** | **datetime** | The date this code assignment was last updated. | [optional] 
**last_update_user** | **str** | The name of the user that last updated this code assignment. | [optional] 
**resource_code_description** | **str** | The description of the associated resource code. | [optional] 
**resource_code_object_id** | **int** | The unique ID of the associated resource code. | [optional] 
**resource_code_type_name** | **str** | The name of the parent resource code type. | [optional] 
**resource_code_type_object_id** | **int** | The unique ID of the parent resource code type. | [optional] 
**resource_code_value** | **str** | The value of the associated resource code. | [optional] 
**resource_id** | **str** | The short code that uniquely identifies the associated resource. | [optional] 
**resource_name** | **str** | The name of the resource to which the resource code is assigned. | [optional] 
**resource_object_id** | **int** | The unique ID of the resource to which the resource code is assigned. | [optional] 

## Example

```python
from openapi_client.models.resource_code_assignment import ResourceCodeAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceCodeAssignment from a JSON string
resource_code_assignment_instance = ResourceCodeAssignment.from_json(json)
# print the JSON string representation of the object
print(ResourceCodeAssignment.to_json())

# convert the object into a dict
resource_code_assignment_dict = resource_code_assignment_instance.to_dict()
# create an instance of ResourceCodeAssignment from a dict
resource_code_assignment_from_dict = ResourceCodeAssignment.from_dict(resource_code_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


