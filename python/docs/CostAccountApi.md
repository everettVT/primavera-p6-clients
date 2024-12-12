# openapi_client.CostAccountApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cost_account**](CostAccountApi.md#create_cost_account) | **POST** /costAccount | Create CostAccount
[**delete_cost_account**](CostAccountApi.md#delete_cost_account) | **DELETE** /costAccount | Delete CostAccount
[**get_cost_account**](CostAccountApi.md#get_cost_account) | **GET** /costAccount | Read CostAccount
[**get_cost_account_field_length**](CostAccountApi.md#get_cost_account_field_length) | **GET** /costAccount/getFieldLength/{fieldName} | View CostAccount Field Length
[**get_cost_account_fields**](CostAccountApi.md#get_cost_account_fields) | **GET** /costAccount/fields | View CostAccount fields
[**update_cost_account**](CostAccountApi.md#update_cost_account) | **PUT** /costAccount | Update CostAccount


# **create_cost_account**
> str create_cost_account(cost_account, authorization=authorization)

Create CostAccount

Send a request to this endpoint to create one or more CostAccount. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.cost_account import CostAccount
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
    api_instance = openapi_client.CostAccountApi(api_client)
    cost_account = [openapi_client.CostAccount()] # List[CostAccount] | A list of costaccount objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create CostAccount
        api_response = api_instance.create_cost_account(cost_account, authorization=authorization)
        print("The response of CostAccountApi->create_cost_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostAccountApi->create_cost_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cost_account** | [**List[CostAccount]**](CostAccount.md)| A list of costaccount objects. | 
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

# **delete_cost_account**
> bool delete_cost_account(authorization=authorization, object_id=object_id)

Delete CostAccount

Send a request to this endpoint to delete one or more CostAccount. An application object will be created for each JSON object provided in the request body

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
    api_instance = openapi_client.CostAccountApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of costaccount. (optional)

    try:
        # Delete CostAccount
        api_response = api_instance.delete_cost_account(authorization=authorization, object_id=object_id)
        print("The response of CostAccountApi->delete_cost_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostAccountApi->delete_cost_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| One or more system-generated identifiers of costaccount. | [optional] 

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

# **get_cost_account**
> List[CostAccount] get_cost_account(fields, filter=filter, order_by=order_by, authorization=authorization)

Read CostAccount

Reads CostAccount objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.cost_account import CostAccount
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
    api_instance = openapi_client.CostAccountApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read CostAccount
        api_response = api_instance.get_cost_account(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of CostAccountApi->get_cost_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostAccountApi->get_cost_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[CostAccount]**](CostAccount.md)

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

# **get_cost_account_field_length**
> str get_cost_account_field_length(field_name, authorization=authorization)

View CostAccount Field Length

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
    api_instance = openapi_client.CostAccountApi(api_client)
    field_name = 'field_name_example' # str | An project field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View CostAccount Field Length
        api_response = api_instance.get_cost_account_field_length(field_name, authorization=authorization)
        print("The response of CostAccountApi->get_cost_account_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostAccountApi->get_cost_account_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An project field. | 
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

# **get_cost_account_fields**
> str get_cost_account_fields()

View CostAccount fields

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
    api_instance = openapi_client.CostAccountApi(api_client)

    try:
        # View CostAccount fields
        api_response = api_instance.get_cost_account_fields()
        print("The response of CostAccountApi->get_cost_account_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostAccountApi->get_cost_account_fields: %s\n" % e)
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

# **update_cost_account**
> bool update_cost_account(cost_account, authorization=authorization)

Update CostAccount

Send a request to this endpoint to update one or more CostAccount. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.cost_account import CostAccount
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
    api_instance = openapi_client.CostAccountApi(api_client)
    cost_account = [openapi_client.CostAccount()] # List[CostAccount] | A list of costaccount objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update CostAccount
        api_response = api_instance.update_cost_account(cost_account, authorization=authorization)
        print("The response of CostAccountApi->update_cost_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostAccountApi->update_cost_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cost_account** | [**List[CostAccount]**](CostAccount.md)| A list of costaccount objects. | 
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

