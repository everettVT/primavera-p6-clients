# openapi_client.GlobalReplaceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_global_replace**](GlobalReplaceApi.md#get_global_replace) | **GET** /globalReplace | Read GlobalReplace
[**get_global_replace_field_length**](GlobalReplaceApi.md#get_global_replace_field_length) | **GET** /globalReplace/getFieldLength/{fieldName} | View GlobalReplace Field Length
[**get_global_replace_fields**](GlobalReplaceApi.md#get_global_replace_fields) | **GET** /globalReplace/fields | View GlobalReplace fields
[**update_global_replace**](GlobalReplaceApi.md#update_global_replace) | **PUT** /globalReplace | Update GlobalReplace


# **get_global_replace**
> List[GlobalReplace] get_global_replace(fields, filter=filter, order_by=order_by, authorization=authorization)

Read GlobalReplace

Reads GlobalReplace objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.global_replace import GlobalReplace
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
    api_instance = openapi_client.GlobalReplaceApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read GlobalReplace
        api_response = api_instance.get_global_replace(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of GlobalReplaceApi->get_global_replace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalReplaceApi->get_global_replace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[GlobalReplace]**](GlobalReplace.md)

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

# **get_global_replace_field_length**
> str get_global_replace_field_length(field_name, authorization=authorization)

View GlobalReplace Field Length

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
    api_instance = openapi_client.GlobalReplaceApi(api_client)
    field_name = 'field_name_example' # str | An GlobalReplace field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View GlobalReplace Field Length
        api_response = api_instance.get_global_replace_field_length(field_name, authorization=authorization)
        print("The response of GlobalReplaceApi->get_global_replace_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalReplaceApi->get_global_replace_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An GlobalReplace field. | 
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

# **get_global_replace_fields**
> str get_global_replace_fields()

View GlobalReplace fields

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
    api_instance = openapi_client.GlobalReplaceApi(api_client)

    try:
        # View GlobalReplace fields
        api_response = api_instance.get_global_replace_fields()
        print("The response of GlobalReplaceApi->get_global_replace_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalReplaceApi->get_global_replace_fields: %s\n" % e)
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

# **update_global_replace**
> bool update_global_replace(global_replace, authorization=authorization)

Update GlobalReplace

Send a request to this endpoint to update one or more GlobalReplace. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.global_replace import GlobalReplace
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
    api_instance = openapi_client.GlobalReplaceApi(api_client)
    global_replace = [openapi_client.GlobalReplace()] # List[GlobalReplace] | A list of globalReplace objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update GlobalReplace
        api_response = api_instance.update_global_replace(global_replace, authorization=authorization)
        print("The response of GlobalReplaceApi->update_global_replace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalReplaceApi->update_global_replace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **global_replace** | [**List[GlobalReplace]**](GlobalReplace.md)| A list of globalReplace objects. | 
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

