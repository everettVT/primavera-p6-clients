# ActivityPeriodActualExport

ActivityPeriodActual Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **bool** | Boolean flag that indicates whether the associated object is to be exported. The default value of the Include element is true. To exclude a business object from the XML export file, specify false in the Include element for that business object. | [optional] 
**var_field** | **List[str]** | List of Fields for ActivityPeriodActual Business Object | [optional] 

## Example

```python
from openapi_client.models.activity_period_actual_export import ActivityPeriodActualExport

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityPeriodActualExport from a JSON string
activity_period_actual_export_instance = ActivityPeriodActualExport.from_json(json)
# print the JSON string representation of the object
print(ActivityPeriodActualExport.to_json())

# convert the object into a dict
activity_period_actual_export_dict = activity_period_actual_export_instance.to_dict()
# create an instance of ActivityPeriodActualExport from a dict
activity_period_actual_export_from_dict = ActivityPeriodActualExport.from_dict(activity_period_actual_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


