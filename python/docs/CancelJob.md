# CancelJob

CancelJob Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.cancel_job import CancelJob

# TODO update the JSON string below
json = "{}"
# create an instance of CancelJob from a JSON string
cancel_job_instance = CancelJob.from_json(json)
# print the JSON string representation of the object
print(CancelJob.to_json())

# convert the object into a dict
cancel_job_dict = cancel_job_instance.to_dict()
# create an instance of CancelJob from a dict
cancel_job_from_dict = CancelJob.from_dict(cancel_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


