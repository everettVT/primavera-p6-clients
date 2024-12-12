# openapi_client.EPSFundingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_eps_funding**](EPSFundingApi.md#create_eps_funding) | **POST** /epsFunding | Create EPSFunding
[**delete_eps_funding**](EPSFundingApi.md#delete_eps_funding) | **DELETE** /epsFunding | Delete EPSFunding
[**get_eps_funding**](EPSFundingApi.md#get_eps_funding) | **GET** /epsFunding | Read EPSFunding
[**get_eps_funding_field_length**](EPSFundingApi.md#get_eps_funding_field_length) | **GET** /epsFunding/getFieldLength/{fieldName} | View EPSFunding Field Length
[**get_eps_funding_fields**](EPSFundingApi.md#get_eps_funding_fields) | **GET** /epsFunding/fields | View EPSFunding fields
[**update_eps_funding**](EPSFundingApi.md#update_eps_funding) | **PUT** /epsFunding | Update EPSFunding


# **create_eps_funding**
> str create_eps_funding(eps_funding, authorization=authorization)

Create EPSFunding

Send a request to this endpoint to create one or more EPSFunding. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.eps_funding import EPSFunding
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
    api_instance = openapi_client.EPSFundingApi(api_client)
    eps_funding = [openapi_client.EPSFunding()] # List[EPSFunding] | A list of EPSFunding objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create EPSFunding
        api_response = api_instance.create_eps_funding(eps_funding, authorization=authorization)
        print("The response of EPSFundingApi->create_eps_funding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPSFundingApi->create_eps_funding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eps_funding** | [**List[EPSFunding]**](EPSFunding.md)| A list of EPSFunding objects. | 
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

# **delete_eps_funding**
> bool delete_eps_funding(object_id, authorization=authorization)

Delete EPSFunding

Send a request to this endpoint to delete one or more EPSFunding. An application object will be created for each JSON object provided in the request body

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
    api_instance = openapi_client.EPSFundingApi(api_client)
    object_id = '1,2,3' # str | One or more system-generated identifiers of EPSFunding.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete EPSFunding
        api_response = api_instance.delete_eps_funding(object_id, authorization=authorization)
        print("The response of EPSFundingApi->delete_eps_funding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPSFundingApi->delete_eps_funding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| One or more system-generated identifiers of EPSFunding. | 
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

# **get_eps_funding**
> List[EPSFunding] get_eps_funding(fields, filter=filter, order_by=order_by, authorization=authorization)

Read EPSFunding

Reads EPSFunding objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.eps_funding import EPSFunding
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
    api_instance = openapi_client.EPSFundingApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read EPSFunding
        api_response = api_instance.get_eps_funding(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of EPSFundingApi->get_eps_funding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPSFundingApi->get_eps_funding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[EPSFunding]**](EPSFunding.md)

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

# **get_eps_funding_field_length**
> str get_eps_funding_field_length(field_name, authorization=authorization)

View EPSFunding Field Length

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
    api_instance = openapi_client.EPSFundingApi(api_client)
    field_name = 'field_name_example' # str | An project field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View EPSFunding Field Length
        api_response = api_instance.get_eps_funding_field_length(field_name, authorization=authorization)
        print("The response of EPSFundingApi->get_eps_funding_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPSFundingApi->get_eps_funding_field_length: %s\n" % e)
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

# **get_eps_funding_fields**
> str get_eps_funding_fields()

View EPSFunding fields

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
    api_instance = openapi_client.EPSFundingApi(api_client)

    try:
        # View EPSFunding fields
        api_response = api_instance.get_eps_funding_fields()
        print("The response of EPSFundingApi->get_eps_funding_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPSFundingApi->get_eps_funding_fields: %s\n" % e)
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

# **update_eps_funding**
> bool update_eps_funding(eps_funding, authorization=authorization)

Update EPSFunding

Send a request to this endpoint to update one or more EPSFunding. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.eps_funding import EPSFunding
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
    api_instance = openapi_client.EPSFundingApi(api_client)
    eps_funding = [openapi_client.EPSFunding()] # List[EPSFunding] | A list of EPSFunding objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update EPSFunding
        api_response = api_instance.update_eps_funding(eps_funding, authorization=authorization)
        print("The response of EPSFundingApi->update_eps_funding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPSFundingApi->update_eps_funding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eps_funding** | [**List[EPSFunding]**](EPSFunding.md)| A list of EPSFunding objects. | 
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

