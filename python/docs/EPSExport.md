# EPSExport

EPS Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **bool** | Boolean flag that indicates whether the associated object is to be exported. The default value of the Include element is true. To exclude a business object from the XML export file, specify false in the Include element for that business object. | [optional] 
**var_field** | **List[str]** | List of Fields for EPS Business Object | [optional] 

## Example

```python
from openapi_client.models.eps_export import EPSExport

# TODO update the JSON string below
json = "{}"
# create an instance of EPSExport from a JSON string
eps_export_instance = EPSExport.from_json(json)
# print the JSON string representation of the object
print(EPSExport.to_json())

# convert the object into a dict
eps_export_dict = eps_export_instance.to_dict()
# create an instance of EPSExport from a dict
eps_export_from_dict = EPSExport.from_dict(eps_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


