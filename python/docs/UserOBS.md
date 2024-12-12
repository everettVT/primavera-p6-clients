# UserOBS

UserOBS Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_date** | **datetime** | The date this association was created. | [optional] 
**create_user** | **str** | The name of the user that created this association. | [optional] 
**last_update_date** | **datetime** | The date this association was last updated. | [optional] 
**last_update_user** | **str** | The name of the user that last updated this association. | [optional] 
**profile_name** | **str** | The name of security profile. | [optional] 
**project_profile_object_id** | **int** | The unique ID of the project profile with which the user is granted access to the project and OBS. See the ProjectProfile class for a constant defining the fixed profile of Project Superuser. | [optional] 
**user_name** | **str** | The user&#39;s login name. | [optional] 
**user_object_id** | **int** | The unique ID of the user who is assigned to the project OBS. | [optional] 
**obs_name** | **str** | The name of the person/role in the organization, sometimes referred to as the \&quot;responsible manager\&quot;. | [optional] 
**obs_object_id** | **int** | The unique ID of the OBS to which the user is granted access. | [optional] 

## Example

```python
from openapi_client.models.user_obs import UserOBS

# TODO update the JSON string below
json = "{}"
# create an instance of UserOBS from a JSON string
user_obs_instance = UserOBS.from_json(json)
# print the JSON string representation of the object
print(UserOBS.to_json())

# convert the object into a dict
user_obs_dict = user_obs_instance.to_dict()
# create an instance of UserOBS from a dict
user_obs_from_dict = UserOBS.from_dict(user_obs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


