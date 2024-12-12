# openapi_client.RiskMatrixScoreApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_risk_matrix_score**](RiskMatrixScoreApi.md#create_risk_matrix_score) | **POST** /riskMatrixScore | Create RiskMatrixScores
[**delete_risk_matrix_score**](RiskMatrixScoreApi.md#delete_risk_matrix_score) | **DELETE** /riskMatrixScore | Delete RiskMatrixScores
[**get_risk_matrix_score**](RiskMatrixScoreApi.md#get_risk_matrix_score) | **GET** /riskMatrixScore | Read RiskMatrixScores
[**get_risk_matrix_score_field_length**](RiskMatrixScoreApi.md#get_risk_matrix_score_field_length) | **GET** /riskMatrixScore/getFieldLength/{fieldName} | View RiskMatrixScore Field Length
[**get_risk_matrix_score_fields**](RiskMatrixScoreApi.md#get_risk_matrix_score_fields) | **GET** /riskMatrixScore/fields | View RiskMatrixScore fields
[**update_risk_matrix_score**](RiskMatrixScoreApi.md#update_risk_matrix_score) | **PUT** /riskMatrixScore | Update RiskMatrixScores


# **create_risk_matrix_score**
> str create_risk_matrix_score(risk_matrix_score, authorization=authorization)

Create RiskMatrixScores

Send a request to this endpoint to create one or more riskMatrixScore. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.risk_matrix_score import RiskMatrixScore
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
    api_instance = openapi_client.RiskMatrixScoreApi(api_client)
    risk_matrix_score = [openapi_client.RiskMatrixScore()] # List[RiskMatrixScore] | A list of riskMatrixScore objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create RiskMatrixScores
        api_response = api_instance.create_risk_matrix_score(risk_matrix_score, authorization=authorization)
        print("The response of RiskMatrixScoreApi->create_risk_matrix_score:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskMatrixScoreApi->create_risk_matrix_score: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_matrix_score** | [**List[RiskMatrixScore]**](RiskMatrixScore.md)| A list of riskMatrixScore objects. | 
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

# **delete_risk_matrix_score**
> bool delete_risk_matrix_score(authorization=authorization, object_id=object_id)

Delete RiskMatrixScores

Send a request to this endpoint to delete one or more riskMatrixScore. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.RiskMatrixScoreApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of riskMatrixScore. (optional)

    try:
        # Delete RiskMatrixScores
        api_response = api_instance.delete_risk_matrix_score(authorization=authorization, object_id=object_id)
        print("The response of RiskMatrixScoreApi->delete_risk_matrix_score:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskMatrixScoreApi->delete_risk_matrix_score: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| One or more system-generated identifiers of riskMatrixScore. | [optional] 

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

# **get_risk_matrix_score**
> List[RiskMatrixScore] get_risk_matrix_score(fields, filter=filter, order_by=order_by, authorization=authorization)

Read RiskMatrixScores

Reads RiskMatrixScore objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.risk_matrix_score import RiskMatrixScore
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
    api_instance = openapi_client.RiskMatrixScoreApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read RiskMatrixScores
        api_response = api_instance.get_risk_matrix_score(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of RiskMatrixScoreApi->get_risk_matrix_score:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskMatrixScoreApi->get_risk_matrix_score: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[RiskMatrixScore]**](RiskMatrixScore.md)

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

# **get_risk_matrix_score_field_length**
> str get_risk_matrix_score_field_length(field_name, authorization=authorization)

View RiskMatrixScore Field Length

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
    api_instance = openapi_client.RiskMatrixScoreApi(api_client)
    field_name = 'field_name_example' # str | A riskMatrixScore field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View RiskMatrixScore Field Length
        api_response = api_instance.get_risk_matrix_score_field_length(field_name, authorization=authorization)
        print("The response of RiskMatrixScoreApi->get_risk_matrix_score_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskMatrixScoreApi->get_risk_matrix_score_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| A riskMatrixScore field. | 
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

# **get_risk_matrix_score_fields**
> str get_risk_matrix_score_fields()

View RiskMatrixScore fields

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
    api_instance = openapi_client.RiskMatrixScoreApi(api_client)

    try:
        # View RiskMatrixScore fields
        api_response = api_instance.get_risk_matrix_score_fields()
        print("The response of RiskMatrixScoreApi->get_risk_matrix_score_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskMatrixScoreApi->get_risk_matrix_score_fields: %s\n" % e)
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

# **update_risk_matrix_score**
> bool update_risk_matrix_score(risk_matrix_score, authorization=authorization)

Update RiskMatrixScores

Send a request to this endpoint to update one or more riskMatrixScore. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.risk_matrix_score import RiskMatrixScore
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
    api_instance = openapi_client.RiskMatrixScoreApi(api_client)
    risk_matrix_score = [openapi_client.RiskMatrixScore()] # List[RiskMatrixScore] | A list of riskMatrixScore objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update RiskMatrixScores
        api_response = api_instance.update_risk_matrix_score(risk_matrix_score, authorization=authorization)
        print("The response of RiskMatrixScoreApi->update_risk_matrix_score:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskMatrixScoreApi->update_risk_matrix_score: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_matrix_score** | [**List[RiskMatrixScore]**](RiskMatrixScore.md)| A list of riskMatrixScore objects. | 
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

