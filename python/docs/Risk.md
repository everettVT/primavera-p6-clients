# Risk

Risk Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cause** | **str** | The description of the cause of the Risk. | [optional] 
**cost_threshold_id** | **int** |  | [optional] 
**create_date** | **datetime** | The date this risk was created. | [optional] 
**create_user** | **str** | The name of the user that created the risk. | [optional] 
**description** | **str** | The description of the Risk. | [optional] 
**effect** | **str** | The description of the risks effect on the project. | [optional] 
**exposure** | **float** | The calculated exposure value for the risk. | [optional] 
**exposure_finish_date** | **datetime** | The calculated date the exposure finishes for the risk. | [optional] 
**exposure_start_date** | **datetime** | The calculated date the exposure starts for the risk. | [optional] 
**id** | **str** | The ID of the Risk. Must be unique within a project. | 
**identified_by_resource_id** | **str** | The short code of the resource that identified the risk. | [optional] 
**identified_by_resource_name** | **str** | The name of the resource that identified the risk. | [optional] 
**identified_by_resource_object_id** | **int** | The unique ID of the resource that identified the risk. | [optional] 
**identified_date** | **datetime** | The date this risk was identified. | [optional] 
**impact_threshold_values** | **int** |  | [optional] 
**is_baseline** | **bool** | The boolean value indicating if this business object is related to a Project or Baseline. | [optional] 
**is_template** | **bool** | The boolean value indicating if this business object is related to a template Project. | [optional] 
**last_update_date** | **datetime** | The date this risk was last updated. | [optional] 
**last_update_user** | **str** | The name of the user that last updated the risk. | [optional] 
**name** | **str** | The name of the Risk. Does not need to be unique. | [optional] 
**note** | **str** | The comments associated with the Risk. | [optional] 
**object_id** | **int** | The unique ID generated by the system. | [optional] 
**probability_threshold_id** | **int** |  | [optional] 
**project_id** | **str** | The short name of the associated project. | [optional] 
**project_name** | **str** | The name of the associated project. | [optional] 
**project_object_id** | **int** | The unique ID of the associated project. | 
**resource_id** | **str** | The ID of the resource who owns the Risk. The owner of the Risk is responsible for resolving the Risk. | [optional] 
**resource_name** | **str** | The name of the resource who owns the Risk. The owner of the Risk is responsible for resolving the Risk. | [optional] 
**resource_object_id** | **int** | The unique ID of the associated resource. | [optional] 
**response_total_cost** | **float** | The total estimated cost for the risk. If the risk has an associated response plan, the cost is calculated from the risk response actions for the response plan. Not available if user does not have View Project Costs-Financial privilege. | [optional] 
**risk_category_name** | **str** | The name of the category to which the Risk is assigned. e.g. Weather, Health, Legal etc. A Risk can only be associated with a single category. | [optional] 
**risk_category_object_id** | **int** | The unique ID of the category to which the Risk is assigned. e.g. Weather, Health, Legal etc. A Risk can only be associated with a single category. | [optional] 
**schedule_threshold_id** | **int** |  | [optional] 
**score** | **int** | The calculated score value of the impact values assigned to the risk. | [optional] 
**score_color** | **str** | The color of the tolerance threshold for the score value. | [optional] 
**score_text** | **str** | The calculated score text value of the impact values assigned to the risk. | [optional] 
**status** | **str** | The current status of the Risk. Valid values are &#39;Proposed&#39;, &#39;Open&#39;, &#39;Rejected&#39;, &#39;Managed&#39;, and &#39;Impacted&#39;. | [optional] 
**type** | **str** | The type of the risk. Valid values are &#39;Threat&#39; and &#39;Opportunity&#39;. | [optional] 

## Example

```python
from openapi_client.models.risk import Risk

# TODO update the JSON string below
json = "{}"
# create an instance of Risk from a JSON string
risk_instance = Risk.from_json(json)
# print the JSON string representation of the object
print(Risk.to_json())

# convert the object into a dict
risk_dict = risk_instance.to_dict()
# create an instance of Risk from a dict
risk_from_dict = Risk.from_dict(risk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

