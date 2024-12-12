# openapi_client.RiskThresholdApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_risk_threshold**](RiskThresholdApi.md#create_risk_threshold) | **POST** /riskThreshold | Create RiskThresholds
[**delete_risk_threshold**](RiskThresholdApi.md#delete_risk_threshold) | **DELETE** /riskThreshold | Delete RiskThresholds
[**get_risk_threshold**](RiskThresholdApi.md#get_risk_threshold) | **GET** /riskThreshold | Read RiskThresholds
[**get_risk_threshold_field_length**](RiskThresholdApi.md#get_risk_threshold_field_length) | **GET** /riskThreshold/getFieldLength/{fieldName} | View RiskThreshold Field Length
[**get_risk_threshold_fields**](RiskThresholdApi.md#get_risk_threshold_fields) | **GET** /riskThreshold/fields | View RiskThreshold fields
[**update_risk_threshold**](RiskThresholdApi.md#update_risk_threshold) | **PUT** /riskThreshold | Update  RiskThresholds


# **create_risk_threshold**
> str create_risk_threshold(risk_threshold, authorization=authorization)

Create RiskThresholds

Send a request to this endpoint to create one or more riskThreshold. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.risk_threshold import RiskThreshold
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
    api_instance = openapi_client.RiskThresholdApi(api_client)
    risk_threshold = [openapi_client.RiskThreshold()] # List[RiskThreshold] | A list of riskThreshold objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create RiskThresholds
        api_response = api_instance.create_risk_threshold(risk_threshold, authorization=authorization)
        print("The response of RiskThresholdApi->create_risk_threshold:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskThresholdApi->create_risk_threshold: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_threshold** | [**List[RiskThreshold]**](RiskThreshold.md)| A list of riskThreshold objects. | 
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

# **delete_risk_threshold**
> bool delete_risk_threshold(authorization=authorization, object_id=object_id)

Delete RiskThresholds

Send a request to this endpoint to delete one or more riskThreshold. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.RiskThresholdApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of riskThreshold. (optional)

    try:
        # Delete RiskThresholds
        api_response = api_instance.delete_risk_threshold(authorization=authorization, object_id=object_id)
        print("The response of RiskThresholdApi->delete_risk_threshold:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskThresholdApi->delete_risk_threshold: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| One or more system-generated identifiers of riskThreshold. | [optional] 

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

# **get_risk_threshold**
> List[RiskThreshold] get_risk_threshold(fields, filter=filter, order_by=order_by, authorization=authorization)

Read RiskThresholds

Reads RiskThreshold objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.risk_threshold import RiskThreshold
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
    api_instance = openapi_client.RiskThresholdApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read RiskThresholds
        api_response = api_instance.get_risk_threshold(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of RiskThresholdApi->get_risk_threshold:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskThresholdApi->get_risk_threshold: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[RiskThreshold]**](RiskThreshold.md)

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

# **get_risk_threshold_field_length**
> str get_risk_threshold_field_length(field_name, authorization=authorization)

View RiskThreshold Field Length

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
    api_instance = openapi_client.RiskThresholdApi(api_client)
    field_name = 'field_name_example' # str | An riskThreshold field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View RiskThreshold Field Length
        api_response = api_instance.get_risk_threshold_field_length(field_name, authorization=authorization)
        print("The response of RiskThresholdApi->get_risk_threshold_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskThresholdApi->get_risk_threshold_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An riskThreshold field. | 
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

# **get_risk_threshold_fields**
> str get_risk_threshold_fields()

View RiskThreshold fields

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
    api_instance = openapi_client.RiskThresholdApi(api_client)

    try:
        # View RiskThreshold fields
        api_response = api_instance.get_risk_threshold_fields()
        print("The response of RiskThresholdApi->get_risk_threshold_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskThresholdApi->get_risk_threshold_fields: %s\n" % e)
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

# **update_risk_threshold**
> bool update_risk_threshold(risk_threshold, authorization=authorization)

Update  RiskThresholds

Send a request to this endpoint to update one or more riskThreshold. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.risk_threshold import RiskThreshold
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
    api_instance = openapi_client.RiskThresholdApi(api_client)
    risk_threshold = [openapi_client.RiskThreshold()] # List[RiskThreshold] | A list of riskThreshold objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update  RiskThresholds
        api_response = api_instance.update_risk_threshold(risk_threshold, authorization=authorization)
        print("The response of RiskThresholdApi->update_risk_threshold:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskThresholdApi->update_risk_threshold: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_threshold** | [**List[RiskThreshold]**](RiskThreshold.md)| A list of riskThreshold objects. | 
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

