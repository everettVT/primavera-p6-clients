# openapi_client.RiskResponsePlanApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_risk_response_plan**](RiskResponsePlanApi.md#create_risk_response_plan) | **POST** /riskResponsePlan | Create RiskResponsePlans
[**delete_risk_response_plan**](RiskResponsePlanApi.md#delete_risk_response_plan) | **DELETE** /riskResponsePlan | Delete RiskResponsePlans
[**get_risk_response_plan**](RiskResponsePlanApi.md#get_risk_response_plan) | **GET** /riskResponsePlan | Read RiskResponsePlans
[**get_risk_response_plan_field_length**](RiskResponsePlanApi.md#get_risk_response_plan_field_length) | **GET** /riskResponsePlan/getFieldLength/{fieldName} | View RiskResponsePlan Field Length
[**get_risk_response_plan_fields**](RiskResponsePlanApi.md#get_risk_response_plan_fields) | **GET** /riskResponsePlan/fields | View RiskResponsePlan fields
[**update_risk_response_plan**](RiskResponsePlanApi.md#update_risk_response_plan) | **PUT** /riskResponsePlan | Update RiskResponsePlans


# **create_risk_response_plan**
> str create_risk_response_plan(risk_response_plan, authorization=authorization)

Create RiskResponsePlans

Send a request to this endpoint to create one or more riskResponsePlan. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.risk_response_plan import RiskResponsePlan
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
    api_instance = openapi_client.RiskResponsePlanApi(api_client)
    risk_response_plan = [openapi_client.RiskResponsePlan()] # List[RiskResponsePlan] | A list of riskResponsePlan objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create RiskResponsePlans
        api_response = api_instance.create_risk_response_plan(risk_response_plan, authorization=authorization)
        print("The response of RiskResponsePlanApi->create_risk_response_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskResponsePlanApi->create_risk_response_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_response_plan** | [**List[RiskResponsePlan]**](RiskResponsePlan.md)| A list of riskResponsePlan objects. | 
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

# **delete_risk_response_plan**
> bool delete_risk_response_plan(authorization=authorization, object_id=object_id)

Delete RiskResponsePlans

Send a request to this endpoint to delete one or more riskResponsePlan. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.RiskResponsePlanApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of riskResponsePlan. (optional)

    try:
        # Delete RiskResponsePlans
        api_response = api_instance.delete_risk_response_plan(authorization=authorization, object_id=object_id)
        print("The response of RiskResponsePlanApi->delete_risk_response_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskResponsePlanApi->delete_risk_response_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| One or more system-generated identifiers of riskResponsePlan. | [optional] 

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

# **get_risk_response_plan**
> List[RiskResponsePlan] get_risk_response_plan(fields, filter=filter, order_by=order_by, authorization=authorization)

Read RiskResponsePlans

Reads RiskResponsePlan objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.risk_response_plan import RiskResponsePlan
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
    api_instance = openapi_client.RiskResponsePlanApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read RiskResponsePlans
        api_response = api_instance.get_risk_response_plan(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of RiskResponsePlanApi->get_risk_response_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskResponsePlanApi->get_risk_response_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[RiskResponsePlan]**](RiskResponsePlan.md)

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

# **get_risk_response_plan_field_length**
> str get_risk_response_plan_field_length(field_name, authorization=authorization)

View RiskResponsePlan Field Length

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
    api_instance = openapi_client.RiskResponsePlanApi(api_client)
    field_name = 'field_name_example' # str | A riskResponsePlan field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View RiskResponsePlan Field Length
        api_response = api_instance.get_risk_response_plan_field_length(field_name, authorization=authorization)
        print("The response of RiskResponsePlanApi->get_risk_response_plan_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskResponsePlanApi->get_risk_response_plan_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| A riskResponsePlan field. | 
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

# **get_risk_response_plan_fields**
> str get_risk_response_plan_fields()

View RiskResponsePlan fields

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
    api_instance = openapi_client.RiskResponsePlanApi(api_client)

    try:
        # View RiskResponsePlan fields
        api_response = api_instance.get_risk_response_plan_fields()
        print("The response of RiskResponsePlanApi->get_risk_response_plan_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskResponsePlanApi->get_risk_response_plan_fields: %s\n" % e)
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

# **update_risk_response_plan**
> bool update_risk_response_plan(risk_response_plan, authorization=authorization)

Update RiskResponsePlans

Send a request to this endpoint to update one or more riskResponsePlan. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.risk_response_plan import RiskResponsePlan
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
    api_instance = openapi_client.RiskResponsePlanApi(api_client)
    risk_response_plan = [openapi_client.RiskResponsePlan()] # List[RiskResponsePlan] | A list of riskResponsePlan objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update RiskResponsePlans
        api_response = api_instance.update_risk_response_plan(risk_response_plan, authorization=authorization)
        print("The response of RiskResponsePlanApi->update_risk_response_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskResponsePlanApi->update_risk_response_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_response_plan** | [**List[RiskResponsePlan]**](RiskResponsePlan.md)| A list of riskResponsePlan objects. | 
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

