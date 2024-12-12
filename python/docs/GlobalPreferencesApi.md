# openapi_client.GlobalPreferencesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_global_preference_field_length**](GlobalPreferencesApi.md#get_global_preference_field_length) | **GET** /globalPreferences/getFieldLength/{fieldName} | View GlobalPreferences Field Length
[**get_global_preference_fields**](GlobalPreferencesApi.md#get_global_preference_fields) | **GET** /globalPreferences/fields | View GlobalPreferences fields
[**get_global_preferences**](GlobalPreferencesApi.md#get_global_preferences) | **GET** /globalPreferences | Read GlobalPreferences
[**update_global_preference**](GlobalPreferencesApi.md#update_global_preference) | **PUT** /globalPreferences | Update GlobalPreferences


# **get_global_preference_field_length**
> str get_global_preference_field_length(field_name, authorization=authorization)

View GlobalPreferences Field Length

Send a request to this endpoint to load length of variable character fields for a BO.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GlobalPreferencesApi(api_client)
    field_name = 'field_name_example' # str | An project field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View GlobalPreferences Field Length
        api_response = api_instance.get_global_preference_field_length(field_name, authorization=authorization)
        print("The response of GlobalPreferencesApi->get_global_preference_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalPreferencesApi->get_global_preference_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An project field. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_global_preference_fields**
> str get_global_preference_fields()

View GlobalPreferences fields

Send a request to this endpoint to load length of variable character fields for a BO.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GlobalPreferencesApi(api_client)

    try:
        # View GlobalPreferences fields
        api_response = api_instance.get_global_preference_fields()
        print("The response of GlobalPreferencesApi->get_global_preference_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalPreferencesApi->get_global_preference_fields: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_global_preferences**
> List[GlobalPreferences] get_global_preferences(fields, filter=filter, order_by=order_by, authorization=authorization)

Read GlobalPreferences

Reads GlobalPreferences objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.global_preferences import GlobalPreferences
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GlobalPreferencesApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read GlobalPreferences
        api_response = api_instance.get_global_preferences(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of GlobalPreferencesApi->get_global_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalPreferencesApi->get_global_preferences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[GlobalPreferences]**](GlobalPreferences.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_global_preference**
> bool update_global_preference(global_preferences, authorization=authorization)

Update GlobalPreferences

Send a request to this endpoint to update one or more GlobalPreferences. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.global_preferences import GlobalPreferences
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GlobalPreferencesApi(api_client)
    global_preferences = [openapi_client.GlobalPreferences()] # List[GlobalPreferences] | A list of GlobalPreferences objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update GlobalPreferences
        api_response = api_instance.update_global_preference(global_preferences, authorization=authorization)
        print("The response of GlobalPreferencesApi->update_global_preference:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalPreferencesApi->update_global_preference: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **global_preferences** | [**List[GlobalPreferences]**](GlobalPreferences.md)| A list of GlobalPreferences objects. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

