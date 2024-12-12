# ApplyActuals

ApplyActuals Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_object_id** | **int** | The unique identifier of the project you want to summarize. | [optional] 
**new_data_date** | **datetime** | The unique identifier of the project you want to summarize. | [optional] 
**timeout** | **int** | The unique identifier of the project you want to summarize. | [optional] 

## Example

```python
from openapi_client.models.apply_actuals import ApplyActuals

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyActuals from a JSON string
apply_actuals_instance = ApplyActuals.from_json(json)
# print the JSON string representation of the object
print(ApplyActuals.to_json())

# convert the object into a dict
apply_actuals_dict = apply_actuals_instance.to_dict()
# create an instance of ApplyActuals from a dict
apply_actuals_from_dict = ApplyActuals.from_dict(apply_actuals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


