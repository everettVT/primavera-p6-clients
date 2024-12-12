# openapi_client.RoleRateApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role_rate**](RoleRateApi.md#create_role_rate) | **POST** /roleRate | Create RoleRate
[**get_role_rate**](RoleRateApi.md#get_role_rate) | **GET** /roleRate | Read RoleRate
[**get_role_rate_field_length**](RoleRateApi.md#get_role_rate_field_length) | **GET** /roleRate/getFieldLength/{fieldName} | View RoleRate Field Length
[**get_role_rate_fields**](RoleRateApi.md#get_role_rate_fields) | **GET** /roleRate/fields | View RoleRate fields
[**update_role_rate**](RoleRateApi.md#update_role_rate) | **PUT** /roleRate | Update Activities


# **create_role_rate**
> str create_role_rate(role_rate, authorization=authorization)

Create RoleRate

Send a request to this endpoint to create one or more RoleRate. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.role_rate import RoleRate
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
    api_instance = openapi_client.RoleRateApi(api_client)
    role_rate = [openapi_client.RoleRate()] # List[RoleRate] | A list of RoleRate objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create RoleRate
        api_response = api_instance.create_role_rate(role_rate, authorization=authorization)
        print("The response of RoleRateApi->create_role_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleRateApi->create_role_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_rate** | [**List[RoleRate]**](RoleRate.md)| A list of RoleRate objects. | 
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

# **get_role_rate**
> List[RoleRate] get_role_rate(fields, filter=filter, order_by=order_by, authorization=authorization)

Read RoleRate

Reads RoleRate objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.role_rate import RoleRate
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
    api_instance = openapi_client.RoleRateApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read RoleRate
        api_response = api_instance.get_role_rate(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of RoleRateApi->get_role_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleRateApi->get_role_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[RoleRate]**](RoleRate.md)

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

# **get_role_rate_field_length**
> str get_role_rate_field_length(field_name, authorization=authorization)

View RoleRate Field Length

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
    api_instance = openapi_client.RoleRateApi(api_client)
    field_name = 'field_name_example' # str | A RoleRate field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View RoleRate Field Length
        api_response = api_instance.get_role_rate_field_length(field_name, authorization=authorization)
        print("The response of RoleRateApi->get_role_rate_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleRateApi->get_role_rate_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| A RoleRate field. | 
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

# **get_role_rate_fields**
> str get_role_rate_fields()

View RoleRate fields

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
    api_instance = openapi_client.RoleRateApi(api_client)

    try:
        # View RoleRate fields
        api_response = api_instance.get_role_rate_fields()
        print("The response of RoleRateApi->get_role_rate_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleRateApi->get_role_rate_fields: %s\n" % e)
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

# **update_role_rate**
> bool update_role_rate(role_rate, authorization=authorization)

Update Activities

Send a request to this endpoint to update one or more RoleRate. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.role_rate import RoleRate
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
    api_instance = openapi_client.RoleRateApi(api_client)
    role_rate = [openapi_client.RoleRate()] # List[RoleRate] | A list of RoleRate objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update Activities
        api_response = api_instance.update_role_rate(role_rate, authorization=authorization)
        print("The response of RoleRateApi->update_role_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleRateApi->update_role_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_rate** | [**List[RoleRate]**](RoleRate.md)| A list of RoleRate objects. | 
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

