# openapi_client.EPSBudgetChangeLogApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_eps_budget_change_log**](EPSBudgetChangeLogApi.md#create_eps_budget_change_log) | **POST** /epsBudgetChangeLog | Create EPSBudgetChangeLog to the store
[**delete_eps_budget_change_log**](EPSBudgetChangeLogApi.md#delete_eps_budget_change_log) | **DELETE** /epsBudgetChangeLog | Delete EPSBudgetChangeLog
[**get_eps_budget_change_log**](EPSBudgetChangeLogApi.md#get_eps_budget_change_log) | **GET** /epsBudgetChangeLog | Read EPSBudgetChangeLog
[**get_eps_budget_change_log_field_length**](EPSBudgetChangeLogApi.md#get_eps_budget_change_log_field_length) | **GET** /epsBudgetChangeLog/getFieldLength/{fieldName} | View EPSBudgetChangeLog Field Length
[**get_eps_budget_change_log_fields**](EPSBudgetChangeLogApi.md#get_eps_budget_change_log_fields) | **GET** /epsBudgetChangeLog/fields | View EPSBudgetChangeLog fields
[**update_eps_budget_change_log**](EPSBudgetChangeLogApi.md#update_eps_budget_change_log) | **PUT** /epsBudgetChangeLog | Update EPSBudgetChangeLog


# **create_eps_budget_change_log**
> str create_eps_budget_change_log(eps_budget_change_log, authorization=authorization)

Create EPSBudgetChangeLog to the store

Send a request to this endpoint to create one or more Project. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.eps_budget_change_log import EPSBudgetChangeLog
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
    api_instance = openapi_client.EPSBudgetChangeLogApi(api_client)
    eps_budget_change_log = [openapi_client.EPSBudgetChangeLog()] # List[EPSBudgetChangeLog] | A list of EPSBudgetChangeLog objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create EPSBudgetChangeLog to the store
        api_response = api_instance.create_eps_budget_change_log(eps_budget_change_log, authorization=authorization)
        print("The response of EPSBudgetChangeLogApi->create_eps_budget_change_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPSBudgetChangeLogApi->create_eps_budget_change_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eps_budget_change_log** | [**List[EPSBudgetChangeLog]**](EPSBudgetChangeLog.md)| A list of EPSBudgetChangeLog objects. | 
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

# **delete_eps_budget_change_log**
> bool delete_eps_budget_change_log(object_id, authorization=authorization)

Delete EPSBudgetChangeLog

Send a request to this endpoint to delete one or more Project. An application object will be created for each JSON object provided in the request body

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
    api_instance = openapi_client.EPSBudgetChangeLogApi(api_client)
    object_id = '1,2,3' # str | One or more system-generated identifiers of EPSBudgetChangeLog.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete EPSBudgetChangeLog
        api_response = api_instance.delete_eps_budget_change_log(object_id, authorization=authorization)
        print("The response of EPSBudgetChangeLogApi->delete_eps_budget_change_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPSBudgetChangeLogApi->delete_eps_budget_change_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| One or more system-generated identifiers of EPSBudgetChangeLog. | 
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

# **get_eps_budget_change_log**
> List[EPSBudgetChangeLog] get_eps_budget_change_log(fields, filter=filter, order_by=order_by, authorization=authorization)

Read EPSBudgetChangeLog

Reads EPSBudgetChangeLog objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.eps_budget_change_log import EPSBudgetChangeLog
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
    api_instance = openapi_client.EPSBudgetChangeLogApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read EPSBudgetChangeLog
        api_response = api_instance.get_eps_budget_change_log(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of EPSBudgetChangeLogApi->get_eps_budget_change_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPSBudgetChangeLogApi->get_eps_budget_change_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[EPSBudgetChangeLog]**](EPSBudgetChangeLog.md)

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

# **get_eps_budget_change_log_field_length**
> str get_eps_budget_change_log_field_length(field_name, authorization=authorization)

View EPSBudgetChangeLog Field Length

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
    api_instance = openapi_client.EPSBudgetChangeLogApi(api_client)
    field_name = 'field_name_example' # str | An EPSBudgetChangeLog field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View EPSBudgetChangeLog Field Length
        api_response = api_instance.get_eps_budget_change_log_field_length(field_name, authorization=authorization)
        print("The response of EPSBudgetChangeLogApi->get_eps_budget_change_log_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPSBudgetChangeLogApi->get_eps_budget_change_log_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An EPSBudgetChangeLog field. | 
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

# **get_eps_budget_change_log_fields**
> str get_eps_budget_change_log_fields()

View EPSBudgetChangeLog fields

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
    api_instance = openapi_client.EPSBudgetChangeLogApi(api_client)

    try:
        # View EPSBudgetChangeLog fields
        api_response = api_instance.get_eps_budget_change_log_fields()
        print("The response of EPSBudgetChangeLogApi->get_eps_budget_change_log_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPSBudgetChangeLogApi->get_eps_budget_change_log_fields: %s\n" % e)
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

# **update_eps_budget_change_log**
> bool update_eps_budget_change_log(eps_budget_change_log, authorization=authorization)

Update EPSBudgetChangeLog

Send a request to this endpoint to update one or more Project. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.eps_budget_change_log import EPSBudgetChangeLog
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
    api_instance = openapi_client.EPSBudgetChangeLogApi(api_client)
    eps_budget_change_log = [openapi_client.EPSBudgetChangeLog()] # List[EPSBudgetChangeLog] | A list of EPSBudgetChangeLog objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update EPSBudgetChangeLog
        api_response = api_instance.update_eps_budget_change_log(eps_budget_change_log, authorization=authorization)
        print("The response of EPSBudgetChangeLogApi->update_eps_budget_change_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPSBudgetChangeLogApi->update_eps_budget_change_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eps_budget_change_log** | [**List[EPSBudgetChangeLog]**](EPSBudgetChangeLog.md)| A list of EPSBudgetChangeLog objects. | 
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

