# RiskMatrixThresholdExport

RiskMatrixThreshold Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **bool** | Boolean flag that indicates whether the associated object is to be exported. The default value of the Include element is true. To exclude a business object from the XML export file, specify false in the Include element for that business object. | [optional] 
**var_field** | **List[str]** | List of Fields for RiskMatrixThreshold Business Object | [optional] 

## Example

```python
from openapi_client.models.risk_matrix_threshold_export import RiskMatrixThresholdExport

# TODO update the JSON string below
json = "{}"
# create an instance of RiskMatrixThresholdExport from a JSON string
risk_matrix_threshold_export_instance = RiskMatrixThresholdExport.from_json(json)
# print the JSON string representation of the object
print(RiskMatrixThresholdExport.to_json())

# convert the object into a dict
risk_matrix_threshold_export_dict = risk_matrix_threshold_export_instance.to_dict()
# create an instance of RiskMatrixThresholdExport from a dict
risk_matrix_threshold_export_from_dict = RiskMatrixThresholdExport.from_dict(risk_matrix_threshold_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


