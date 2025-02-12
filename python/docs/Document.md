# Document

Document Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_object_id** | **int** |  | [optional] 
**author** | **str** | The person who created the work product or document. | [optional] 
**content_repository_document_internal_id** | **str** | The internal ID of the content repository document. | [optional] 
**create_date** | **datetime** | The date this document was created. | [optional] 
**create_user** | **str** | The name of the user that created this document. | [optional] 
**deliverable** | **bool** | The flag that indicates that the work product or document is a project deliverable. | [optional] 
**description** | **str** | The narrative description of the work product or document. | [optional] 
**document_category_name** | **str** | The name of the associated document category. | [optional] 
**document_category_object_id** | **int** | The unique ID of the associated document category. | [optional] 
**document_status_code_name** | **str** | The name of the associated document status code. | [optional] 
**document_status_code_object_id** | **int** | The unique ID of the associated document status code. | [optional] 
**document_type** | **str** | The type of document: &#39;Non-Collaboration&#39; or &#39;Collaboration&#39;. | [optional] 
**guid** | **str** | The globally unique ID generated by the system. | [optional] 
**is_baseline** | **bool** | The boolean value indicating if this business object is related to a Project or Baseline | [optional] 
**is_template** | **bool** | The boolean value indicating if this business object is related to a template Project. | [optional] 
**last_update_date** | **datetime** | The date this document was last updated. | [optional] 
**last_update_user** | **str** | The name of the user that last updated this document. | [optional] 
**object_id** | **int** | The unique ID generated by the system. | [optional] 
**parent_object_id** | **int** | The unique ID of the parent document of this document in the hierarchy. | [optional] 
**private_location** | **str** | The work product or document&#39;s private file location. | [optional] 
**project_id** | **str** | The short code that uniquely identifies the project. | [optional] 
**project_object_id** | **int** | The unique ID of the associated project. | 
**public_location** | **str** | The work product or document&#39;s publicly-accessible file location. | [optional] 
**reference_number** | **str** | The work product or document&#39;s reference or catalog number. | [optional] 
**resource_id** | **str** | The short code that uniquely identifies the associated resource. | [optional] 
**resource_name** | **str** | The name of the associated resource. | [optional] 
**resource_object_id** | **int** | The unique ID of the associated resource. | [optional] 
**revision_date** | **datetime** | The date of the work product or document&#39;s last update. | [optional] 
**sequence_number** | **int** | The sequence number for sorting. | [optional] 
**title** | **str** | The title or name of a project work product or document. | 
**version** | **str** | The work product or document&#39;s version number. | [optional] 

## Example

```python
from openapi_client.models.document import Document

# TODO update the JSON string below
json = "{}"
# create an instance of Document from a JSON string
document_instance = Document.from_json(json)
# print the JSON string representation of the object
print(Document.to_json())

# convert the object into a dict
document_dict = document_instance.to_dict()
# create an instance of Document from a dict
document_from_dict = Document.from_dict(document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


