# openapi_client.ProjectResourceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_resource**](ProjectResourceApi.md#create_project_resource) | **POST** /projectResource | Create ProjectResource
[**delete_project_resource**](ProjectResourceApi.md#delete_project_resource) | **DELETE** /projectResource | Delete ProjectResource
[**get_project_resource**](ProjectResourceApi.md#get_project_resource) | **GET** /projectResource | Read ProjectResource
[**get_project_resource_field_length**](ProjectResourceApi.md#get_project_resource_field_length) | **GET** /projectResource/getFieldLength/{fieldName} | View ProjectResource Field Length
[**get_project_resource_fields**](ProjectResourceApi.md#get_project_resource_fields) | **GET** /projectResource/fields | View ProjectResource fields
[**update_project_resource**](ProjectResourceApi.md#update_project_resource) | **PUT** /projectResource | Update ProjectResource


# **create_project_resource**
> str create_project_resource(project_resource, authorization=authorization)

Create ProjectResource

Send a request to this endpoint to create one or more ProjectResource. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.project_resource import ProjectResource
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
    api_instance = openapi_client.ProjectResourceApi(api_client)
    project_resource = [openapi_client.ProjectResource()] # List[ProjectResource] | A list of ProjectResource objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ProjectResource
        api_response = api_instance.create_project_resource(project_resource, authorization=authorization)
        print("The response of ProjectResourceApi->create_project_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectResourceApi->create_project_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_resource** | [**List[ProjectResource]**](ProjectResource.md)| A list of ProjectResource objects. | 
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

# **delete_project_resource**
> bool delete_project_resource(object_id, authorization=authorization)

Delete ProjectResource

Send a request to this endpoint to delete one or more ProjectResource. An application object will be created for each JSON object provided in the request body

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
    api_instance = openapi_client.ProjectResourceApi(api_client)
    object_id = '1,2,3' # str | One or more system-generated identifiers of ProjectResource.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete ProjectResource
        api_response = api_instance.delete_project_resource(object_id, authorization=authorization)
        print("The response of ProjectResourceApi->delete_project_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectResourceApi->delete_project_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| One or more system-generated identifiers of ProjectResource. | 
 **authorization** | **str**| OAuth token | [optional] 

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

# **get_project_resource**
> List[ProjectResource] get_project_resource(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ProjectResource

Reads ProjectResource objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.project_resource import ProjectResource
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
    api_instance = openapi_client.ProjectResourceApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ProjectResource
        api_response = api_instance.get_project_resource(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ProjectResourceApi->get_project_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectResourceApi->get_project_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ProjectResource]**](ProjectResource.md)

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

# **get_project_resource_field_length**
> str get_project_resource_field_length(field_name, authorization=authorization)

View ProjectResource Field Length

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
    api_instance = openapi_client.ProjectResourceApi(api_client)
    field_name = 'field_name_example' # str | An ProjectResource field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ProjectResource Field Length
        api_response = api_instance.get_project_resource_field_length(field_name, authorization=authorization)
        print("The response of ProjectResourceApi->get_project_resource_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectResourceApi->get_project_resource_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An ProjectResource field. | 
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

# **get_project_resource_fields**
> str get_project_resource_fields()

View ProjectResource fields

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
    api_instance = openapi_client.ProjectResourceApi(api_client)

    try:
        # View ProjectResource fields
        api_response = api_instance.get_project_resource_fields()
        print("The response of ProjectResourceApi->get_project_resource_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectResourceApi->get_project_resource_fields: %s\n" % e)
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

# **update_project_resource**
> bool update_project_resource(project_resource, authorization=authorization)

Update ProjectResource

Send a request to this endpoint to update one or more ProjectResource. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.project_resource import ProjectResource
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
    api_instance = openapi_client.ProjectResourceApi(api_client)
    project_resource = [openapi_client.ProjectResource()] # List[ProjectResource] | A list of ProjectResource objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ProjectResource
        api_response = api_instance.update_project_resource(project_resource, authorization=authorization)
        print("The response of ProjectResourceApi->update_project_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectResourceApi->update_project_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_resource** | [**List[ProjectResource]**](ProjectResource.md)| A list of ProjectResource objects. | 
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

