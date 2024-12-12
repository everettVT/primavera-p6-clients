# openapi_client.BaselineTypeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_baseline_type**](BaselineTypeApi.md#create_baseline_type) | **POST** /baselineType | Create BaselineTypes
[**delete_baseline_type**](BaselineTypeApi.md#delete_baseline_type) | **DELETE** /baselineType | Delete BaselineTypes
[**get_baseline_type_field_length**](BaselineTypeApi.md#get_baseline_type_field_length) | **GET** /baselineType/getFieldLength/{fieldName} | View BaselineType Field Length
[**get_baseline_type_fields**](BaselineTypeApi.md#get_baseline_type_fields) | **GET** /baselineType/fields | View BaselineType fields
[**get_baseline_types**](BaselineTypeApi.md#get_baseline_types) | **GET** /baselineType | Read BaselineTypes
[**update_baseline_type**](BaselineTypeApi.md#update_baseline_type) | **PUT** /baselineType | Update BaselineTypes


# **create_baseline_type**
> str create_baseline_type(baseline_type, authorization=authorization)

Create BaselineTypes

Send a request to this endpoint to create one or more baselineType. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.baseline_type import BaselineType
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
    api_instance = openapi_client.BaselineTypeApi(api_client)
    baseline_type = [openapi_client.BaselineType()] # List[BaselineType] | A list of baselineType objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create BaselineTypes
        api_response = api_instance.create_baseline_type(baseline_type, authorization=authorization)
        print("The response of BaselineTypeApi->create_baseline_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BaselineTypeApi->create_baseline_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **baseline_type** | [**List[BaselineType]**](BaselineType.md)| A list of baselineType objects. | 
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

# **delete_baseline_type**
> bool delete_baseline_type(authorization=authorization, object_id=object_id)

Delete BaselineTypes

Send a request to this endpoint to delete one or more baselineType. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.BaselineTypeApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of baselineType. (optional)

    try:
        # Delete BaselineTypes
        api_response = api_instance.delete_baseline_type(authorization=authorization, object_id=object_id)
        print("The response of BaselineTypeApi->delete_baseline_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BaselineTypeApi->delete_baseline_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| One or more system-generated identifiers of baselineType. | [optional] 

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

# **get_baseline_type_field_length**
> str get_baseline_type_field_length(field_name, authorization=authorization)

View BaselineType Field Length

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
    api_instance = openapi_client.BaselineTypeApi(api_client)
    field_name = 'field_name_example' # str | A baselineType field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View BaselineType Field Length
        api_response = api_instance.get_baseline_type_field_length(field_name, authorization=authorization)
        print("The response of BaselineTypeApi->get_baseline_type_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BaselineTypeApi->get_baseline_type_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| A baselineType field. | 
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

# **get_baseline_type_fields**
> str get_baseline_type_fields()

View BaselineType fields

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
    api_instance = openapi_client.BaselineTypeApi(api_client)

    try:
        # View BaselineType fields
        api_response = api_instance.get_baseline_type_fields()
        print("The response of BaselineTypeApi->get_baseline_type_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BaselineTypeApi->get_baseline_type_fields: %s\n" % e)
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

# **get_baseline_types**
> List[BaselineType] get_baseline_types(fields, filter=filter, order_by=order_by, authorization=authorization)

Read BaselineTypes

Reads BaselineType objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.baseline_type import BaselineType
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
    api_instance = openapi_client.BaselineTypeApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read BaselineTypes
        api_response = api_instance.get_baseline_types(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of BaselineTypeApi->get_baseline_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BaselineTypeApi->get_baseline_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[BaselineType]**](BaselineType.md)

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

# **update_baseline_type**
> bool update_baseline_type(baseline_type, authorization=authorization)

Update BaselineTypes

Send a request to this endpoint to update one or more baselineType. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.baseline_type import BaselineType
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
    api_instance = openapi_client.BaselineTypeApi(api_client)
    baseline_type = [openapi_client.BaselineType()] # List[BaselineType] | A list of baselineType objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update BaselineTypes
        api_response = api_instance.update_baseline_type(baseline_type, authorization=authorization)
        print("The response of BaselineTypeApi->update_baseline_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BaselineTypeApi->update_baseline_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **baseline_type** | [**List[BaselineType]**](BaselineType.md)| A list of baselineType objects. | 
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

