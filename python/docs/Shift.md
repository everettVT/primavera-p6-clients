# Shift

Shift Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_date** | **datetime** | The date this shift was created. | [optional] 
**create_user** | **str** | The name of the user that created this shift. | [optional] 
**last_update_date** | **datetime** | The date this shift was last updated. | [optional] 
**last_update_user** | **str** | The date this shift was last updated. | [optional] 
**name** | **str** | The name of the shift. | [optional] 
**object_id** | **int** | The unique ID generated by the system. | [optional] 
**shift_period** | [**List[ShiftPeriod]**](ShiftPeriod.md) |  | [optional] 

## Example

```python
from openapi_client.models.shift import Shift

# TODO update the JSON string below
json = "{}"
# create an instance of Shift from a JSON string
shift_instance = Shift.from_json(json)
# print the JSON string representation of the object
print(Shift.to_json())

# convert the object into a dict
shift_dict = shift_instance.to_dict()
# create an instance of Shift from a dict
shift_from_dict = Shift.from_dict(shift_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

