# openapi_client.TimesheetApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_timesheet**](TimesheetApi.md#create_timesheet) | **POST** /timesheet | Create Timesheet
[**delete_timesheet**](TimesheetApi.md#delete_timesheet) | **DELETE** /timesheet | Delete Timesheet
[**get_timesheet**](TimesheetApi.md#get_timesheet) | **GET** /timesheet | Read Timesheet
[**get_timesheet_field_length**](TimesheetApi.md#get_timesheet_field_length) | **GET** /timesheet/getFieldLength/{fieldName} | View Timesheet Field Length
[**get_timesheet_fields**](TimesheetApi.md#get_timesheet_fields) | **GET** /timesheet/fields | View Timesheet fields
[**update_timesheet**](TimesheetApi.md#update_timesheet) | **PUT** /timesheet | Update Timesheet


# **create_timesheet**
> List[CreateTimesheetsResponse] create_timesheet(timesheet, authorization=authorization)

Create Timesheet

Send a request to this endpoint to create one or more timesheet. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.create_timesheets_response import CreateTimesheetsResponse
from openapi_client.models.timesheet import Timesheet
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
    api_instance = openapi_client.TimesheetApi(api_client)
    timesheet = [openapi_client.Timesheet()] # List[Timesheet] | A list of timesheet objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create Timesheet
        api_response = api_instance.create_timesheet(timesheet, authorization=authorization)
        print("The response of TimesheetApi->create_timesheet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimesheetApi->create_timesheet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timesheet** | [**List[Timesheet]**](Timesheet.md)| A list of timesheet objects. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[CreateTimesheetsResponse]**](CreateTimesheetsResponse.md)

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

# **delete_timesheet**
> bool delete_timesheet(timesheet, authorization=authorization)

Delete Timesheet

Send a request to this endpoint to delete one or more timesheet. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.timesheet import Timesheet
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
    api_instance = openapi_client.TimesheetApi(api_client)
    timesheet = [openapi_client.Timesheet()] # List[Timesheet] | <p>A list of timesheet objects.<p><p>Required fields: You must supply both the ResourceObjectId and TimesheetPeriodObjectId fields when you use the Delete timesheet operation. All other fields are optional.</p>
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete Timesheet
        api_response = api_instance.delete_timesheet(timesheet, authorization=authorization)
        print("The response of TimesheetApi->delete_timesheet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimesheetApi->delete_timesheet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timesheet** | [**List[Timesheet]**](Timesheet.md)| &lt;p&gt;A list of timesheet objects.&lt;p&gt;&lt;p&gt;Required fields: You must supply both the ResourceObjectId and TimesheetPeriodObjectId fields when you use the Delete timesheet operation. All other fields are optional.&lt;/p&gt; | 
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

# **get_timesheet**
> List[Timesheet] get_timesheet(fields, filter=filter, order_by=order_by, authorization=authorization)

Read Timesheet

Reads timesheet objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.timesheet import Timesheet
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
    api_instance = openapi_client.TimesheetApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read Timesheet
        api_response = api_instance.get_timesheet(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of TimesheetApi->get_timesheet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimesheetApi->get_timesheet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[Timesheet]**](Timesheet.md)

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

# **get_timesheet_field_length**
> str get_timesheet_field_length(field_name, authorization=authorization)

View Timesheet Field Length

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
    api_instance = openapi_client.TimesheetApi(api_client)
    field_name = 'field_name_example' # str | An timesheet field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View Timesheet Field Length
        api_response = api_instance.get_timesheet_field_length(field_name, authorization=authorization)
        print("The response of TimesheetApi->get_timesheet_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimesheetApi->get_timesheet_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An timesheet field. | 
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

# **get_timesheet_fields**
> str get_timesheet_fields()

View Timesheet fields

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
    api_instance = openapi_client.TimesheetApi(api_client)

    try:
        # View Timesheet fields
        api_response = api_instance.get_timesheet_fields()
        print("The response of TimesheetApi->get_timesheet_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimesheetApi->get_timesheet_fields: %s\n" % e)
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

# **update_timesheet**
> bool update_timesheet(timesheet, authorization=authorization)

Update Timesheet

Send a request to this endpoint to update one or more timesheet. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.timesheet import Timesheet
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
    api_instance = openapi_client.TimesheetApi(api_client)
    timesheet = [openapi_client.Timesheet()] # List[Timesheet] | <p>A list of timesheet objects.<p><p>Required fields: You must supply both the ResourceObjectId and TimesheetPeriodObjectId fields when you use the Update timesheet operation. All other fields are optional.</p>
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update Timesheet
        api_response = api_instance.update_timesheet(timesheet, authorization=authorization)
        print("The response of TimesheetApi->update_timesheet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimesheetApi->update_timesheet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timesheet** | [**List[Timesheet]**](Timesheet.md)| &lt;p&gt;A list of timesheet objects.&lt;p&gt;&lt;p&gt;Required fields: You must supply both the ResourceObjectId and TimesheetPeriodObjectId fields when you use the Update timesheet operation. All other fields are optional.&lt;/p&gt; | 
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

