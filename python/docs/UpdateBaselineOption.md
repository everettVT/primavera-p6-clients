# UpdateBaselineOption

UpdateBaselineOption Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activities_filter** | **str** | The option used to update activity IDs of the selected filter when updating the baseline. | [optional] 
**activities_filter_logic** | **str** | The option used to update activity filter logic when updating the baseline. | [optional] 
**activity_code_assignments** | **bool** | The option used to update activity code assignments when updating the baseline. | [optional] 
**activity_filter_id** | **str** | The option used to update activity filter id when updating the baseline. | [optional] 
**activity_filter_name** | **str** | The option used to update activity filter name when updating the baseline. | [optional] 
**activity_information** | **bool** | The option used to update activity information for existing resource and role assignments when updating the baseline. | [optional] 
**activity_notebooks** | **bool** | The option used to update activity information for existing resource and role assignments when updating the baseline. | [optional] 
**activity_rsrc_assignment_codes** | **bool** |  | [optional] 
**activity_rsrc_assignment_udfs** | **bool** | The option used to update activity resource assignment UDFs when updating the baseline. | [optional] 
**activity_udfs** | **bool** | The option used to update activity UDFs when updating the baseline | [optional] 
**actual_units_cost_wo_rsrc_assignmnt** | **bool** | The option used to update activity actual units and cost without resource assignments when updating the baseline. | [optional] 
**add_new_activities_data** | **bool** | The option used to add new activities with data when updating the baseline. | [optional] 
**add_new_rsrc_role** | **bool** | The option used to add new resource and role assignments when updating the baseline. | [optional] 
**all_activities** | **bool** | The option used to include all activities when updating the baseline. | [optional] 
**batch_mode_enabled** | **bool** | The option used to enable the batch update mode when updating the baseline. | [optional] 
**budget_units_cost** | **bool** | The option used to update budget units and cost for existing resource and role assignments when updating the baseline. | [optional] 
**budget_units_cost_wo_rsrc_assignmnt** | **bool** | The option used to update activity budget units and cost without resource assignment when updating the baseline. | [optional] 
**constraints** | **bool** | The option used to update activity constraints when updating the baseline | [optional] 
**dates_duration_datadates** | **bool** | The option used to update activity dates, duration, and data dates when updating the baseline | [optional] 
**delete_non_existing_activities** | **bool** | The option used to delete non existing activities when updating the baseline. | [optional] 
**expense_udfs** | **bool** | the option used to update activity expense UDFs when updating the baseline. | [optional] 
**expenses** | **bool** | The option used to update activity expenses when updating the baseline. | [optional] 
**filtered_activities** | **bool** | The option used to include activities in the selected folder when updating the baseline. | [optional] 
**general_activiti_info** | **bool** | The option used to update general activity info when updating the baseline. | [optional] 
**ignore_last_update_date** | **bool** | The option used to ignore LastUpdateDate when updating the baseline. | [optional] 
**issue_udfs** | **bool** | The option used to update the Issue UDFs when updating the baseline. | [optional] 
**new_activity_information** | **bool** |  | [optional] 
**new_budget_units_cost** | **bool** |  | [optional] 
**object_id** | **int** | The unique ID of the associated user. | 
**project_details** | **bool** | The option used to update the project details when updating the baseline. | [optional] 
**project_risks_issues_and_thresholds** | **bool** | The option used to update the Project Risks Issues and Thresholds when updating the baseline. | [optional] 
**project_udfs** | **bool** | The option used to update the project UDFs when updating the baseline. | [optional] 
**relationships** | **bool** | The option used to update activity relationships when updating the baseline. | [optional] 
**risk_assignments** | **bool** | The option used to update risk assignments when updating the baseline. | [optional] 
**risk_udfs** | **bool** | The option used to update the Risks UDFs when updating the baseline. | [optional] 
**steps** | **bool** | The option used to update activity steps when updating the baseline. | [optional] 
**steps_udf** | **bool** | The option used to update activity steps UDFs when updating the baseline. | [optional] 
**update_exist_rsrc_role_assignment** | **bool** | The option used to update existing resource and role assignments when updating the baseline. | [optional] 
**update_existing_activities** | **bool** | The option used to update existing activities when updating the baseline. | [optional] 
**user_name** | **str** | The user&#39;s login name. | [optional] 
**wp_document_udfs** | **bool** | The option used to update the WPDocument UDFs when updating the baseline. | [optional] 
**wbs_assignments** | **bool** | The option used to update WBS assignments when updating the baseline. | [optional] 
**wbs_udfs** | **bool** | The option used to update the WBS UDFs when updating the baseline. | [optional] 
**work_products_and_documents** | **bool** | The option used to update the work products and documents when updating the baseline. | [optional] 

## Example

```python
from openapi_client.models.update_baseline_option import UpdateBaselineOption

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBaselineOption from a JSON string
update_baseline_option_instance = UpdateBaselineOption.from_json(json)
# print the JSON string representation of the object
print(UpdateBaselineOption.to_json())

# convert the object into a dict
update_baseline_option_dict = update_baseline_option_instance.to_dict()
# create an instance of UpdateBaselineOption from a dict
update_baseline_option_from_dict = UpdateBaselineOption.from_dict(update_baseline_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


