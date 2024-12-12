# FinancialPeriodExport

FinancialPeriod Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **bool** | Boolean flag that indicates whether the associated object is to be exported. The default value of the Include element is true. To exclude a business object from the XML export file, specify false in the Include element for that business object. | [optional] 
**var_field** | **List[str]** | List of Fields for FinancialPeriod Business Object | [optional] 

## Example

```python
from openapi_client.models.financial_period_export import FinancialPeriodExport

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialPeriodExport from a JSON string
financial_period_export_instance = FinancialPeriodExport.from_json(json)
# print the JSON string representation of the object
print(FinancialPeriodExport.to_json())

# convert the object into a dict
financial_period_export_dict = financial_period_export_instance.to_dict()
# create an instance of FinancialPeriodExport from a dict
financial_period_export_from_dict = FinancialPeriodExport.from_dict(financial_period_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


