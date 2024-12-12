# SendToUnifier

SendToUnifier Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_object_id** | **List[int]** | The unique identifier of the project that you want to send to Primavera Unifier. | [optional] 
**timeout** | **int** | The amount of time in seconds that the server side will wait for the job service to complete before it returns with the current job status. The Timeout parameter is optional. When this operation is used without specifying a Timeout parameter or with a Timeout of 0, the server immediately returns without waiting for the job service to complete. | [optional] 

## Example

```python
from openapi_client.models.send_to_unifier import SendToUnifier

# TODO update the JSON string below
json = "{}"
# create an instance of SendToUnifier from a JSON string
send_to_unifier_instance = SendToUnifier.from_json(json)
# print the JSON string representation of the object
print(SendToUnifier.to_json())

# convert the object into a dict
send_to_unifier_dict = send_to_unifier_instance.to_dict()
# create an instance of SendToUnifier from a dict
send_to_unifier_from_dict = SendToUnifier.from_dict(send_to_unifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


