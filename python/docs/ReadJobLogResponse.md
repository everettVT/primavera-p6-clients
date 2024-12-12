# ReadJobLogResponse

ReadJobLogResponse Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_log** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.read_job_log_response import ReadJobLogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadJobLogResponse from a JSON string
read_job_log_response_instance = ReadJobLogResponse.from_json(json)
# print the JSON string representation of the object
print(ReadJobLogResponse.to_json())

# convert the object into a dict
read_job_log_response_dict = read_job_log_response_instance.to_dict()
# create an instance of ReadJobLogResponse from a dict
read_job_log_response_from_dict = ReadJobLogResponse.from_dict(read_job_log_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


