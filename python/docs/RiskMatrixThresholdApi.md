# openapi_client.RiskMatrixThresholdApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_risk_matrix_threshold**](RiskMatrixThresholdApi.md#create_risk_matrix_threshold) | **POST** /riskMatrixThreshold | Create RiskMatrixThresholds
[**delete_risk_matrix_threshold**](RiskMatrixThresholdApi.md#delete_risk_matrix_threshold) | **DELETE** /riskMatrixThreshold | Delete RiskMatrixThresholds
[**get_risk_matrix_threshold**](RiskMatrixThresholdApi.md#get_risk_matrix_threshold) | **GET** /riskMatrixThreshold | Read RiskMatrixThresholds
[**get_risk_matrix_threshold_field_length**](RiskMatrixThresholdApi.md#get_risk_matrix_threshold_field_length) | **GET** /riskMatrixThreshold/getFieldLength/{fieldName} | View RiskMatrixThreshold Field Length
[**get_risk_matrix_threshold_fields**](RiskMatrixThresholdApi.md#get_risk_matrix_threshold_fields) | **GET** /riskMatrixThreshold/fields | View RiskMatrixThreshold fields


# **create_risk_matrix_threshold**
> CreateRiskMatrixThresholdResponse create_risk_matrix_threshold(risk_matrix_threshold, authorization=authorization)

Create RiskMatrixThresholds

Send a request to this endpoint to create one or more riskMatrixThreshold. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.create_risk_matrix_threshold_response import CreateRiskMatrixThresholdResponse
from openapi_client.models.risk_matrix_threshold import RiskMatrixThreshold
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
    api_instance = openapi_client.RiskMatrixThresholdApi(api_client)
    risk_matrix_threshold = [openapi_client.RiskMatrixThreshold()] # List[RiskMatrixThreshold] | A list of riskMatrixThreshold objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create RiskMatrixThresholds
        api_response = api_instance.create_risk_matrix_threshold(risk_matrix_threshold, authorization=authorization)
        print("The response of RiskMatrixThresholdApi->create_risk_matrix_threshold:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskMatrixThresholdApi->create_risk_matrix_threshold: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_matrix_threshold** | [**List[RiskMatrixThreshold]**](RiskMatrixThreshold.md)| A list of riskMatrixThreshold objects. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**CreateRiskMatrixThresholdResponse**](CreateRiskMatrixThresholdResponse.md)

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

# **delete_risk_matrix_threshold**
> bool delete_risk_matrix_threshold(risk_matrix_threshold, authorization=authorization)

Delete RiskMatrixThresholds

Send a request to this endpoint to delete one or more riskMatrixThreshold. Objects with ID values that match the values provided in the request body will be deleted.

### Example


```python
import openapi_client
from openapi_client.models.risk_matrix_threshold import RiskMatrixThreshold
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
    api_instance = openapi_client.RiskMatrixThresholdApi(api_client)
    risk_matrix_threshold = [openapi_client.RiskMatrixThreshold()] # List[RiskMatrixThreshold] | <p>A list of riskMatrixThreshold objects.<p><p>Required fields: You must supply both the RiskMatrixObjectId and RiskThresholdObjectId fields when you use the Delete RiskMatrixThresholds operation. All other fields are optional.</p>
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete RiskMatrixThresholds
        api_response = api_instance.delete_risk_matrix_threshold(risk_matrix_threshold, authorization=authorization)
        print("The response of RiskMatrixThresholdApi->delete_risk_matrix_threshold:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskMatrixThresholdApi->delete_risk_matrix_threshold: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_matrix_threshold** | [**List[RiskMatrixThreshold]**](RiskMatrixThreshold.md)| &lt;p&gt;A list of riskMatrixThreshold objects.&lt;p&gt;&lt;p&gt;Required fields: You must supply both the RiskMatrixObjectId and RiskThresholdObjectId fields when you use the Delete RiskMatrixThresholds operation. All other fields are optional.&lt;/p&gt; | 
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

# **get_risk_matrix_threshold**
> List[RiskMatrixThreshold] get_risk_matrix_threshold(fields, filter=filter, order_by=order_by, authorization=authorization)

Read RiskMatrixThresholds

Reads RiskMatrixThreshold objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.risk_matrix_threshold import RiskMatrixThreshold
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
    api_instance = openapi_client.RiskMatrixThresholdApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read RiskMatrixThresholds
        api_response = api_instance.get_risk_matrix_threshold(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of RiskMatrixThresholdApi->get_risk_matrix_threshold:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskMatrixThresholdApi->get_risk_matrix_threshold: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[RiskMatrixThreshold]**](RiskMatrixThreshold.md)

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

# **get_risk_matrix_threshold_field_length**
> str get_risk_matrix_threshold_field_length(field_name, authorization=authorization)

View RiskMatrixThreshold Field Length

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
    api_instance = openapi_client.RiskMatrixThresholdApi(api_client)
    field_name = 'field_name_example' # str | A riskMatrixThreshold field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View RiskMatrixThreshold Field Length
        api_response = api_instance.get_risk_matrix_threshold_field_length(field_name, authorization=authorization)
        print("The response of RiskMatrixThresholdApi->get_risk_matrix_threshold_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskMatrixThresholdApi->get_risk_matrix_threshold_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| A riskMatrixThreshold field. | 
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

# **get_risk_matrix_threshold_fields**
> str get_risk_matrix_threshold_fields()

View RiskMatrixThreshold fields

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
    api_instance = openapi_client.RiskMatrixThresholdApi(api_client)

    try:
        # View RiskMatrixThreshold fields
        api_response = api_instance.get_risk_matrix_threshold_fields()
        print("The response of RiskMatrixThresholdApi->get_risk_matrix_threshold_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskMatrixThresholdApi->get_risk_matrix_threshold_fields: %s\n" % e)
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

