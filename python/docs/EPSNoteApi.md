# openapi_client.EPSNoteApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_eps_note**](EPSNoteApi.md#create_eps_note) | **POST** /epsNote | Create EPSNote
[**delete_eps_note**](EPSNoteApi.md#delete_eps_note) | **DELETE** /epsNote | Delete EPSNote
[**get_eps_note**](EPSNoteApi.md#get_eps_note) | **GET** /epsNote | Read EPSNote
[**get_eps_note_field_length**](EPSNoteApi.md#get_eps_note_field_length) | **GET** /epsNote/getFieldLength/{fieldName} | View EPSNote Field Length
[**get_eps_note_fields**](EPSNoteApi.md#get_eps_note_fields) | **GET** /epsNote/fields | View EPSNote fields
[**update_eps_note**](EPSNoteApi.md#update_eps_note) | **PUT** /epsNote | Update EPSNote


# **create_eps_note**
> str create_eps_note(eps_note, authorization=authorization)

Create EPSNote

Send a request to this endpoint to create one or more EPSNote. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.eps_note import EPSNote
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
    api_instance = openapi_client.EPSNoteApi(api_client)
    eps_note = [openapi_client.EPSNote()] # List[EPSNote] | A list of EPSNote objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create EPSNote
        api_response = api_instance.create_eps_note(eps_note, authorization=authorization)
        print("The response of EPSNoteApi->create_eps_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPSNoteApi->create_eps_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eps_note** | [**List[EPSNote]**](EPSNote.md)| A list of EPSNote objects. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource Created. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_eps_note**
> bool delete_eps_note(object_id, authorization=authorization)

Delete EPSNote

Send a request to this endpoint to delete one or more EPSNote. An application object will be created for each JSON object provided in the request body

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
    api_instance = openapi_client.EPSNoteApi(api_client)
    object_id = '1,2,3' # str | One or more system-generated identifiers of EPSNote.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete EPSNote
        api_response = api_instance.delete_eps_note(object_id, authorization=authorization)
        print("The response of EPSNoteApi->delete_eps_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPSNoteApi->delete_eps_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| One or more system-generated identifiers of EPSNote. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

**bool**

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

# **get_eps_note**
> List[EPSNote] get_eps_note(fields, filter=filter, order_by=order_by, authorization=authorization)

Read EPSNote

Reads EPSNote objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.eps_note import EPSNote
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
    api_instance = openapi_client.EPSNoteApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read EPSNote
        api_response = api_instance.get_eps_note(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of EPSNoteApi->get_eps_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPSNoteApi->get_eps_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[EPSNote]**](EPSNote.md)

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

# **get_eps_note_field_length**
> str get_eps_note_field_length(field_name, authorization=authorization)

View EPSNote Field Length

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
    api_instance = openapi_client.EPSNoteApi(api_client)
    field_name = 'field_name_example' # str | An EPSNote field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View EPSNote Field Length
        api_response = api_instance.get_eps_note_field_length(field_name, authorization=authorization)
        print("The response of EPSNoteApi->get_eps_note_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPSNoteApi->get_eps_note_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An EPSNote field. | 
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

# **get_eps_note_fields**
> str get_eps_note_fields()

View EPSNote fields

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
    api_instance = openapi_client.EPSNoteApi(api_client)

    try:
        # View EPSNote fields
        api_response = api_instance.get_eps_note_fields()
        print("The response of EPSNoteApi->get_eps_note_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPSNoteApi->get_eps_note_fields: %s\n" % e)
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

# **update_eps_note**
> bool update_eps_note(eps_note, authorization=authorization)

Update EPSNote

Send a request to this endpoint to update one or more EPSNote. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.eps_note import EPSNote
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
    api_instance = openapi_client.EPSNoteApi(api_client)
    eps_note = [openapi_client.EPSNote()] # List[EPSNote] | A list of EPSNote objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update EPSNote
        api_response = api_instance.update_eps_note(eps_note, authorization=authorization)
        print("The response of EPSNoteApi->update_eps_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPSNoteApi->update_eps_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eps_note** | [**List[EPSNote]**](EPSNote.md)| A list of EPSNote objects. | 
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

