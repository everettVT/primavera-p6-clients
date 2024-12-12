# openapi_client.ProjectCodeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_code**](ProjectCodeApi.md#create_project_code) | **POST** /projectCode | Create ProjectCodes
[**delete_project_code**](ProjectCodeApi.md#delete_project_code) | **DELETE** /projectCode | Delete ProjectCodes
[**get_project_code**](ProjectCodeApi.md#get_project_code) | **GET** /projectCode | Read ProjectCodes
[**get_project_code_field_length**](ProjectCodeApi.md#get_project_code_field_length) | **GET** /projectCode/getFieldLength/{fieldName} | View ProjectCode Field Length
[**get_project_code_fields**](ProjectCodeApi.md#get_project_code_fields) | **GET** /projectCode/fields | View ProjectCode fields
[**update_project_code**](ProjectCodeApi.md#update_project_code) | **PUT** /projectCode | Update ProjectCodes


# **create_project_code**
> str create_project_code(project_code, authorization=authorization)

Create ProjectCodes

Send a request to this endpoint to create one or more projectCode. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.project_code import ProjectCode
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
    api_instance = openapi_client.ProjectCodeApi(api_client)
    project_code = [openapi_client.ProjectCode()] # List[ProjectCode] | A list of projectCode objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ProjectCodes
        api_response = api_instance.create_project_code(project_code, authorization=authorization)
        print("The response of ProjectCodeApi->create_project_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectCodeApi->create_project_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_code** | [**List[ProjectCode]**](ProjectCode.md)| A list of projectCode objects. | 
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

# **delete_project_code**
> bool delete_project_code(authorization=authorization, object_id=object_id)

Delete ProjectCodes

Send a request to this endpoint to delete one or more projectCode. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.ProjectCodeApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of projectCode. (optional)

    try:
        # Delete ProjectCodes
        api_response = api_instance.delete_project_code(authorization=authorization, object_id=object_id)
        print("The response of ProjectCodeApi->delete_project_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectCodeApi->delete_project_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| One or more system-generated identifiers of projectCode. | [optional] 

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

# **get_project_code**
> List[ProjectCode] get_project_code(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ProjectCodes

Reads ProjectCode objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.project_code import ProjectCode
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
    api_instance = openapi_client.ProjectCodeApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ProjectCodes
        api_response = api_instance.get_project_code(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ProjectCodeApi->get_project_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectCodeApi->get_project_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ProjectCode]**](ProjectCode.md)

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

# **get_project_code_field_length**
> str get_project_code_field_length(field_name, authorization=authorization)

View ProjectCode Field Length

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
    api_instance = openapi_client.ProjectCodeApi(api_client)
    field_name = 'field_name_example' # str | A projectCode field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ProjectCode Field Length
        api_response = api_instance.get_project_code_field_length(field_name, authorization=authorization)
        print("The response of ProjectCodeApi->get_project_code_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectCodeApi->get_project_code_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| A projectCode field. | 
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

# **get_project_code_fields**
> str get_project_code_fields()

View ProjectCode fields

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
    api_instance = openapi_client.ProjectCodeApi(api_client)

    try:
        # View ProjectCode fields
        api_response = api_instance.get_project_code_fields()
        print("The response of ProjectCodeApi->get_project_code_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectCodeApi->get_project_code_fields: %s\n" % e)
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

# **update_project_code**
> bool update_project_code(project_code, authorization=authorization)

Update ProjectCodes

Send a request to this endpoint to update one or more projectCode. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.project_code import ProjectCode
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
    api_instance = openapi_client.ProjectCodeApi(api_client)
    project_code = [openapi_client.ProjectCode()] # List[ProjectCode] | A list of projectCode objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ProjectCodes
        api_response = api_instance.update_project_code(project_code, authorization=authorization)
        print("The response of ProjectCodeApi->update_project_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectCodeApi->update_project_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_code** | [**List[ProjectCode]**](ProjectCode.md)| A list of projectCode objects. | 
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

