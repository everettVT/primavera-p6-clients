# FinancialPeriod

FinancialPeriod Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_date** | **datetime** | The date this financial period was created. | [optional] 
**create_user** | **str** | The name of the user that created this financial period. | [optional] 
**end_date** | **datetime** | The end date of the period. | 
**financial_period_template_id** | **int** |  | [optional] 
**last_update_date** | **datetime** | The date this financial period was last updated. | [optional] 
**last_update_user** | **str** | The name of the user that last updated this financial period. | [optional] 
**name** | **str** | The name of the financial period. | 
**object_id** | **int** | The unique ID generated by the system. | [optional] 
**start_date** | **datetime** | The start date of the period. | 

## Example

```python
from openapi_client.models.financial_period import FinancialPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialPeriod from a JSON string
financial_period_instance = FinancialPeriod.from_json(json)
# print the JSON string representation of the object
print(FinancialPeriod.to_json())

# convert the object into a dict
financial_period_dict = financial_period_instance.to_dict()
# create an instance of FinancialPeriod from a dict
financial_period_from_dict = FinancialPeriod.from_dict(financial_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


