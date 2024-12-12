# ActivityOwner

ActivityOwner Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_object_id** | **int** | The unique ID of the associated activity. | 
**create_date** | **datetime** | The date this activity owner was created. | [optional] 
**create_user** | **str** | The name of the user that created this activity owner. | [optional] 
**is_activity_flagged** | **bool** | The flag that indicates whether the owner of the activity has flagged the activity as important. | [optional] 
**is_baseline** | **bool** | The boolean value indicating if this business object is related to a Project or Baseline. | [optional] 
**is_template** | **bool** | The boolean value indicating if this business object is related to a template Project. | [optional] 
**last_update_date** | **datetime** | The date this activity owner was last updated. | [optional] 
**last_update_user** | **str** | The name of the user that last updated this activity owner. | [optional] 
**project_flag** | **str** | Indicates if this WBS node is a Project/EPS node. | [optional] 
**project_object_id** | **int** | The unique ID of the associated project. | [optional] 
**project_project_flag** | **str** | Indicates if this Project/EPS node is a Project or EPS. | [optional] 
**status_code** | **str** | The project status, either &#39;Planned&#39;, &#39;Active&#39;, &#39;Inactive&#39;, &#39;What-If&#39;, &#39;Requested&#39;, or &#39;Template&#39;. | [optional] 
**user_object_id** | **int** | The unique ID of the associated user. | 

## Example

```python
from openapi_client.models.activity_owner import ActivityOwner

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityOwner from a JSON string
activity_owner_instance = ActivityOwner.from_json(json)
# print the JSON string representation of the object
print(ActivityOwner.to_json())

# convert the object into a dict
activity_owner_dict = activity_owner_instance.to_dict()
# create an instance of ActivityOwner from a dict
activity_owner_from_dict = ActivityOwner.from_dict(activity_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


