# UpdateResourceAssignmentSpread

UpdateResourceAssignmentSpread Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_type** | **str** | Spread period type enumerations are used to specify the spread interval for EPS, project, WBS, Activity, and resource assignment spreads. | [optional] 
**resource_assignment_spread** | [**List[ResourceAssignmentSpread]**](ResourceAssignmentSpread.md) | The live resource assignment spread data. | [optional] 

## Example

```python
from openapi_client.models.update_resource_assignment_spread import UpdateResourceAssignmentSpread

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateResourceAssignmentSpread from a JSON string
update_resource_assignment_spread_instance = UpdateResourceAssignmentSpread.from_json(json)
# print the JSON string representation of the object
print(UpdateResourceAssignmentSpread.to_json())

# convert the object into a dict
update_resource_assignment_spread_dict = update_resource_assignment_spread_instance.to_dict()
# create an instance of UpdateResourceAssignmentSpread from a dict
update_resource_assignment_spread_from_dict = UpdateResourceAssignmentSpread.from_dict(update_resource_assignment_spread_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


