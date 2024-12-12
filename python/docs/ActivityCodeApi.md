# openapi_client.ActivityCodeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_activity_code**](ActivityCodeApi.md#create_activity_code) | **POST** /activityCode | Create ActivityCodes
[**delete_activity_code**](ActivityCodeApi.md#delete_activity_code) | **DELETE** /activityCode | Delete ActivityCodes
[**get_activity_code_field_length**](ActivityCodeApi.md#get_activity_code_field_length) | **GET** /activityCode/getFieldLength/{fieldName} | View ActivityCode Field Length
[**get_activity_code_fields**](ActivityCodeApi.md#get_activity_code_fields) | **GET** /activityCode/fields | View Activity fields
[**get_activity_codes**](ActivityCodeApi.md#get_activity_codes) | **GET** /activityCode | Read ActivityCodes
[**update_activity_code**](ActivityCodeApi.md#update_activity_code) | **PUT** /activityCode | Update ActivityCodes


# **create_activity_code**
> str create_activity_code(activity_code, authorization=authorization)

Create ActivityCodes

Send a request to this endpoint to create one or more activityCode. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.activity_code import ActivityCode
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
    api_instance = openapi_client.ActivityCodeApi(api_client)
    activity_code = [openapi_client.ActivityCode()] # List[ActivityCode] | A list of activityCode objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ActivityCodes
        api_response = api_instance.create_activity_code(activity_code, authorization=authorization)
        print("The response of ActivityCodeApi->create_activity_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityCodeApi->create_activity_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_code** | [**List[ActivityCode]**](ActivityCode.md)| A list of activityCode objects. | 
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

# **delete_activity_code**
> bool delete_activity_code(object_id, authorization=authorization)

Delete ActivityCodes

Send a request to this endpoint to delete one or more activityCode. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.ActivityCodeApi(api_client)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of activityCode.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete ActivityCodes
        api_response = api_instance.delete_activity_code(object_id, authorization=authorization)
        print("The response of ActivityCodeApi->delete_activity_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityCodeApi->delete_activity_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| One or more system-generated identifiers of activityCode. | 
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

# **get_activity_code_field_length**
> str get_activity_code_field_length(field_name, authorization=authorization)

View ActivityCode Field Length

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
    api_instance = openapi_client.ActivityCodeApi(api_client)
    field_name = 'field_name_example' # str | An activityCode field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ActivityCode Field Length
        api_response = api_instance.get_activity_code_field_length(field_name, authorization=authorization)
        print("The response of ActivityCodeApi->get_activity_code_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityCodeApi->get_activity_code_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An activityCode field. | 
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

# **get_activity_code_fields**
> str get_activity_code_fields()

View Activity fields

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
    api_instance = openapi_client.ActivityCodeApi(api_client)

    try:
        # View Activity fields
        api_response = api_instance.get_activity_code_fields()
        print("The response of ActivityCodeApi->get_activity_code_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityCodeApi->get_activity_code_fields: %s\n" % e)
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

# **get_activity_codes**
> List[ActivityCode] get_activity_codes(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ActivityCodes

Reads ActivityCode objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.activity_code import ActivityCode
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
    api_instance = openapi_client.ActivityCodeApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ActivityCodes
        api_response = api_instance.get_activity_codes(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ActivityCodeApi->get_activity_codes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityCodeApi->get_activity_codes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ActivityCode]**](ActivityCode.md)

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

# **update_activity_code**
> bool update_activity_code(activity_code, authorization=authorization)

Update ActivityCodes

Send a request to this endpoint to update one or more activityCode. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.activity_code import ActivityCode
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
    api_instance = openapi_client.ActivityCodeApi(api_client)
    activity_code = [openapi_client.ActivityCode()] # List[ActivityCode] | A list of activityCode objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ActivityCodes
        api_response = api_instance.update_activity_code(activity_code, authorization=authorization)
        print("The response of ActivityCodeApi->update_activity_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityCodeApi->update_activity_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_code** | [**List[ActivityCode]**](ActivityCode.md)| A list of activityCode objects. | 
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

