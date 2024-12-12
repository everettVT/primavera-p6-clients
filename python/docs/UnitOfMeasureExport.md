# UnitOfMeasureExport

UnitOfMeasure Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **bool** | Boolean flag that indicates whether the associated object is to be exported. The default value of the Include element is true. To exclude a business object from the XML export file, specify false in the Include element for that business object. | [optional] 
**var_field** | **List[str]** | List of Fields for UnitOfMeasure Business Object | [optional] 

## Example

```python
from openapi_client.models.unit_of_measure_export import UnitOfMeasureExport

# TODO update the JSON string below
json = "{}"
# create an instance of UnitOfMeasureExport from a JSON string
unit_of_measure_export_instance = UnitOfMeasureExport.from_json(json)
# print the JSON string representation of the object
print(UnitOfMeasureExport.to_json())

# convert the object into a dict
unit_of_measure_export_dict = unit_of_measure_export_instance.to_dict()
# create an instance of UnitOfMeasureExport from a dict
unit_of_measure_export_from_dict = UnitOfMeasureExport.from_dict(unit_of_measure_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


