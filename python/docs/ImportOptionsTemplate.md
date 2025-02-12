# ImportOptionsTemplate

ImportOptionsTemplate Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_options_template_type** | **str** | The content of the template. | [optional] 
**name** | **str** | The name of the template. | [optional] 
**object_id** | **int** | The unique ID generated by the system. | [optional] 
**view_data** | **str** | The content of the template. | [optional] 

## Example

```python
from openapi_client.models.import_options_template import ImportOptionsTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ImportOptionsTemplate from a JSON string
import_options_template_instance = ImportOptionsTemplate.from_json(json)
# print the JSON string representation of the object
print(ImportOptionsTemplate.to_json())

# convert the object into a dict
import_options_template_dict = import_options_template_instance.to_dict()
# create an instance of ImportOptionsTemplate from a dict
import_options_template_from_dict = ImportOptionsTemplate.from_dict(import_options_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


