# Level

SummarizeProject Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_object_id** | **int** | The unique identifier of the project you want to summarize. | [optional] 
**timeout** | **int** | The unique identifier of the project you want to summarize. | [optional] 

## Example

```python
from openapi_client.models.level import Level

# TODO update the JSON string below
json = "{}"
# create an instance of Level from a JSON string
level_instance = Level.from_json(json)
# print the JSON string representation of the object
print(Level.to_json())

# convert the object into a dict
level_dict = level_instance.to_dict()
# create an instance of Level from a dict
level_from_dict = Level.from_dict(level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


