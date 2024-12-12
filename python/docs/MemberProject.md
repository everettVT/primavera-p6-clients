# MemberProject

MemberProject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**object_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.member_project import MemberProject

# TODO update the JSON string below
json = "{}"
# create an instance of MemberProject from a JSON string
member_project_instance = MemberProject.from_json(json)
# print the JSON string representation of the object
print(MemberProject.to_json())

# convert the object into a dict
member_project_dict = member_project_instance.to_dict()
# create an instance of MemberProject from a dict
member_project_from_dict = MemberProject.from_dict(member_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


