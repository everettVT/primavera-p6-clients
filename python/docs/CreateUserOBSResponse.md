# CreateUserOBSResponse

CreateUserOBSResponse Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_object_id** | **int** | The unique ID of the associated user. | [optional] 
**obs_object_id** | **int** | The unique ID of the associated OBS. | [optional] 

## Example

```python
from openapi_client.models.create_user_obs_response import CreateUserOBSResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserOBSResponse from a JSON string
create_user_obs_response_instance = CreateUserOBSResponse.from_json(json)
# print the JSON string representation of the object
print(CreateUserOBSResponse.to_json())

# convert the object into a dict
create_user_obs_response_dict = create_user_obs_response_instance.to_dict()
# create an instance of CreateUserOBSResponse from a dict
create_user_obs_response_from_dict = CreateUserOBSResponse.from_dict(create_user_obs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


