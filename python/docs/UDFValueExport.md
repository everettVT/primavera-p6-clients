# UDFValueExport

UDFValue Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **bool** | Boolean flag that indicates whether the associated object is to be exported. The default value of the Include element is true. To exclude a business object from the XML export file, specify false in the Include element for that business object. | [optional] 

## Example

```python
from openapi_client.models.udf_value_export import UDFValueExport

# TODO update the JSON string below
json = "{}"
# create an instance of UDFValueExport from a JSON string
udf_value_export_instance = UDFValueExport.from_json(json)
# print the JSON string representation of the object
print(UDFValueExport.to_json())

# convert the object into a dict
udf_value_export_dict = udf_value_export_instance.to_dict()
# create an instance of UDFValueExport from a dict
udf_value_export_from_dict = UDFValueExport.from_dict(udf_value_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


