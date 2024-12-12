# ResourceRoleExport

ResourceRole Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **bool** | Boolean flag that indicates whether the associated object is to be exported. The default value of the Include element is true. To exclude a business object from the XML export file, specify false in the Include element for that business object. | [optional] 
**var_field** | **List[str]** | List of Fields for ResourceRole Business Object | [optional] 

## Example

```python
from openapi_client.models.resource_role_export import ResourceRoleExport

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRoleExport from a JSON string
resource_role_export_instance = ResourceRoleExport.from_json(json)
# print the JSON string representation of the object
print(ResourceRoleExport.to_json())

# convert the object into a dict
resource_role_export_dict = resource_role_export_instance.to_dict()
# create an instance of ResourceRoleExport from a dict
resource_role_export_from_dict = ResourceRoleExport.from_dict(resource_role_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


