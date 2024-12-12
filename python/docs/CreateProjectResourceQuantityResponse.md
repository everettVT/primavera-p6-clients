# CreateProjectResourceQuantityResponse

CreateProjectResourceQuantityResponse Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_resource_object_id** | **int** | The unique ID of the associated project resource. | [optional] 
**week_start_date** | **str** | The date value that represents the first day of the week. | [optional] 
**month_start_date** | **str** | The value that represents the resource allocation hours per week for this project resource quantity. If the week contains days from two different months, two ProjectResourceQuantity business objects will exist. The first business object&#39;s Quantity field represents the hours of the first week fragment (WeekStartDate and MonthStartDate have the same month value). The second business object&#39;s Quantity field represents the second week fragment (WeekStartDate and MonthStartDate have different month values). | [optional] 

## Example

```python
from openapi_client.models.create_project_resource_quantity_response import CreateProjectResourceQuantityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectResourceQuantityResponse from a JSON string
create_project_resource_quantity_response_instance = CreateProjectResourceQuantityResponse.from_json(json)
# print the JSON string representation of the object
print(CreateProjectResourceQuantityResponse.to_json())

# convert the object into a dict
create_project_resource_quantity_response_dict = create_project_resource_quantity_response_instance.to_dict()
# create an instance of CreateProjectResourceQuantityResponse from a dict
create_project_resource_quantity_response_from_dict = CreateProjectResourceQuantityResponse.from_dict(create_project_resource_quantity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


