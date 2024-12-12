# JobServiceResponse

CreateJobServiceResponse Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | The unique ID of the associated job. | [optional] 
**job_status** | **str** | Status of the job. | [optional] 

## Example

```python
from openapi_client.models.job_service_response import JobServiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JobServiceResponse from a JSON string
job_service_response_instance = JobServiceResponse.from_json(json)
# print the JSON string representation of the object
print(JobServiceResponse.to_json())

# convert the object into a dict
job_service_response_dict = job_service_response_instance.to_dict()
# create an instance of JobServiceResponse from a dict
job_service_response_from_dict = JobServiceResponse.from_dict(job_service_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


