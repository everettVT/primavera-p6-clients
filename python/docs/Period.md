# Period


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start of the time period that you are interested in. | [optional] 
**planned_units** | **float** | The planned units of work for the resource assignment on the activity. This field is named BudgetedUnits in Primavera&#39;s Engineering &amp; Construction and Maintenance &amp; Turnaround solutions. | [optional] 
**remaining_units** | **float** | The remaining units of work to be performed by this resource on this activity. Before the activity is started, the remaining units are the same as the planned units. After the activity is completed, the remaining units are zero. | [optional] 

## Example

```python
from openapi_client.models.period import Period

# TODO update the JSON string below
json = "{}"
# create an instance of Period from a JSON string
period_instance = Period.from_json(json)
# print the JSON string representation of the object
print(Period.to_json())

# convert the object into a dict
period_dict = period_instance.to_dict()
# create an instance of Period from a dict
period_from_dict = Period.from_dict(period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


