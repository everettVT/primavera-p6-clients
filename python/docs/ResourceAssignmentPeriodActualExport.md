# ResourceAssignmentPeriodActualExport

ResourceAssignmentPeriodActual Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **bool** | Boolean flag that indicates whether the associated object is to be exported. The default value of the Include element is true. To exclude a business object from the XML export file, specify false in the Include element for that business object. | [optional] 
**var_field** | **List[str]** | List of Fields for ResourceAssignmentPeriodActual Business Object | [optional] 

## Example

```python
from openapi_client.models.resource_assignment_period_actual_export import ResourceAssignmentPeriodActualExport

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceAssignmentPeriodActualExport from a JSON string
resource_assignment_period_actual_export_instance = ResourceAssignmentPeriodActualExport.from_json(json)
# print the JSON string representation of the object
print(ResourceAssignmentPeriodActualExport.to_json())

# convert the object into a dict
resource_assignment_period_actual_export_dict = resource_assignment_period_actual_export_instance.to_dict()
# create an instance of ResourceAssignmentPeriodActualExport from a dict
resource_assignment_period_actual_export_from_dict = ResourceAssignmentPeriodActualExport.from_dict(resource_assignment_period_actual_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

