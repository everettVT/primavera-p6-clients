# UserLicense

UserLicense Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_date** | **datetime** | The date this user license was created. | [optional] 
**create_user** | **str** | The name of the user that created this user license. | [optional] 
**last_update_date** | **datetime** | The date this user license was last updated. | [optional] 
**last_update_user** | **str** | The name of the user that last updated this user license. | [optional] 
**license_type** | **str** | The property that permits you to configure access to different functional areas of the application suite. | [optional] 
**object_id** | **int** | The unique ID generated by the system. | [optional] 
**user_name** | **str** | The user&#39;s login name. | [optional] 
**user_object_id** | **int** | The unique ID of the associated user. | [optional] 

## Example

```python
from openapi_client.models.user_license import UserLicense

# TODO update the JSON string below
json = "{}"
# create an instance of UserLicense from a JSON string
user_license_instance = UserLicense.from_json(json)
# print the JSON string representation of the object
print(UserLicense.to_json())

# convert the object into a dict
user_license_dict = user_license_instance.to_dict()
# create an instance of UserLicense from a dict
user_license_from_dict = UserLicense.from_dict(user_license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

