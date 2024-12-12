# ExportProjects

ExportProjects Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encoding** | **str** | Specifies the encoding of the XML file that is exported, e.g., UTF-8. | [optional] 
**file_type** | **str** | FileTypeType Entity | [optional] 
**line_separator** | **str** | Specifies whether the Windows (\&quot;\\r\\n\&quot;) or Unix (\&quot;\\n\&quot;) line endings will be used. | [optional] 
**project_object_id** | **List[int]** |  | [optional] 
**spread_period_type** | **str** | SpreadPeriodType Entity | [optional] 
**spacing** | **str** | Specifies the indentation between the elements in the XML export file. For example, use \&quot; \&quot; to specify 5 spaces of indentation. | [optional] 
**business_object_options** | [**BusinessObjectOptions**](BusinessObjectOptions.md) |  | [optional] 

## Example

```python
from openapi_client.models.export_projects import ExportProjects

# TODO update the JSON string below
json = "{}"
# create an instance of ExportProjects from a JSON string
export_projects_instance = ExportProjects.from_json(json)
# print the JSON string representation of the object
print(ExportProjects.to_json())

# convert the object into a dict
export_projects_dict = export_projects_instance.to_dict()
# create an instance of ExportProjects from a dict
export_projects_from_dict = ExportProjects.from_dict(export_projects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


