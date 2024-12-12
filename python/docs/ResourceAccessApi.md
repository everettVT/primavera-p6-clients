# openapi_client.ResourceAccessApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_resource_access**](ResourceAccessApi.md#create_resource_access) | **POST** /resourceAccess | Create ResourceAccess
[**delete_resource_access**](ResourceAccessApi.md#delete_resource_access) | **DELETE** /resourceAccess | Delete ResourceAccess
[**get_resource_access**](ResourceAccessApi.md#get_resource_access) | **GET** /resourceAccess | Read ResourceAccess
[**get_resource_access_field_length**](ResourceAccessApi.md#get_resource_access_field_length) | **GET** /resourceAccess/getFieldLength/{fieldName} | View ResourceAccess Field Length
[**get_resource_access_fields**](ResourceAccessApi.md#get_resource_access_fields) | **GET** /resourceAccess/fields | View ResourceAccess fields


# **create_resource_access**
> CreateResourceAccessResponse create_resource_access(resource_access, authorization=authorization)

Create ResourceAccess

Send a request to this endpoint to create one or more resourceAccess. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.create_resource_access_response import CreateResourceAccessResponse
from openapi_client.models.resource_access import ResourceAccess
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
    api_instance = openapi_client.ResourceAccessApi(api_client)
    resource_access = [openapi_client.ResourceAccess()] # List[ResourceAccess] | A list of resourceAccess objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ResourceAccess
        api_response = api_instance.create_resource_access(resource_access, authorization=authorization)
        print("The response of ResourceAccessApi->create_resource_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceAccessApi->create_resource_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_access** | [**List[ResourceAccess]**](ResourceAccess.md)| A list of resourceAccess objects. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**CreateResourceAccessResponse**](CreateResourceAccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource Access Created. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resource_access**
> bool delete_resource_access(resource_access, authorization=authorization)

Delete ResourceAccess

Send a request to this endpoint to delete one or more resourceAccess. Objects with ID values that match the values provided in the request body will be deleted.

### Example


```python
import openapi_client
from openapi_client.models.resource_access import ResourceAccess
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
    api_instance = openapi_client.ResourceAccessApi(api_client)
    resource_access = [openapi_client.ResourceAccess()] # List[ResourceAccess] | <p>A list of ResourceAccess objects.<p><p>Required fields: You must supply both the UserObjectId and ResourceObjectId fields when you use the Delete ResourceAccess operation. All other fields are optional.</p>
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete ResourceAccess
        api_response = api_instance.delete_resource_access(resource_access, authorization=authorization)
        print("The response of ResourceAccessApi->delete_resource_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceAccessApi->delete_resource_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_access** | [**List[ResourceAccess]**](ResourceAccess.md)| &lt;p&gt;A list of ResourceAccess objects.&lt;p&gt;&lt;p&gt;Required fields: You must supply both the UserObjectId and ResourceObjectId fields when you use the Delete ResourceAccess operation. All other fields are optional.&lt;/p&gt; | 
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

# **get_resource_access**
> List[ResourceAccess] get_resource_access(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ResourceAccess

Reads ResourceAccess objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.resource_access import ResourceAccess
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
    api_instance = openapi_client.ResourceAccessApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ResourceAccess
        api_response = api_instance.get_resource_access(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ResourceAccessApi->get_resource_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceAccessApi->get_resource_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ResourceAccess]**](ResourceAccess.md)

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

# **get_resource_access_field_length**
> str get_resource_access_field_length(field_name, authorization=authorization)

View ResourceAccess Field Length

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
    api_instance = openapi_client.ResourceAccessApi(api_client)
    field_name = 'field_name_example' # str | A resourceAccess field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ResourceAccess Field Length
        api_response = api_instance.get_resource_access_field_length(field_name, authorization=authorization)
        print("The response of ResourceAccessApi->get_resource_access_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceAccessApi->get_resource_access_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| A resourceAccess field. | 
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

# **get_resource_access_fields**
> str get_resource_access_fields()

View ResourceAccess fields

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
    api_instance = openapi_client.ResourceAccessApi(api_client)

    try:
        # View ResourceAccess fields
        api_response = api_instance.get_resource_access_fields()
        print("The response of ResourceAccessApi->get_resource_access_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceAccessApi->get_resource_access_fields: %s\n" % e)
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

