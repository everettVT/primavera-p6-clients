# RiskImpact

RiskImpact Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_date** | **datetime** | The date this risk impact was created. | [optional] 
**create_user** | **str** | The name of the user that created the risk impact. | [optional] 
**is_baseline** | **bool** | The boolean value indicating if this business object is related to a Project or Baseline. | [optional] 
**is_template** | **bool** | The boolean value indicating if this business object is related to a template Project. | [optional] 
**last_update_date** | **datetime** | The date this risk impact was last updated. | [optional] 
**last_update_user** | **str** | The name of the user that last updated the risk impact. | [optional] 
**project_id** | **str** | The short name of the associated project. | [optional] 
**project_name** | **str** | The name of the associated project. | [optional] 
**project_object_id** | **int** | The unique ID of the associated project. | [optional] 
**risk_id** | **str** | The ID of the Risk. Must be unique within a project. | [optional] 
**risk_name** | **str** | The name of the Risk. Does not need to be unique. | [optional] 
**risk_object_id** | **int** | The unique ID of the associated risk. | 
**risk_threshold_level_code** | **str** | The 10 character short name for the threshold level. Must be unique. | [optional] 
**risk_threshold_level_name** | **str** | The 40 character name for the threshold level. Does not need to be unique. | [optional] 
**risk_threshold_level_object_id** | **int** | The unique ID of the associated Risk Threshold. | 
**risk_threshold_name** | **str** | The name of the associated risk score type. | [optional] 
**risk_threshold_object_id** | **int** | The unique ID of the associated Risk Threshold Type. | [optional] 

## Example

```python
from openapi_client.models.risk_impact import RiskImpact

# TODO update the JSON string below
json = "{}"
# create an instance of RiskImpact from a JSON string
risk_impact_instance = RiskImpact.from_json(json)
# print the JSON string representation of the object
print(RiskImpact.to_json())

# convert the object into a dict
risk_impact_dict = risk_impact_instance.to_dict()
# create an instance of RiskImpact from a dict
risk_impact_from_dict = RiskImpact.from_dict(risk_impact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


