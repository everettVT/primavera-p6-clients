# openapi_client.DocumentStatusCodeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_document_status_code**](DocumentStatusCodeApi.md#create_document_status_code) | **POST** /documentStatusCode | Create DocumentStatusCode
[**delete_document_status_code**](DocumentStatusCodeApi.md#delete_document_status_code) | **DELETE** /documentStatusCode | Delete DocumentStatusCode
[**get_document_status_code**](DocumentStatusCodeApi.md#get_document_status_code) | **GET** /documentStatusCode | Read DocumentStatusCode
[**get_document_status_code_field_length**](DocumentStatusCodeApi.md#get_document_status_code_field_length) | **GET** /documentStatusCode/getFieldLength/{fieldName} | View DocumentStatusCode Field Length
[**get_document_status_code_fields**](DocumentStatusCodeApi.md#get_document_status_code_fields) | **GET** /documentStatusCode/fields | View DocumentStatusCode fields
[**update_document_status_code**](DocumentStatusCodeApi.md#update_document_status_code) | **PUT** /documentStatusCode | Update DocumentStatusCode


# **create_document_status_code**
> str create_document_status_code(document_status_code, authorization=authorization)

Create DocumentStatusCode

Send a request to this endpoint to create one or more DocumentStatusCode. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.document_status_code import DocumentStatusCode
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
    api_instance = openapi_client.DocumentStatusCodeApi(api_client)
    document_status_code = [openapi_client.DocumentStatusCode()] # List[DocumentStatusCode] | A list of documentstatuscode objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create DocumentStatusCode
        api_response = api_instance.create_document_status_code(document_status_code, authorization=authorization)
        print("The response of DocumentStatusCodeApi->create_document_status_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentStatusCodeApi->create_document_status_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_status_code** | [**List[DocumentStatusCode]**](DocumentStatusCode.md)| A list of documentstatuscode objects. | 
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

# **delete_document_status_code**
> bool delete_document_status_code(authorization=authorization, object_id=object_id)

Delete DocumentStatusCode

Send a request to this endpoint to delete one or more DocumentStatusCode. An application object will be created for each JSON object provided in the request body

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
    api_instance = openapi_client.DocumentStatusCodeApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of documentstatuscode. (optional)

    try:
        # Delete DocumentStatusCode
        api_response = api_instance.delete_document_status_code(authorization=authorization, object_id=object_id)
        print("The response of DocumentStatusCodeApi->delete_document_status_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentStatusCodeApi->delete_document_status_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| One or more system-generated identifiers of documentstatuscode. | [optional] 

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

# **get_document_status_code**
> List[DocumentStatusCode] get_document_status_code(fields, filter=filter, order_by=order_by, authorization=authorization)

Read DocumentStatusCode

Reads DocumentStatusCode objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.document_status_code import DocumentStatusCode
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
    api_instance = openapi_client.DocumentStatusCodeApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read DocumentStatusCode
        api_response = api_instance.get_document_status_code(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of DocumentStatusCodeApi->get_document_status_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentStatusCodeApi->get_document_status_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[DocumentStatusCode]**](DocumentStatusCode.md)

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

# **get_document_status_code_field_length**
> str get_document_status_code_field_length(field_name, authorization=authorization)

View DocumentStatusCode Field Length

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
    api_instance = openapi_client.DocumentStatusCodeApi(api_client)
    field_name = 'field_name_example' # str | An documentstatuscode field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View DocumentStatusCode Field Length
        api_response = api_instance.get_document_status_code_field_length(field_name, authorization=authorization)
        print("The response of DocumentStatusCodeApi->get_document_status_code_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentStatusCodeApi->get_document_status_code_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An documentstatuscode field. | 
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

# **get_document_status_code_fields**
> str get_document_status_code_fields()

View DocumentStatusCode fields

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
    api_instance = openapi_client.DocumentStatusCodeApi(api_client)

    try:
        # View DocumentStatusCode fields
        api_response = api_instance.get_document_status_code_fields()
        print("The response of DocumentStatusCodeApi->get_document_status_code_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentStatusCodeApi->get_document_status_code_fields: %s\n" % e)
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

# **update_document_status_code**
> bool update_document_status_code(document_status_code, authorization=authorization)

Update DocumentStatusCode

Send a request to this endpoint to update one or more DocumentStatusCode. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.document_status_code import DocumentStatusCode
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
    api_instance = openapi_client.DocumentStatusCodeApi(api_client)
    document_status_code = [openapi_client.DocumentStatusCode()] # List[DocumentStatusCode] | A list of documentstatuscode objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update DocumentStatusCode
        api_response = api_instance.update_document_status_code(document_status_code, authorization=authorization)
        print("The response of DocumentStatusCodeApi->update_document_status_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentStatusCodeApi->update_document_status_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_status_code** | [**List[DocumentStatusCode]**](DocumentStatusCode.md)| A list of documentstatuscode objects. | 
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

