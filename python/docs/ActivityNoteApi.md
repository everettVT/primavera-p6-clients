# openapi_client.ActivityNoteApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_activity_notes**](ActivityNoteApi.md#create_activity_notes) | **POST** /activityNote | Create ActivityNotes
[**delete_activity_notes**](ActivityNoteApi.md#delete_activity_notes) | **DELETE** /activityNote | Delete ActivityNotes
[**get_activity_notes**](ActivityNoteApi.md#get_activity_notes) | **GET** /activityNote | Read ActivityNotes
[**get_activity_notes_field_length**](ActivityNoteApi.md#get_activity_notes_field_length) | **GET** /activityNote/getFieldLength/{fieldName} | View ActivityNote Field Length
[**get_activity_notes_fields**](ActivityNoteApi.md#get_activity_notes_fields) | **GET** /activityNote/fields | View ActivityNote fields
[**put_activity_notes**](ActivityNoteApi.md#put_activity_notes) | **PUT** /activityNote | Update ActivityNotes


# **create_activity_notes**
> str create_activity_notes(activity_note, authorization=authorization)

Create ActivityNotes

Send a request to this endpoint to create one or more activityNode. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.activity_note import ActivityNote
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
    api_instance = openapi_client.ActivityNoteApi(api_client)
    activity_note = [openapi_client.ActivityNote()] # List[ActivityNote] | A list of activityNode objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ActivityNotes
        api_response = api_instance.create_activity_notes(activity_note, authorization=authorization)
        print("The response of ActivityNoteApi->create_activity_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNoteApi->create_activity_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_note** | [**List[ActivityNote]**](ActivityNote.md)| A list of activityNode objects. | 
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

# **delete_activity_notes**
> bool delete_activity_notes(authorization=authorization, object_id=object_id)

Delete ActivityNotes

Send a request to this endpoint to delete one or more activityNode. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.ActivityNoteApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of activityNode. (optional)

    try:
        # Delete ActivityNotes
        api_response = api_instance.delete_activity_notes(authorization=authorization, object_id=object_id)
        print("The response of ActivityNoteApi->delete_activity_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNoteApi->delete_activity_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| One or more system-generated identifiers of activityNode. | [optional] 

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

# **get_activity_notes**
> List[ActivityNote] get_activity_notes(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ActivityNotes

Reads ActivityNote objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.activity_note import ActivityNote
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
    api_instance = openapi_client.ActivityNoteApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ActivityNotes
        api_response = api_instance.get_activity_notes(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ActivityNoteApi->get_activity_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNoteApi->get_activity_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ActivityNote]**](ActivityNote.md)

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

# **get_activity_notes_field_length**
> str get_activity_notes_field_length(field_name, authorization=authorization)

View ActivityNote Field Length

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
    api_instance = openapi_client.ActivityNoteApi(api_client)
    field_name = 'field_name_example' # str | An activityNote field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ActivityNote Field Length
        api_response = api_instance.get_activity_notes_field_length(field_name, authorization=authorization)
        print("The response of ActivityNoteApi->get_activity_notes_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNoteApi->get_activity_notes_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An activityNote field. | 
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

# **get_activity_notes_fields**
> str get_activity_notes_fields()

View ActivityNote fields

Send a request to this endpoint to load all the fields for a BO.

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
    api_instance = openapi_client.ActivityNoteApi(api_client)

    try:
        # View ActivityNote fields
        api_response = api_instance.get_activity_notes_fields()
        print("The response of ActivityNoteApi->get_activity_notes_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNoteApi->get_activity_notes_fields: %s\n" % e)
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

# **put_activity_notes**
> bool put_activity_notes(activity_note, authorization=authorization)

Update ActivityNotes

Send a request to this endpoint to update one or more activityNode. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.activity_note import ActivityNote
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
    api_instance = openapi_client.ActivityNoteApi(api_client)
    activity_note = [openapi_client.ActivityNote()] # List[ActivityNote] | A list of activityNode objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ActivityNotes
        api_response = api_instance.put_activity_notes(activity_note, authorization=authorization)
        print("The response of ActivityNoteApi->put_activity_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityNoteApi->put_activity_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_note** | [**List[ActivityNote]**](ActivityNote.md)| A list of activityNode objects. | 
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

