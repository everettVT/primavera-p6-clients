# Relationship

Relationship Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aref** | **datetime** | The Adjusted Relationship Early Finish where one of the activities of the relationship is in a project which is not present in this database. | [optional] 
**arls** | **datetime** | The Adjusted Relationship Late Start where one of the activities of the relationship is in a project which is not present in this database. | [optional] 
**comments** | **str** |  | [optional] 
**create_date** | **datetime** | The date this dependency was created. | [optional] 
**create_user** | **str** | The name of the user that created this dependency. | [optional] 
**driving** | **bool** |  | [optional] 
**is_predecessor_baseline** | **bool** | The YesNo value indicating if the predecessor activity is related to a Project or Baseline | [optional] 
**is_predecessor_template** | **bool** | The boolean value indicating if this business object is related to a template Project. | [optional] 
**is_successor_baseline** | **bool** | The YesNo value indicating if the successor activity is related to a Project or Baseline | [optional] 
**is_successor_template** | **bool** | The boolean value indicating if this business object is related to a template Project. | [optional] 
**lag** | **float** | The time lag of the relationship. This is the time lag between the predecessor activity&#39;s start or finish date and the successor activity&#39;s start or finish date, depending on the relationship type. The time lag is based on the successor activity&#39;s calendar. This value is specified by the project manager and is used by the project scheduler when scheduling activities. | [optional] 
**last_update_date** | **datetime** | The date this dependency was last updated. | [optional] 
**last_update_user** | **str** | The name of the user that last updated this dependency. | [optional] 
**object_id** | **int** | The unique ID generated by the system. | [optional] 
**predecessor_activity_id** | **str** | The activity ID of the predecessor activity. | [optional] 
**predecessor_activity_name** | **str** | The name of the predecessor activity. | [optional] 
**predecessor_activity_object_id** | **int** | The unique ID of the predecessor activity. | 
**predecessor_activity_type** | **str** | The type of the predecessor activity, either &#39;Task Dependent&#39;, &#39;Resource Dependent&#39;, &#39;Level of Effort&#39;, or &#39;Milestone&#39;. | [optional] 
**predecessor_finish_date** | **datetime** | The finish date of the predecessor activity. | [optional] 
**predecessor_project_id** | **str** | The project ID of the project that owns the predecessor activity. | [optional] 
**predecessor_project_object_id** | **int** | The unique ID of the project that owns the predecessor activity. | [optional] 
**predecessor_start_date** | **datetime** | The start date of the predecessor activity. | [optional] 
**predecessor_wbs_name** | **str** | The name of each WBS element in the predecessor activity. | [optional] 
**successor_activity_id** | **str** | The activity ID of the successor activity. | [optional] 
**successor_activity_name** | **str** | The name of the successor activity. | [optional] 
**successor_activity_object_id** | **int** | The unique ID of the successor activity. | 
**successor_activity_type** | **str** | The type of the successor activity, either &#39;Task Dependent&#39;, &#39;Resource Dependent&#39;, &#39;Level of Effort&#39;, or &#39;Milestone&#39;. | [optional] 
**successor_finish_date** | **datetime** | The finish date of the successor activity. | [optional] 
**successor_project_id** | **str** | The project ID of the project that owns the successor activity. | [optional] 
**successor_project_object_id** | **int** | The unique ID of the project that owns the successor activity. | [optional] 
**successor_start_date** | **datetime** | The start date of the successor activity. | [optional] 
**successor_wbs_name** | **str** | The name of each WBS element in the successor activity. | [optional] 
**type** | **str** | The type of relationship: &#39;Finish to Start&#39;, &#39;Finish to Finish&#39;, &#39;Start to Start&#39;, or &#39;Start to Finish&#39;. | [optional] 

## Example

```python
from openapi_client.models.relationship import Relationship

# TODO update the JSON string below
json = "{}"
# create an instance of Relationship from a JSON string
relationship_instance = Relationship.from_json(json)
# print the JSON string representation of the object
print(Relationship.to_json())

# convert the object into a dict
relationship_dict = relationship_instance.to_dict()
# create an instance of Relationship from a dict
relationship_from_dict = Relationship.from_dict(relationship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

