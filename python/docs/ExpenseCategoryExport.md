# ExpenseCategoryExport

ExpenseCategory Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **bool** | Boolean flag that indicates whether the associated object is to be exported. The default value of the Include element is true. To exclude a business object from the XML export file, specify false in the Include element for that business object. | [optional] 
**var_field** | **List[str]** | List of Fields for ExpenseCategory Business Object | [optional] 

## Example

```python
from openapi_client.models.expense_category_export import ExpenseCategoryExport

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseCategoryExport from a JSON string
expense_category_export_instance = ExpenseCategoryExport.from_json(json)
# print the JSON string representation of the object
print(ExpenseCategoryExport.to_json())

# convert the object into a dict
expense_category_export_dict = expense_category_export_instance.to_dict()
# create an instance of ExpenseCategoryExport from a dict
expense_category_export_from_dict = ExpenseCategoryExport.from_dict(expense_category_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


