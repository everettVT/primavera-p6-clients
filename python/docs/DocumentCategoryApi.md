# openapi_client.DocumentCategoryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_document_category**](DocumentCategoryApi.md#create_document_category) | **POST** /documentCategory | Create DocumentCategory
[**delete_document_category**](DocumentCategoryApi.md#delete_document_category) | **DELETE** /documentCategory | Delete DocumentCategory
[**get_document_category**](DocumentCategoryApi.md#get_document_category) | **GET** /documentCategory | Read DocumentCategory
[**get_document_category_field_length**](DocumentCategoryApi.md#get_document_category_field_length) | **GET** /documentCategory/getFieldLength/{fieldName} | View DocumentCategory Field Length
[**get_document_category_fields**](DocumentCategoryApi.md#get_document_category_fields) | **GET** /documentCategory/fields | View DocumentCategory fields
[**update_document_category**](DocumentCategoryApi.md#update_document_category) | **PUT** /documentCategory | Update DocumentCategory


# **create_document_category**
> str create_document_category(document_category, authorization=authorization)

Create DocumentCategory

Send a request to this endpoint to create one or more DocumentCategory. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.document_category import DocumentCategory
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
    api_instance = openapi_client.DocumentCategoryApi(api_client)
    document_category = [openapi_client.DocumentCategory()] # List[DocumentCategory] | A list of documentcategory objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create DocumentCategory
        api_response = api_instance.create_document_category(document_category, authorization=authorization)
        print("The response of DocumentCategoryApi->create_document_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentCategoryApi->create_document_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_category** | [**List[DocumentCategory]**](DocumentCategory.md)| A list of documentcategory objects. | 
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

# **delete_document_category**
> bool delete_document_category(authorization=authorization, object_id=object_id)

Delete DocumentCategory

Send a request to this endpoint to delete one or more DocumentCategory. An application object will be created for each JSON object provided in the request body

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
    api_instance = openapi_client.DocumentCategoryApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of documentcategory. (optional)

    try:
        # Delete DocumentCategory
        api_response = api_instance.delete_document_category(authorization=authorization, object_id=object_id)
        print("The response of DocumentCategoryApi->delete_document_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentCategoryApi->delete_document_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| One or more system-generated identifiers of documentcategory. | [optional] 

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

# **get_document_category**
> List[DocumentCategory] get_document_category(fields, filter=filter, order_by=order_by, authorization=authorization)

Read DocumentCategory

Reads DocumentCategory objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.document_category import DocumentCategory
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
    api_instance = openapi_client.DocumentCategoryApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read DocumentCategory
        api_response = api_instance.get_document_category(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of DocumentCategoryApi->get_document_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentCategoryApi->get_document_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[DocumentCategory]**](DocumentCategory.md)

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

# **get_document_category_field_length**
> str get_document_category_field_length(field_name, authorization=authorization)

View DocumentCategory Field Length

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
    api_instance = openapi_client.DocumentCategoryApi(api_client)
    field_name = 'field_name_example' # str | An documentcategory field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View DocumentCategory Field Length
        api_response = api_instance.get_document_category_field_length(field_name, authorization=authorization)
        print("The response of DocumentCategoryApi->get_document_category_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentCategoryApi->get_document_category_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An documentcategory field. | 
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

# **get_document_category_fields**
> str get_document_category_fields()

View DocumentCategory fields

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
    api_instance = openapi_client.DocumentCategoryApi(api_client)

    try:
        # View DocumentCategory fields
        api_response = api_instance.get_document_category_fields()
        print("The response of DocumentCategoryApi->get_document_category_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentCategoryApi->get_document_category_fields: %s\n" % e)
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

# **update_document_category**
> bool update_document_category(document_category, authorization=authorization)

Update DocumentCategory

Send a request to this endpoint to update one or more DocumentCategory. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.document_category import DocumentCategory
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
    api_instance = openapi_client.DocumentCategoryApi(api_client)
    document_category = [openapi_client.DocumentCategory()] # List[DocumentCategory] | A list of documentcategory objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update DocumentCategory
        api_response = api_instance.update_document_category(document_category, authorization=authorization)
        print("The response of DocumentCategoryApi->update_document_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentCategoryApi->update_document_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_category** | [**List[DocumentCategory]**](DocumentCategory.md)| A list of documentcategory objects. | 
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

