# openapi_client.ResourceRateApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_resource_rate**](ResourceRateApi.md#create_resource_rate) | **POST** /resourceRate | Create ResourceRate
[**delete_resource_rate**](ResourceRateApi.md#delete_resource_rate) | **DELETE** /resourceRate | Delete ResourceRate
[**get_resource_rate**](ResourceRateApi.md#get_resource_rate) | **GET** /resourceRate | Read ResourceRate
[**get_resource_rate_field_length**](ResourceRateApi.md#get_resource_rate_field_length) | **GET** /resourceRate/getFieldLength/{fieldName} | View ResourceRate Field Length
[**get_resource_rate_fields**](ResourceRateApi.md#get_resource_rate_fields) | **GET** /resourceRate/fields | View ResourceRate fields
[**update_resource_rate**](ResourceRateApi.md#update_resource_rate) | **PUT** /resourceRate | Update ResourceRate


# **create_resource_rate**
> str create_resource_rate(resource_rate, authorization=authorization)

Create ResourceRate

Send a request to this endpoint to create one or more ResourceRate. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.resource_rate import ResourceRate
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
    api_instance = openapi_client.ResourceRateApi(api_client)
    resource_rate = [openapi_client.ResourceRate()] # List[ResourceRate] | A list of ResourceHour objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ResourceRate
        api_response = api_instance.create_resource_rate(resource_rate, authorization=authorization)
        print("The response of ResourceRateApi->create_resource_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceRateApi->create_resource_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_rate** | [**List[ResourceRate]**](ResourceRate.md)| A list of ResourceHour objects. | 
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
**201** | ResourceRate Created. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resource_rate**
> bool delete_resource_rate(object_id, authorization=authorization)

Delete ResourceRate

Send a request to this endpoint to delete one or more ResourceRate. An application object will be created for each JSON object provided in the request body

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
    api_instance = openapi_client.ResourceRateApi(api_client)
    object_id = '1,2,3' # str | One or more system-generated identifiers of ResourceRate.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete ResourceRate
        api_response = api_instance.delete_resource_rate(object_id, authorization=authorization)
        print("The response of ResourceRateApi->delete_resource_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceRateApi->delete_resource_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| One or more system-generated identifiers of ResourceRate. | 
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

# **get_resource_rate**
> List[ResourceRate] get_resource_rate(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ResourceRate

Reads ResourceRate objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.resource_rate import ResourceRate
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
    api_instance = openapi_client.ResourceRateApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ResourceRate
        api_response = api_instance.get_resource_rate(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ResourceRateApi->get_resource_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceRateApi->get_resource_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ResourceRate]**](ResourceRate.md)

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

# **get_resource_rate_field_length**
> str get_resource_rate_field_length(field_name, authorization=authorization)

View ResourceRate Field Length

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
    api_instance = openapi_client.ResourceRateApi(api_client)
    field_name = 'field_name_example' # str | An ResourceRate field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ResourceRate Field Length
        api_response = api_instance.get_resource_rate_field_length(field_name, authorization=authorization)
        print("The response of ResourceRateApi->get_resource_rate_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceRateApi->get_resource_rate_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An ResourceRate field. | 
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

# **get_resource_rate_fields**
> str get_resource_rate_fields()

View ResourceRate fields

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
    api_instance = openapi_client.ResourceRateApi(api_client)

    try:
        # View ResourceRate fields
        api_response = api_instance.get_resource_rate_fields()
        print("The response of ResourceRateApi->get_resource_rate_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceRateApi->get_resource_rate_fields: %s\n" % e)
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

# **update_resource_rate**
> bool update_resource_rate(resource_rate, authorization=authorization)

Update ResourceRate

Send a request to this endpoint to update one or more ResourceRate. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.resource_rate import ResourceRate
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
    api_instance = openapi_client.ResourceRateApi(api_client)
    resource_rate = [openapi_client.ResourceRate()] # List[ResourceRate] | A list of ResourceHour objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ResourceRate
        api_response = api_instance.update_resource_rate(resource_rate, authorization=authorization)
        print("The response of ResourceRateApi->update_resource_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceRateApi->update_resource_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_rate** | [**List[ResourceRate]**](ResourceRate.md)| A list of ResourceHour objects. | 
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

