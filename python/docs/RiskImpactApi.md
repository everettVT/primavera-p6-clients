# openapi_client.RiskImpactApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_risk_impact**](RiskImpactApi.md#create_risk_impact) | **POST** /riskImpact | Create RiskImpacts
[**delete_risk_impact**](RiskImpactApi.md#delete_risk_impact) | **DELETE** /riskImpact | Delete RiskImpacts
[**get_risk_impact**](RiskImpactApi.md#get_risk_impact) | **GET** /riskImpact | Read RiskImpacts
[**get_risk_impact_field_length**](RiskImpactApi.md#get_risk_impact_field_length) | **GET** /riskImpact/getFieldLength/{fieldName} | View RiskImpact Field Length
[**get_risk_impact_fields**](RiskImpactApi.md#get_risk_impact_fields) | **GET** /riskImpact/fields | View RiskImpact fields
[**update_risk_impact**](RiskImpactApi.md#update_risk_impact) | **PUT** /riskImpact | Update RiskImpacts


# **create_risk_impact**
> CreateRiskImpactResponse create_risk_impact(risk_impact, authorization=authorization)

Create RiskImpacts

Send a request to this endpoint to create one or more riskImpact. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.create_risk_impact_response import CreateRiskImpactResponse
from openapi_client.models.risk_impact import RiskImpact
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
    api_instance = openapi_client.RiskImpactApi(api_client)
    risk_impact = [openapi_client.RiskImpact()] # List[RiskImpact] | A list of riskImpact objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create RiskImpacts
        api_response = api_instance.create_risk_impact(risk_impact, authorization=authorization)
        print("The response of RiskImpactApi->create_risk_impact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskImpactApi->create_risk_impact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_impact** | [**List[RiskImpact]**](RiskImpact.md)| A list of riskImpact objects. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**CreateRiskImpactResponse**](CreateRiskImpactResponse.md)

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

# **delete_risk_impact**
> bool delete_risk_impact(risk_impact, authorization=authorization)

Delete RiskImpacts

Send a request to this endpoint to delete one or more riskImpact. Objects with ID values that match the values provided in the request body will be deleted.

### Example


```python
import openapi_client
from openapi_client.models.risk_impact import RiskImpact
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
    api_instance = openapi_client.RiskImpactApi(api_client)
    risk_impact = [openapi_client.RiskImpact()] # List[RiskImpact] | <p>A list of RiskImpact objects.<p><p>Required fields: You must supply both the RiskObjectId and RiskThresholdObjectId fields when you use the Delete RiskImpact operation. All other fields are optional.</p>
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete RiskImpacts
        api_response = api_instance.delete_risk_impact(risk_impact, authorization=authorization)
        print("The response of RiskImpactApi->delete_risk_impact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskImpactApi->delete_risk_impact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_impact** | [**List[RiskImpact]**](RiskImpact.md)| &lt;p&gt;A list of RiskImpact objects.&lt;p&gt;&lt;p&gt;Required fields: You must supply both the RiskObjectId and RiskThresholdObjectId fields when you use the Delete RiskImpact operation. All other fields are optional.&lt;/p&gt; | 
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

# **get_risk_impact**
> List[RiskImpact] get_risk_impact(fields, filter=filter, order_by=order_by, authorization=authorization)

Read RiskImpacts

Reads RiskImpact objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.risk_impact import RiskImpact
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
    api_instance = openapi_client.RiskImpactApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read RiskImpacts
        api_response = api_instance.get_risk_impact(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of RiskImpactApi->get_risk_impact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskImpactApi->get_risk_impact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[RiskImpact]**](RiskImpact.md)

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

# **get_risk_impact_field_length**
> str get_risk_impact_field_length(field_name, authorization=authorization)

View RiskImpact Field Length

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
    api_instance = openapi_client.RiskImpactApi(api_client)
    field_name = 'field_name_example' # str | A riskImpact field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View RiskImpact Field Length
        api_response = api_instance.get_risk_impact_field_length(field_name, authorization=authorization)
        print("The response of RiskImpactApi->get_risk_impact_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskImpactApi->get_risk_impact_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| A riskImpact field. | 
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

# **get_risk_impact_fields**
> str get_risk_impact_fields()

View RiskImpact fields

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
    api_instance = openapi_client.RiskImpactApi(api_client)

    try:
        # View RiskImpact fields
        api_response = api_instance.get_risk_impact_fields()
        print("The response of RiskImpactApi->get_risk_impact_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskImpactApi->get_risk_impact_fields: %s\n" % e)
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

# **update_risk_impact**
> bool update_risk_impact(risk_impact, authorization=authorization)

Update RiskImpacts

Send a request to this endpoint to update one or more riskImpact. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.risk_impact import RiskImpact
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
    api_instance = openapi_client.RiskImpactApi(api_client)
    risk_impact = [openapi_client.RiskImpact()] # List[RiskImpact] | A list of riskImpact objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update RiskImpacts
        api_response = api_instance.update_risk_impact(risk_impact, authorization=authorization)
        print("The response of RiskImpactApi->update_risk_impact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskImpactApi->update_risk_impact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_impact** | [**List[RiskImpact]**](RiskImpact.md)| A list of riskImpact objects. | 
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

