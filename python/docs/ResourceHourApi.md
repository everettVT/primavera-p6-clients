# openapi_client.ResourceHourApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_resource_hour**](ResourceHourApi.md#create_resource_hour) | **POST** /resourceHour | Create ResourceHour
[**delete_resource_hour**](ResourceHourApi.md#delete_resource_hour) | **DELETE** /resourceHour | Delete ResourceHour
[**get_resource_hour**](ResourceHourApi.md#get_resource_hour) | **GET** /resourceHour | Read ResourceHour
[**get_resource_hour_field_length**](ResourceHourApi.md#get_resource_hour_field_length) | **GET** /resourceHour/getFieldLength/{fieldName} | View ResourceHour Field Length
[**get_resource_hour_fields**](ResourceHourApi.md#get_resource_hour_fields) | **GET** /resourceHour/fields | View ResourceHour fields
[**update_resource_hour**](ResourceHourApi.md#update_resource_hour) | **PUT** /resourceHour | Update ResourceHour


# **create_resource_hour**
> str create_resource_hour(resource_hour, authorization=authorization)

Create ResourceHour

Send a request to this endpoint to create one or more ResourceHour. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.resource_hour import ResourceHour
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
    api_instance = openapi_client.ResourceHourApi(api_client)
    resource_hour = [openapi_client.ResourceHour()] # List[ResourceHour] | A list of ResourceHour objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ResourceHour
        api_response = api_instance.create_resource_hour(resource_hour, authorization=authorization)
        print("The response of ResourceHourApi->create_resource_hour:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceHourApi->create_resource_hour: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_hour** | [**List[ResourceHour]**](ResourceHour.md)| A list of ResourceHour objects. | 
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

# **delete_resource_hour**
> bool delete_resource_hour(object_id, authorization=authorization)

Delete ResourceHour

Send a request to this endpoint to delete one or more ResourceHour. An application object will be created for each JSON object provided in the request body

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
    api_instance = openapi_client.ResourceHourApi(api_client)
    object_id = '1,2,3' # str | One or more system-generated identifiers of ResourceHour.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete ResourceHour
        api_response = api_instance.delete_resource_hour(object_id, authorization=authorization)
        print("The response of ResourceHourApi->delete_resource_hour:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceHourApi->delete_resource_hour: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| One or more system-generated identifiers of ResourceHour. | 
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

# **get_resource_hour**
> List[ResourceHour] get_resource_hour(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ResourceHour

Reads ResourceHour objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.resource_hour import ResourceHour
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
    api_instance = openapi_client.ResourceHourApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ResourceHour
        api_response = api_instance.get_resource_hour(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ResourceHourApi->get_resource_hour:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceHourApi->get_resource_hour: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ResourceHour]**](ResourceHour.md)

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

# **get_resource_hour_field_length**
> str get_resource_hour_field_length(field_name, authorization=authorization)

View ResourceHour Field Length

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
    api_instance = openapi_client.ResourceHourApi(api_client)
    field_name = 'field_name_example' # str | An ResourceHour field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ResourceHour Field Length
        api_response = api_instance.get_resource_hour_field_length(field_name, authorization=authorization)
        print("The response of ResourceHourApi->get_resource_hour_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceHourApi->get_resource_hour_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An ResourceHour field. | 
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

# **get_resource_hour_fields**
> str get_resource_hour_fields()

View ResourceHour fields

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
    api_instance = openapi_client.ResourceHourApi(api_client)

    try:
        # View ResourceHour fields
        api_response = api_instance.get_resource_hour_fields()
        print("The response of ResourceHourApi->get_resource_hour_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceHourApi->get_resource_hour_fields: %s\n" % e)
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

# **update_resource_hour**
> bool update_resource_hour(resource_hour, authorization=authorization)

Update ResourceHour

Send a request to this endpoint to update one or more ResourceHour. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.resource_hour import ResourceHour
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
    api_instance = openapi_client.ResourceHourApi(api_client)
    resource_hour = [openapi_client.ResourceHour()] # List[ResourceHour] | A list of ResourceHour objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ResourceHour
        api_response = api_instance.update_resource_hour(resource_hour, authorization=authorization)
        print("The response of ResourceHourApi->update_resource_hour:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceHourApi->update_resource_hour: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_hour** | [**List[ResourceHour]**](ResourceHour.md)| A list of ResourceHour objects. | 
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

