# ProjectResourceCategoryExport

ProjectResourceCategory Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **bool** | Boolean flag that indicates whether the associated object is to be exported. The default value of the Include element is true. To exclude a business object from the XML export file, specify false in the Include element for that business object. | [optional] 
**var_field** | **List[str]** | List of Fields for ProjectResourceCategory Business Object | [optional] 

## Example

```python
from openapi_client.models.project_resource_category_export import ProjectResourceCategoryExport

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectResourceCategoryExport from a JSON string
project_resource_category_export_instance = ProjectResourceCategoryExport.from_json(json)
# print the JSON string representation of the object
print(ProjectResourceCategoryExport.to_json())

# convert the object into a dict
project_resource_category_export_dict = project_resource_category_export_instance.to_dict()
# create an instance of ProjectResourceCategoryExport from a dict
project_resource_category_export_from_dict = ProjectResourceCategoryExport.from_dict(project_resource_category_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


