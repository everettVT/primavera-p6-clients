# SummarizeCBS

SummarizeCBS Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_object_id** | **int** | The unique identifier of the project that you want to send to Primavera Unifier. | [optional] 
**timeout** | **int** | The amount of time in seconds that the server side will wait for the job service to complete before it returns with the current job status. The Timeout parameter is optional. When this operation is used without specifying a Timeout parameter or with a Timeout of 0, the server immediately returns without waiting for the job service to complete. | [optional] 

## Example

```python
from openapi_client.models.summarize_cbs import SummarizeCBS

# TODO update the JSON string below
json = "{}"
# create an instance of SummarizeCBS from a JSON string
summarize_cbs_instance = SummarizeCBS.from_json(json)
# print the JSON string representation of the object
print(SummarizeCBS.to_json())

# convert the object into a dict
summarize_cbs_dict = summarize_cbs_instance.to_dict()
# create an instance of SummarizeCBS from a dict
summarize_cbs_from_dict = SummarizeCBS.from_dict(summarize_cbs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


