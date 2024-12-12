# openapi_client.ProjectCodeTypeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_code_type**](ProjectCodeTypeApi.md#create_project_code_type) | **POST** /projectCodeType | Create ProjectCodeTypes
[**delete_project_code_type**](ProjectCodeTypeApi.md#delete_project_code_type) | **DELETE** /projectCodeType | Delete ProjectCodeTypes
[**get_project_code_type**](ProjectCodeTypeApi.md#get_project_code_type) | **GET** /projectCodeType | Read ProjectCodeTypes
[**get_project_code_type_field_length**](ProjectCodeTypeApi.md#get_project_code_type_field_length) | **GET** /projectCodeType/getFieldLength/{fieldName} | View ProjectCodeType Field Length
[**get_project_code_type_fields**](ProjectCodeTypeApi.md#get_project_code_type_fields) | **GET** /projectCodeType/fields | View ProjectCodeType fields
[**update_project_code_type**](ProjectCodeTypeApi.md#update_project_code_type) | **PUT** /projectCodeType | Update ProjectCodeTypes


# **create_project_code_type**
> str create_project_code_type(project_code_type, authorization=authorization)

Create ProjectCodeTypes

Send a request to this endpoint to create one or more projectCodeType. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.project_code_type import ProjectCodeType
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
    api_instance = openapi_client.ProjectCodeTypeApi(api_client)
    project_code_type = [openapi_client.ProjectCodeType()] # List[ProjectCodeType] | A list of projectCodeType objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ProjectCodeTypes
        api_response = api_instance.create_project_code_type(project_code_type, authorization=authorization)
        print("The response of ProjectCodeTypeApi->create_project_code_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectCodeTypeApi->create_project_code_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_code_type** | [**List[ProjectCodeType]**](ProjectCodeType.md)| A list of projectCodeType objects. | 
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

# **delete_project_code_type**
> bool delete_project_code_type(authorization=authorization, object_id=object_id)

Delete ProjectCodeTypes

Send a request to this endpoint to delete one or more projectCodeType. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.ProjectCodeTypeApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of projectCodeType. (optional)

    try:
        # Delete ProjectCodeTypes
        api_response = api_instance.delete_project_code_type(authorization=authorization, object_id=object_id)
        print("The response of ProjectCodeTypeApi->delete_project_code_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectCodeTypeApi->delete_project_code_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| One or more system-generated identifiers of projectCodeType. | [optional] 

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

# **get_project_code_type**
> List[ProjectCodeType] get_project_code_type(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ProjectCodeTypes

Reads ProjectCodeType objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.project_code_type import ProjectCodeType
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
    api_instance = openapi_client.ProjectCodeTypeApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ProjectCodeTypes
        api_response = api_instance.get_project_code_type(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ProjectCodeTypeApi->get_project_code_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectCodeTypeApi->get_project_code_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ProjectCodeType]**](ProjectCodeType.md)

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

# **get_project_code_type_field_length**
> str get_project_code_type_field_length(field_name, authorization=authorization)

View ProjectCodeType Field Length

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
    api_instance = openapi_client.ProjectCodeTypeApi(api_client)
    field_name = 'field_name_example' # str | A projectCodeType field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ProjectCodeType Field Length
        api_response = api_instance.get_project_code_type_field_length(field_name, authorization=authorization)
        print("The response of ProjectCodeTypeApi->get_project_code_type_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectCodeTypeApi->get_project_code_type_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| A projectCodeType field. | 
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

# **get_project_code_type_fields**
> str get_project_code_type_fields()

View ProjectCodeType fields

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
    api_instance = openapi_client.ProjectCodeTypeApi(api_client)

    try:
        # View ProjectCodeType fields
        api_response = api_instance.get_project_code_type_fields()
        print("The response of ProjectCodeTypeApi->get_project_code_type_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectCodeTypeApi->get_project_code_type_fields: %s\n" % e)
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

# **update_project_code_type**
> bool update_project_code_type(project_code_type, authorization=authorization)

Update ProjectCodeTypes

Send a request to this endpoint to update one or more projectCodeType. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.project_code_type import ProjectCodeType
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
    api_instance = openapi_client.ProjectCodeTypeApi(api_client)
    project_code_type = [openapi_client.ProjectCodeType()] # List[ProjectCodeType] | A list of projectCodeType objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ProjectCodeTypes
        api_response = api_instance.update_project_code_type(project_code_type, authorization=authorization)
        print("The response of ProjectCodeTypeApi->update_project_code_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectCodeTypeApi->update_project_code_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_code_type** | [**List[ProjectCodeType]**](ProjectCodeType.md)| A list of projectCodeType objects. | 
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

