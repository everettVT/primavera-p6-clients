# EPSNote

EPSNote Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_date** | **datetime** | The date this EPS Note was created. | [optional] 
**create_user** | **str** | The name of the user that created this EPS Note. | [optional] 
**epsid** | **str** | The short code assigned to the associated EPS. | [optional] 
**eps_name** | **str** | The name of the EPS element associated with this note. | [optional] 
**eps_object_id** | **int** | The unique ID of the associated EPS. | 
**note** | **str** | The information that is associated with the notebook topic. | [optional] 
**last_update_date** | **datetime** | The date this EPS Note was last updated. | [optional] 
**last_update_user** | **str** | The name of the user that last updated this EPS Note. | [optional] 
**notebook_topic_name** | **str** | The name of the associated notebook topic. | [optional] 
**notebook_topic_object_id** | **int** | The unique ID of the associated notebook topic. | 
**object_id** | **int** | The unique ID generated by the system. | [optional] 
**raw_text_note** | **str** | The information that is associated with the notebook topic, without any HTML. | [optional] 

## Example

```python
from openapi_client.models.eps_note import EPSNote

# TODO update the JSON string below
json = "{}"
# create an instance of EPSNote from a JSON string
eps_note_instance = EPSNote.from_json(json)
# print the JSON string representation of the object
print(EPSNote.to_json())

# convert the object into a dict
eps_note_dict = eps_note_instance.to_dict()
# create an instance of EPSNote from a dict
eps_note_from_dict = EPSNote.from_dict(eps_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


