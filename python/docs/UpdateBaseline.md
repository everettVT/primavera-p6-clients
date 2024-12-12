# UpdateBaseline

UpdateBaseline Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_id** | **int** | The unique identifier for the job. | [optional] 
**baseline_proj_id** | **int** | The unique identifier for the baseline project. | [optional] 
**timeout** | **int** | The amount of time in seconds that the server side will wait for the job service to complete before it returns with the current job status. The Timeout parameter is optional. When this operation is used without specifying a Timeout parameter or with a Timeout of 0, the server immediately returns without waiting for the job service to complete. | [optional] 

## Example

```python
from openapi_client.models.update_baseline import UpdateBaseline

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBaseline from a JSON string
update_baseline_instance = UpdateBaseline.from_json(json)
# print the JSON string representation of the object
print(UpdateBaseline.to_json())

# convert the object into a dict
update_baseline_dict = update_baseline_instance.to_dict()
# create an instance of UpdateBaseline from a dict
update_baseline_from_dict = UpdateBaseline.from_dict(update_baseline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


