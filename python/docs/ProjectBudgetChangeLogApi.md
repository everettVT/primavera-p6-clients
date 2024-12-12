# openapi_client.ProjectBudgetChangeLogApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_budget_change_log**](ProjectBudgetChangeLogApi.md#create_project_budget_change_log) | **POST** /projectBudgetChangeLog | Create ProjectBudgetChangeLog
[**delete_project_budget_change_log**](ProjectBudgetChangeLogApi.md#delete_project_budget_change_log) | **DELETE** /projectBudgetChangeLog | Delete ProjectBudgetChangeLog
[**get_project_budget_change_log**](ProjectBudgetChangeLogApi.md#get_project_budget_change_log) | **GET** /projectBudgetChangeLog | Read ProjectBudgetChangeLog
[**get_project_budget_change_log_field_length**](ProjectBudgetChangeLogApi.md#get_project_budget_change_log_field_length) | **GET** /projectBudgetChangeLog/getFieldLength/{fieldName} | View ProjectBudgetChangeLog Field Length
[**get_project_budget_change_log_fields**](ProjectBudgetChangeLogApi.md#get_project_budget_change_log_fields) | **GET** /projectBudgetChangeLog/fields | View ProjectBudgetChangeLog fields
[**update_project_budget_change_log**](ProjectBudgetChangeLogApi.md#update_project_budget_change_log) | **PUT** /projectBudgetChangeLog | Update ProjectBudgetChangeLog


# **create_project_budget_change_log**
> str create_project_budget_change_log(project_budget_change_log, authorization=authorization)

Create ProjectBudgetChangeLog

Send a request to this endpoint to create one or more ProjectBudgetChangeLog. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.project_budget_change_log import ProjectBudgetChangeLog
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
    api_instance = openapi_client.ProjectBudgetChangeLogApi(api_client)
    project_budget_change_log = [openapi_client.ProjectBudgetChangeLog()] # List[ProjectBudgetChangeLog] | A list of projectbudgetchangelog objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ProjectBudgetChangeLog
        api_response = api_instance.create_project_budget_change_log(project_budget_change_log, authorization=authorization)
        print("The response of ProjectBudgetChangeLogApi->create_project_budget_change_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectBudgetChangeLogApi->create_project_budget_change_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_budget_change_log** | [**List[ProjectBudgetChangeLog]**](ProjectBudgetChangeLog.md)| A list of projectbudgetchangelog objects. | 
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

# **delete_project_budget_change_log**
> bool delete_project_budget_change_log(object_id, authorization=authorization)

Delete ProjectBudgetChangeLog

Send a request to this endpoint to delete one or more ProjectBudgetChangeLog. An application object will be created for each JSON object provided in the request body

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
    api_instance = openapi_client.ProjectBudgetChangeLogApi(api_client)
    object_id = '1,2,3' # str | One or more system-generated identifiers of projectbudgetchangelog.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete ProjectBudgetChangeLog
        api_response = api_instance.delete_project_budget_change_log(object_id, authorization=authorization)
        print("The response of ProjectBudgetChangeLogApi->delete_project_budget_change_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectBudgetChangeLogApi->delete_project_budget_change_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| One or more system-generated identifiers of projectbudgetchangelog. | 
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

# **get_project_budget_change_log**
> List[ProjectBudgetChangeLog] get_project_budget_change_log(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ProjectBudgetChangeLog

Reads ProjectBudgetChangeLog objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.project_budget_change_log import ProjectBudgetChangeLog
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
    api_instance = openapi_client.ProjectBudgetChangeLogApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ProjectBudgetChangeLog
        api_response = api_instance.get_project_budget_change_log(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ProjectBudgetChangeLogApi->get_project_budget_change_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectBudgetChangeLogApi->get_project_budget_change_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ProjectBudgetChangeLog]**](ProjectBudgetChangeLog.md)

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

# **get_project_budget_change_log_field_length**
> str get_project_budget_change_log_field_length(field_name, authorization=authorization)

View ProjectBudgetChangeLog Field Length

Returns length of variable character fields for a BO.

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
    api_instance = openapi_client.ProjectBudgetChangeLogApi(api_client)
    field_name = 'field_name_example' # str | An projectbudgetchangelog field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ProjectBudgetChangeLog Field Length
        api_response = api_instance.get_project_budget_change_log_field_length(field_name, authorization=authorization)
        print("The response of ProjectBudgetChangeLogApi->get_project_budget_change_log_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectBudgetChangeLogApi->get_project_budget_change_log_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An projectbudgetchangelog field. | 
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

# **get_project_budget_change_log_fields**
> str get_project_budget_change_log_fields()

View ProjectBudgetChangeLog fields

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
    api_instance = openapi_client.ProjectBudgetChangeLogApi(api_client)

    try:
        # View ProjectBudgetChangeLog fields
        api_response = api_instance.get_project_budget_change_log_fields()
        print("The response of ProjectBudgetChangeLogApi->get_project_budget_change_log_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectBudgetChangeLogApi->get_project_budget_change_log_fields: %s\n" % e)
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

# **update_project_budget_change_log**
> bool update_project_budget_change_log(project_budget_change_log, authorization=authorization)

Update ProjectBudgetChangeLog

Send a request to this endpoint to update one or more ProjectBudgetChangeLog. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.project_budget_change_log import ProjectBudgetChangeLog
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
    api_instance = openapi_client.ProjectBudgetChangeLogApi(api_client)
    project_budget_change_log = [openapi_client.ProjectBudgetChangeLog()] # List[ProjectBudgetChangeLog] | A list of projectbudgetchangelog objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ProjectBudgetChangeLog
        api_response = api_instance.update_project_budget_change_log(project_budget_change_log, authorization=authorization)
        print("The response of ProjectBudgetChangeLogApi->update_project_budget_change_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectBudgetChangeLogApi->update_project_budget_change_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_budget_change_log** | [**List[ProjectBudgetChangeLog]**](ProjectBudgetChangeLog.md)| A list of projectbudgetchangelog objects. | 
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

