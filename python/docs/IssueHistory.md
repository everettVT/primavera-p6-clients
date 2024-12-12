# IssueHistory

IssueHistory Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_date** | **datetime** | The date this issue history was created. | [optional] 
**create_user** | **str** | The name of the user that created this issue history. | [optional] 
**is_baseline** | **bool** | The boolean value indicating if this business object is related to a Project or Baseline | [optional] 
**is_template** | **bool** | The boolean value indicating if this business object is related to a template Project. | [optional] 
**last_update_date** | **datetime** | The date this issue history was last updated. | [optional] 
**last_update_user** | **str** | The name of the user that last updated this issue history. | [optional] 
**notes** | **str** | The notes associated with the issue history. | [optional] 
**project_issue_object_id** | **int** | The unique ID of the associated project issue for this issue history. | [optional] 
**project_object_id** | **int** | The unique ID of the associated project for this issue history. | [optional] 

## Example

```python
from openapi_client.models.issue_history import IssueHistory

# TODO update the JSON string below
json = "{}"
# create an instance of IssueHistory from a JSON string
issue_history_instance = IssueHistory.from_json(json)
# print the JSON string representation of the object
print(IssueHistory.to_json())

# convert the object into a dict
issue_history_dict = issue_history_instance.to_dict()
# create an instance of IssueHistory from a dict
issue_history_from_dict = IssueHistory.from_dict(issue_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


