# Resource

Resource Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_compute_actuals** | **bool** |  | [optional] 
**calculate_cost_from_units** | **bool** |  | [optional] 
**calendar_name** | **str** |  | [optional] 
**calendar_object_id** | **int** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**create_user** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**currency_name** | **str** |  | [optional] 
**currency_object_id** | **int** |  | [optional] 
**default_units_per_time** | **float** |  | [optional] 
**effective_date** | **datetime** |  | [optional] 
**email_address** | **str** |  | [optional] 
**employee_id** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**integrated_type** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**is_over_time_allowed** | **bool** |  | [optional] 
**last_update_date** | **datetime** |  | [optional] 
**last_update_user** | **str** |  | [optional] 
**latitude** | **float** |  | [optional] 
**location_name** | **str** |  | [optional] 
**location_object_id** | **int** |  | [optional] 
**longitude** | **float** |  | [optional] 
**max_units_per_time** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**object_id** | **int** |  | [optional] 
**office_phone** | **str** |  | [optional] 
**other_phone** | **str** |  | [optional] 
**overtime_factor** | **float** |  | [optional] 
**parent_object_id** | **int** |  | [optional] 
**price_per_unit** | **float** |  | [optional] 
**primary_role_id** | **str** |  | [optional] 
**primary_role_name** | **str** |  | [optional] 
**primary_role_object_id** | **int** |  | [optional] 
**resource_notes** | **str** |  | [optional] 
**resource_type** | **str** |  | [optional] 
**sequence_number** | **int** |  | [optional] 
**shift_object_id** | **int** |  | [optional] 
**timesheet_approval_manager** | **str** |  | [optional] 
**timesheet_approval_manager_object_id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**unit_of_measure_abbreviation** | **str** |  | [optional] 
**unit_of_measure_name** | **str** |  | [optional] 
**unit_of_measure_object_id** | **int** |  | [optional] 
**use_timesheets** | **bool** |  | [optional] 
**user_name** | **str** |  | [optional] 
**user_object_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.resource import Resource

# TODO update the JSON string below
json = "{}"
# create an instance of Resource from a JSON string
resource_instance = Resource.from_json(json)
# print the JSON string representation of the object
print(Resource.to_json())

# convert the object into a dict
resource_dict = resource_instance.to_dict()
# create an instance of Resource from a dict
resource_from_dict = Resource.from_dict(resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


