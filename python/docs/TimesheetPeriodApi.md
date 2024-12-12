# openapi_client.TimesheetPeriodApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_timesheet_period**](TimesheetPeriodApi.md#create_timesheet_period) | **POST** /timesheetPeriod | Create TimesheetPeriods
[**delete_timesheet_period**](TimesheetPeriodApi.md#delete_timesheet_period) | **DELETE** /timesheetPeriod | Delete TimesheetPeriods
[**get_timesheet_period**](TimesheetPeriodApi.md#get_timesheet_period) | **GET** /timesheetPeriod | Read TimesheetPeriods
[**get_timesheet_period_field_length**](TimesheetPeriodApi.md#get_timesheet_period_field_length) | **GET** /timesheetPeriod/getFieldLength/{fieldName} | View TimesheetPeriod Field Length
[**get_timesheet_period_fields**](TimesheetPeriodApi.md#get_timesheet_period_fields) | **GET** /timesheetPeriod/fields | View TimesheetPeriod fields
[**update_timesheet_period**](TimesheetPeriodApi.md#update_timesheet_period) | **PUT** /timesheetPeriod | Update TimesheetPeriods


# **create_timesheet_period**
> str create_timesheet_period(timesheet_period, authorization=authorization)

Create TimesheetPeriods

Send a request to this endpoint to create one or more timesheetPeriod. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.timesheet_period import TimesheetPeriod
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
    api_instance = openapi_client.TimesheetPeriodApi(api_client)
    timesheet_period = [openapi_client.TimesheetPeriod()] # List[TimesheetPeriod] | A list of timesheetPeriod objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create TimesheetPeriods
        api_response = api_instance.create_timesheet_period(timesheet_period, authorization=authorization)
        print("The response of TimesheetPeriodApi->create_timesheet_period:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimesheetPeriodApi->create_timesheet_period: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timesheet_period** | [**List[TimesheetPeriod]**](TimesheetPeriod.md)| A list of timesheetPeriod objects. | 
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

# **delete_timesheet_period**
> bool delete_timesheet_period(authorization=authorization, object_id=object_id)

Delete TimesheetPeriods

Send a request to this endpoint to delete one or more timesheetPeriod. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.TimesheetPeriodApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of timesheetPeriod. (optional)

    try:
        # Delete TimesheetPeriods
        api_response = api_instance.delete_timesheet_period(authorization=authorization, object_id=object_id)
        print("The response of TimesheetPeriodApi->delete_timesheet_period:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimesheetPeriodApi->delete_timesheet_period: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| One or more system-generated identifiers of timesheetPeriod. | [optional] 

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

# **get_timesheet_period**
> List[TimesheetPeriod] get_timesheet_period(fields, filter=filter, order_by=order_by, authorization=authorization)

Read TimesheetPeriods

Reads TimesheetPeriod objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.timesheet_period import TimesheetPeriod
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
    api_instance = openapi_client.TimesheetPeriodApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read TimesheetPeriods
        api_response = api_instance.get_timesheet_period(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of TimesheetPeriodApi->get_timesheet_period:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimesheetPeriodApi->get_timesheet_period: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[TimesheetPeriod]**](TimesheetPeriod.md)

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

# **get_timesheet_period_field_length**
> str get_timesheet_period_field_length(field_name, authorization=authorization)

View TimesheetPeriod Field Length

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
    api_instance = openapi_client.TimesheetPeriodApi(api_client)
    field_name = 'field_name_example' # str | A timesheetPeriod field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View TimesheetPeriod Field Length
        api_response = api_instance.get_timesheet_period_field_length(field_name, authorization=authorization)
        print("The response of TimesheetPeriodApi->get_timesheet_period_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimesheetPeriodApi->get_timesheet_period_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| A timesheetPeriod field. | 
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

# **get_timesheet_period_fields**
> str get_timesheet_period_fields()

View TimesheetPeriod fields

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
    api_instance = openapi_client.TimesheetPeriodApi(api_client)

    try:
        # View TimesheetPeriod fields
        api_response = api_instance.get_timesheet_period_fields()
        print("The response of TimesheetPeriodApi->get_timesheet_period_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimesheetPeriodApi->get_timesheet_period_fields: %s\n" % e)
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

# **update_timesheet_period**
> bool update_timesheet_period(timesheet_period, authorization=authorization)

Update TimesheetPeriods

Send a request to this endpoint to update one or more timesheetPeriod. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.timesheet_period import TimesheetPeriod
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
    api_instance = openapi_client.TimesheetPeriodApi(api_client)
    timesheet_period = [openapi_client.TimesheetPeriod()] # List[TimesheetPeriod] | A list of timesheetPeriod objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update TimesheetPeriods
        api_response = api_instance.update_timesheet_period(timesheet_period, authorization=authorization)
        print("The response of TimesheetPeriodApi->update_timesheet_period:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimesheetPeriodApi->update_timesheet_period: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timesheet_period** | [**List[TimesheetPeriod]**](TimesheetPeriod.md)| A list of timesheetPeriod objects. | 
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

