# StandardWorkWeek


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**standard_work_hours** | [**List[StandardWorkHours]**](StandardWorkHours.md) |  | [optional] 

## Example

```python
from openapi_client.models.standard_work_week import StandardWorkWeek

# TODO update the JSON string below
json = "{}"
# create an instance of StandardWorkWeek from a JSON string
standard_work_week_instance = StandardWorkWeek.from_json(json)
# print the JSON string representation of the object
print(StandardWorkWeek.to_json())

# convert the object into a dict
standard_work_week_dict = standard_work_week_instance.to_dict()
# create an instance of StandardWorkWeek from a dict
standard_work_week_from_dict = StandardWorkWeek.from_dict(standard_work_week_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


