# ProjectDeployment

ProjectDeployment Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_name** | **str** |  | [optional] 
**deployment_object_id** | **int** |  | [optional] 
**object_id** | **int** |  | [optional] 
**project_object_id** | **int** |  | [optional] 
**provider_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.project_deployment import ProjectDeployment

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDeployment from a JSON string
project_deployment_instance = ProjectDeployment.from_json(json)
# print the JSON string representation of the object
print(ProjectDeployment.to_json())

# convert the object into a dict
project_deployment_dict = project_deployment_instance.to_dict()
# create an instance of ProjectDeployment from a dict
project_deployment_from_dict = ProjectDeployment.from_dict(project_deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


