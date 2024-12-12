# ResourceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**finish_date** | **datetime** |  | [optional] 
**match_all_criteria** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**requested_units** | **float** |  | [optional] 
**sequence_number** | **int** |  | [optional] 
**show_only_labor_resources** | **bool** |  | [optional] 
**show_overallocated_resources** | **bool** |  | [optional] 
**sort_results_by_availability** | **bool** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**use_activity_dates** | **bool** |  | [optional] 
**resource_request_criterion** | [**List[ResourceRequestCriterion]**](ResourceRequestCriterion.md) |  | [optional] 

## Example

```python
from openapi_client.models.resource_request import ResourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRequest from a JSON string
resource_request_instance = ResourceRequest.from_json(json)
# print the JSON string representation of the object
print(ResourceRequest.to_json())

# convert the object into a dict
resource_request_dict = resource_request_instance.to_dict()
# create an instance of ResourceRequest from a dict
resource_request_from_dict = ResourceRequest.from_dict(resource_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


