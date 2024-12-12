# StandardWorkHours


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_of_week** | **str** |  | [optional] 
**work_time** | [**List[WorkTime]**](WorkTime.md) |  | [optional] 

## Example

```python
from openapi_client.models.standard_work_hours import StandardWorkHours

# TODO update the JSON string below
json = "{}"
# create an instance of StandardWorkHours from a JSON string
standard_work_hours_instance = StandardWorkHours.from_json(json)
# print the JSON string representation of the object
print(StandardWorkHours.to_json())

# convert the object into a dict
standard_work_hours_dict = standard_work_hours_instance.to_dict()
# create an instance of StandardWorkHours from a dict
standard_work_hours_from_dict = StandardWorkHours.from_dict(standard_work_hours_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


