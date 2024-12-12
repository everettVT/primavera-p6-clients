# ProjectResourceQuantity

ProjectResourceQuantity Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**committed_flag** | **bool** | The Boolean value that determines whether a resource is committed, and so, the resource assignment is stable and unlikely to change. When calculating availability, Primavera considers only assignments that are marked as committed. | [optional] 
**create_date** | **datetime** | The date this project resource quantity was created. | [optional] 
**create_user** | **str** | The name of the user that created this project resource quantity. | [optional] 
**financial_period1_object_id** | **int** | The unique ID of the associated first financial period for this project resource quantity. | [optional] 
**financial_period1_quantity** | **float** | The value that represents the resource allocation hours for the first financial period for this project resource quantity. If the week contains days from two different months, two ProjectResourceQuantity business objects will exist. The first business object&#39;s Quantity field represents the hours of the first week fragment (WeekStartDate and MonthStartDate have the same month value). The second business object&#39;s Quantity field represents the second week fragment (WeekStartDate and MonthStartDate have different month values). | 
**financial_period2_object_id** | **int** | The unique ID of the associated second financial period for this project resource quantity. | [optional] 
**financial_period2_quantity** | **float** | The value that represents the resource allocation hours for the second financial period for this project resource quantity. If the week contains days from two different months, two ProjectResourceQuantity business objects will exist. The first business object&#39;s Quantity field represents the hours of the first week fragment (WeekStartDate and MonthStartDate have the same month value). The second business object&#39;s Quantity field represents the second week fragment (WeekStartDate and MonthStartDate have different month values). | 
**financial_period_tmpl_id** | **int** |  | [optional] 
**is_baseline** | **bool** | The boolean value indicating if this business object is related to a Project or Baseline | [optional] 
**is_template** | **bool** | The boolean value indicating if this business object is related to a template Project. | [optional] 
**last_update_date** | **datetime** | The date this project resource quantity was last updated. | [optional] 
**last_update_user** | **str** | The name of the user that last updated this project resource quantity. | [optional] 
**month_start_date** | **datetime** | The date value that represents the first day of the month. If the week contains days from two different months, two objects will exist. The first ProjectResourceQuantity object&#39;s MonthStartDate is the first day of the month for the first week fragment. The second ProjectResourceQuantity object&#39;s MonthStartDate is the first day of the month for the second week fragment. | [optional] 
**project_object_id** | **int** | The unique ID of the associated project. | [optional] 
**project_resource_object_id** | **int** | The unique ID of the associated project resource. | 
**quantity** | **float** | The value that represents the resource allocation hours per week for this project resource quantity. If the week contains days from two different months, two ProjectResourceQuantity business objects will exist. The first business object&#39;s Quantity field represents the hours of the first week fragment (WeekStartDate and MonthStartDate have the same month value). The second business object&#39;s Quantity field represents the second week fragment (WeekStartDate and MonthStartDate have different month values). | 
**resource_object_id** | **int** | The unique ID of the associated resource. | [optional] 
**role_object_id** | **int** | The unique ID of the associated role. | [optional] 
**wbs_object_id** | **int** | The unique ID of the associated WBS. | [optional] 
**week_start_date** | **datetime** | The date value that represents the first day of the week. | 

## Example

```python
from openapi_client.models.project_resource_quantity import ProjectResourceQuantity

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectResourceQuantity from a JSON string
project_resource_quantity_instance = ProjectResourceQuantity.from_json(json)
# print the JSON string representation of the object
print(ProjectResourceQuantity.to_json())

# convert the object into a dict
project_resource_quantity_dict = project_resource_quantity_instance.to_dict()
# create an instance of ProjectResourceQuantity from a dict
project_resource_quantity_from_dict = ProjectResourceQuantity.from_dict(project_resource_quantity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


