# openapi_client.RiskThresholdLevelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_risk_threshold_level**](RiskThresholdLevelApi.md#create_risk_threshold_level) | **POST** /riskThresholdLevel | Create RiskThresholdLevels
[**delete_risk_threshold_level**](RiskThresholdLevelApi.md#delete_risk_threshold_level) | **DELETE** /riskThresholdLevel | Delete RiskThresholdLevels
[**get_risk_threshold_level**](RiskThresholdLevelApi.md#get_risk_threshold_level) | **GET** /riskThresholdLevel | Read RiskThresholdLevels
[**get_risk_threshold_level_field_length**](RiskThresholdLevelApi.md#get_risk_threshold_level_field_length) | **GET** /riskThresholdLevel/getFieldLength/{fieldName} | View RiskThresholdLevel Field Length
[**get_risk_threshold_level_fields**](RiskThresholdLevelApi.md#get_risk_threshold_level_fields) | **GET** /riskThresholdLevel/fields | View RiskThresholdLevel fields
[**update_risk_threshold_level**](RiskThresholdLevelApi.md#update_risk_threshold_level) | **PUT** /riskThresholdLevel | Update RiskThresholdLevels


# **create_risk_threshold_level**
> str create_risk_threshold_level(risk_threshold_level, authorization=authorization)

Create RiskThresholdLevels

Send a request to this endpoint to create one or more riskThresholdLevel. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.risk_threshold_level import RiskThresholdLevel
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
    api_instance = openapi_client.RiskThresholdLevelApi(api_client)
    risk_threshold_level = [openapi_client.RiskThresholdLevel()] # List[RiskThresholdLevel] | A list of riskThresholdLevel objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create RiskThresholdLevels
        api_response = api_instance.create_risk_threshold_level(risk_threshold_level, authorization=authorization)
        print("The response of RiskThresholdLevelApi->create_risk_threshold_level:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskThresholdLevelApi->create_risk_threshold_level: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_threshold_level** | [**List[RiskThresholdLevel]**](RiskThresholdLevel.md)| A list of riskThresholdLevel objects. | 
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

# **delete_risk_threshold_level**
> bool delete_risk_threshold_level(authorization=authorization, object_id=object_id)

Delete RiskThresholdLevels

Send a request to this endpoint to delete one or more riskThresholdLevel. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.RiskThresholdLevelApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of riskThresholdLevel. (optional)

    try:
        # Delete RiskThresholdLevels
        api_response = api_instance.delete_risk_threshold_level(authorization=authorization, object_id=object_id)
        print("The response of RiskThresholdLevelApi->delete_risk_threshold_level:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskThresholdLevelApi->delete_risk_threshold_level: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| One or more system-generated identifiers of riskThresholdLevel. | [optional] 

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

# **get_risk_threshold_level**
> List[RiskThresholdLevel] get_risk_threshold_level(fields, filter=filter, order_by=order_by, authorization=authorization)

Read RiskThresholdLevels

Reads RiskThresholdLevel objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.risk_threshold_level import RiskThresholdLevel
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
    api_instance = openapi_client.RiskThresholdLevelApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read RiskThresholdLevels
        api_response = api_instance.get_risk_threshold_level(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of RiskThresholdLevelApi->get_risk_threshold_level:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskThresholdLevelApi->get_risk_threshold_level: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[RiskThresholdLevel]**](RiskThresholdLevel.md)

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

# **get_risk_threshold_level_field_length**
> str get_risk_threshold_level_field_length(field_name, authorization=authorization)

View RiskThresholdLevel Field Length

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
    api_instance = openapi_client.RiskThresholdLevelApi(api_client)
    field_name = 'field_name_example' # str | A riskThresholdLevel field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View RiskThresholdLevel Field Length
        api_response = api_instance.get_risk_threshold_level_field_length(field_name, authorization=authorization)
        print("The response of RiskThresholdLevelApi->get_risk_threshold_level_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskThresholdLevelApi->get_risk_threshold_level_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| A riskThresholdLevel field. | 
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

# **get_risk_threshold_level_fields**
> str get_risk_threshold_level_fields()

View RiskThresholdLevel fields

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
    api_instance = openapi_client.RiskThresholdLevelApi(api_client)

    try:
        # View RiskThresholdLevel fields
        api_response = api_instance.get_risk_threshold_level_fields()
        print("The response of RiskThresholdLevelApi->get_risk_threshold_level_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskThresholdLevelApi->get_risk_threshold_level_fields: %s\n" % e)
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

# **update_risk_threshold_level**
> bool update_risk_threshold_level(risk_threshold_level, authorization=authorization)

Update RiskThresholdLevels

Send a request to this endpoint to update one or more riskThresholdLevel. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.risk_threshold_level import RiskThresholdLevel
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
    api_instance = openapi_client.RiskThresholdLevelApi(api_client)
    risk_threshold_level = [openapi_client.RiskThresholdLevel()] # List[RiskThresholdLevel] | A list of riskThresholdLevel objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update RiskThresholdLevels
        api_response = api_instance.update_risk_threshold_level(risk_threshold_level, authorization=authorization)
        print("The response of RiskThresholdLevelApi->update_risk_threshold_level:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskThresholdLevelApi->update_risk_threshold_level: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_threshold_level** | [**List[RiskThresholdLevel]**](RiskThresholdLevel.md)| A list of riskThresholdLevel objects. | 
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

