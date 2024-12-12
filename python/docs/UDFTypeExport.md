# UDFTypeExport

UDFType Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **bool** | Boolean flag that indicates whether the associated object is to be exported. The default value of the Include element is true. To exclude a business object from the XML export file, specify false in the Include element for that business object. | [optional] 
**var_field** | **List[str]** | List of Fields for UDFType Business Object | [optional] 

## Example

```python
from openapi_client.models.udf_type_export import UDFTypeExport

# TODO update the JSON string below
json = "{}"
# create an instance of UDFTypeExport from a JSON string
udf_type_export_instance = UDFTypeExport.from_json(json)
# print the JSON string representation of the object
print(UDFTypeExport.to_json())

# convert the object into a dict
udf_type_export_dict = udf_type_export_instance.to_dict()
# create an instance of UDFTypeExport from a dict
udf_type_export_from_dict = UDFTypeExport.from_dict(udf_type_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


