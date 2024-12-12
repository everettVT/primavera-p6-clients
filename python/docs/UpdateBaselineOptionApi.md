# openapi_client.UpdateBaselineOptionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_update_baseline_option**](UpdateBaselineOptionApi.md#get_update_baseline_option) | **GET** /updateBaselineOption | Read UpdateBaselineOption
[**get_update_baseline_option_field_length**](UpdateBaselineOptionApi.md#get_update_baseline_option_field_length) | **GET** /updateBaselineOption/getFieldLength/{fieldName} | View UpdateBaselineOption Field Length
[**get_update_baseline_option_fields**](UpdateBaselineOptionApi.md#get_update_baseline_option_fields) | **GET** /updateBaselineOption/fields | View UpdateBaselineOption fields
[**update_update_baseline_option**](UpdateBaselineOptionApi.md#update_update_baseline_option) | **PUT** /updateBaselineOption | Update UpdateBaselineOption


# **get_update_baseline_option**
> List[UpdateBaselineOption] get_update_baseline_option(fields, filter=filter, order_by=order_by, authorization=authorization)

Read UpdateBaselineOption

Reads UpdateBaselineOption objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.update_baseline_option import UpdateBaselineOption
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
    api_instance = openapi_client.UpdateBaselineOptionApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read UpdateBaselineOption
        api_response = api_instance.get_update_baseline_option(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of UpdateBaselineOptionApi->get_update_baseline_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpdateBaselineOptionApi->get_update_baseline_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[UpdateBaselineOption]**](UpdateBaselineOption.md)

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

# **get_update_baseline_option_field_length**
> str get_update_baseline_option_field_length(field_name, authorization=authorization)

View UpdateBaselineOption Field Length

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
    api_instance = openapi_client.UpdateBaselineOptionApi(api_client)
    field_name = 'field_name_example' # str | An UpdateBaselineOption field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View UpdateBaselineOption Field Length
        api_response = api_instance.get_update_baseline_option_field_length(field_name, authorization=authorization)
        print("The response of UpdateBaselineOptionApi->get_update_baseline_option_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpdateBaselineOptionApi->get_update_baseline_option_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An UpdateBaselineOption field. | 
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

# **get_update_baseline_option_fields**
> str get_update_baseline_option_fields()

View UpdateBaselineOption fields

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
    api_instance = openapi_client.UpdateBaselineOptionApi(api_client)

    try:
        # View UpdateBaselineOption fields
        api_response = api_instance.get_update_baseline_option_fields()
        print("The response of UpdateBaselineOptionApi->get_update_baseline_option_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpdateBaselineOptionApi->get_update_baseline_option_fields: %s\n" % e)
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

# **update_update_baseline_option**
> bool update_update_baseline_option(update_baseline_option, authorization=authorization)

Update UpdateBaselineOption

Send a request to this endpoint to update one or more UpdateBaselineOption. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.update_baseline_option import UpdateBaselineOption
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
    api_instance = openapi_client.UpdateBaselineOptionApi(api_client)
    update_baseline_option = [openapi_client.UpdateBaselineOption()] # List[UpdateBaselineOption] | A list of UpdateBaselineOption objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update UpdateBaselineOption
        api_response = api_instance.update_update_baseline_option(update_baseline_option, authorization=authorization)
        print("The response of UpdateBaselineOptionApi->update_update_baseline_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpdateBaselineOptionApi->update_update_baseline_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_baseline_option** | [**List[UpdateBaselineOption]**](UpdateBaselineOption.md)| A list of UpdateBaselineOption objects. | 
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

