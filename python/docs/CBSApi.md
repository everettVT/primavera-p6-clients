# openapi_client.CBSApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cbs**](CBSApi.md#create_cbs) | **POST** /cbs | Create CBSs
[**delete_cbs**](CBSApi.md#delete_cbs) | **DELETE** /cbs | Delete CBSs
[**get_cbs**](CBSApi.md#get_cbs) | **GET** /cbs | Read CBSs
[**get_cbs_field_length**](CBSApi.md#get_cbs_field_length) | **GET** /cbs/getFieldLength/{fieldName} | View CBS Field Length
[**get_cbs_fields**](CBSApi.md#get_cbs_fields) | **GET** /cbs/fields | View CBS fields
[**update_cbs**](CBSApi.md#update_cbs) | **PUT** /cbs | Update CBSs


# **create_cbs**
> str create_cbs(cbs, authorization=authorization)

Create CBSs

Send a request to this endpoint to create one or more cbs. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.cbs import CBS
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
    api_instance = openapi_client.CBSApi(api_client)
    cbs = [openapi_client.CBS()] # List[CBS] | A list of cbs objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create CBSs
        api_response = api_instance.create_cbs(cbs, authorization=authorization)
        print("The response of CBSApi->create_cbs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CBSApi->create_cbs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cbs** | [**List[CBS]**](CBS.md)| A list of cbs objects. | 
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

# **delete_cbs**
> bool delete_cbs(authorization=authorization, object_id=object_id)

Delete CBSs

Send a request to this endpoint to delete one or more cbs. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.CBSApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of cbs. (optional)

    try:
        # Delete CBSs
        api_response = api_instance.delete_cbs(authorization=authorization, object_id=object_id)
        print("The response of CBSApi->delete_cbs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CBSApi->delete_cbs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| One or more system-generated identifiers of cbs. | [optional] 

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

# **get_cbs**
> List[CBS] get_cbs(fields, filter=filter, order_by=order_by, authorization=authorization)

Read CBSs

Reads CBS objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.cbs import CBS
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
    api_instance = openapi_client.CBSApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read CBSs
        api_response = api_instance.get_cbs(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of CBSApi->get_cbs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CBSApi->get_cbs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[CBS]**](CBS.md)

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

# **get_cbs_field_length**
> str get_cbs_field_length(field_name, authorization=authorization)

View CBS Field Length

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
    api_instance = openapi_client.CBSApi(api_client)
    field_name = 'field_name_example' # str | A cbs field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View CBS Field Length
        api_response = api_instance.get_cbs_field_length(field_name, authorization=authorization)
        print("The response of CBSApi->get_cbs_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CBSApi->get_cbs_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| A cbs field. | 
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

# **get_cbs_fields**
> str get_cbs_fields()

View CBS fields

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
    api_instance = openapi_client.CBSApi(api_client)

    try:
        # View CBS fields
        api_response = api_instance.get_cbs_fields()
        print("The response of CBSApi->get_cbs_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CBSApi->get_cbs_fields: %s\n" % e)
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

# **update_cbs**
> bool update_cbs(cbs, authorization=authorization)

Update CBSs

Send a request to this endpoint to update one or more cbs. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.cbs import CBS
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
    api_instance = openapi_client.CBSApi(api_client)
    cbs = [openapi_client.CBS()] # List[CBS] | A list of cbs objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update CBSs
        api_response = api_instance.update_cbs(cbs, authorization=authorization)
        print("The response of CBSApi->update_cbs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CBSApi->update_cbs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cbs** | [**List[CBS]**](CBS.md)| A list of cbs objects. | 
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

