# ResourceAssignment

ResourceAssignment Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_actual_finish** | **datetime** | The date on which the activity was completed. | [optional] 
**activity_id** | **str** | The short ID that uniquely identifies the activity within the project. | [optional] 
**activity_name** | **str** | The name of the activity. The activity name does not have to be unique. | [optional] 
**activity_object_id** | **int** | The unique ID of the activity to which the resource is assigned. | 
**activity_type** | **str** | Determines how duration and schedule dates are calculated for an activity. | [optional] 
**actual_cost** | **float** | The actual non-overtime plus overtime cost for the resource assignment on the activity. Computed as actual cost &#x3D; actual regular cost + actual overtime cost. | [optional] 
**actual_curve** | **str** |  | [optional] 
**actual_duration** | **float** | The actual duration for the resource assignment on the activity. | [optional] 
**actual_finish_date** | **datetime** | The date the resource actually finished working on the activity. | [optional] 
**actual_overtime_cost** | **float** | The actual overtime cost for the resource assignment on the activity. Computed as actual overtime cost &#x3D; actual overtime units * cost per time * overtime factor. | [optional] 
**actual_overtime_units** | **float** | The actual overtime units worked by the resource on this activity. This value is computed from timesheets when project actuals are applied or may be entered directly by the project manager. | [optional] 
**actual_regular_cost** | **float** | The actual non-overtime cost for the resource assignment on the activity. Computed as actual regular cost &#x3D; actual regular units * cost per time. | [optional] 
**actual_regular_units** | **float** | The actual non-overtime units worked by the resource on this activity. This value is computed from timesheets when project actuals are applied or may be entered directly by the project manager. | [optional] 
**actual_start_date** | **datetime** | The date the resource actually started working on the activity. | [optional] 
**actual_this_period_cost** | **float** | The actual this period cost (will be labor or nonlabor). | [optional] 
**actual_this_period_units** | **float** | The actual this period units (hours) (will be labor or nonlabor). | [optional] 
**actual_units** | **float** | The actual non-overtime plus overtime units worked by the resource on this activity. This value is computed from timesheets when project actuals are applied or may be entered directly by the project manager. Computed as actual units &#x3D; actual regular units + actual overtime units. | [optional] 
**at_completion_cost** | **float** | The sum of the actual plus remaining costs for the resource assignment on the activity. | [optional] 
**at_completion_duration** | **float** | The total working time from the activity&#39;s current start date to the current finish date. The current start date is the planned start date until the activity is started, then it is the actual start date. The current finish date is the activity planned finish date while the activity is not started, the remaining finish date while the activity is in progress, and the actual finish date once the activity is completed. The total working time is computed using the activity&#39;s calendar. | [optional] 
**at_completion_units** | **float** | The sum of the actual plus remaining units for the resource assignment on the activity. | [optional] 
**auto_compute_actuals** | **bool** | The option that determines whether the activity&#39;s actual and remaining units, start date, finish date, and percent complete are computed automatically using the planned dates, planned units and the schedule percent complete. If this option is selected, the actual/remaining units and actual dates are automatically updated when project actuals are applied. Use this option to assume that all work for the activity proceeds according to plan. | [optional] 
**budget_at_completion_costs** | **float** |  | [optional] 
**budget_at_completion_units** | **float** |  | [optional] 
**calendar_name** | **str** | The name of the calendar. | [optional] 
**calendar_object_id** | **int** | The unique ID generated by the system for the calendar associated with the resource assignment. | [optional] 
**cost_account_id** | **str** | The id of associated cost account. | [optional] 
**cost_account_name** | **str** | The name of the associated cost account. | [optional] 
**cost_account_object_id** | **int** | The unique ID of the cost account associated with this resource assignment. | [optional] 
**create_date** | **datetime** | The date this assignment was created. | [optional] 
**create_user** | **str** | The name of the user that created this assignment. | [optional] 
**driving_activity_dates_flag** | **bool** | The flag indicating whether new resource/role assignments drive activity dates, by default. | [optional] 
**duration_percent_complete** | **float** |  | [optional] 
**estimate_to_completion_costs** | **float** |  | [optional] 
**estimate_to_completion_units** | **float** |  | [optional] 
**financial_period_tmpl_id** | **int** |  | [optional] 
**finish_date** | **datetime** | The finish date of the resource assignment on the activity. Set to the remaining finish date until the activity is completed, then set to the actual finish date. | [optional] 
**guid** | **str** | The globally unique ID generated by the system. | [optional] 
**has_future_bucket_data** | **bool** | The flag that indicates whether the assignment has future bucket data. | [optional] 
**is_active** | **bool** | The flag that indicates whether this resource assignment is active. | [optional] 
**is_activity_flagged** | **bool** | The flag that indicates whether the resource who is assigned to the activity assignment has flagged the activity as important to the resource. | [optional] 
**is_baseline** | **bool** | The boolean value indicating if this business object is related to a Project or Baseline. | [optional] 
**is_cost_units_linked** | **bool** | The flag that determines whether or not cost should be calculated based on units. | [optional] 
**is_overtime_allowed** | **bool** | The flag that indicates whether the resource is allowed to log overtime hours. | [optional] 
**is_primary_resource** | **bool** | The flag that indicates whether this resource is the activity&#39;s primary resource. | [optional] 
**is_template** | **bool** | The boolean value indicating if this business object is related to a template Project. | [optional] 
**last_update_date** | **datetime** | The date this assignment was last updated. | [optional] 
**last_update_user** | **str** | The name of the user that last updated this assignment. | [optional] 
**object_id** | **int** | The unique ID generated by the system. | [optional] 
**overtime_factor** | **float** | The overtime factor used to compute the overtime price for the resource assignment on this activity. Overtime price &#x3D; standard price * overtime factor. When the resource is assigned to the activity, the resource&#39;s overtime factor is copied to the assignment. The assignment overtime factor is refreshed from the resource value when resource prices are synchronized for the project. | [optional] 
**pending_actual_overtime_units** | **float** | The actual overtime units worked by the resource on this activity. This value is computed from values entered by a user in the Progress Reporter application and is applied to the resource assignment when the Apply Actuals service is invoked. | [optional] 
**pending_actual_regular_units** | **float** | The actual nonovertime units worked by the resource on this activity. This value is computed from values entered by a user in the Progress Reporter application and is applied to the resource assignment when the Apply Actuals service is invoked. | [optional] 
**pending_percent_complete** | **float** | The estimate of the percentage of the resource&#39;s units of work completed on this activity. The pending percent complete is entered by each resource using Timesheets. This value is used to compute the resource&#39;s remaining units for the activity when project actuals are applied. The project manager specifies whether resources update their percent complete or remaining units for each project. | [optional] 
**pending_remaining_units** | **float** | The estimate of the resource&#39;s remaining units on this activity. The pending remaining units is entered by each resource using Timesheets. This value is copied to the resource&#39;s remaining units for the activity when project actuals are applied. The project manager specifies whether resources update their percent complete or remaining units for each project. | [optional] 
**percent_complete** | **float** |  | [optional] 
**percent_complete_type** | **str** |  | [optional] 
**planned_cost** | **float** | The planned cost for the resource assignment on the activity. Computed as planned cost &#x3D; planned units * price per time. This field is named BudgetedCost in Primavera&#39;s Engineering &amp; Construction and Maintenance &amp; Turnaround solutions. | [optional] 
**planned_curve** | **str** |  | [optional] 
**planned_duration** | **float** | The planned working time for the resource assignment on the activity, from the resource&#39;s planned start date to the planned finish date. This field is named BudgetedDuration in Primavera&#39;s Engineering &amp; Construction and Maintenance &amp; Turnaround solutions. | [optional] 
**planned_finish_date** | **datetime** | The date the resource is scheduled to finish working on the activity. This date is computed by the project scheduler but can be updated manually by the project manager. This date is not changed by the project scheduler after the activity has been started. This is the finish date that Timesheets users follow and schedule variance is measured against. | [optional] 
**planned_lag** | **float** | The planned time lag between the activity&#39;s planned start date and the resource&#39;s planned start date on the activity. If the resource is planned to start work when the activity is planned to start, the planned lag is zero. This field is named BudgetedLag in Primavera&#39;s Engineering &amp; Construction and Maintenance &amp; Turnaround solutions. | [optional] 
**planned_start_date** | **datetime** | The date the resource is scheduled to begin working on the activity. This date is computed by the project scheduler but can be updated manually by the project manager. This date is not changed by the project scheduler after the activity has been started. This is the start date that Timesheets users follow and schedule variance is measured against. | [optional] 
**planned_units** | **float** | The planned units of work for the resource assignment on the activity. This field is named BudgetedUnits in Primavera&#39;s Engineering &amp; Construction and Maintenance &amp; Turnaround solutions. | [optional] 
**planned_units_per_time** | **float** | The planned units per time at which the resource is to perform work on this activity. For example, a person assigned full time would perform 8 hours of work per day. A department of five people may perform at 5 days per day. This field is named BudgetedUnitsPerTime in Primavera&#39;s Engineering &amp; Construction and Maintenance &amp; Turnaround solutions. | [optional] 
**price_per_unit** | **float** | The price per time for the resource on this activity. This price is used to compute the resource&#39;s cost for the activity. When the resource is assigned to the activity, the resource&#39;s price is copied to the assignment based on the effective date of the price and the activity start date. The assignment price is refreshed whenever resource prices are synchronized for the project. | [optional] 
**prior_actual_overtime_units** | **float** | The difference between the pending quantity value and the actual quantity value for overtime before applying the new actual value. | [optional] 
**prior_actual_regular_units** | **float** | The difference between the pending quantity value and the actual quantity value before applying the new actual value. | [optional] 
**proficiency** | **str** | The skill level that is associated with the role. The values are &#39;Master&#39;, &#39;Expert&#39;, &#39;Skilled&#39;, &#39;Proficient&#39;, and &#39;Inexperienced&#39;. If the current user does not have the ViewResourceRoleProficiency global security privilege, this field may not be accessed. | [optional] 
**project_flag** | **str** | Indicates if this WBS node is a Project/EPS node. | [optional] 
**project_id** | **str** | The short code that uniquely identifies the project. | [optional] 
**project_name** | **str** | The name of the associated project. | [optional] 
**project_object_id** | **int** | The unique ID of the associated project. | [optional] 
**project_project_flag** | **str** | Indicates if this Project/EPS nose is a Project or EPS. | [optional] 
**rate_source** | **str** | The value that indicates which price/unit will be used to calculate costs for the assignment, such as &#39;Resource&#39;, &#39;Role&#39;, and &#39;Override&#39;. When a resource and only a resource is assigned to an activity, the rate source will automatically equal &#39;Resource&#39;. When a role and only a role is assigned to an activity, the rate source will automatically equal &#39;Role&#39;. When both a resource and role are assigned to the activity, the rate source can be either &#39;Resource&#39; or &#39;Role&#39; determined by the RateSourcePreference. In any case, the &#39;Override&#39; value allows you to specify any other price/unit. | [optional] 
**rate_type** | **str** | The rate type that determines which of the five prices specified for the resource will be used to calculate the cost for the resource assignment. Valid values are &#39;Price / Unit&#39;, &#39;Price / Unit2&#39;, &#39;Price / Unit3&#39;, &#39;Price / Unit4&#39;, &#39;Price / Unit5&#39;, and &#39;None&#39;. | [optional] 
**remaining_cost** | **float** | The remaining cost for the resource assignment on the activity. Computed as remaining cost &#x3D; remaining units * cost per time. | [optional] 
**remaining_curve** | **str** |  | [optional] 
**remaining_duration** | **float** | The remaining duration of the resource assignment. The remaining duration is the remaining working time for the resource assignment on the activity, from the resource&#39;s remaining start date to the remaining finish date. The remaining working time is computed using the calendar determined by the activity Type. Resource Dependent activities use the resource&#39;s calendar, other activity types use the activity&#39;s calendar. Before the activity is started, the remaining duration is the same as the Original duration. After the activity is completed, the remaining duration is zero. | [optional] 
**remaining_finish_date** | **datetime** | The date the resource is scheduled to finish the remaining work for the activity. This date is computed by the project scheduler but can be updated manually by the project manager. Before the activity is started, the remaining finish date is the same as the planned finish date. | [optional] 
**remaining_lag** | **float** | The time lag between the activity&#39;s remaining start date and the resource&#39;s remaining start date on the activity. If the resource&#39;s remaining work starts on the activity&#39;s remaining start date, the lag is zero. Before the activity is started, the remaining lag is the same as the planned lag. | [optional] 
**remaining_late_finish_date** | **datetime** | The remaining late finish date calculated by the scheduler. | [optional] 
**remaining_late_start_date** | **datetime** | The remaining late start date calculated by the scheduler. | [optional] 
**remaining_start_date** | **datetime** | The date the resource is scheduled to begin the remaining work for the activity. This date is computed by the project scheduler but can be updated manually by the project manager. Before the activity is started, the remaining start date is the same as the planned start date. | [optional] 
**remaining_units** | **float** | The remaining units of work to be performed by this resource on this activity. Before the activity is started, the remaining units are the same as the planned units. After the activity is completed, the remaining units are zero. | [optional] 
**remaining_units_per_time** | **float** | The units per time at which the resource will be performing work on the remaining portion of this activity. For example, a person assigned full time would perform 8 hours of work per day. A department of five people may perform at 5 days per day. | [optional] 
**resource_calendar_name** | **str** | The name of the calendar for the resource. | [optional] 
**resource_curve_name** | **str** | The name of the resource curve that determines how resources and costs are distributed over time for this activity. | [optional] 
**resource_curve_object_id** | **int** | The unique ID of the resource curve. | [optional] 
**resource_id** | **str** | The short code that uniquely identifies the resource. | [optional] 
**resource_name** | **str** | The name of the resource. | [optional] 
**resource_object_id** | **int** | The unique ID of the associated resource. | 
**resource_type** | **str** | The resource type: \&quot;Labor\&quot;, \&quot;Nonlabor\&quot;, or \&quot;Material\&quot;. | [optional] 
**review_required** | **bool** | Determines if all new activities added to the project require approval. | [optional] 
**role_id** | **str** | The short code that uniquely identifies the role. | [optional] 
**role_name** | **str** | The name of the role. The role name uniquely identifies the role. | [optional] 
**role_object_id** | **int** | The unique ID of the role the resource is performing on this activity. A resource may be assigned to the same activity more than once, performing different roles. The project manager controls whether the same resource can be assigned to an activity more than once. | 
**role_short_name** | **str** | The short code that uniquely identifies a role. | [optional] 
**staffed_remaining_cost** | **float** | The time distribution of the resource&#39;s remaining cost for resource assignments that have filled a role. | [optional] 
**staffed_remaining_units** | **float** | The time distribution of the resource&#39;s remaining units for resource assignments that have filled a role. | [optional] 
**start_date** | **datetime** | The start date of the resource assignment on the activity. Set to the remaining start date until the activity is started, then set to the actual start date. | [optional] 
**status_code** | **str** | The project status, either &#39;Planned&#39;, &#39;Active&#39;, &#39;Inactive&#39;, &#39;What-If&#39;, &#39;Requested&#39;, or &#39;Template&#39;. | [optional] 
**units_percent_complete** | **float** | The percent complete of units for the resource assignment on the activity. Computed as actual units / at completion units * 100. Always in the range 0 to 100. | [optional] 
**unread_comment_count** | **int** | The total number of unread comments on this activity for a user. | [optional] 
**unstaffed_remaining_cost** | **float** | The time distribution of the resource&#39;s remaining cost for resource assignments that have not filled a role. | [optional] 
**unstaffed_remaining_units** | **float** | The time distribution of the resource&#39;s remaining units for resource assignments that have not filled a role. | [optional] 
**resource_request** | [**ResourceRequest**](ResourceRequest.md) |  | [optional] 
**wbs_name_path** | **str** |  | [optional] 
**wbs_object_id** | **int** | The unique ID of the WBS for the activity. | [optional] 
**cbs_code** | **str** | CBS Code. | [optional] 
**cbsid** | **int** | The unique Id of CBS. | [optional] 

## Example

```python
from openapi_client.models.resource_assignment import ResourceAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceAssignment from a JSON string
resource_assignment_instance = ResourceAssignment.from_json(json)
# print the JSON string representation of the object
print(ResourceAssignment.to_json())

# convert the object into a dict
resource_assignment_dict = resource_assignment_instance.to_dict()
# create an instance of ResourceAssignment from a dict
resource_assignment_from_dict = ResourceAssignment.from_dict(resource_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

