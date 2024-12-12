# openapi_client.UserInterfaceViewApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_interface_view**](UserInterfaceViewApi.md#get_user_interface_view) | **GET** /userInterfaceView | Read UserInterfaceView
[**get_user_interface_view_field_length**](UserInterfaceViewApi.md#get_user_interface_view_field_length) | **GET** /userInterfaceView/getFieldLength/{fieldName} | View UserInterfaceView Field Length
[**get_user_interface_view_fields**](UserInterfaceViewApi.md#get_user_interface_view_fields) | **GET** /userInterfaceView/fields | View UserInterfaceView fields


# **get_user_interface_view**
> List[UserInterfaceView] get_user_interface_view(fields, filter=filter, order_by=order_by, authorization=authorization)

Read UserInterfaceView

Reads UserInterfaceView objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.user_interface_view import UserInterfaceView
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
    api_instance = openapi_client.UserInterfaceViewApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read UserInterfaceView
        api_response = api_instance.get_user_interface_view(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of UserInterfaceViewApi->get_user_interface_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserInterfaceViewApi->get_user_interface_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[UserInterfaceView]**](UserInterfaceView.md)

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

# **get_user_interface_view_field_length**
> str get_user_interface_view_field_length(field_name, authorization=authorization)

View UserInterfaceView Field Length

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
    api_instance = openapi_client.UserInterfaceViewApi(api_client)
    field_name = 'field_name_example' # str | Field to retun length
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View UserInterfaceView Field Length
        api_response = api_instance.get_user_interface_view_field_length(field_name, authorization=authorization)
        print("The response of UserInterfaceViewApi->get_user_interface_view_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserInterfaceViewApi->get_user_interface_view_field_length: %s\n" % e)
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

# **get_user_interface_view_fields**
> str get_user_interface_view_fields()

View UserInterfaceView fields

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
    api_instance = openapi_client.UserInterfaceViewApi(api_client)

    try:
        # View UserInterfaceView fields
        api_response = api_instance.get_user_interface_view_fields()
        print("The response of UserInterfaceViewApi->get_user_interface_view_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserInterfaceViewApi->get_user_interface_view_fields: %s\n" % e)
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

