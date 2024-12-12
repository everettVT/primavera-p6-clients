# ResourceRole

ResourceRole Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_date** | **datetime** | The date this resource role was created. | [optional] 
**create_user** | **str** | The name of the user that created this resource role. | [optional] 
**last_update_date** | **datetime** | The date this resource role was last updated. | [optional] 
**last_update_user** | **str** | The name of the user that last updated this resource role. | [optional] 
**proficiency** | **str** | The resource&#39;s proficiency at performing this role. The values are &#39;1 - Master&#39;, &#39;2 - Expert&#39;, &#39;3 - Skilled&#39;, &#39;4 - Proficient&#39;, and &#39;5 - Inexperienced&#39;. If the current user does not have the ViewResourceRoleProficiency global security privilege, this field may not be accessed. | [optional] 
**resource_id** | **str** | The short code that uniquely identifies the resource. | [optional] 
**resource_name** | **str** | The name of the resource. | [optional] 
**resource_object_id** | **int** | The unique ID of the associated resource. | [optional] 
**role_id** | **str** | The short code that uniquely identifies the role. | [optional] 
**role_name** | **str** | The name of the role. The role name uniquely identifies the role. | [optional] 
**role_object_id** | **int** | The unique ID of the associated role. | [optional] 

## Example

```python
from openapi_client.models.resource_role import ResourceRole

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRole from a JSON string
resource_role_instance = ResourceRole.from_json(json)
# print the JSON string representation of the object
print(ResourceRole.to_json())

# convert the object into a dict
resource_role_dict = resource_role_instance.to_dict()
# create an instance of ResourceRole from a dict
resource_role_from_dict = ResourceRole.from_dict(resource_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


