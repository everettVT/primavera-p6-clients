# CreateRiskMatrixThresholdResponse

CreateRiskMatrixThresholdResponse Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**risk_matrix_object_id** | **int** | The unique ID of the associated Risk Matrix. | [optional] 
**risk_threshold_object_id** | **int** | The unique ID of the associated Risk Threshold. | [optional] 

## Example

```python
from openapi_client.models.create_risk_matrix_threshold_response import CreateRiskMatrixThresholdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRiskMatrixThresholdResponse from a JSON string
create_risk_matrix_threshold_response_instance = CreateRiskMatrixThresholdResponse.from_json(json)
# print the JSON string representation of the object
print(CreateRiskMatrixThresholdResponse.to_json())

# convert the object into a dict
create_risk_matrix_threshold_response_dict = create_risk_matrix_threshold_response_instance.to_dict()
# create an instance of CreateRiskMatrixThresholdResponse from a dict
create_risk_matrix_threshold_response_from_dict = CreateRiskMatrixThresholdResponse.from_dict(create_risk_matrix_threshold_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


