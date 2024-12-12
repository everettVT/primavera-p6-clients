# NotebookTopicExport

NotebookTopic Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **bool** | Boolean flag that indicates whether the associated object is to be exported. The default value of the Include element is true. To exclude a business object from the XML export file, specify false in the Include element for that business object. | [optional] 
**var_field** | **List[str]** | List of Fields for NotebookTopic Business Object | [optional] 

## Example

```python
from openapi_client.models.notebook_topic_export import NotebookTopicExport

# TODO update the JSON string below
json = "{}"
# create an instance of NotebookTopicExport from a JSON string
notebook_topic_export_instance = NotebookTopicExport.from_json(json)
# print the JSON string representation of the object
print(NotebookTopicExport.to_json())

# convert the object into a dict
notebook_topic_export_dict = notebook_topic_export_instance.to_dict()
# create an instance of NotebookTopicExport from a dict
notebook_topic_export_from_dict = NotebookTopicExport.from_dict(notebook_topic_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


