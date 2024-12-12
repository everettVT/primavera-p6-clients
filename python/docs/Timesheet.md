# Timesheet

Timesheet Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_date** | **datetime** | The date this timesheet was created. | [optional] 
**create_user** | **str** | The name of the user that created this timesheet. | [optional] 
**is_daily** | **bool** | The flag that identifies whether timesheet users enter hours daily or by entire timesheet reporting period. | [optional] 
**last_received_date** | **datetime** | The last date on which the timesheet was submitted by the resource. | [optional] 
**last_update_date** | **datetime** | The date this timesheet was last updated. | [optional] 
**last_update_user** | **str** | The name of the user that last updated this timesheet. | [optional] 
**notes** | **str** | The notes associated with the timesheet. | [optional] 
**resource_id** | **str** | The short code that uniquely identifies the resource. | [optional] 
**resource_name** | **str** | The name of the resource. | [optional] 
**resource_object_id** | **int** | The unique ID of the associated resource. | 
**status** | **str** | The current status of the timesheet: &#39;Submitted&#39;, &#39;Approved&#39;, &#39;Resource Manager Approved&#39;, &#39;Project Manager Approved&#39;, &#39;Active&#39;, or &#39;Rejected&#39;. | [optional] 
**status_date** | **datetime** | The date on which the status of the timesheet was last changed. | [optional] 
**timesheet_period_object_id** | **int** | The unique ID of the timesheet period. | 

## Example

```python
from openapi_client.models.timesheet import Timesheet

# TODO update the JSON string below
json = "{}"
# create an instance of Timesheet from a JSON string
timesheet_instance = Timesheet.from_json(json)
# print the JSON string representation of the object
print(Timesheet.to_json())

# convert the object into a dict
timesheet_dict = timesheet_instance.to_dict()
# create an instance of Timesheet from a dict
timesheet_from_dict = Timesheet.from_dict(timesheet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


