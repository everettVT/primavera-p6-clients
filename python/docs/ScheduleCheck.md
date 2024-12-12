# ScheduleCheck

ScheduleCheck Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_object_id** | **List[int]** | The unique identifier of the project in P6. | [optional] 
**timeout** | **int** | The amount of time in seconds that the server side will wait for the job service to complete before it returns with the current job status. The Timeout parameter is optional. When this operation is used without specifying a Timeout parameter or with a Timeout of 0, the server immediately returns without waiting for the job service to complete. | [optional] 

## Example

```python
from openapi_client.models.schedule_check import ScheduleCheck

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleCheck from a JSON string
schedule_check_instance = ScheduleCheck.from_json(json)
# print the JSON string representation of the object
print(ScheduleCheck.to_json())

# convert the object into a dict
schedule_check_dict = schedule_check_instance.to_dict()
# create an instance of ScheduleCheck from a dict
schedule_check_from_dict = ScheduleCheck.from_dict(schedule_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


