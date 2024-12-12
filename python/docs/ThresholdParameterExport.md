# ThresholdParameterExport

ThresholdParameter Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **bool** | Boolean flag that indicates whether the associated object is to be exported. The default value of the Include element is true. To exclude a business object from the XML export file, specify false in the Include element for that business object. | [optional] 
**var_field** | **List[str]** | List of Fields for ThresholdParameter Business Object | [optional] 

## Example

```python
from openapi_client.models.threshold_parameter_export import ThresholdParameterExport

# TODO update the JSON string below
json = "{}"
# create an instance of ThresholdParameterExport from a JSON string
threshold_parameter_export_instance = ThresholdParameterExport.from_json(json)
# print the JSON string representation of the object
print(ThresholdParameterExport.to_json())

# convert the object into a dict
threshold_parameter_export_dict = threshold_parameter_export_instance.to_dict()
# create an instance of ThresholdParameterExport from a dict
threshold_parameter_export_from_dict = ThresholdParameterExport.from_dict(threshold_parameter_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


