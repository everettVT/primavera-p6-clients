# TimesheetPeriod

TimesheetPeriod Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_date** | **datetime** | The date this timesheet period was created. | [optional] 
**create_user** | **str** | The name of the user that created this timesheet period. | [optional] 
**end_date** | **datetime** | The timesheet period end date. | [optional] 
**last_update_date** | **datetime** | The date this timesheet period was last updated. | [optional] 
**last_update_user** | **str** | The name of the user that last updated this timesheet period. | [optional] 
**object_id** | **int** | The unique ID generated by the system. | [optional] 
**start_date** | **datetime** | The timesheet period start date. | [optional] 

## Example

```python
from openapi_client.models.timesheet_period import TimesheetPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of TimesheetPeriod from a JSON string
timesheet_period_instance = TimesheetPeriod.from_json(json)
# print the JSON string representation of the object
print(TimesheetPeriod.to_json())

# convert the object into a dict
timesheet_period_dict = timesheet_period_instance.to_dict()
# create an instance of TimesheetPeriod from a dict
timesheet_period_from_dict = TimesheetPeriod.from_dict(timesheet_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


