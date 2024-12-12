# CreateActivityRiskResponse

CreateActivityRiskResponse Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**risk_object_id** | **int** | The unique ID of the associated risk. | [optional] 
**activity_object_id** | **int** | The unique ID of the activity to which the risk is assigned. | [optional] 

## Example

```python
from openapi_client.models.create_activity_risk_response import CreateActivityRiskResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateActivityRiskResponse from a JSON string
create_activity_risk_response_instance = CreateActivityRiskResponse.from_json(json)
# print the JSON string representation of the object
print(CreateActivityRiskResponse.to_json())

# convert the object into a dict
create_activity_risk_response_dict = create_activity_risk_response_instance.to_dict()
# create an instance of CreateActivityRiskResponse from a dict
create_activity_risk_response_from_dict = CreateActivityRiskResponse.from_dict(create_activity_risk_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


