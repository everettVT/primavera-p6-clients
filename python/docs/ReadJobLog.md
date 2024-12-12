# ReadJobLog

ReadJobLog Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | The unique identifier for the job. | [optional] 

## Example

```python
from openapi_client.models.read_job_log import ReadJobLog

# TODO update the JSON string below
json = "{}"
# create an instance of ReadJobLog from a JSON string
read_job_log_instance = ReadJobLog.from_json(json)
# print the JSON string representation of the object
print(ReadJobLog.to_json())

# convert the object into a dict
read_job_log_dict = read_job_log_instance.to_dict()
# create an instance of ReadJobLog from a dict
read_job_log_from_dict = ReadJobLog.from_dict(read_job_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


