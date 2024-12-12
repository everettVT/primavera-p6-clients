# openapi_client.CalendarApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_calendar**](CalendarApi.md#create_calendar) | **POST** /calendar | Create Calendars
[**delete_calendar**](CalendarApi.md#delete_calendar) | **DELETE** /calendar | Delete Calendars
[**get_calendar_detailed_work_hours**](CalendarApi.md#get_calendar_detailed_work_hours) | **GET** /calendar/detailedWorkHours | Load Calendar DetailedWorkHours
[**get_calendar_field_length**](CalendarApi.md#get_calendar_field_length) | **GET** /calendar/getFieldLength/{fieldName} | View Calendar Field Length
[**get_calendar_fields**](CalendarApi.md#get_calendar_fields) | **GET** /calendar/fields | View Calendar fields
[**get_calendar_holiday_exception_dates**](CalendarApi.md#get_calendar_holiday_exception_dates) | **GET** /calendar/holidayExceptionDates | Load Calendar HolidayExceptionDates
[**get_calendar_standard_detailed_work_hours**](CalendarApi.md#get_calendar_standard_detailed_work_hours) | **GET** /calendar/standardDetailedWorkHours | Load Calendar StandardDetailedWorkHours
[**get_calendar_standard_total_work_hours**](CalendarApi.md#get_calendar_standard_total_work_hours) | **GET** /calendar/standardTotalWorkHours | Load Calendar StandardTotalWorkHours
[**get_calendar_total_work_hours**](CalendarApi.md#get_calendar_total_work_hours) | **GET** /calendar/totalWorkHours | Load Calendar TotalWorkHours
[**get_calendars**](CalendarApi.md#get_calendars) | **GET** /calendar | Read Calendars
[**update_calendar**](CalendarApi.md#update_calendar) | **PUT** /calendar | Update Calendars
[**update_calendar_detailed_work_hours**](CalendarApi.md#update_calendar_detailed_work_hours) | **PUT** /calendar/detailedWorkHours | Update DetailedWorkHours of Calendar
[**update_calendar_standard_detailed_work_hours**](CalendarApi.md#update_calendar_standard_detailed_work_hours) | **PUT** /calendar/standardDetailedWorkHours | Update StandardDetailedWorkHours of Calendar


# **create_calendar**
> str create_calendar(calendar, authorization=authorization)

Create Calendars

Send a request to this endpoint to create one or more calendar. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.calendar import Calendar
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
    api_instance = openapi_client.CalendarApi(api_client)
    calendar = [openapi_client.Calendar()] # List[Calendar] | A list of calendar objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create Calendars
        api_response = api_instance.create_calendar(calendar, authorization=authorization)
        print("The response of CalendarApi->create_calendar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarApi->create_calendar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calendar** | [**List[Calendar]**](Calendar.md)| A list of calendar objects. | 
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

# **delete_calendar**
> bool delete_calendar(authorization=authorization, object_id=object_id)

Delete Calendars

Send a request to this endpoint to delete one or more calendar. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.CalendarApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | Calendar to delete (optional)

    try:
        # Delete Calendars
        api_response = api_instance.delete_calendar(authorization=authorization, object_id=object_id)
        print("The response of CalendarApi->delete_calendar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarApi->delete_calendar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| Calendar to delete | [optional] 

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

# **get_calendar_detailed_work_hours**
> str get_calendar_detailed_work_hours(filter, authorization=authorization)

Load Calendar DetailedWorkHours

Returns Calendar DetailedWorkHours

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
    api_instance = openapi_client.CalendarApi(api_client)
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or:
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Load Calendar DetailedWorkHours
        api_response = api_instance.get_calendar_detailed_work_hours(filter, authorization=authorization)
        print("The response of CalendarApi->get_calendar_detailed_work_hours:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarApi->get_calendar_detailed_work_hours: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | 
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

# **get_calendar_field_length**
> str get_calendar_field_length(field_name, authorization=authorization)

View Calendar Field Length

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
    api_instance = openapi_client.CalendarApi(api_client)
    field_name = 'field_name_example' # str | Field to retun length
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View Calendar Field Length
        api_response = api_instance.get_calendar_field_length(field_name, authorization=authorization)
        print("The response of CalendarApi->get_calendar_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarApi->get_calendar_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| Field to retun length | 
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

# **get_calendar_fields**
> str get_calendar_fields()

View Calendar fields

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
    api_instance = openapi_client.CalendarApi(api_client)

    try:
        # View Calendar fields
        api_response = api_instance.get_calendar_fields()
        print("The response of CalendarApi->get_calendar_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarApi->get_calendar_fields: %s\n" % e)
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

# **get_calendar_holiday_exception_dates**
> str get_calendar_holiday_exception_dates(filter, authorization=authorization)

Load Calendar HolidayExceptionDates

Returns Calendar HolidayExceptionDates

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
    api_instance = openapi_client.CalendarApi(api_client)
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or:
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Load Calendar HolidayExceptionDates
        api_response = api_instance.get_calendar_holiday_exception_dates(filter, authorization=authorization)
        print("The response of CalendarApi->get_calendar_holiday_exception_dates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarApi->get_calendar_holiday_exception_dates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | 
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

# **get_calendar_standard_detailed_work_hours**
> str get_calendar_standard_detailed_work_hours(filter, authorization=authorization)

Load Calendar StandardDetailedWorkHours

Returns Calendar StandardDetailedWorkHours

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
    api_instance = openapi_client.CalendarApi(api_client)
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or:
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Load Calendar StandardDetailedWorkHours
        api_response = api_instance.get_calendar_standard_detailed_work_hours(filter, authorization=authorization)
        print("The response of CalendarApi->get_calendar_standard_detailed_work_hours:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarApi->get_calendar_standard_detailed_work_hours: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | 
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

# **get_calendar_standard_total_work_hours**
> str get_calendar_standard_total_work_hours(filter, authorization=authorization)

Load Calendar StandardTotalWorkHours

Returns Calendar StandardTotalWorkHours

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
    api_instance = openapi_client.CalendarApi(api_client)
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or:
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Load Calendar StandardTotalWorkHours
        api_response = api_instance.get_calendar_standard_total_work_hours(filter, authorization=authorization)
        print("The response of CalendarApi->get_calendar_standard_total_work_hours:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarApi->get_calendar_standard_total_work_hours: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | 
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

# **get_calendar_total_work_hours**
> str get_calendar_total_work_hours(filter, authorization=authorization)

Load Calendar TotalWorkHours

Returns Calendar TotalWorkHours

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
    api_instance = openapi_client.CalendarApi(api_client)
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or:
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Load Calendar TotalWorkHours
        api_response = api_instance.get_calendar_total_work_hours(filter, authorization=authorization)
        print("The response of CalendarApi->get_calendar_total_work_hours:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarApi->get_calendar_total_work_hours: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | 
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

# **get_calendars**
> List[Calendar] get_calendars(fields, filter=filter, order_by=order_by, authorization=authorization)

Read Calendars

Reads Calendar objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.calendar import Calendar
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
    api_instance = openapi_client.CalendarApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read Calendars
        api_response = api_instance.get_calendars(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of CalendarApi->get_calendars:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarApi->get_calendars: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[Calendar]**](Calendar.md)

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

# **update_calendar**
> bool update_calendar(calendar, authorization=authorization)

Update Calendars

Send a request to this endpoint to update one or more calendar. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.calendar import Calendar
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
    api_instance = openapi_client.CalendarApi(api_client)
    calendar = [openapi_client.Calendar()] # List[Calendar] | A list of calendar objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update Calendars
        api_response = api_instance.update_calendar(calendar, authorization=authorization)
        print("The response of CalendarApi->update_calendar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarApi->update_calendar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calendar** | [**List[Calendar]**](Calendar.md)| A list of calendar objects. | 
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

# **update_calendar_detailed_work_hours**
> bool update_calendar_detailed_work_hours(request_body, authorization=authorization)

Update DetailedWorkHours of Calendar

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
    api_instance = openapi_client.CalendarApi(api_client)
    request_body = None # Dict[str, object] | DetailedWorkHours of Calendar object that needs to be added to the store
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update DetailedWorkHours of Calendar
        api_response = api_instance.update_calendar_detailed_work_hours(request_body, authorization=authorization)
        print("The response of CalendarApi->update_calendar_detailed_work_hours:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarApi->update_calendar_detailed_work_hours: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)| DetailedWorkHours of Calendar object that needs to be added to the store | 
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

# **update_calendar_standard_detailed_work_hours**
> bool update_calendar_standard_detailed_work_hours(request_body, authorization=authorization)

Update StandardDetailedWorkHours of Calendar

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
    api_instance = openapi_client.CalendarApi(api_client)
    request_body = None # Dict[str, object] | StandardDetailedWorkHours of Calendar object that needs to be added to the store
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update StandardDetailedWorkHours of Calendar
        api_response = api_instance.update_calendar_standard_detailed_work_hours(request_body, authorization=authorization)
        print("The response of CalendarApi->update_calendar_standard_detailed_work_hours:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarApi->update_calendar_standard_detailed_work_hours: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)| StandardDetailedWorkHours of Calendar object that needs to be added to the store | 
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

