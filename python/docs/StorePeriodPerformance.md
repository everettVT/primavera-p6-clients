# StorePeriodPerformance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_object_id** | **List[int]** |  | [optional] 
**financial_period_object_id** | **int** |  | [optional] 
**timeout** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.store_period_performance import StorePeriodPerformance

# TODO update the JSON string below
json = "{}"
# create an instance of StorePeriodPerformance from a JSON string
store_period_performance_instance = StorePeriodPerformance.from_json(json)
# print the JSON string representation of the object
print(StorePeriodPerformance.to_json())

# convert the object into a dict
store_period_performance_dict = store_period_performance_instance.to_dict()
# create an instance of StorePeriodPerformance from a dict
store_period_performance_from_dict = StorePeriodPerformance.from_dict(store_period_performance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


