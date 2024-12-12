# ResourceAssignmentSpread

The live resource assignment spread data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_assignment_object_id** | **str** | The unique ID of the associated resource assignment. | [optional] 
**period** | [**List[Period]**](Period.md) |  | [optional] 

## Example

```python
from openapi_client.models.resource_assignment_spread import ResourceAssignmentSpread

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceAssignmentSpread from a JSON string
resource_assignment_spread_instance = ResourceAssignmentSpread.from_json(json)
# print the JSON string representation of the object
print(ResourceAssignmentSpread.to_json())

# convert the object into a dict
resource_assignment_spread_dict = resource_assignment_spread_instance.to_dict()
# create an instance of ResourceAssignmentSpread from a dict
resource_assignment_spread_from_dict = ResourceAssignmentSpread.from_dict(resource_assignment_spread_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


