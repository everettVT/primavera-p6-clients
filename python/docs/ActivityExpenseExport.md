# ActivityExpenseExport

ActivityExpense Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **bool** | Boolean flag that indicates whether the associated object is to be exported. The default value of the Include element is true. To exclude a business object from the XML export file, specify false in the Include element for that business object. | [optional] 
**var_field** | **List[str]** | ActivityExpenseFieldType: List of Fields for ActivityExpense Business Object | [optional] 

## Example

```python
from openapi_client.models.activity_expense_export import ActivityExpenseExport

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityExpenseExport from a JSON string
activity_expense_export_instance = ActivityExpenseExport.from_json(json)
# print the JSON string representation of the object
print(ActivityExpenseExport.to_json())

# convert the object into a dict
activity_expense_export_dict = activity_expense_export_instance.to_dict()
# create an instance of ActivityExpenseExport from a dict
activity_expense_export_from_dict = ActivityExpenseExport.from_dict(activity_expense_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


