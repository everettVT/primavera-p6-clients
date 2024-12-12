# CurrentJobResponse

CurrentJobResponse Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 
**job_type** | **str** |  | [optional] 
**job_status** | **str** |  | [optional] 
**submitted_date** | **str** |  | [optional] 
**last_run_date** | **str** |  | [optional] 
**project_object_id** | **List[str]** |  | [optional] 
**eps_object_id** | **List[str]** |  | [optional] 
**worker_host** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.current_job_response import CurrentJobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentJobResponse from a JSON string
current_job_response_instance = CurrentJobResponse.from_json(json)
# print the JSON string representation of the object
print(CurrentJobResponse.to_json())

# convert the object into a dict
current_job_response_dict = current_job_response_instance.to_dict()
# create an instance of CurrentJobResponse from a dict
current_job_response_from_dict = CurrentJobResponse.from_dict(current_job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


