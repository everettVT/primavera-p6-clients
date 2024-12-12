# openapi_client.ResourceCurveApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_resource_curve**](ResourceCurveApi.md#create_resource_curve) | **POST** /resourceCurve | Create ResourceCurve
[**delete_resource_curve**](ResourceCurveApi.md#delete_resource_curve) | **DELETE** /resourceCurve | Delete ResourceCurve
[**get_resource_curve**](ResourceCurveApi.md#get_resource_curve) | **GET** /resourceCurve | Read ResourceCurve
[**get_resource_curve_field_length**](ResourceCurveApi.md#get_resource_curve_field_length) | **GET** /resourceCurve/getFieldLength/{fieldName} | View ResourceCurve Field Length
[**get_resource_curve_fields**](ResourceCurveApi.md#get_resource_curve_fields) | **GET** /resourceCurve/fields | View ResourceCurve fields
[**update_resource_curve**](ResourceCurveApi.md#update_resource_curve) | **PUT** /resourceCurve | Update ResourceCurve


# **create_resource_curve**
> str create_resource_curve(resource_curve, authorization=authorization)

Create ResourceCurve

Send a request to this endpoint to create one or more ResourceCurve. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.resource_curve import ResourceCurve
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
    api_instance = openapi_client.ResourceCurveApi(api_client)
    resource_curve = [openapi_client.ResourceCurve()] # List[ResourceCurve] | A list of ResourceCurve objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ResourceCurve
        api_response = api_instance.create_resource_curve(resource_curve, authorization=authorization)
        print("The response of ResourceCurveApi->create_resource_curve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceCurveApi->create_resource_curve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_curve** | [**List[ResourceCurve]**](ResourceCurve.md)| A list of ResourceCurve objects. | 
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

# **delete_resource_curve**
> bool delete_resource_curve(object_id, authorization=authorization)

Delete ResourceCurve

Send a request to this endpoint to delete one or more ResourceCurve. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.ResourceCurveApi(api_client)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of resourceCurve.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete ResourceCurve
        api_response = api_instance.delete_resource_curve(object_id, authorization=authorization)
        print("The response of ResourceCurveApi->delete_resource_curve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceCurveApi->delete_resource_curve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| One or more system-generated identifiers of resourceCurve. | 
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

# **get_resource_curve**
> List[ResourceCurve] get_resource_curve(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ResourceCurve

Reads ResourceCurve objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.resource_curve import ResourceCurve
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
    api_instance = openapi_client.ResourceCurveApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ResourceCurve
        api_response = api_instance.get_resource_curve(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ResourceCurveApi->get_resource_curve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceCurveApi->get_resource_curve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ResourceCurve]**](ResourceCurve.md)

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

# **get_resource_curve_field_length**
> str get_resource_curve_field_length(field_name, authorization=authorization)

View ResourceCurve Field Length

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
    api_instance = openapi_client.ResourceCurveApi(api_client)
    field_name = 'field_name_example' # str | A ResourceCurve field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ResourceCurve Field Length
        api_response = api_instance.get_resource_curve_field_length(field_name, authorization=authorization)
        print("The response of ResourceCurveApi->get_resource_curve_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceCurveApi->get_resource_curve_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| A ResourceCurve field. | 
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

# **get_resource_curve_fields**
> str get_resource_curve_fields()

View ResourceCurve fields

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
    api_instance = openapi_client.ResourceCurveApi(api_client)

    try:
        # View ResourceCurve fields
        api_response = api_instance.get_resource_curve_fields()
        print("The response of ResourceCurveApi->get_resource_curve_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceCurveApi->get_resource_curve_fields: %s\n" % e)
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

# **update_resource_curve**
> bool update_resource_curve(resource_curve, authorization=authorization)

Update ResourceCurve

Send a request to this endpoint to update one or more ResourceCurve. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.resource_curve import ResourceCurve
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
    api_instance = openapi_client.ResourceCurveApi(api_client)
    resource_curve = [openapi_client.ResourceCurve()] # List[ResourceCurve] | A list of ResourceCurve objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ResourceCurve
        api_response = api_instance.update_resource_curve(resource_curve, authorization=authorization)
        print("The response of ResourceCurveApi->update_resource_curve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceCurveApi->update_resource_curve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_curve** | [**List[ResourceCurve]**](ResourceCurve.md)| A list of ResourceCurve objects. | 
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

