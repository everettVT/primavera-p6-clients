# openapi_client.RiskResponseActionImpactApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_risk_response_action_impact**](RiskResponseActionImpactApi.md#create_risk_response_action_impact) | **POST** /riskResponseActionImpact | Create RiskResponseActionImpacts
[**delete_risk_response_action_impact**](RiskResponseActionImpactApi.md#delete_risk_response_action_impact) | **DELETE** /riskResponseActionImpact | Delete RiskResponseActionImpacts
[**get_risk_response_action_impact**](RiskResponseActionImpactApi.md#get_risk_response_action_impact) | **GET** /riskResponseActionImpact | Read RiskResponseActionImpacts
[**get_risk_response_action_impact_field_length**](RiskResponseActionImpactApi.md#get_risk_response_action_impact_field_length) | **GET** /riskResponseActionImpact/getFieldLength/{fieldName} | View RiskResponseActionImpact Field Length
[**get_risk_response_action_impact_fields**](RiskResponseActionImpactApi.md#get_risk_response_action_impact_fields) | **GET** /riskResponseActionImpact/fields | View RiskResponseActionImpact fields
[**update_risk_response_action_impact**](RiskResponseActionImpactApi.md#update_risk_response_action_impact) | **PUT** /riskResponseActionImpact | Update RiskResponseActionImpacts


# **create_risk_response_action_impact**
> CreateRiskResponseActionImpactResponse create_risk_response_action_impact(risk_response_action_impact, authorization=authorization)

Create RiskResponseActionImpacts

Send a request to this endpoint to create one or more riskResponseActionImpact. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.create_risk_response_action_impact_response import CreateRiskResponseActionImpactResponse
from openapi_client.models.risk_response_action_impact import RiskResponseActionImpact
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
    api_instance = openapi_client.RiskResponseActionImpactApi(api_client)
    risk_response_action_impact = [openapi_client.RiskResponseActionImpact()] # List[RiskResponseActionImpact] | A list of riskResponseActionImpact objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create RiskResponseActionImpacts
        api_response = api_instance.create_risk_response_action_impact(risk_response_action_impact, authorization=authorization)
        print("The response of RiskResponseActionImpactApi->create_risk_response_action_impact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskResponseActionImpactApi->create_risk_response_action_impact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_response_action_impact** | [**List[RiskResponseActionImpact]**](RiskResponseActionImpact.md)| A list of riskResponseActionImpact objects. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**CreateRiskResponseActionImpactResponse**](CreateRiskResponseActionImpactResponse.md)

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

# **delete_risk_response_action_impact**
> bool delete_risk_response_action_impact(risk_response_action_impact, authorization=authorization)

Delete RiskResponseActionImpacts

Send a request to this endpoint to delete one or more riskResponseActionImpact. Objects with ID values that match the values provided in the request body will be deleted.

### Example


```python
import openapi_client
from openapi_client.models.risk_response_action_impact import RiskResponseActionImpact
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
    api_instance = openapi_client.RiskResponseActionImpactApi(api_client)
    risk_response_action_impact = [openapi_client.RiskResponseActionImpact()] # List[RiskResponseActionImpact] | <p>A list of riskResponseActionImpact objects.<p><p>Required fields: You must supply both the RiskResponseActionObjectId and RiskThresholdObjectId fields when you use the Delete RiskResponseActionImpacts operation. All other fields are optional.</p>
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete RiskResponseActionImpacts
        api_response = api_instance.delete_risk_response_action_impact(risk_response_action_impact, authorization=authorization)
        print("The response of RiskResponseActionImpactApi->delete_risk_response_action_impact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskResponseActionImpactApi->delete_risk_response_action_impact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_response_action_impact** | [**List[RiskResponseActionImpact]**](RiskResponseActionImpact.md)| &lt;p&gt;A list of riskResponseActionImpact objects.&lt;p&gt;&lt;p&gt;Required fields: You must supply both the RiskResponseActionObjectId and RiskThresholdObjectId fields when you use the Delete RiskResponseActionImpacts operation. All other fields are optional.&lt;/p&gt; | 
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

# **get_risk_response_action_impact**
> List[RiskResponseActionImpact] get_risk_response_action_impact(fields, filter=filter, order_by=order_by, authorization=authorization)

Read RiskResponseActionImpacts

Reads RiskResponseActionImpact objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.risk_response_action_impact import RiskResponseActionImpact
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
    api_instance = openapi_client.RiskResponseActionImpactApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read RiskResponseActionImpacts
        api_response = api_instance.get_risk_response_action_impact(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of RiskResponseActionImpactApi->get_risk_response_action_impact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskResponseActionImpactApi->get_risk_response_action_impact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[RiskResponseActionImpact]**](RiskResponseActionImpact.md)

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

# **get_risk_response_action_impact_field_length**
> str get_risk_response_action_impact_field_length(field_name, authorization=authorization)

View RiskResponseActionImpact Field Length

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
    api_instance = openapi_client.RiskResponseActionImpactApi(api_client)
    field_name = 'field_name_example' # str | A riskResponseActionImpact field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View RiskResponseActionImpact Field Length
        api_response = api_instance.get_risk_response_action_impact_field_length(field_name, authorization=authorization)
        print("The response of RiskResponseActionImpactApi->get_risk_response_action_impact_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskResponseActionImpactApi->get_risk_response_action_impact_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| A riskResponseActionImpact field. | 
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

# **get_risk_response_action_impact_fields**
> str get_risk_response_action_impact_fields()

View RiskResponseActionImpact fields

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
    api_instance = openapi_client.RiskResponseActionImpactApi(api_client)

    try:
        # View RiskResponseActionImpact fields
        api_response = api_instance.get_risk_response_action_impact_fields()
        print("The response of RiskResponseActionImpactApi->get_risk_response_action_impact_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskResponseActionImpactApi->get_risk_response_action_impact_fields: %s\n" % e)
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

# **update_risk_response_action_impact**
> bool update_risk_response_action_impact(risk_response_action_impact, authorization=authorization)

Update RiskResponseActionImpacts

Send a request to this endpoint to update one or more riskResponseActionImpact. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.risk_response_action_impact import RiskResponseActionImpact
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
    api_instance = openapi_client.RiskResponseActionImpactApi(api_client)
    risk_response_action_impact = [openapi_client.RiskResponseActionImpact()] # List[RiskResponseActionImpact] | A list of riskResponseActionImpact objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update RiskResponseActionImpacts
        api_response = api_instance.update_risk_response_action_impact(risk_response_action_impact, authorization=authorization)
        print("The response of RiskResponseActionImpactApi->update_risk_response_action_impact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskResponseActionImpactApi->update_risk_response_action_impact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_response_action_impact** | [**List[RiskResponseActionImpact]**](RiskResponseActionImpact.md)| A list of riskResponseActionImpact objects. | 
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

