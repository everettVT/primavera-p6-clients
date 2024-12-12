# CreateActivityPeriodActualResponse

CreateProjectResourceQuantityResponse Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**financial_period_object_id** | **int** | The unique ID of the associated financial period. | [optional] 
**activity_object_id** | **int** | The unique ID of the associated activity. | [optional] 

## Example

```python
from openapi_client.models.create_activity_period_actual_response import CreateActivityPeriodActualResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateActivityPeriodActualResponse from a JSON string
create_activity_period_actual_response_instance = CreateActivityPeriodActualResponse.from_json(json)
# print the JSON string representation of the object
print(CreateActivityPeriodActualResponse.to_json())

# convert the object into a dict
create_activity_period_actual_response_dict = create_activity_period_actual_response_instance.to_dict()
# create an instance of CreateActivityPeriodActualResponse from a dict
create_activity_period_actual_response_from_dict = CreateActivityPeriodActualResponse.from_dict(create_activity_period_actual_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


