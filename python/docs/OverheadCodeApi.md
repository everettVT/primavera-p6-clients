# openapi_client.OverheadCodeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_overhead_code**](OverheadCodeApi.md#create_overhead_code) | **POST** /overheadCode | Create OverheadCodes
[**delete_overhead_code**](OverheadCodeApi.md#delete_overhead_code) | **DELETE** /overheadCode | Delete OverheadCodes
[**get_overhead_code**](OverheadCodeApi.md#get_overhead_code) | **GET** /overheadCode | Read OverheadCodes
[**get_overhead_code_field_length**](OverheadCodeApi.md#get_overhead_code_field_length) | **GET** /overheadCode/getFieldLength/{fieldName} | View OverheadCode Field Length
[**get_overhead_code_fields**](OverheadCodeApi.md#get_overhead_code_fields) | **GET** /overheadCode/fields | View OverheadCode fields
[**update_overhead_code**](OverheadCodeApi.md#update_overhead_code) | **PUT** /overheadCode | Update OverheadCodes


# **create_overhead_code**
> str create_overhead_code(overhead_code, authorization=authorization)

Create OverheadCodes

Send a request to this endpoint to create one or more overheadCode. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.overhead_code import OverheadCode
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
    api_instance = openapi_client.OverheadCodeApi(api_client)
    overhead_code = [openapi_client.OverheadCode()] # List[OverheadCode] | A list of overheadCode objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create OverheadCodes
        api_response = api_instance.create_overhead_code(overhead_code, authorization=authorization)
        print("The response of OverheadCodeApi->create_overhead_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OverheadCodeApi->create_overhead_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **overhead_code** | [**List[OverheadCode]**](OverheadCode.md)| A list of overheadCode objects. | 
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

# **delete_overhead_code**
> bool delete_overhead_code(authorization=authorization, object_id=object_id)

Delete OverheadCodes

Send a request to this endpoint to delete one or more overheadCode. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.OverheadCodeApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of overheadCode. (optional)

    try:
        # Delete OverheadCodes
        api_response = api_instance.delete_overhead_code(authorization=authorization, object_id=object_id)
        print("The response of OverheadCodeApi->delete_overhead_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OverheadCodeApi->delete_overhead_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| One or more system-generated identifiers of overheadCode. | [optional] 

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

# **get_overhead_code**
> List[OverheadCode] get_overhead_code(fields, filter=filter, order_by=order_by, authorization=authorization)

Read OverheadCodes

Reads OverheadCode objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.overhead_code import OverheadCode
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
    api_instance = openapi_client.OverheadCodeApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read OverheadCodes
        api_response = api_instance.get_overhead_code(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of OverheadCodeApi->get_overhead_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OverheadCodeApi->get_overhead_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[OverheadCode]**](OverheadCode.md)

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

# **get_overhead_code_field_length**
> str get_overhead_code_field_length(field_name, authorization=authorization)

View OverheadCode Field Length

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
    api_instance = openapi_client.OverheadCodeApi(api_client)
    field_name = 'field_name_example' # str | An overheadCode field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View OverheadCode Field Length
        api_response = api_instance.get_overhead_code_field_length(field_name, authorization=authorization)
        print("The response of OverheadCodeApi->get_overhead_code_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OverheadCodeApi->get_overhead_code_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An overheadCode field. | 
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

# **get_overhead_code_fields**
> str get_overhead_code_fields()

View OverheadCode fields

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
    api_instance = openapi_client.OverheadCodeApi(api_client)

    try:
        # View OverheadCode fields
        api_response = api_instance.get_overhead_code_fields()
        print("The response of OverheadCodeApi->get_overhead_code_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OverheadCodeApi->get_overhead_code_fields: %s\n" % e)
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

# **update_overhead_code**
> bool update_overhead_code(overhead_code, authorization=authorization)

Update OverheadCodes

Send a request to this endpoint to update one or more overheadCode. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.overhead_code import OverheadCode
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
    api_instance = openapi_client.OverheadCodeApi(api_client)
    overhead_code = [openapi_client.OverheadCode()] # List[OverheadCode] | A list of overheadCode objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update OverheadCodes
        api_response = api_instance.update_overhead_code(overhead_code, authorization=authorization)
        print("The response of OverheadCodeApi->update_overhead_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OverheadCodeApi->update_overhead_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **overhead_code** | [**List[OverheadCode]**](OverheadCode.md)| A list of overheadCode objects. | 
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

