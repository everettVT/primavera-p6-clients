# Location

Location Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** | The first line of the address with street number and street name. | [optional] 
**address_line2** | **str** | The second line of the address with street number and street name. | [optional] 
**city** | **str** | The city name of the address. | [optional] 
**country** | **str** | The country of the address. | [optional] 
**country_code** | **str** | The country code of the address. | [optional] 
**create_date** | **datetime** | The creation date of the Location. | [optional] 
**create_user** | **str** | The name of the user that created this location. | [optional] 
**last_update_date** | **datetime** | The date this location was last updated. | [optional] 
**last_update_user** | **str** | The name of the user that last updated this location. | [optional] 
**latitude** | **float** | The latitude of the address. | 
**longitude** | **float** | The longitude of the address. | 
**municipality** | **str** | The municipality name of the address. | [optional] 
**name** | **str** | The name of the location. | 
**object_id** | **int** | The unique ID of the location. | [optional] 
**postal_code** | **str** | The postal code of the address. | [optional] 
**state** | **str** | The state name of the address. | [optional] 
**state_code** | **str** | The state abbreviation of the address. | [optional] 

## Example

```python
from openapi_client.models.location import Location

# TODO update the JSON string below
json = "{}"
# create an instance of Location from a JSON string
location_instance = Location.from_json(json)
# print the JSON string representation of the object
print(Location.to_json())

# convert the object into a dict
location_dict = location_instance.to_dict()
# create an instance of Location from a dict
location_from_dict = Location.from_dict(location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


