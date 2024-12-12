# openapi_client.RiskResponseActionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_risk_response_action**](RiskResponseActionApi.md#create_risk_response_action) | **POST** /riskResponseAction | Create RiskResponseActions
[**delete_risk_response_action**](RiskResponseActionApi.md#delete_risk_response_action) | **DELETE** /riskResponseAction | Delete RiskResponseActions
[**get_risk_response_action**](RiskResponseActionApi.md#get_risk_response_action) | **GET** /riskResponseAction | Read RiskResponseActions
[**get_risk_response_action_field_length**](RiskResponseActionApi.md#get_risk_response_action_field_length) | **GET** /riskResponseAction/getFieldLength/{fieldName} | View RiskResponseAction Field Length
[**get_risk_response_action_fields**](RiskResponseActionApi.md#get_risk_response_action_fields) | **GET** /riskResponseAction/fields | View RiskResponseAction fields
[**update_risk_response_action**](RiskResponseActionApi.md#update_risk_response_action) | **PUT** /riskResponseAction | Update RiskResponseActions


# **create_risk_response_action**
> str create_risk_response_action(risk_response_action, authorization=authorization)

Create RiskResponseActions

Send a request to this endpoint to create one or more riskResponseAction. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.risk_response_action import RiskResponseAction
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
    api_instance = openapi_client.RiskResponseActionApi(api_client)
    risk_response_action = [openapi_client.RiskResponseAction()] # List[RiskResponseAction] | A list of riskResponseAction objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create RiskResponseActions
        api_response = api_instance.create_risk_response_action(risk_response_action, authorization=authorization)
        print("The response of RiskResponseActionApi->create_risk_response_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskResponseActionApi->create_risk_response_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_response_action** | [**List[RiskResponseAction]**](RiskResponseAction.md)| A list of riskResponseAction objects. | 
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

# **delete_risk_response_action**
> bool delete_risk_response_action(authorization=authorization, object_id=object_id)

Delete RiskResponseActions

Send a request to this endpoint to delete one or more riskResponseAction. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.RiskResponseActionApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of riskResponseAction. (optional)

    try:
        # Delete RiskResponseActions
        api_response = api_instance.delete_risk_response_action(authorization=authorization, object_id=object_id)
        print("The response of RiskResponseActionApi->delete_risk_response_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskResponseActionApi->delete_risk_response_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| One or more system-generated identifiers of riskResponseAction. | [optional] 

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

# **get_risk_response_action**
> List[RiskResponseAction] get_risk_response_action(fields, filter=filter, order_by=order_by, authorization=authorization)

Read RiskResponseActions

Reads RiskResponseAction objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.risk_response_action import RiskResponseAction
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
    api_instance = openapi_client.RiskResponseActionApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read RiskResponseActions
        api_response = api_instance.get_risk_response_action(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of RiskResponseActionApi->get_risk_response_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskResponseActionApi->get_risk_response_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[RiskResponseAction]**](RiskResponseAction.md)

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

# **get_risk_response_action_field_length**
> str get_risk_response_action_field_length(field_name, authorization=authorization)

View RiskResponseAction Field Length

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
    api_instance = openapi_client.RiskResponseActionApi(api_client)
    field_name = 'field_name_example' # str | A riskResponseAction field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View RiskResponseAction Field Length
        api_response = api_instance.get_risk_response_action_field_length(field_name, authorization=authorization)
        print("The response of RiskResponseActionApi->get_risk_response_action_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskResponseActionApi->get_risk_response_action_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| A riskResponseAction field. | 
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

# **get_risk_response_action_fields**
> str get_risk_response_action_fields()

View RiskResponseAction fields

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
    api_instance = openapi_client.RiskResponseActionApi(api_client)

    try:
        # View RiskResponseAction fields
        api_response = api_instance.get_risk_response_action_fields()
        print("The response of RiskResponseActionApi->get_risk_response_action_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskResponseActionApi->get_risk_response_action_fields: %s\n" % e)
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

# **update_risk_response_action**
> bool update_risk_response_action(risk_response_action, authorization=authorization)

Update RiskResponseActions

Send a request to this endpoint to update one or more riskResponseAction. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.risk_response_action import RiskResponseAction
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
    api_instance = openapi_client.RiskResponseActionApi(api_client)
    risk_response_action = [openapi_client.RiskResponseAction()] # List[RiskResponseAction] | A list of riskResponseAction objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update RiskResponseActions
        api_response = api_instance.update_risk_response_action(risk_response_action, authorization=authorization)
        print("The response of RiskResponseActionApi->update_risk_response_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskResponseActionApi->update_risk_response_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_response_action** | [**List[RiskResponseAction]**](RiskResponseAction.md)| A list of riskResponseAction objects. | 
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

