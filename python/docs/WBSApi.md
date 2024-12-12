# openapi_client.WBSApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_wbs**](WBSApi.md#create_wbs) | **POST** /wbs | Create WBS
[**delete_wbs**](WBSApi.md#delete_wbs) | **DELETE** /wbs | Delete WBS
[**get_eps_fields1**](WBSApi.md#get_eps_fields1) | **GET** /wbs/fields | View WBS fields
[**get_wbs**](WBSApi.md#get_wbs) | **GET** /wbs | Read WBS
[**get_wbs_field_length**](WBSApi.md#get_wbs_field_length) | **GET** /wbs/getFieldLength/{fieldName} | View WBS Field Length
[**update_wbs**](WBSApi.md#update_wbs) | **PUT** /wbs | Update WBS


# **create_wbs**
> str create_wbs(wbs, authorization=authorization)

Create WBS

Send a request to this endpoint to create one or more WBS. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.wbs import WBS
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
    api_instance = openapi_client.WBSApi(api_client)
    wbs = [openapi_client.WBS()] # List[WBS] | A list of WBS objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create WBS
        api_response = api_instance.create_wbs(wbs, authorization=authorization)
        print("The response of WBSApi->create_wbs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WBSApi->create_wbs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wbs** | [**List[WBS]**](WBS.md)| A list of WBS objects. | 
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

# **delete_wbs**
> bool delete_wbs(object_id, authorization=authorization)

Delete WBS

Send a request to this endpoint to delete one or more WBS. An application object will be created for each JSON object provided in the request body

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
    api_instance = openapi_client.WBSApi(api_client)
    object_id = '1,2,3' # str | One or more system-generated identifiers of WBS.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete WBS
        api_response = api_instance.delete_wbs(object_id, authorization=authorization)
        print("The response of WBSApi->delete_wbs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WBSApi->delete_wbs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| One or more system-generated identifiers of WBS. | 
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

# **get_eps_fields1**
> str get_eps_fields1()

View WBS fields

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
    api_instance = openapi_client.WBSApi(api_client)

    try:
        # View WBS fields
        api_response = api_instance.get_eps_fields1()
        print("The response of WBSApi->get_eps_fields1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WBSApi->get_eps_fields1: %s\n" % e)
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

# **get_wbs**
> List[WBS] get_wbs(fields, filter=filter, order_by=order_by, authorization=authorization)

Read WBS

Reads WBS objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.wbs import WBS
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
    api_instance = openapi_client.WBSApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read WBS
        api_response = api_instance.get_wbs(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of WBSApi->get_wbs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WBSApi->get_wbs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[WBS]**](WBS.md)

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

# **get_wbs_field_length**
> str get_wbs_field_length(field_name, authorization=authorization)

View WBS Field Length

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
    api_instance = openapi_client.WBSApi(api_client)
    field_name = 'field_name_example' # str | An project field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View WBS Field Length
        api_response = api_instance.get_wbs_field_length(field_name, authorization=authorization)
        print("The response of WBSApi->get_wbs_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WBSApi->get_wbs_field_length: %s\n" % e)
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

# **update_wbs**
> bool update_wbs(wbs, authorization=authorization)

Update WBS

Send a request to this endpoint to update one or more WBS. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.wbs import WBS
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
    api_instance = openapi_client.WBSApi(api_client)
    wbs = [openapi_client.WBS()] # List[WBS] | A list of WBS objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update WBS
        api_response = api_instance.update_wbs(wbs, authorization=authorization)
        print("The response of WBSApi->update_wbs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WBSApi->update_wbs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wbs** | [**List[WBS]**](WBS.md)| A list of WBS objects. | 
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

