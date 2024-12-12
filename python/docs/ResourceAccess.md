# ResourceAccess

ResourceAccess Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_date** | **datetime** | The date this resource security was created. | [optional] 
**create_user** | **str** | The name of the user that created this resource security. | [optional] 
**last_update_date** | **datetime** | The date this resource security was last updated. | [optional] 
**last_update_user** | **str** | The name of the user that last updated this resource security. | [optional] 
**resource_id** | **str** | The short code that uniquely identifies the resource. | [optional] 
**resource_name** | **str** | The name of the resource. | [optional] 
**resource_object_id** | **int** | The unique ID of the associated resource. | [optional] 
**sequence_number** | **int** |  | [optional] 
**user_name** | **str** | The user&#39;s login name. | [optional] 
**user_object_id** | **int** | The unique ID of the associated user. | [optional] 

## Example

```python
from openapi_client.models.resource_access import ResourceAccess

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceAccess from a JSON string
resource_access_instance = ResourceAccess.from_json(json)
# print the JSON string representation of the object
print(ResourceAccess.to_json())

# convert the object into a dict
resource_access_dict = resource_access_instance.to_dict()
# create an instance of ResourceAccess from a dict
resource_access_from_dict = ResourceAccess.from_dict(resource_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


