# openapi_client.ProjectDocumentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_document**](ProjectDocumentApi.md#create_project_document) | **POST** /projectDocument | Create ProjectDocument
[**delete_project_document**](ProjectDocumentApi.md#delete_project_document) | **DELETE** /projectDocument | Delete ProjectDocument
[**get_project_document**](ProjectDocumentApi.md#get_project_document) | **GET** /projectDocument | Read ProjectDocument
[**get_project_document_field_length**](ProjectDocumentApi.md#get_project_document_field_length) | **GET** /projectDocument/getFieldLength/{fieldName} | View ProjectDocument Field Length
[**get_project_document_fields**](ProjectDocumentApi.md#get_project_document_fields) | **GET** /projectDocument/fields | View ProjectDocument fields
[**update_project_document**](ProjectDocumentApi.md#update_project_document) | **PUT** /projectDocument | Update ProjectDocument


# **create_project_document**
> str create_project_document(project_document, authorization=authorization)

Create ProjectDocument

Send a request to this endpoint to create one or more ProjectDocument. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.project_document import ProjectDocument
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
    api_instance = openapi_client.ProjectDocumentApi(api_client)
    project_document = [openapi_client.ProjectDocument()] # List[ProjectDocument] | A list of projectdocument objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ProjectDocument
        api_response = api_instance.create_project_document(project_document, authorization=authorization)
        print("The response of ProjectDocumentApi->create_project_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDocumentApi->create_project_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_document** | [**List[ProjectDocument]**](ProjectDocument.md)| A list of projectdocument objects. | 
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

# **delete_project_document**
> bool delete_project_document(object_id, authorization=authorization)

Delete ProjectDocument

Send a request to this endpoint to delete one or more ProjectDocument. An application object will be created for each JSON object provided in the request body

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
    api_instance = openapi_client.ProjectDocumentApi(api_client)
    object_id = '1,2,3' # str | One or more system-generated identifiers of projectdocument.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete ProjectDocument
        api_response = api_instance.delete_project_document(object_id, authorization=authorization)
        print("The response of ProjectDocumentApi->delete_project_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDocumentApi->delete_project_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| One or more system-generated identifiers of projectdocument. | 
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

# **get_project_document**
> List[ProjectDocument] get_project_document(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ProjectDocument

Reads ProjectDocument objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.project_document import ProjectDocument
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
    api_instance = openapi_client.ProjectDocumentApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ProjectDocument
        api_response = api_instance.get_project_document(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ProjectDocumentApi->get_project_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDocumentApi->get_project_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ProjectDocument]**](ProjectDocument.md)

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

# **get_project_document_field_length**
> str get_project_document_field_length(field_name, authorization=authorization)

View ProjectDocument Field Length

Returns Field length

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
    api_instance = openapi_client.ProjectDocumentApi(api_client)
    field_name = 'field_name_example' # str | An projectdocument field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ProjectDocument Field Length
        api_response = api_instance.get_project_document_field_length(field_name, authorization=authorization)
        print("The response of ProjectDocumentApi->get_project_document_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDocumentApi->get_project_document_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An projectdocument field. | 
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

# **get_project_document_fields**
> str get_project_document_fields()

View ProjectDocument fields

Returns ProjectDocument fields

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
    api_instance = openapi_client.ProjectDocumentApi(api_client)

    try:
        # View ProjectDocument fields
        api_response = api_instance.get_project_document_fields()
        print("The response of ProjectDocumentApi->get_project_document_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDocumentApi->get_project_document_fields: %s\n" % e)
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

# **update_project_document**
> bool update_project_document(project_document, authorization=authorization)

Update ProjectDocument

Send a request to this endpoint to update one or more ProjectDocument. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.project_document import ProjectDocument
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
    api_instance = openapi_client.ProjectDocumentApi(api_client)
    project_document = [openapi_client.ProjectDocument()] # List[ProjectDocument] | A list of projectdocument objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ProjectDocument
        api_response = api_instance.update_project_document(project_document, authorization=authorization)
        print("The response of ProjectDocumentApi->update_project_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDocumentApi->update_project_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_document** | [**List[ProjectDocument]**](ProjectDocument.md)| A list of projectdocument objects. | 
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

