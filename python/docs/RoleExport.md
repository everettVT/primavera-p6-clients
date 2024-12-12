# RoleExport

Role Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **bool** | Boolean flag that indicates whether the associated object is to be exported. The default value of the Include element is true. To exclude a business object from the XML export file, specify false in the Include element for that business object. | [optional] 
**var_field** | **List[str]** | List of Fields for Role Business Object | [optional] 

## Example

```python
from openapi_client.models.role_export import RoleExport

# TODO update the JSON string below
json = "{}"
# create an instance of RoleExport from a JSON string
role_export_instance = RoleExport.from_json(json)
# print the JSON string representation of the object
print(RoleExport.to_json())

# convert the object into a dict
role_export_dict = role_export_instance.to_dict()
# create an instance of RoleExport from a dict
role_export_from_dict = RoleExport.from_dict(role_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


