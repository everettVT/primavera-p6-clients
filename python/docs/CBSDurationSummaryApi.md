# openapi_client.CBSDurationSummaryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cbs_duration_summary**](CBSDurationSummaryApi.md#create_cbs_duration_summary) | **POST** /cbsDurationSummary | Create CBSDurationSummarys
[**delete_cbs_duration_summary**](CBSDurationSummaryApi.md#delete_cbs_duration_summary) | **DELETE** /cbsDurationSummary | Delete CBSDurationSummarys
[**get_cbs_duration_summaries**](CBSDurationSummaryApi.md#get_cbs_duration_summaries) | **GET** /cbsDurationSummary | Read CBSDurationSummarys
[**get_cbs_duration_summary_field_length**](CBSDurationSummaryApi.md#get_cbs_duration_summary_field_length) | **GET** /cbsDurationSummary/getFieldLength/{fieldName} | View CBSDurationSummary Field Length
[**get_cbs_duration_summary_fields**](CBSDurationSummaryApi.md#get_cbs_duration_summary_fields) | **GET** /cbsDurationSummary/fields | View CBSDurationSummary fields
[**update_cbs_duration_summary**](CBSDurationSummaryApi.md#update_cbs_duration_summary) | **PUT** /cbsDurationSummary | Update CBSDurationSummarys


# **create_cbs_duration_summary**
> str create_cbs_duration_summary(cbs_duration_summary, authorization=authorization)

Create CBSDurationSummarys

Send a request to this endpoint to create one or more cbsDurationSummary. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.cbs_duration_summary import CBSDurationSummary
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
    api_instance = openapi_client.CBSDurationSummaryApi(api_client)
    cbs_duration_summary = [openapi_client.CBSDurationSummary()] # List[CBSDurationSummary] | A list of cbsDurationSummary objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create CBSDurationSummarys
        api_response = api_instance.create_cbs_duration_summary(cbs_duration_summary, authorization=authorization)
        print("The response of CBSDurationSummaryApi->create_cbs_duration_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CBSDurationSummaryApi->create_cbs_duration_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cbs_duration_summary** | [**List[CBSDurationSummary]**](CBSDurationSummary.md)| A list of cbsDurationSummary objects. | 
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

# **delete_cbs_duration_summary**
> bool delete_cbs_duration_summary(authorization=authorization, object_id=object_id)

Delete CBSDurationSummarys

Send a request to this endpoint to delete one or more cbsDurationSummary. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.CBSDurationSummaryApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of cbsDurationSummary. (optional)

    try:
        # Delete CBSDurationSummarys
        api_response = api_instance.delete_cbs_duration_summary(authorization=authorization, object_id=object_id)
        print("The response of CBSDurationSummaryApi->delete_cbs_duration_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CBSDurationSummaryApi->delete_cbs_duration_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| One or more system-generated identifiers of cbsDurationSummary. | [optional] 

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

# **get_cbs_duration_summaries**
> List[CBSDurationSummary] get_cbs_duration_summaries(fields, filter=filter, order_by=order_by, authorization=authorization)

Read CBSDurationSummarys

Reads CBSDurationSummary objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.cbs_duration_summary import CBSDurationSummary
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
    api_instance = openapi_client.CBSDurationSummaryApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read CBSDurationSummarys
        api_response = api_instance.get_cbs_duration_summaries(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of CBSDurationSummaryApi->get_cbs_duration_summaries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CBSDurationSummaryApi->get_cbs_duration_summaries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[CBSDurationSummary]**](CBSDurationSummary.md)

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

# **get_cbs_duration_summary_field_length**
> str get_cbs_duration_summary_field_length(field_name, authorization=authorization)

View CBSDurationSummary Field Length

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
    api_instance = openapi_client.CBSDurationSummaryApi(api_client)
    field_name = 'field_name_example' # str | A cbsDurationSummary field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View CBSDurationSummary Field Length
        api_response = api_instance.get_cbs_duration_summary_field_length(field_name, authorization=authorization)
        print("The response of CBSDurationSummaryApi->get_cbs_duration_summary_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CBSDurationSummaryApi->get_cbs_duration_summary_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| A cbsDurationSummary field. | 
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

# **get_cbs_duration_summary_fields**
> str get_cbs_duration_summary_fields()

View CBSDurationSummary fields

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
    api_instance = openapi_client.CBSDurationSummaryApi(api_client)

    try:
        # View CBSDurationSummary fields
        api_response = api_instance.get_cbs_duration_summary_fields()
        print("The response of CBSDurationSummaryApi->get_cbs_duration_summary_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CBSDurationSummaryApi->get_cbs_duration_summary_fields: %s\n" % e)
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

# **update_cbs_duration_summary**
> bool update_cbs_duration_summary(cbs_duration_summary, authorization=authorization)

Update CBSDurationSummarys

Send a request to this endpoint to update one or more cbsDurationSummary. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.cbs_duration_summary import CBSDurationSummary
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
    api_instance = openapi_client.CBSDurationSummaryApi(api_client)
    cbs_duration_summary = [openapi_client.CBSDurationSummary()] # List[CBSDurationSummary] | A list of cbsDurationSummary objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update CBSDurationSummarys
        api_response = api_instance.update_cbs_duration_summary(cbs_duration_summary, authorization=authorization)
        print("The response of CBSDurationSummaryApi->update_cbs_duration_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CBSDurationSummaryApi->update_cbs_duration_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cbs_duration_summary** | [**List[CBSDurationSummary]**](CBSDurationSummary.md)| A list of cbsDurationSummary objects. | 
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

