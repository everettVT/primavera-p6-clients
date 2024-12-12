# HolidayOrException


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** |  | [optional] 
**work_time** | [**List[WorkTime]**](WorkTime.md) |  | [optional] 

## Example

```python
from openapi_client.models.holiday_or_exception import HolidayOrException

# TODO update the JSON string below
json = "{}"
# create an instance of HolidayOrException from a JSON string
holiday_or_exception_instance = HolidayOrException.from_json(json)
# print the JSON string representation of the object
print(HolidayOrException.to_json())

# convert the object into a dict
holiday_or_exception_dict = holiday_or_exception_instance.to_dict()
# create an instance of HolidayOrException from a dict
holiday_or_exception_from_dict = HolidayOrException.from_dict(holiday_or_exception_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


