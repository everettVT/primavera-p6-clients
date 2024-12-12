# ResourceRequestCriterion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criterion_type** | **str** |  | [optional] 
**proficiency** | **str** |  | [optional] 
**value_object_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.resource_request_criterion import ResourceRequestCriterion

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRequestCriterion from a JSON string
resource_request_criterion_instance = ResourceRequestCriterion.from_json(json)
# print the JSON string representation of the object
print(ResourceRequestCriterion.to_json())

# convert the object into a dict
resource_request_criterion_dict = resource_request_criterion_instance.to_dict()
# create an instance of ResourceRequestCriterion from a dict
resource_request_criterion_from_dict = ResourceRequestCriterion.from_dict(resource_request_criterion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


