# openapi_client.FinancialPeriodApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_financial_period**](FinancialPeriodApi.md#create_financial_period) | **POST** /financialPeriod | Create FinancialPeriods
[**delete_financial_period**](FinancialPeriodApi.md#delete_financial_period) | **DELETE** /financialPeriod | Delete FinancialPeriods
[**get_financial_period**](FinancialPeriodApi.md#get_financial_period) | **GET** /financialPeriod | Read FinancialPeriods
[**get_financial_period_field_length**](FinancialPeriodApi.md#get_financial_period_field_length) | **GET** /financialPeriod/getFieldLength/{fieldName} | View FinancialPeriod Field Length
[**get_financial_period_fields**](FinancialPeriodApi.md#get_financial_period_fields) | **GET** /financialPeriod/fields | View FinancialPeriod fields
[**update_financial_period**](FinancialPeriodApi.md#update_financial_period) | **PUT** /financialPeriod | Update FinancialPeriods


# **create_financial_period**
> str create_financial_period(financial_period, authorization=authorization)

Create FinancialPeriods

Send a request to this endpoint to create one or more financialPeriod. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.financial_period import FinancialPeriod
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
    api_instance = openapi_client.FinancialPeriodApi(api_client)
    financial_period = [openapi_client.FinancialPeriod()] # List[FinancialPeriod] | A list of financialPeriod objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create FinancialPeriods
        api_response = api_instance.create_financial_period(financial_period, authorization=authorization)
        print("The response of FinancialPeriodApi->create_financial_period:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialPeriodApi->create_financial_period: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **financial_period** | [**List[FinancialPeriod]**](FinancialPeriod.md)| A list of financialPeriod objects. | 
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

# **delete_financial_period**
> bool delete_financial_period(authorization=authorization, object_id=object_id)

Delete FinancialPeriods

Send a request to this endpoint to delete one or more financialPeriod. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.FinancialPeriodApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of financialPeriod. (optional)

    try:
        # Delete FinancialPeriods
        api_response = api_instance.delete_financial_period(authorization=authorization, object_id=object_id)
        print("The response of FinancialPeriodApi->delete_financial_period:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialPeriodApi->delete_financial_period: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| One or more system-generated identifiers of financialPeriod. | [optional] 

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

# **get_financial_period**
> List[FinancialPeriod] get_financial_period(fields, filter=filter, order_by=order_by, authorization=authorization)

Read FinancialPeriods

Reads FinancialPeriod objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.financial_period import FinancialPeriod
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
    api_instance = openapi_client.FinancialPeriodApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read FinancialPeriods
        api_response = api_instance.get_financial_period(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of FinancialPeriodApi->get_financial_period:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialPeriodApi->get_financial_period: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[FinancialPeriod]**](FinancialPeriod.md)

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

# **get_financial_period_field_length**
> str get_financial_period_field_length(field_name, authorization=authorization)

View FinancialPeriod Field Length

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
    api_instance = openapi_client.FinancialPeriodApi(api_client)
    field_name = 'field_name_example' # str | A financialPeriod field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View FinancialPeriod Field Length
        api_response = api_instance.get_financial_period_field_length(field_name, authorization=authorization)
        print("The response of FinancialPeriodApi->get_financial_period_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialPeriodApi->get_financial_period_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| A financialPeriod field. | 
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

# **get_financial_period_fields**
> str get_financial_period_fields()

View FinancialPeriod fields

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
    api_instance = openapi_client.FinancialPeriodApi(api_client)

    try:
        # View FinancialPeriod fields
        api_response = api_instance.get_financial_period_fields()
        print("The response of FinancialPeriodApi->get_financial_period_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialPeriodApi->get_financial_period_fields: %s\n" % e)
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

# **update_financial_period**
> bool update_financial_period(financial_period, authorization=authorization)

Update FinancialPeriods

Send a request to this endpoint to update one or more financialPeriod. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.financial_period import FinancialPeriod
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
    api_instance = openapi_client.FinancialPeriodApi(api_client)
    financial_period = [openapi_client.FinancialPeriod()] # List[FinancialPeriod] | A list of financialPeriod objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update FinancialPeriods
        api_response = api_instance.update_financial_period(financial_period, authorization=authorization)
        print("The response of FinancialPeriodApi->update_financial_period:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialPeriodApi->update_financial_period: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **financial_period** | [**List[FinancialPeriod]**](FinancialPeriod.md)| A list of financialPeriod objects. | 
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

