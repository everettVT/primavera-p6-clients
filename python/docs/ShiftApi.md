# openapi_client.ShiftApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_shift**](ShiftApi.md#create_shift) | **POST** /shift | Create Shift
[**delete_shift**](ShiftApi.md#delete_shift) | **DELETE** /shift | Delete Shift
[**get_shift**](ShiftApi.md#get_shift) | **GET** /shift | Read Shift
[**get_shift_field_length**](ShiftApi.md#get_shift_field_length) | **GET** /shift/getFieldLength/{fieldName} | View Shift Field Length
[**get_shift_fields**](ShiftApi.md#get_shift_fields) | **GET** /shift/fields | View Shift fields
[**update_shift**](ShiftApi.md#update_shift) | **PUT** /shift | Update Activities


# **create_shift**
> str create_shift(shift, authorization=authorization)

Create Shift

Send a request to this endpoint to create one or more Shift. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.shift import Shift
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
    api_instance = openapi_client.ShiftApi(api_client)
    shift = [openapi_client.Shift()] # List[Shift] | A list of Shift objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create Shift
        api_response = api_instance.create_shift(shift, authorization=authorization)
        print("The response of ShiftApi->create_shift:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShiftApi->create_shift: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shift** | [**List[Shift]**](Shift.md)| A list of Shift objects. | 
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

# **delete_shift**
> bool delete_shift(object_id, authorization=authorization)

Delete Shift

Send a request to this endpoint to delete one or more Shift. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.ShiftApi(api_client)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of Shift.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete Shift
        api_response = api_instance.delete_shift(object_id, authorization=authorization)
        print("The response of ShiftApi->delete_shift:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShiftApi->delete_shift: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| One or more system-generated identifiers of Shift. | 
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

# **get_shift**
> List[Shift] get_shift(fields, filter=filter, order_by=order_by, authorization=authorization)

Read Shift

Reads Shift objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.shift import Shift
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
    api_instance = openapi_client.ShiftApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read Shift
        api_response = api_instance.get_shift(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ShiftApi->get_shift:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShiftApi->get_shift: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[Shift]**](Shift.md)

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

# **get_shift_field_length**
> str get_shift_field_length(field_name, authorization=authorization)

View Shift Field Length

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
    api_instance = openapi_client.ShiftApi(api_client)
    field_name = 'field_name_example' # str | A Shift field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View Shift Field Length
        api_response = api_instance.get_shift_field_length(field_name, authorization=authorization)
        print("The response of ShiftApi->get_shift_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShiftApi->get_shift_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| A Shift field. | 
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

# **get_shift_fields**
> str get_shift_fields()

View Shift fields

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
    api_instance = openapi_client.ShiftApi(api_client)

    try:
        # View Shift fields
        api_response = api_instance.get_shift_fields()
        print("The response of ShiftApi->get_shift_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShiftApi->get_shift_fields: %s\n" % e)
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

# **update_shift**
> bool update_shift(shift, authorization=authorization)

Update Activities

Send a request to this endpoint to update one or more Shift. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.shift import Shift
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
    api_instance = openapi_client.ShiftApi(api_client)
    shift = [openapi_client.Shift()] # List[Shift] | A list of Shift objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update Activities
        api_response = api_instance.update_shift(shift, authorization=authorization)
        print("The response of ShiftApi->update_shift:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShiftApi->update_shift: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shift** | [**List[Shift]**](Shift.md)| A list of Shift objects. | 
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

