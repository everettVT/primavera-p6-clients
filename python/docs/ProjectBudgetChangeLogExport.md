# ProjectBudgetChangeLogExport

ProjectBudgetChangeLog Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **bool** |  | [optional] 
**var_field** | **List[str]** | List of Fields for ProjectBudgetChangeLog Business Object | [optional] 

## Example

```python
from openapi_client.models.project_budget_change_log_export import ProjectBudgetChangeLogExport

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectBudgetChangeLogExport from a JSON string
project_budget_change_log_export_instance = ProjectBudgetChangeLogExport.from_json(json)
# print the JSON string representation of the object
print(ProjectBudgetChangeLogExport.to_json())

# convert the object into a dict
project_budget_change_log_export_dict = project_budget_change_log_export_instance.to_dict()
# create an instance of ProjectBudgetChangeLogExport from a dict
project_budget_change_log_export_from_dict = ProjectBudgetChangeLogExport.from_dict(project_budget_change_log_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


