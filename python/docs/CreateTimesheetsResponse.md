# CreateTimesheetsResponse

CreateTimesheetsResponse Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_object_id** | **int** | The unique ID of the associated resource. | [optional] 
**timesheet_period_object_id** | **int** | The unique ID of the timesheet period. | [optional] 

## Example

```python
from openapi_client.models.create_timesheets_response import CreateTimesheetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTimesheetsResponse from a JSON string
create_timesheets_response_instance = CreateTimesheetsResponse.from_json(json)
# print the JSON string representation of the object
print(CreateTimesheetsResponse.to_json())

# convert the object into a dict
create_timesheets_response_dict = create_timesheets_response_instance.to_dict()
# create an instance of CreateTimesheetsResponse from a dict
create_timesheets_response_from_dict = CreateTimesheetsResponse.from_dict(create_timesheets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


