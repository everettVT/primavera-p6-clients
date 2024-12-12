# openapi_client.BaselineProjectApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_baseline_project**](BaselineProjectApi.md#create_baseline_project) | **POST** /baselineProject | Create BaselineProjects
[**delete_baseline_project**](BaselineProjectApi.md#delete_baseline_project) | **DELETE** /baselineProject | Delete BaselineProjects
[**get_baseline_project_field_length**](BaselineProjectApi.md#get_baseline_project_field_length) | **GET** /baselineProject/getFieldLength/{fieldName} | View BaselineProject Field Length
[**get_baseline_project_fields**](BaselineProjectApi.md#get_baseline_project_fields) | **GET** /baselineProject/fields | View BaselineProject fields
[**get_baseline_projects**](BaselineProjectApi.md#get_baseline_projects) | **GET** /baselineProject | Read BaselineProjects
[**update_baseline_project**](BaselineProjectApi.md#update_baseline_project) | **PUT** /baselineProject | Update BaselineProjects


# **create_baseline_project**
> str create_baseline_project(baseline_project, authorization=authorization)

Create BaselineProjects

Send a request to this endpoint to create one or more baselineProject. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.baseline_project import BaselineProject
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
    api_instance = openapi_client.BaselineProjectApi(api_client)
    baseline_project = [openapi_client.BaselineProject()] # List[BaselineProject] | A list of baselineProject objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create BaselineProjects
        api_response = api_instance.create_baseline_project(baseline_project, authorization=authorization)
        print("The response of BaselineProjectApi->create_baseline_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BaselineProjectApi->create_baseline_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **baseline_project** | [**List[BaselineProject]**](BaselineProject.md)| A list of baselineProject objects. | 
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

# **delete_baseline_project**
> bool delete_baseline_project(authorization=authorization, object_id=object_id)

Delete BaselineProjects

Send a request to this endpoint to delete one or more baselineProject. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.BaselineProjectApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of baselineProject. (optional)

    try:
        # Delete BaselineProjects
        api_response = api_instance.delete_baseline_project(authorization=authorization, object_id=object_id)
        print("The response of BaselineProjectApi->delete_baseline_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BaselineProjectApi->delete_baseline_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| One or more system-generated identifiers of baselineProject. | [optional] 

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

# **get_baseline_project_field_length**
> str get_baseline_project_field_length(field_name, authorization=authorization)

View BaselineProject Field Length

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
    api_instance = openapi_client.BaselineProjectApi(api_client)
    field_name = 'field_name_example' # str | A baselineProject field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View BaselineProject Field Length
        api_response = api_instance.get_baseline_project_field_length(field_name, authorization=authorization)
        print("The response of BaselineProjectApi->get_baseline_project_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BaselineProjectApi->get_baseline_project_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| A baselineProject field. | 
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

# **get_baseline_project_fields**
> str get_baseline_project_fields()

View BaselineProject fields

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
    api_instance = openapi_client.BaselineProjectApi(api_client)

    try:
        # View BaselineProject fields
        api_response = api_instance.get_baseline_project_fields()
        print("The response of BaselineProjectApi->get_baseline_project_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BaselineProjectApi->get_baseline_project_fields: %s\n" % e)
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

# **get_baseline_projects**
> List[BaselineProject] get_baseline_projects(fields, filter=filter, order_by=order_by, authorization=authorization)

Read BaselineProjects

Reads BaselineProject objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.baseline_project import BaselineProject
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
    api_instance = openapi_client.BaselineProjectApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read BaselineProjects
        api_response = api_instance.get_baseline_projects(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of BaselineProjectApi->get_baseline_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BaselineProjectApi->get_baseline_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[BaselineProject]**](BaselineProject.md)

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

# **update_baseline_project**
> bool update_baseline_project(baseline_project, authorization=authorization)

Update BaselineProjects

Send a request to this endpoint to update one or more baselineProject. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.baseline_project import BaselineProject
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
    api_instance = openapi_client.BaselineProjectApi(api_client)
    baseline_project = [openapi_client.BaselineProject()] # List[BaselineProject] | A list of baselineProject objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update BaselineProjects
        api_response = api_instance.update_baseline_project(baseline_project, authorization=authorization)
        print("The response of BaselineProjectApi->update_baseline_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BaselineProjectApi->update_baseline_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **baseline_project** | [**List[BaselineProject]**](BaselineProject.md)| A list of baselineProject objects. | 
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

