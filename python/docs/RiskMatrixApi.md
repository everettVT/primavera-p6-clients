# openapi_client.RiskMatrixApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_risk_matrix**](RiskMatrixApi.md#create_risk_matrix) | **POST** /riskMatrix | Create RiskMatrixs
[**delete_risk_matrix**](RiskMatrixApi.md#delete_risk_matrix) | **DELETE** /riskMatrix | Delete RiskMatrixs
[**get_risk_matrix**](RiskMatrixApi.md#get_risk_matrix) | **GET** /riskMatrix | Read RiskMatrixs
[**get_risk_matrix_field_length**](RiskMatrixApi.md#get_risk_matrix_field_length) | **GET** /riskMatrix/getFieldLength/{fieldName} | View RiskMatrix Field Length
[**get_risk_matrix_fields**](RiskMatrixApi.md#get_risk_matrix_fields) | **GET** /riskMatrix/fields | View RiskMatrix fields
[**update_risk_matrix**](RiskMatrixApi.md#update_risk_matrix) | **PUT** /riskMatrix | Update RiskMatrixs


# **create_risk_matrix**
> str create_risk_matrix(risk_matrix, authorization=authorization)

Create RiskMatrixs

Send a request to this endpoint to create one or more riskMatrix. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.risk_matrix import RiskMatrix
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
    api_instance = openapi_client.RiskMatrixApi(api_client)
    risk_matrix = [openapi_client.RiskMatrix()] # List[RiskMatrix] | A list of riskMatrix objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create RiskMatrixs
        api_response = api_instance.create_risk_matrix(risk_matrix, authorization=authorization)
        print("The response of RiskMatrixApi->create_risk_matrix:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskMatrixApi->create_risk_matrix: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_matrix** | [**List[RiskMatrix]**](RiskMatrix.md)| A list of riskMatrix objects. | 
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

# **delete_risk_matrix**
> bool delete_risk_matrix(authorization=authorization, object_id=object_id)

Delete RiskMatrixs

Send a request to this endpoint to delete one or more riskMatrix. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.RiskMatrixApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of riskMatrix. (optional)

    try:
        # Delete RiskMatrixs
        api_response = api_instance.delete_risk_matrix(authorization=authorization, object_id=object_id)
        print("The response of RiskMatrixApi->delete_risk_matrix:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskMatrixApi->delete_risk_matrix: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| One or more system-generated identifiers of riskMatrix. | [optional] 

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

# **get_risk_matrix**
> List[RiskMatrix] get_risk_matrix(fields, filter=filter, order_by=order_by, authorization=authorization)

Read RiskMatrixs

Reads RiskMatrix objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.risk_matrix import RiskMatrix
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
    api_instance = openapi_client.RiskMatrixApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read RiskMatrixs
        api_response = api_instance.get_risk_matrix(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of RiskMatrixApi->get_risk_matrix:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskMatrixApi->get_risk_matrix: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[RiskMatrix]**](RiskMatrix.md)

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

# **get_risk_matrix_field_length**
> str get_risk_matrix_field_length(field_name, authorization=authorization)

View RiskMatrix Field Length

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
    api_instance = openapi_client.RiskMatrixApi(api_client)
    field_name = 'field_name_example' # str | A riskMatrix field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View RiskMatrix Field Length
        api_response = api_instance.get_risk_matrix_field_length(field_name, authorization=authorization)
        print("The response of RiskMatrixApi->get_risk_matrix_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskMatrixApi->get_risk_matrix_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| A riskMatrix field. | 
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

# **get_risk_matrix_fields**
> str get_risk_matrix_fields()

View RiskMatrix fields

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
    api_instance = openapi_client.RiskMatrixApi(api_client)

    try:
        # View RiskMatrix fields
        api_response = api_instance.get_risk_matrix_fields()
        print("The response of RiskMatrixApi->get_risk_matrix_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskMatrixApi->get_risk_matrix_fields: %s\n" % e)
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

# **update_risk_matrix**
> bool update_risk_matrix(risk_matrix, authorization=authorization)

Update RiskMatrixs

Send a request to this endpoint to update one or more riskMatrix. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.risk_matrix import RiskMatrix
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
    api_instance = openapi_client.RiskMatrixApi(api_client)
    risk_matrix = [openapi_client.RiskMatrix()] # List[RiskMatrix] | A list of riskMatrix objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update RiskMatrixs
        api_response = api_instance.update_risk_matrix(risk_matrix, authorization=authorization)
        print("The response of RiskMatrixApi->update_risk_matrix:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskMatrixApi->update_risk_matrix: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_matrix** | [**List[RiskMatrix]**](RiskMatrix.md)| A list of riskMatrix objects. | 
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

