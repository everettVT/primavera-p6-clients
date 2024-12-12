# ScheduleOptions

ScheduleOptions Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculate_float_based_on_finish_date** | **bool** | The flag that indicates how each activity&#39;s float will be calculated with respect to other projects in the scheduling batch. This setting only has an effect when scheduling multiple projects at the same time. If true, each activity&#39;s float is calculated based on its project&#39;s ScheduledFinishDate. If false, then each activity&#39;s float is calculated based on the latest ScheduledFinishDate of all of the projects in the scheduling batch. | [optional] 
**compute_total_float_type** | **str** | The method for calculating total float for all activities. Start Float is the difference between the early and late start dates (Start Float &#x3D; Late Start - Early Start); Finish Float is the difference between the early and late finish dates (Finish Float &#x3D; Late Finish - Early Finish); and Smallest of Start Float and Finish Float is the most critical float value. | [optional] 
**create_date** | **datetime** | The date this schedule option was created. | [optional] 
**create_user** | **str** | The name of the user that created this schedule option. | [optional] 
**critical_activity_float_threshold** | **float** | The maximum float time for activities before they are marked critical. | [optional] 
**critical_activity_path_type** | **str** | The critical path type, which indicates how critical path activities are identified for the project, based on either &#39;Critical Float&#39; or &#39;Longest Path&#39;. | [optional] 
**external_project_priority_limit** | **int** |  | [optional] 
**ignore_other_project_relationships** | **bool** | The option used by the scheduler for treating activity relationships between projects when scheduling. | [optional] 
**include_external_res_ass** | **bool** |  | [optional] 
**last_update_date** | **datetime** | The date this schedule option was last updated. | [optional] 
**last_update_user** | **str** | The name of the user that last updated this schedule option. | [optional] 
**level_all_resources** | **bool** |  | [optional] 
**level_within_float** | **bool** |  | [optional] 
**make_open_ended_activities_critical** | **bool** | The option used by the scheduler for automatically leveling resources when scheduling projects. | [optional] 
**maximum_multiple_float_paths** | **int** | The number of critical float paths to calculate. For example, if you set the field to five, the module calculates the five most critical float paths ending with the activity you selected. The module ranks each float path from most critical to least critical, and stores the value for each activity in the Float Path field. For example, if you calculate five float paths, the module will store a value of one in the Float Path field for each activity in the most critical float path; the module will store a value of five for each activity in the least critical float path. Note: To view the critical float paths after you schedule the project, group activities in the Activity Table by Float Path and sort by Float Path Order. A Float Path value of one indicates that those activities are part of the most critical float path. The Float Path Order value indicates the order in which the activities were processed. | [optional] 
**min_float_to_preserve** | **int** |  | [optional] 
**multiple_float_paths_enabled** | **bool** | The Boolean value that indicates whether multiple critical float paths (sequences of activities) should be calculated in the project schedule. | [optional] 
**multiple_float_paths_ending_activity_object_id** | **int** | The activity in the WBS that you want to represent the end of the float paths. Typically, this will be a milestone activity or some other significant activity that has a start date or end date that cannot change. Note: if a value is not assigned, the module will choose an activity based on MultipleFloatPathsUseTotalFloat. If you are calculating multiple paths using Free Float, the module will choose the open-ended activity with the most critical Free Float. If you are calculating multiple paths using Total Float, the module will calculate the Total Float for all activity relationships, then choose the activity with the most critical Relationship Total Float. | [optional] 
**multiple_float_paths_ending_activity_short_name** | **str** |  | [optional] 
**multiple_float_paths_use_total_float** | **bool** | The Boolean value that decides whether or not to use total float in multiple float path calculations.If True, then based on the activity you want the paths to end on, the module determines which predecessor activity has the most critical Relationship Total Float on the backward pass. The module repeats this process until an activity is reached that has no relationship. The module begins the forward pass from this activity and determines which successor activity has the most critical Relationship Successor Total Float. The module repeats this process until an activity is reached that has no relationship. These activities represent the most critical float path. The process begins again until the remaining sub-critical paths are calculated.If False, then critical float paths are defined based on longest path. The most critical path will be identical to the critical path that is derived when you choose to define critical activities as Longest Path in the General tab. In a multicalendar project, the longest path is calculated by identifying the activities that have an early finish equal to the latest calculated early finish for the project and tracing all driving relationships for those activities back to the project start date. After the most critical path is identified, the module will calculate the remaining sub-critical paths. | [optional] 
**out_of_sequence_schedule_type** | **str** | The type of logic used to schedule the progressed activities: &#39;Retained Logic&#39;, &#39;Progress Override&#39;, or &#39;Actual Dates&#39;. | [optional] 
**over_allocation_percentage** | **float** |  | [optional] 
**preserve_scheduled_early_and_late_dates** | **bool** |  | [optional] 
**priority_list** | **str** |  | [optional] 
**project_id** | **str** | The short code that uniquely identifies the project. | [optional] 
**project_object_id** | **int** | The unique ID of the associated project. | [optional] 
**relationship_lag_calendar** | **str** | The calendar used to calculate the lag between predecessors and successors for all activities. Valid values are &#39;Predecessor Activity Calendar&#39;, &#39;Successor Activity Calendar&#39;, &#39;24 Hour Calendar&#39;, and &#39;Project Default Calendar&#39;. If you do not select a calendar, the successor activity calendar is used. | [optional] 
**resource_list** | **str** |  | [optional] 
**start_to_start_lag_calculation_type** | **bool** | he method used to calculate lag when a start-to-start relationship exists and the predecessor starts out of sequence. Actual Start sets the successor&#39;s start according to the time elapsed from the predecessor&#39;s actual start (the successor&#39;s start date is the data date plus any remaining lag). Early Start sets the successor&#39;s start according to the amount of work that the predecessor activity accomplishes (the expired lag is calculated as the number of work periods between the actual start and the data date, and the successor&#39;s start date is the predecessor&#39;s internal early start plus any remaining lag). | [optional] 
**use_expected_finish_dates** | **bool** | The option used for setting activity finish dates as the expected finish dates when scheduling projects. | [optional] 
**user_name** | **str** | The user&#39;s login name. | [optional] 
**user_object_id** | **int** | The unique ID of the associated user. | [optional] 

## Example

```python
from openapi_client.models.schedule_options import ScheduleOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleOptions from a JSON string
schedule_options_instance = ScheduleOptions.from_json(json)
# print the JSON string representation of the object
print(ScheduleOptions.to_json())

# convert the object into a dict
schedule_options_dict = schedule_options_instance.to_dict()
# create an instance of ScheduleOptions from a dict
schedule_options_from_dict = ScheduleOptions.from_dict(schedule_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


