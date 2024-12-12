# CreateRiskResponseActionImpactResponse

CreateRiskResponseActionImpactResponse Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**risk_response_action_object_id** | **int** | The unique ID of the RiskResponseAction. | [optional] 
**risk_threshold_object_id** | **int** | The unique ID of the associated Risk Threshold. | [optional] 

## Example

```python
from openapi_client.models.create_risk_response_action_impact_response import CreateRiskResponseActionImpactResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRiskResponseActionImpactResponse from a JSON string
create_risk_response_action_impact_response_instance = CreateRiskResponseActionImpactResponse.from_json(json)
# print the JSON string representation of the object
print(CreateRiskResponseActionImpactResponse.to_json())

# convert the object into a dict
create_risk_response_action_impact_response_dict = create_risk_response_action_impact_response_instance.to_dict()
# create an instance of CreateRiskResponseActionImpactResponse from a dict
create_risk_response_action_impact_response_from_dict = CreateRiskResponseActionImpactResponse.from_dict(create_risk_response_action_impact_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


