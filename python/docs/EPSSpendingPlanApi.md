# openapi_client.EPSSpendingPlanApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_eps_spending_plan**](EPSSpendingPlanApi.md#create_eps_spending_plan) | **POST** /epsSpendingPlan | Create EPSSpendingPlan
[**delete_eps_spending_plan**](EPSSpendingPlanApi.md#delete_eps_spending_plan) | **DELETE** /epsSpendingPlan | Delete EPSSpendingPlan
[**get_eps_spending_plan**](EPSSpendingPlanApi.md#get_eps_spending_plan) | **GET** /epsSpendingPlan | Read EPSSpendingPlan
[**get_eps_spending_plan_field_length**](EPSSpendingPlanApi.md#get_eps_spending_plan_field_length) | **GET** /epsSpendingPlan/getFieldLength/{fieldName} | View EPSSpendingPlan Field Length
[**get_eps_spending_plan_fields**](EPSSpendingPlanApi.md#get_eps_spending_plan_fields) | **GET** /epsSpendingPlan/fields | View EPSSpendingPlan fields
[**update_eps_spending_plan**](EPSSpendingPlanApi.md#update_eps_spending_plan) | **PUT** /epsSpendingPlan | Update EPSSpendingPlan


# **create_eps_spending_plan**
> str create_eps_spending_plan(eps_spending_plan, authorization=authorization)

Create EPSSpendingPlan

Send a request to this endpoint to create one or more EPSSpendingPlan. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.eps_spending_plan import EPSSpendingPlan
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
    api_instance = openapi_client.EPSSpendingPlanApi(api_client)
    eps_spending_plan = [openapi_client.EPSSpendingPlan()] # List[EPSSpendingPlan] | A list of EPSSpendingPlan objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create EPSSpendingPlan
        api_response = api_instance.create_eps_spending_plan(eps_spending_plan, authorization=authorization)
        print("The response of EPSSpendingPlanApi->create_eps_spending_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPSSpendingPlanApi->create_eps_spending_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eps_spending_plan** | [**List[EPSSpendingPlan]**](EPSSpendingPlan.md)| A list of EPSSpendingPlan objects. | 
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

# **delete_eps_spending_plan**
> bool delete_eps_spending_plan(object_id, authorization=authorization)

Delete EPSSpendingPlan

Send a request to this endpoint to delete one or more EPSSpendingPlan. An application object will be created for each JSON object provided in the request body

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
    api_instance = openapi_client.EPSSpendingPlanApi(api_client)
    object_id = '1,2,3' # str | One or more system-generated identifiers of EPSSpendingPlan.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete EPSSpendingPlan
        api_response = api_instance.delete_eps_spending_plan(object_id, authorization=authorization)
        print("The response of EPSSpendingPlanApi->delete_eps_spending_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPSSpendingPlanApi->delete_eps_spending_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| One or more system-generated identifiers of EPSSpendingPlan. | 
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

# **get_eps_spending_plan**
> List[EPSSpendingPlan] get_eps_spending_plan(fields, filter=filter, order_by=order_by, authorization=authorization)

Read EPSSpendingPlan

Reads EPSSpendingPlan objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.eps_spending_plan import EPSSpendingPlan
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
    api_instance = openapi_client.EPSSpendingPlanApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read EPSSpendingPlan
        api_response = api_instance.get_eps_spending_plan(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of EPSSpendingPlanApi->get_eps_spending_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPSSpendingPlanApi->get_eps_spending_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[EPSSpendingPlan]**](EPSSpendingPlan.md)

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

# **get_eps_spending_plan_field_length**
> str get_eps_spending_plan_field_length(field_name, authorization=authorization)

View EPSSpendingPlan Field Length

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
    api_instance = openapi_client.EPSSpendingPlanApi(api_client)
    field_name = 'field_name_example' # str | An EPSSpendingPlan field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View EPSSpendingPlan Field Length
        api_response = api_instance.get_eps_spending_plan_field_length(field_name, authorization=authorization)
        print("The response of EPSSpendingPlanApi->get_eps_spending_plan_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPSSpendingPlanApi->get_eps_spending_plan_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An EPSSpendingPlan field. | 
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

# **get_eps_spending_plan_fields**
> str get_eps_spending_plan_fields()

View EPSSpendingPlan fields

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
    api_instance = openapi_client.EPSSpendingPlanApi(api_client)

    try:
        # View EPSSpendingPlan fields
        api_response = api_instance.get_eps_spending_plan_fields()
        print("The response of EPSSpendingPlanApi->get_eps_spending_plan_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPSSpendingPlanApi->get_eps_spending_plan_fields: %s\n" % e)
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

# **update_eps_spending_plan**
> bool update_eps_spending_plan(eps_spending_plan, authorization=authorization)

Update EPSSpendingPlan

Send a request to this endpoint to update one or more EPSSpendingPlan. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.eps_spending_plan import EPSSpendingPlan
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
    api_instance = openapi_client.EPSSpendingPlanApi(api_client)
    eps_spending_plan = [openapi_client.EPSSpendingPlan()] # List[EPSSpendingPlan] | A list of EPSSpendingPlan objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update EPSSpendingPlan
        api_response = api_instance.update_eps_spending_plan(eps_spending_plan, authorization=authorization)
        print("The response of EPSSpendingPlanApi->update_eps_spending_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPSSpendingPlanApi->update_eps_spending_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eps_spending_plan** | [**List[EPSSpendingPlan]**](EPSSpendingPlan.md)| A list of EPSSpendingPlan objects. | 
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

