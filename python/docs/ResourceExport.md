# ResourceExport

Resource Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **bool** | Boolean flag that indicates whether the associated object is to be exported. The default value of the Include element is true. To exclude a business object from the XML export file, specify false in the Include element for that business object. | [optional] 
**var_field** | **List[str]** | List of Fields for Resource Business Object | [optional] 

## Example

```python
from openapi_client.models.resource_export import ResourceExport

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceExport from a JSON string
resource_export_instance = ResourceExport.from_json(json)
# print the JSON string representation of the object
print(ResourceExport.to_json())

# convert the object into a dict
resource_export_dict = resource_export_instance.to_dict()
# create an instance of ResourceExport from a dict
resource_export_from_dict = ResourceExport.from_dict(resource_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


