# GlobalReplace

GlobalReplace Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_projects** | **bool** | The option used to set all of projects to which a user has access. | [optional] 
**global_replace_data** | **str** | The Global Replace template. | [optional] 
**global_replace_name** | **str** | The Global Replace template name. | [optional] 
**greplace_object_id** | **int** | The unique id of the Global Replace template. | [optional] 
**project_id_name** | **str** | Project ids and names that are separated by commas. | [optional] 
**project_ids** | **str** | TProject ids that are separated by commas. | [optional] 
**replace_field_name_one** | **str** | First field name the user has selected to replace. | [optional] 
**search_criteria** | **str** | The criteria that is used to search and load business objects. | [optional] 
**subject_area_type** | **str** | The name of the object to be updated. | [optional] 
**user_object_id** | **int** | The unique id of the associated user. | [optional] 

## Example

```python
from openapi_client.models.global_replace import GlobalReplace

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalReplace from a JSON string
global_replace_instance = GlobalReplace.from_json(json)
# print the JSON string representation of the object
print(GlobalReplace.to_json())

# convert the object into a dict
global_replace_dict = global_replace_instance.to_dict()
# create an instance of GlobalReplace from a dict
global_replace_from_dict = GlobalReplace.from_dict(global_replace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


