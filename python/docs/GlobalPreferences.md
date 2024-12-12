# GlobalPreferences

GlobalPreferences Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_approved_ts_rejection** | **bool** |  | [optional] 
**always_launch_online_help** | **bool** | The flag indicating that Online Help should be launched whenever a user accesses help. | [optional] 
**base_currency_object_id** | **int** | The unique ID of the currency. | [optional] 
**contract_management_url** | **str** | This is the URL of the Contract Management application. | [optional] 
**create_date** | **datetime** | The date this global preferences was created. | [optional] 
**create_user** | **str** | The name of the user that created this global preferences. | [optional] 
**custom_label1** | **str** | The custom (user-defined) text that will be inserted into any report containing the Custom Label 1 global variable text cell, when printed. | [optional] 
**custom_label2** | **str** | The custom (user-defined) text that will be inserted into any report containing the Custom Label 2 global variable text cell, when printed. | [optional] 
**custom_label3** | **str** | The custom (user-defined) text that will be inserted into any report containing the Custom Label 3 global variable text cell, when printed. | [optional] 
**day_abbreviation** | **str** | The abbreviation character for time periods of days. This abbreviation is used for displaying time units and durations in the user&#39;s selected display formats. | [optional] 
**default_duration** | **float** | The planned duration assigned to new activities by default. | [optional] 
**default_timesheet_approval_manager** | **int** | The unique ID of the resource manager assigned to approve timesheets for new resources by default. | [optional] 
**eppm_consent_message** | **str** |  | [optional] 
**eppm_enable_consent** | **str** |  | [optional] 
**ev_estimate_to_complete_factor** | **float** | The user-defined performance factor, PF, for computing earned-value estimate-to-complete. ETC is computed as PF * ( BAC - earned value). This value is assigned to new projects by default. It can be modified for each project WBS element. | [optional] 
**ev_estimate_to_complete_technique** | **str** | The technique for computing earned-value estimate-to-complete. This setting is assigned to new projects by default. It can be modified for each project WBS element. | [optional] 
**ev_performance_pct_complete_custom_pct** | **float** | The user-defined percent complete for computing earned value for activities within the WBS. A value of, say, 25 means that 25% of the planned amount is earned when the activity is started and the remainder is earned when the activity is completed. This value is assigned to new projects by default. It can be modified for each project WBS element. | [optional] 
**ev_performance_pct_complete_technique** | **str** | The technique used for computing earned-value percent complete. This setting is assigned to new projects by default. It can be modified for each project WBS element. | [optional] 
**earned_value_calculation** | **str** | The flag indicating which values to use when calculating earned value when using a primary baseline. Valid values are &#39;At Completion Values with Current Dates&#39;, &#39;Planned Values with Planned Dates&#39;, and &#39;Planned Values with Current Dates&#39;. | [optional] 
**email_notify_ts_rejection** | **bool** |  | [optional] 
**enable_password_policy** | **bool** | The flag that indicates whether the password policy is enforced. | [optional] 
**enable_ts_audit** | **bool** | The flag indicating whether to track timesheet submission, approval, and rejection. When you set this option, the application saves each user who reviews a timesheet, and when the timesheet was reviewed. This information can be viewed by loading TimesheetAudit business objects. | [optional] 
**enable_web_services_ip_check** | **bool** |  | [optional] 
**enable_whats_new_dialog** | **bool** |  | [optional] 
**exception_site_list** | **str** |  | [optional] 
**footer_label1** | **str** | The first footer for reports. The Project Management application allows up to three different footer text strings that can be optionally placed at the bottom of all reports using the report writer. | [optional] 
**footer_label2** | **str** | The second footer for reports. The Project Management application allows up to three different footer text strings that can be optionally placed at the bottom of all reports using the report writer. | [optional] 
**footer_label3** | **str** | The third footer for reports. The Project Management application allows up to three different footer text strings that can be optionally placed at the bottom of all reports using the report writer. | [optional] 
**gateway_api_url** | **str** | The Primavera Gateway URL that will allow you to integrate other products with P6 and P6 Professional. | [optional] 
**gateway_export_erp_sync_name** | **str** | The synchronization for exporting to ERP. | [optional] 
**gateway_export_unifier_sync_name** | **str** | The synchronization for exporting to Primavera Unifier. | [optional] 
**gateway_import_erp_sync_name** | **str** | The synchronization for importing to ERP. | [optional] 
**gateway_import_unifier_sync_name** | **str** | The synchronization for importing to Primavera Unifier. | [optional] 
**gateway_p6_deployment_name** | **str** | The name for the P6 deployment to be integrated with Primavera Gateway. | [optional] 
**gateway_password** | **str** | The password for integration. | [optional] 
**gateway_unifier_enabled** | **bool** | This is the flag to enable Unifier through Gateway. | [optional] 
**gateway_username** | **str** | The username for integration. | [optional] 
**header_label1** | **str** | The first header for reports. The Project Management application allows up to three different header text strings that can be optionally placed at the top of all reports using the report writer. | [optional] 
**header_label2** | **str** | The second header for reports. The Project Management application allows up to three different header text strings that can be optionally placed at the top of all reports using the report writer. | [optional] 
**header_label3** | **str** | The third header for reports. The Project Management application allows up to three different header text strings that can be optionally placed at the top of all reports using the report writer. | [optional] 
**hour_abbreviation** | **str** | The abbreviation character for time periods of hours. This abbreviation is used for displaying time units and durations in the user&#39;s selected display formats. | [optional] 
**hours_per_day** | **float** | The number of work hours per day. This conversion factor is used for displaying time units and durations in the user&#39;s selected display formats. | [optional] 
**hours_per_month** | **float** | The number of work hours per month. This conversion factor is used for displaying time units and durations in the user&#39;s selected display formats. | [optional] 
**hours_per_week** | **float** | The number of work hours per week. This conversion factor is used for displaying time units and durations in the user&#39;s selected display formats. | [optional] 
**hours_per_year** | **float** | The number of work hours per year. This conversion factor is used for displaying time units and durations in the user&#39;s selected display formats. | [optional] 
**ip_site_list** | **str** |  | [optional] 
**last_update_date** | **datetime** | The date this global preferences was last updated. | [optional] 
**last_update_user** | **str** | The name of the user that last updated this global preferences. | [optional] 
**log_hours_after_actual_finish** | **bool** | The flag that indicates whether timesheet application users are allowed to log timesheet hours on activities for dates after the activities&#39; actual finish dates. | [optional] 
**log_hours_before_actual_start** | **bool** | The flag that indicates whether timesheet application users are allowed to log timesheet hours on activities for dates prior to the activities&#39; actual start dates. | [optional] 
**log_hours_completed_activities** | **bool** | The flag that indicates whether timesheet application users are allowed to log timesheet hours on activities that are already marked as completed. | [optional] 
**log_hours_in_future** | **bool** | The flag that indicates whether the user can log hours in the future. | [optional] 
**log_hours_not_started_activities** | **bool** | The flag that indicates whether timesheet application users are allowed to log timesheet hours on activities that are still marked as Not started. | [optional] 
**max_activity_code_tree_levels** | **int** | The maximum number of levels that can be created in activity code hierarchies in the Project Management application. The API ignores this setting when creating activity codes. | [optional] 
**max_activity_codes_per_project** | **int** | The maximum number of project-level activity user codes that can be created per project. | [optional] 
**max_activity_id_length** | **int** | The maximum number of characters allowed for activity IDs. | [optional] 
**max_assignment_code_tree_level_cnt** | **int** |  | [optional] 
**max_baselines_per_project** | **int** | The maximum number of baselines that can be created per project. | [optional] 
**max_cost_account_length** | **int** | The maximum number of characters allowed for cost account IDs (at each level in the cost account tree). | [optional] 
**max_cost_account_tree_levels** | **int** | The maximum number of levels that can be created in the cost account hierarchy in the Project Management application. The API ignores this setting when creating cost accounts. | [optional] 
**max_fp_calendar_count** | **int** |  | [optional] 
**max_obs_tree_levels** | **int** | The maximum number of levels that can be created in OBS hierarchies in the Project Management application. The API ignores this setting when creating OBS objects. | [optional] 
**max_project_code_tree_levels** | **int** | The maximum number of levels in the project category hierarchy in the Project Management application. The API ignores this setting when creating project codes. | [optional] 
**max_project_id_length** | **int** | The maximum number characters allowed for project IDs. | [optional] 
**max_resource_code_tree_levels** | **int** | The maximum number of levels in the resource code hierarchy in the Project Management application. The API ignores this setting when creating resource codes. | [optional] 
**max_resource_id_length** | **int** | The maximum number of characters allowed for resource IDs (at each level in the resource tree). | [optional] 
**max_resource_tree_levels** | **int** | The maximum number of levels that can be created in the resource hierarchy. | [optional] 
**max_role_code_tree_level_cnt** | **int** |  | [optional] 
**max_role_id_length** | **int** | The maximum number characters allowed for role IDs. | [optional] 
**max_role_tree_levels** | **int** | The maximum number of levels in the role hierarchy in the Project Management application. The API ignores this setting when creating roles. | [optional] 
**max_timesheet_resource_hours** | **float** | The maximum hours a resource can enter per day for all of their assigned activities. | [optional] 
**max_wbs_code_length** | **int** | The maximum number of characters allowed for WBS codes (at each level in the WBS tree). | [optional] 
**max_wbs_tree_levels** | **int** | The maximum number of levels that can be created in WBS hierarchies. | [optional] 
**maximum_baselines_copied_with_project** | **int** | The number of baseline projects that can be copied with a project. | [optional] 
**minute_abbreviation** | **str** | The abbreviation character for time periods of minutes. This abbreviation is used for displaying time units and durations in the user&#39;s selected display formats. | [optional] 
**month_abbreviation** | **str** | The abbreviation character for time periods of months. This abbreviation is used for displaying time units and durations in the user&#39;s selected display formats. | [optional] 
**number_of_accessible_future_timesheets** | **int** | The number of future timesheets that timesheet application users are allowed to access. | [optional] 
**number_of_accessible_past_timesheets** | **int** |  | [optional] 
**private_ip_allow_list** | **str** |  | [optional] 
**report_enable_lazy_load** | **bool** |  | [optional] 
**resources_can_assign_themselves_to_activities** | **bool** | The flag that indicates whether timesheet application users are allowed to assign themselves to activities in this project. | [optional] 
**resources_can_assign_themselves_to_activities_outside_their_obs_access** | **bool** |  | [optional] 
**start_day_of_week** | **int** | The starting day of the week as displayed in all calendars. | [optional] 
**summarize_by_calendar** | **bool** | The flag indicating whether to summarize by calendar . | [optional] 
**summarize_by_financial_periods** | **bool** | The flag indicating whether to summarize the EPS, project or WBS by financial periods. | [optional] 
**summary_resource_spread_interval** | **str** | The interval in which resource and role level spreads are summarized and stored. Valid values are &#39;Month&#39; and &#39;Week&#39;. This setting is used by the Summarizer job service. | [optional] 
**summary_wbs_spread_interval** | **str** | The interval in which WBS level spreads are summarized and stored. Valid values are &#39;Month&#39; and &#39;Week&#39;. This setting is used by the Summarizer job service. | [optional] 
**team_member_consent_message** | **str** |  | [optional] 
**team_member_enable_consent** | **str** |  | [optional] 
**time_window_completed_activities** | **int** | The time window (days) to access completed activities in the timesheet application, assigned to new resources by default. | [optional] 
**time_window_not_started_activities** | **int** | The time window (days) to access not started activities in the timesheet application, assigned to new resources by default. | [optional] 
**timesheet_approval_level** | **int** | The number of approval levels required for timesheets (0, 1, or 2) before timesheets hours are applied to activities as actuals. | [optional] 
**timesheet_decimal_digits** | **int** | The number of decimal digits for recording hours in timesheets. | [optional] 
**timesheet_interval** | **bool** | The flag that indicates whether timesheet application users enter timesheet hours daily or by entire timesheet reporting period. | [optional] 
**timesheet_period_ends_on_day** | **str** | The end day of time sheet period used in time sheet application. Valid values are: &#39;Sunday&#39;, &#39;Monday&#39;, &#39;Tuesday&#39;, &#39;Wednesday&#39;, &#39;Thursday&#39;, &#39;Friday&#39; and &#39;Saturday&#39;. | [optional] 
**timesheet_period_type** | **str** | The time period used in time sheet application. Valid values are: &#39;Every Week&#39;, &#39;Every Two Weeks&#39;, &#39;Every Four Weeks&#39; and &#39;Every Month&#39;. | [optional] 
**unifier_auth_code** | **str** |  | [optional] 
**unifier_company_short_name** | **str** |  | [optional] 
**unifier_integration_password** | **str** |  | [optional] 
**unifier_integration_user_name** | **str** |  | [optional] 
**unifier_web_service_url** | **str** |  | [optional] 
**use_calendar_time_periods_flag** | **bool** | The flag that indicates whether the system uses the hours per time period defined in the calendar.If this flag is true, the system uses the hours per time period settings that are defined in the calendar.If this flag is false, the system uses the hours per time period from the global preferences. | [optional] 
**use_max_timesheet_resource_hours** | **bool** | The flag indicating whether to restrict the number of hours a user can enter to the limit specified in MaxTimesheetResourceHours. | [optional] 
**use_project_manager_approval** | **str** | The flag that indicates the approval sequence, if any, required for level 2 timesheet approvals. For example, project managers must approve before resource manager do, or vice versa. | [optional] 
**use_timesheets** | **bool** | The flag that indicates whether new resources use timesheets by default. | [optional] 
**version_for_whats_new** | **str** |  | [optional] 
**wbs_category_label** | **str** | The dynamic label used for the WBS category. Project Planner allows the system administrator to dynamically label the WBS category. | [optional] 
**wbs_code_separator** | **str** | The character used for separating code fields for the cost account tree. This is also the WBS code separator for new projects by default. | [optional] 
**week_abbreviation** | **str** | The abbreviation character for time periods of weeks. This abbreviation is used for displaying time units and durations in the user&#39;s selected display formats. | [optional] 
**year_abbreviation** | **str** | The abbreviation character for time periods of years. This abbreviation is used for displaying time units and durations in the user&#39;s selected display formats. | [optional] 

## Example

```python
from openapi_client.models.global_preferences import GlobalPreferences

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalPreferences from a JSON string
global_preferences_instance = GlobalPreferences.from_json(json)
# print the JSON string representation of the object
print(GlobalPreferences.to_json())

# convert the object into a dict
global_preferences_dict = global_preferences_instance.to_dict()
# create an instance of GlobalPreferences from a dict
global_preferences_from_dict = GlobalPreferences.from_dict(global_preferences_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


