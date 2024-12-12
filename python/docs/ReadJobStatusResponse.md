# ReadJobStatusResponse

ReadJobStatusResponse Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_status** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.read_job_status_response import ReadJobStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadJobStatusResponse from a JSON string
read_job_status_response_instance = ReadJobStatusResponse.from_json(json)
# print the JSON string representation of the object
print(ReadJobStatusResponse.to_json())

# convert the object into a dict
read_job_status_response_dict = read_job_status_response_instance.to_dict()
# create an instance of ReadJobStatusResponse from a dict
read_job_status_response_from_dict = ReadJobStatusResponse.from_dict(read_job_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


