# RiskMatrixThreshold

RiskMatrixThreshold Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_date** | **datetime** | The date this risk matrix score type was created. | [optional] 
**create_user** | **str** | The name of the user that created the risk matrix score type. | [optional] 
**last_update_date** | **datetime** | The date this risk matrix score type was last updated. | [optional] 
**last_update_user** | **str** | The name of the user that last updated the risk matrix score type. | [optional] 
**risk_matrix_name** | **str** | The name of the associated Risk Matrix. | [optional] 
**risk_matrix_object_id** | **int** | The unique ID of the associated Risk Matrix. | 
**risk_threshold_name** | **str** | The name of the associated Risk Threshold. | [optional] 
**risk_threshold_object_id** | **int** | The unique ID of the associated Risk Threshold. | 

## Example

```python
from openapi_client.models.risk_matrix_threshold import RiskMatrixThreshold

# TODO update the JSON string below
json = "{}"
# create an instance of RiskMatrixThreshold from a JSON string
risk_matrix_threshold_instance = RiskMatrixThreshold.from_json(json)
# print the JSON string representation of the object
print(RiskMatrixThreshold.to_json())

# convert the object into a dict
risk_matrix_threshold_dict = risk_matrix_threshold_instance.to_dict()
# create an instance of RiskMatrixThreshold from a dict
risk_matrix_threshold_from_dict = RiskMatrixThreshold.from_dict(risk_matrix_threshold_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


