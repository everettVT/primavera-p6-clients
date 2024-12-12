# RiskResponseAction

RiskResponseAction Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_id** | **str** | The id of an activity impacted by the Risk. | [optional] 
**activity_name** | **str** | The name of an activity impacted by the Risk. The activity name does not have to be unique. | [optional] 
**activity_object_id** | **int** | The unique ID of the associated activity. | [optional] 
**actual_cost** | **float** | The actual cost. | [optional] 
**create_date** | **datetime** | The date this risk response action impact was created. | [optional] 
**create_user** | **str** | The name of the user that created the risk response action impact. | [optional] 
**finish_date** | **datetime** | The finish date of the risk response action. If an activity is assigned, the risk response action uses the activity finish date. | [optional] 
**id** | **str** | The unique Id of the risk response action. | [optional] 
**is_baseline** | **bool** | The boolean value indicating if this business object is related to a Project or Baseline. | [optional] 
**is_template** | **bool** | The boolean value indicating if this business object is related to a template Project. | [optional] 
**last_update_date** | **datetime** | The date this risk response action impact was last updated. | [optional] 
**last_update_user** | **str** | The name of the user that last updated the risk response action impact. | [optional] 
**name** | **str** | The name of the risk response action. | [optional] 
**object_id** | **int** | The unique ID of the associated risk. | [optional] 
**planned_cost** | **float** | The planned cost. | [optional] 
**planned_finish_date** | **datetime** | The planned finish date. | [optional] 
**planned_start_date** | **datetime** | The planned start date. | [optional] 
**project_id** | **str** | The short name of the associated project. | [optional] 
**project_name** | **str** | The name of the associated project. | [optional] 
**project_object_id** | **int** | The unique ID of the associated project. | [optional] 
**remaining_cost** | **float** | The remaining cost associated with the risk response action. | [optional] 
**resource_id** | **str** | The ID of the resource who owns the risk response action. The owner of the risk response action is responsible for resolving the risk response action. | [optional] 
**resource_name** | **str** | The name of the resource who owns the risk response action. The owner of the risk response action is responsible for resolving the risk response action. | [optional] 
**resource_object_id** | **int** | The unique ID of the associated resource. | [optional] 
**risk_id** | **str** | The ID of the Risk. Must be unique within a project. | [optional] 
**risk_object_id** | **int** | The unique ID of the associated risk. | [optional] 
**risk_response_plan_id** | **str** | The ID of the risk response plan. This must be unique within the project. | [optional] 
**risk_response_plan_name** | **str** | The name of the risk response plan. This does not need to be unique within the project. | [optional] 
**risk_response_plan_object_id** | **int** | The unique ID of the associated risk response plan. | [optional] 
**score** | **int** | The risk score from the numeric PID after the response action has been completed. | [optional] 
**score_color** | **str** | The color of the tolerance threshold for the score value. | [optional] 
**score_text** | **str** | The risk score from the alphanumeric PID after the response action has been completed. | [optional] 
**start_date** | **datetime** | The start date of the risk response action. If an activity is assigned, the risk response action uses the activity start date. | [optional] 
**status** | **str** | The status of the risk response action. Valid values are &#39;Proposed&#39;, &#39;Sanctioned&#39;, &#39;Rejected&#39;, &#39;InProgress&#39;, and &#39;Complete&#39;. | [optional] 

## Example

```python
from openapi_client.models.risk_response_action import RiskResponseAction

# TODO update the JSON string below
json = "{}"
# create an instance of RiskResponseAction from a JSON string
risk_response_action_instance = RiskResponseAction.from_json(json)
# print the JSON string representation of the object
print(RiskResponseAction.to_json())

# convert the object into a dict
risk_response_action_dict = risk_response_action_instance.to_dict()
# create an instance of RiskResponseAction from a dict
risk_response_action_from_dict = RiskResponseAction.from_dict(risk_response_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


