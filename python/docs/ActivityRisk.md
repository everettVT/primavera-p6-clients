# ActivityRisk

ActivityRisk Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_id** | **str** | The id of an activity impacted by the Risk. | [optional] 
**activity_name** | **str** | The name of an activity impacted by the Risk. The activity name does not have to be unique. | [optional] 
**activity_object_id** | **int** | The unique ID of the activity to which the risk is assigned. | 
**create_date** | **datetime** | The date this activity was created. | [optional] 
**create_user** | **str** | The name of the user that created this activity risk. | [optional] 
**is_baseline** | **bool** | The boolean value indicating if this business object is related to a Project or Baseline | [optional] 
**is_template** | **bool** | The boolean value indicating if this business object is related to a template Project. | [optional] 
**last_update_date** | **datetime** | The date this activity was last updated. | [optional] 
**last_update_user** | **str** | The name of the user that last updated this activity risk. | [optional] 
**project_id** | **str** | The short code of the associated project. | [optional] 
**project_name** | **str** | The name of the associated project. | [optional] 
**project_object_id** | **int** | The unique ID of the associated project. | [optional] 
**risk_id** | **str** | The ID of the Risk. Must be unique within a project. | [optional] 
**risk_name** | **str** | The name of the Risk. Does not need to be unique. | [optional] 
**risk_object_id** | **int** | The unique ID of the associated risk. | 

## Example

```python
from openapi_client.models.activity_risk import ActivityRisk

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityRisk from a JSON string
activity_risk_instance = ActivityRisk.from_json(json)
# print the JSON string representation of the object
print(ActivityRisk.to_json())

# convert the object into a dict
activity_risk_dict = activity_risk_instance.to_dict()
# create an instance of ActivityRisk from a dict
activity_risk_from_dict = ActivityRisk.from_dict(activity_risk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


