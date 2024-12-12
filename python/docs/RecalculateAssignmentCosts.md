# RecalculateAssignmentCosts

RecalculateAssignmentCosts Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_object_id** | **int** | The unique ID of the associated project. | [optional] 
**synchronize_overtime_factor** | **bool** | Flag that indicates that the overtime factor for the resource should be included when recalculating cost | [optional] 
**timeout** | **int** | The amount of time in seconds that the server side will wait for the job service to complete before it returns with the current job status. The Timeout parameter is optional. When this operation is used without specifying a Timeout parameter or with a Timeout of 0, the server immediately returns without waiting for the job service to complete. | [optional] 

## Example

```python
from openapi_client.models.recalculate_assignment_costs import RecalculateAssignmentCosts

# TODO update the JSON string below
json = "{}"
# create an instance of RecalculateAssignmentCosts from a JSON string
recalculate_assignment_costs_instance = RecalculateAssignmentCosts.from_json(json)
# print the JSON string representation of the object
print(RecalculateAssignmentCosts.to_json())

# convert the object into a dict
recalculate_assignment_costs_dict = recalculate_assignment_costs_instance.to_dict()
# create an instance of RecalculateAssignmentCosts from a dict
recalculate_assignment_costs_from_dict = RecalculateAssignmentCosts.from_dict(recalculate_assignment_costs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


