# CBSDurationSummary

CBSDurationSummary Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cbs_object_id** | **int** | The internal CBS ID of the project. This ID cannot be used to load the CBS object directly. | 
**original_project_object_id** | **int** | The unique ID of the project from which the project baseline was created, if the current project is a project baseline | [optional] 
**project_id** | **str** | The short code of the associated project. | 
**project_name** | **str** | The name of the associated project. | [optional] 
**project_object_id** | **int** | The unique ID of the associated project. | [optional] 
**summary_actual_duration** | **float** | The actual duration. | [optional] 
**summary_actual_finish_date** | **datetime** | The latest actual finish date of all activities in the CBS. | [optional] 
**summary_actual_start_date** | **datetime** | The earliest actual start date of all activities in the CBS. | [optional] 
**summary_percent_complete** | **float** | The measure that indicates how much of the CBS baseline duration has been completed so far. Computed based on where the current data date falls between the activity&#39;s baseline start and finish dates. If the data date is earlier than the baseline start, the schedule % complete is 0. If the data date is later than the baseline finish, the schedule % complete is 100. The schedule % complete indicates how much of the CBS duration should be currently completed, relative to the selected baseline. | [optional] 
**summary_planned_duration** | **float** | The total working days between planned start and finish dates in the CBS. | [optional] 
**summary_planned_finish_date** | **datetime** | The latest planned finish date of all activities in the CBS. | [optional] 
**summary_planned_start_date** | **datetime** | The earliest planned start date of all activities in the CBS. | [optional] 
**summary_remaining_duration** | **float** | The total working time from the CBS remaining start date to the remaining finish date. | [optional] 
**summary_remaining_finish_date** | **datetime** | The date the resource is scheduled to finish the remaining work for the activity. | [optional] 
**summary_remaining_start_date** | **datetime** | The earliest remaining start of all activities assigned to the CBS. | [optional] 

## Example

```python
from openapi_client.models.cbs_duration_summary import CBSDurationSummary

# TODO update the JSON string below
json = "{}"
# create an instance of CBSDurationSummary from a JSON string
cbs_duration_summary_instance = CBSDurationSummary.from_json(json)
# print the JSON string representation of the object
print(CBSDurationSummary.to_json())

# convert the object into a dict
cbs_duration_summary_dict = cbs_duration_summary_instance.to_dict()
# create an instance of CBSDurationSummary from a dict
cbs_duration_summary_from_dict = CBSDurationSummary.from_dict(cbs_duration_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


