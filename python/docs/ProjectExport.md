# ProjectExport

Project Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **bool** | Boolean flag that indicates whether the associated object is to be exported. The default value of the Include element is true. To exclude a business object from the XML export file, specify false in the Include element for that business object. | [optional] 
**var_field** | **List[str]** | List of Fields for Project Business Object | [optional] 

## Example

```python
from openapi_client.models.project_export import ProjectExport

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectExport from a JSON string
project_export_instance = ProjectExport.from_json(json)
# print the JSON string representation of the object
print(ProjectExport.to_json())

# convert the object into a dict
project_export_dict = project_export_instance.to_dict()
# create an instance of ProjectExport from a dict
project_export_from_dict = ProjectExport.from_dict(project_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


