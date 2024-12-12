# openapi_client.ScheduleOptionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_schedule_options**](ScheduleOptionsApi.md#get_schedule_options) | **GET** /scheduleOptions | Read ScheduleOptions
[**get_schedule_options_field_length1**](ScheduleOptionsApi.md#get_schedule_options_field_length1) | **GET** /scheduleOptions/getFieldLength/{fieldName} | View ScheduleOptions Field Length
[**get_schedule_options_fields1**](ScheduleOptionsApi.md#get_schedule_options_fields1) | **GET** /scheduleOptions/fields | View ScheduleOptions fields
[**update_schedule_options**](ScheduleOptionsApi.md#update_schedule_options) | **PUT** /scheduleOptions | Update ScheduleOptions


# **get_schedule_options**
> List[ScheduleOptions] get_schedule_options(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ScheduleOptions

Reads ScheduleOptions objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.schedule_options import ScheduleOptions
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
    api_instance = openapi_client.ScheduleOptionsApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ScheduleOptions
        api_response = api_instance.get_schedule_options(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ScheduleOptionsApi->get_schedule_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleOptionsApi->get_schedule_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ScheduleOptions]**](ScheduleOptions.md)

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

# **get_schedule_options_field_length1**
> str get_schedule_options_field_length1(field_name, authorization=authorization)

View ScheduleOptions Field Length

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
    api_instance = openapi_client.ScheduleOptionsApi(api_client)
    field_name = 'field_name_example' # str | An ScheduleOptions field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ScheduleOptions Field Length
        api_response = api_instance.get_schedule_options_field_length1(field_name, authorization=authorization)
        print("The response of ScheduleOptionsApi->get_schedule_options_field_length1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleOptionsApi->get_schedule_options_field_length1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An ScheduleOptions field. | 
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

# **get_schedule_options_fields1**
> str get_schedule_options_fields1()

View ScheduleOptions fields

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
    api_instance = openapi_client.ScheduleOptionsApi(api_client)

    try:
        # View ScheduleOptions fields
        api_response = api_instance.get_schedule_options_fields1()
        print("The response of ScheduleOptionsApi->get_schedule_options_fields1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleOptionsApi->get_schedule_options_fields1: %s\n" % e)
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

# **update_schedule_options**
> bool update_schedule_options(schedule_options, authorization=authorization)

Update ScheduleOptions

Send a request to this endpoint to update one or more ScheduleOptions. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.schedule_options import ScheduleOptions
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
    api_instance = openapi_client.ScheduleOptionsApi(api_client)
    schedule_options = [openapi_client.ScheduleOptions()] # List[ScheduleOptions] | A list of ScheduleOptions objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ScheduleOptions
        api_response = api_instance.update_schedule_options(schedule_options, authorization=authorization)
        print("The response of ScheduleOptionsApi->update_schedule_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleOptionsApi->update_schedule_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_options** | [**List[ScheduleOptions]**](ScheduleOptions.md)| A list of ScheduleOptions objects. | 
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

