# openapi_client.ProjectNoteApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_note**](ProjectNoteApi.md#create_project_note) | **POST** /projectNote | Create ProjectNote
[**delete_project_note**](ProjectNoteApi.md#delete_project_note) | **DELETE** /projectNote | Delete ProjectNote
[**get_project_note**](ProjectNoteApi.md#get_project_note) | **GET** /projectNote | Read ProjectNote
[**get_project_note_field_length**](ProjectNoteApi.md#get_project_note_field_length) | **GET** /projectNote/getFieldLength/{fieldName} | View ProjectNote Field Length
[**get_project_note_fields**](ProjectNoteApi.md#get_project_note_fields) | **GET** /projectNote/fields | View ProjectNote fields
[**update_project_note**](ProjectNoteApi.md#update_project_note) | **PUT** /projectNote | Update ProjectNote


# **create_project_note**
> str create_project_note(project_note, authorization=authorization)

Create ProjectNote

Send a request to this endpoint to create one or more ProjectNote. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.project_note import ProjectNote
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
    api_instance = openapi_client.ProjectNoteApi(api_client)
    project_note = [openapi_client.ProjectNote()] # List[ProjectNote] | A list of projectnote objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ProjectNote
        api_response = api_instance.create_project_note(project_note, authorization=authorization)
        print("The response of ProjectNoteApi->create_project_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectNoteApi->create_project_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_note** | [**List[ProjectNote]**](ProjectNote.md)| A list of projectnote objects. | 
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

# **delete_project_note**
> bool delete_project_note(object_id, authorization=authorization)

Delete ProjectNote

Send a request to this endpoint to delete one or more ProjectNote. An application object will be created for each JSON object provided in the request body.

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
    api_instance = openapi_client.ProjectNoteApi(api_client)
    object_id = '1,2,3' # str | One or more system-generated identifiers of projectnote.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete ProjectNote
        api_response = api_instance.delete_project_note(object_id, authorization=authorization)
        print("The response of ProjectNoteApi->delete_project_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectNoteApi->delete_project_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| One or more system-generated identifiers of projectnote. | 
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

# **get_project_note**
> List[ProjectNote] get_project_note(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ProjectNote

Reads ProjectNote objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.project_note import ProjectNote
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
    api_instance = openapi_client.ProjectNoteApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ProjectNote
        api_response = api_instance.get_project_note(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ProjectNoteApi->get_project_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectNoteApi->get_project_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ProjectNote]**](ProjectNote.md)

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

# **get_project_note_field_length**
> str get_project_note_field_length(field_name, authorization=authorization)

View ProjectNote Field Length

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
    api_instance = openapi_client.ProjectNoteApi(api_client)
    field_name = 'field_name_example' # str | An projectnote field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ProjectNote Field Length
        api_response = api_instance.get_project_note_field_length(field_name, authorization=authorization)
        print("The response of ProjectNoteApi->get_project_note_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectNoteApi->get_project_note_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An projectnote field. | 
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

# **get_project_note_fields**
> str get_project_note_fields()

View ProjectNote fields

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
    api_instance = openapi_client.ProjectNoteApi(api_client)

    try:
        # View ProjectNote fields
        api_response = api_instance.get_project_note_fields()
        print("The response of ProjectNoteApi->get_project_note_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectNoteApi->get_project_note_fields: %s\n" % e)
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

# **update_project_note**
> bool update_project_note(project_note, authorization=authorization)

Update ProjectNote

Send a request to this endpoint to update one or more ProjectNote. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.project_note import ProjectNote
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
    api_instance = openapi_client.ProjectNoteApi(api_client)
    project_note = [openapi_client.ProjectNote()] # List[ProjectNote] | A list of projectnote objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ProjectNote
        api_response = api_instance.update_project_note(project_note, authorization=authorization)
        print("The response of ProjectNoteApi->update_project_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectNoteApi->update_project_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_note** | [**List[ProjectNote]**](ProjectNote.md)| A list of projectnote objects. | 
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

