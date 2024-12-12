# CreateResourceAssignmentPeriodActualsResponse

CreateResourceAssignmentPeriodActualsResponse Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**financial_period_object_id** | **int** | The unique ID of the associated financial period. | [optional] 
**resource_assignment_object_id** | **int** | The unique ID of the associated resource assignment. | [optional] 

## Example

```python
from openapi_client.models.create_resource_assignment_period_actuals_response import CreateResourceAssignmentPeriodActualsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateResourceAssignmentPeriodActualsResponse from a JSON string
create_resource_assignment_period_actuals_response_instance = CreateResourceAssignmentPeriodActualsResponse.from_json(json)
# print the JSON string representation of the object
print(CreateResourceAssignmentPeriodActualsResponse.to_json())

# convert the object into a dict
create_resource_assignment_period_actuals_response_dict = create_resource_assignment_period_actuals_response_instance.to_dict()
# create an instance of CreateResourceAssignmentPeriodActualsResponse from a dict
create_resource_assignment_period_actuals_response_from_dict = CreateResourceAssignmentPeriodActualsResponse.from_dict(create_resource_assignment_period_actuals_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


