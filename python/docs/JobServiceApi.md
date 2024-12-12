# openapi_client.JobServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_global_profile**](JobServiceApi.md#create_global_profile) | **POST** /jobService | Create JobService
[**delete_job_service**](JobServiceApi.md#delete_job_service) | **DELETE** /jobService | Delete JobService
[**get_job_service**](JobServiceApi.md#get_job_service) | **GET** /jobService | Read JobService
[**get_schedule_options_field_length**](JobServiceApi.md#get_schedule_options_field_length) | **GET** /jobService/getFieldLength/{fieldName} | View JobService Field Length
[**get_schedule_options_fields**](JobServiceApi.md#get_schedule_options_fields) | **GET** /jobService/fields | View ScheduleOptions fields
[**update_job_service**](JobServiceApi.md#update_job_service) | **PUT** /jobService | Update JobService


# **create_global_profile**
> str create_global_profile(job_service, authorization=authorization)

Create JobService

Send a request to this endpoint to create one or more JobService. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.job_service import JobService
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
    api_instance = openapi_client.JobServiceApi(api_client)
    job_service = [openapi_client.JobService()] # List[JobService] | A list of user objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create JobService
        api_response = api_instance.create_global_profile(job_service, authorization=authorization)
        print("The response of JobServiceApi->create_global_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobServiceApi->create_global_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_service** | [**List[JobService]**](JobService.md)| A list of user objects. | 
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

# **delete_job_service**
> bool delete_job_service(object_id, authorization=authorization)

Delete JobService

Send a request to this endpoint to delete one or more JobService. An application object will be created for each JSON object provided in the request body

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
    api_instance = openapi_client.JobServiceApi(api_client)
    object_id = '1,2,3' # str | One or more system-generated identifiers of JobService.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete JobService
        api_response = api_instance.delete_job_service(object_id, authorization=authorization)
        print("The response of JobServiceApi->delete_job_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobServiceApi->delete_job_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| One or more system-generated identifiers of JobService. | 
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

# **get_job_service**
> List[JobService] get_job_service(fields, filter=filter, order_by=order_by, authorization=authorization)

Read JobService

Reads JobService objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.job_service import JobService
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
    api_instance = openapi_client.JobServiceApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read JobService
        api_response = api_instance.get_job_service(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of JobServiceApi->get_job_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobServiceApi->get_job_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[JobService]**](JobService.md)

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

# **get_schedule_options_field_length**
> str get_schedule_options_field_length(field_name, authorization=authorization)

View JobService Field Length

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
    api_instance = openapi_client.JobServiceApi(api_client)
    field_name = 'field_name_example' # str | An ScheduleOptions field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View JobService Field Length
        api_response = api_instance.get_schedule_options_field_length(field_name, authorization=authorization)
        print("The response of JobServiceApi->get_schedule_options_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobServiceApi->get_schedule_options_field_length: %s\n" % e)
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

# **get_schedule_options_fields**
> str get_schedule_options_fields()

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
    api_instance = openapi_client.JobServiceApi(api_client)

    try:
        # View ScheduleOptions fields
        api_response = api_instance.get_schedule_options_fields()
        print("The response of JobServiceApi->get_schedule_options_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobServiceApi->get_schedule_options_fields: %s\n" % e)
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

# **update_job_service**
> bool update_job_service(job_service, authorization=authorization)

Update JobService

Send a request to this endpoint to update one or more JobService. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.job_service import JobService
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
    api_instance = openapi_client.JobServiceApi(api_client)
    job_service = [openapi_client.JobService()] # List[JobService] | A list of ScheduleOptions objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update JobService
        api_response = api_instance.update_job_service(job_service, authorization=authorization)
        print("The response of JobServiceApi->update_job_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobServiceApi->update_job_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_service** | [**List[JobService]**](JobService.md)| A list of ScheduleOptions objects. | 
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

