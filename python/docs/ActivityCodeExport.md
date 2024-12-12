# ActivityCodeExport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **bool** | Boolean flag that indicates whether the associated object is to be exported. The default value of the Include element is true. To exclude a business object from the XML export file, specify false in the Include element for that business object. | [optional] 
**var_field** | **List[str]** | List of Fields for ActivityCode Business Object | [optional] 

## Example

```python
from openapi_client.models.activity_code_export import ActivityCodeExport

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityCodeExport from a JSON string
activity_code_export_instance = ActivityCodeExport.from_json(json)
# print the JSON string representation of the object
print(ActivityCodeExport.to_json())

# convert the object into a dict
activity_code_export_dict = activity_code_export_instance.to_dict()
# create an instance of ActivityCodeExport from a dict
activity_code_export_from_dict = ActivityCodeExport.from_dict(activity_code_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


