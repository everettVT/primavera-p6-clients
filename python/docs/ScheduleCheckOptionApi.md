# openapi_client.ScheduleCheckOptionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_schedule_check_option**](ScheduleCheckOptionApi.md#create_schedule_check_option) | **POST** /scheduleCheckOption | Create ScheduleCheckOption
[**delete_schedule_check_option**](ScheduleCheckOptionApi.md#delete_schedule_check_option) | **DELETE** /scheduleCheckOption | Delete ScheduleCheckOption
[**get_schedule_check_option**](ScheduleCheckOptionApi.md#get_schedule_check_option) | **GET** /scheduleCheckOption | Read ScheduleCheckOption
[**get_schedule_check_option_field_length**](ScheduleCheckOptionApi.md#get_schedule_check_option_field_length) | **GET** /scheduleCheckOption/getFieldLength/{fieldName} | View ScheduleCheckOption Field Length
[**get_schedule_check_option_fields**](ScheduleCheckOptionApi.md#get_schedule_check_option_fields) | **GET** /scheduleCheckOption/fields | View ScheduleCheckOption fields
[**update_schedule_check_option**](ScheduleCheckOptionApi.md#update_schedule_check_option) | **PUT** /scheduleCheckOption | Update ScheduleCheckOption


# **create_schedule_check_option**
> str create_schedule_check_option(schedule_check_option, authorization=authorization)

Create ScheduleCheckOption

Send a request to this endpoint to create ScheduleCheckOption. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.schedule_check_option import ScheduleCheckOption
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
    api_instance = openapi_client.ScheduleCheckOptionApi(api_client)
    schedule_check_option = [openapi_client.ScheduleCheckOption()] # List[ScheduleCheckOption] | A list of risk objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ScheduleCheckOption
        api_response = api_instance.create_schedule_check_option(schedule_check_option, authorization=authorization)
        print("The response of ScheduleCheckOptionApi->create_schedule_check_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleCheckOptionApi->create_schedule_check_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_check_option** | [**List[ScheduleCheckOption]**](ScheduleCheckOption.md)| A list of risk objects. | 
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

# **delete_schedule_check_option**
> bool delete_schedule_check_option(authorization=authorization, object_id=object_id)

Delete ScheduleCheckOption

Send a request to this endpoint to delete one or more ScheduleCheckOption. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.ScheduleCheckOptionApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of ScheduleCheckOption. (optional)

    try:
        # Delete ScheduleCheckOption
        api_response = api_instance.delete_schedule_check_option(authorization=authorization, object_id=object_id)
        print("The response of ScheduleCheckOptionApi->delete_schedule_check_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleCheckOptionApi->delete_schedule_check_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| One or more system-generated identifiers of ScheduleCheckOption. | [optional] 

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

# **get_schedule_check_option**
> List[ScheduleCheckOption] get_schedule_check_option(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ScheduleCheckOption

Reads ScheduleCheckOption objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.schedule_check_option import ScheduleCheckOption
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
    api_instance = openapi_client.ScheduleCheckOptionApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ScheduleCheckOption
        api_response = api_instance.get_schedule_check_option(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ScheduleCheckOptionApi->get_schedule_check_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleCheckOptionApi->get_schedule_check_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ScheduleCheckOption]**](ScheduleCheckOption.md)

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

# **get_schedule_check_option_field_length**
> str get_schedule_check_option_field_length(field_name, authorization=authorization)

View ScheduleCheckOption Field Length

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
    api_instance = openapi_client.ScheduleCheckOptionApi(api_client)
    field_name = 'field_name_example' # str | An ScheduleCheckOption field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ScheduleCheckOption Field Length
        api_response = api_instance.get_schedule_check_option_field_length(field_name, authorization=authorization)
        print("The response of ScheduleCheckOptionApi->get_schedule_check_option_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleCheckOptionApi->get_schedule_check_option_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An ScheduleCheckOption field. | 
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

# **get_schedule_check_option_fields**
> str get_schedule_check_option_fields()

View ScheduleCheckOption fields

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
    api_instance = openapi_client.ScheduleCheckOptionApi(api_client)

    try:
        # View ScheduleCheckOption fields
        api_response = api_instance.get_schedule_check_option_fields()
        print("The response of ScheduleCheckOptionApi->get_schedule_check_option_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleCheckOptionApi->get_schedule_check_option_fields: %s\n" % e)
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

# **update_schedule_check_option**
> bool update_schedule_check_option(schedule_check_option, authorization=authorization)

Update ScheduleCheckOption

Send a request to this endpoint to update one or more ScheduleCheckOption. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.schedule_check_option import ScheduleCheckOption
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
    api_instance = openapi_client.ScheduleCheckOptionApi(api_client)
    schedule_check_option = [openapi_client.ScheduleCheckOption()] # List[ScheduleCheckOption] | A list of ScheduleOptions objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ScheduleCheckOption
        api_response = api_instance.update_schedule_check_option(schedule_check_option, authorization=authorization)
        print("The response of ScheduleCheckOptionApi->update_schedule_check_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleCheckOptionApi->update_schedule_check_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_check_option** | [**List[ScheduleCheckOption]**](ScheduleCheckOption.md)| A list of ScheduleOptions objects. | 
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

