# openapi_client.EPSApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_eps**](EPSApi.md#create_eps) | **POST** /eps | Create EPS
[**delete_eps**](EPSApi.md#delete_eps) | **DELETE** /eps | Delete EPS
[**get_eps**](EPSApi.md#get_eps) | **GET** /eps | Read EPS
[**get_eps_field_length**](EPSApi.md#get_eps_field_length) | **GET** /eps/getFieldLength/{fieldName} | View EPS Field Length
[**get_eps_fields**](EPSApi.md#get_eps_fields) | **GET** /eps/fields | View EPS fields
[**update_eps**](EPSApi.md#update_eps) | **PUT** /eps | Update EPS


# **create_eps**
> str create_eps(eps, authorization=authorization)

Create EPS

Send a request to this endpoint to create one or more EPS. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.eps import EPS
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
    api_instance = openapi_client.EPSApi(api_client)
    eps = [openapi_client.EPS()] # List[EPS] | A list of EPS objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create EPS
        api_response = api_instance.create_eps(eps, authorization=authorization)
        print("The response of EPSApi->create_eps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPSApi->create_eps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eps** | [**List[EPS]**](EPS.md)| A list of EPS objects. | 
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

# **delete_eps**
> bool delete_eps(object_id, authorization=authorization)

Delete EPS

Send a request to this endpoint to delete one or more EPS. An application object will be created for each JSON object provided in the request body

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
    api_instance = openapi_client.EPSApi(api_client)
    object_id = '1,2,3' # str | One or more system-generated identifiers of EPS.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete EPS
        api_response = api_instance.delete_eps(object_id, authorization=authorization)
        print("The response of EPSApi->delete_eps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPSApi->delete_eps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| One or more system-generated identifiers of EPS. | 
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

# **get_eps**
> List[EPS] get_eps(fields, filter=filter, order_by=order_by, authorization=authorization)

Read EPS

Reads EPS objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.eps import EPS
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
    api_instance = openapi_client.EPSApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read EPS
        api_response = api_instance.get_eps(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of EPSApi->get_eps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPSApi->get_eps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[EPS]**](EPS.md)

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

# **get_eps_field_length**
> str get_eps_field_length(field_name, authorization=authorization)

View EPS Field Length

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
    api_instance = openapi_client.EPSApi(api_client)
    field_name = 'field_name_example' # str | An EPS field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View EPS Field Length
        api_response = api_instance.get_eps_field_length(field_name, authorization=authorization)
        print("The response of EPSApi->get_eps_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPSApi->get_eps_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An EPS field. | 
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

# **get_eps_fields**
> str get_eps_fields()

View EPS fields

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
    api_instance = openapi_client.EPSApi(api_client)

    try:
        # View EPS fields
        api_response = api_instance.get_eps_fields()
        print("The response of EPSApi->get_eps_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPSApi->get_eps_fields: %s\n" % e)
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

# **update_eps**
> bool update_eps(eps, authorization=authorization)

Update EPS

Send a request to this endpoint to update one or more EPS. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.eps import EPS
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
    api_instance = openapi_client.EPSApi(api_client)
    eps = [openapi_client.EPS()] # List[EPS] | A list of EPS objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update EPS
        api_response = api_instance.update_eps(eps, authorization=authorization)
        print("The response of EPSApi->update_eps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPSApi->update_eps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eps** | [**List[EPS]**](EPS.md)| A list of EPS objects. | 
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

