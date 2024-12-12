# CreateResourceAccessResponse

CreateResourceAccessResponse Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_object_id** | **int** | The unique ID of the associated user. | [optional] 
**resource_object_id** | **int** | The unique ID of the associated Resource. | [optional] 

## Example

```python
from openapi_client.models.create_resource_access_response import CreateResourceAccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateResourceAccessResponse from a JSON string
create_resource_access_response_instance = CreateResourceAccessResponse.from_json(json)
# print the JSON string representation of the object
print(CreateResourceAccessResponse.to_json())

# convert the object into a dict
create_resource_access_response_dict = create_resource_access_response_instance.to_dict()
# create an instance of CreateResourceAccessResponse from a dict
create_resource_access_response_from_dict = CreateResourceAccessResponse.from_dict(create_resource_access_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


