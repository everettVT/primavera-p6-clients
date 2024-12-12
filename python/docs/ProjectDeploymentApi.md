# openapi_client.ProjectDeploymentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_deployment**](ProjectDeploymentApi.md#create_project_deployment) | **POST** /projectDeployment | Create ProjectDeployment
[**delete_project_deployment**](ProjectDeploymentApi.md#delete_project_deployment) | **DELETE** /projectDeployment | Delete ProjectDeployment
[**get_project_deployment**](ProjectDeploymentApi.md#get_project_deployment) | **GET** /projectDeployment | Read ProjectDeployment
[**get_project_deployment_field_length**](ProjectDeploymentApi.md#get_project_deployment_field_length) | **GET** /projectDeployment/getFieldLength/{fieldName} | View ProjectDeployment Field Length
[**get_project_deployment_fields**](ProjectDeploymentApi.md#get_project_deployment_fields) | **GET** /projectDeployment/fields | View ProjectResourceQuantity fields
[**update_project_deployment**](ProjectDeploymentApi.md#update_project_deployment) | **PUT** /projectDeployment | Update ProjectDeployment


# **create_project_deployment**
> str create_project_deployment(project_deployment, authorization=authorization)

Create ProjectDeployment

Send a request to this endpoint to create one or more ProjectDeployment. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.project_deployment import ProjectDeployment
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
    api_instance = openapi_client.ProjectDeploymentApi(api_client)
    project_deployment = [openapi_client.ProjectDeployment()] # List[ProjectDeployment] | A list of projectdeployment objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ProjectDeployment
        api_response = api_instance.create_project_deployment(project_deployment, authorization=authorization)
        print("The response of ProjectDeploymentApi->create_project_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDeploymentApi->create_project_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_deployment** | [**List[ProjectDeployment]**](ProjectDeployment.md)| A list of projectdeployment objects. | 
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

# **delete_project_deployment**
> bool delete_project_deployment(object_id, authorization=authorization)

Delete ProjectDeployment

Send a request to this endpoint to delete one or more ProjectResourceQuantity. An application object will be created for each JSON object provided in the request body

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
    api_instance = openapi_client.ProjectDeploymentApi(api_client)
    object_id = '1,2,3' # str | A list of ProjectDeployment objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete ProjectDeployment
        api_response = api_instance.delete_project_deployment(object_id, authorization=authorization)
        print("The response of ProjectDeploymentApi->delete_project_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDeploymentApi->delete_project_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| A list of ProjectDeployment objects. | 
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

# **get_project_deployment**
> List[ProjectDeployment] get_project_deployment(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ProjectDeployment

Reads ProjectDeployment objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.project_deployment import ProjectDeployment
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
    api_instance = openapi_client.ProjectDeploymentApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ProjectDeployment
        api_response = api_instance.get_project_deployment(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ProjectDeploymentApi->get_project_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDeploymentApi->get_project_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ProjectDeployment]**](ProjectDeployment.md)

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

# **get_project_deployment_field_length**
> str get_project_deployment_field_length(field_name, authorization=authorization)

View ProjectDeployment Field Length

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
    api_instance = openapi_client.ProjectDeploymentApi(api_client)
    field_name = 'field_name_example' # str | An ProjectDeployment field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ProjectDeployment Field Length
        api_response = api_instance.get_project_deployment_field_length(field_name, authorization=authorization)
        print("The response of ProjectDeploymentApi->get_project_deployment_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDeploymentApi->get_project_deployment_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An ProjectDeployment field. | 
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

# **get_project_deployment_fields**
> str get_project_deployment_fields()

View ProjectResourceQuantity fields

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
    api_instance = openapi_client.ProjectDeploymentApi(api_client)

    try:
        # View ProjectResourceQuantity fields
        api_response = api_instance.get_project_deployment_fields()
        print("The response of ProjectDeploymentApi->get_project_deployment_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDeploymentApi->get_project_deployment_fields: %s\n" % e)
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

# **update_project_deployment**
> bool update_project_deployment(project_deployment, authorization=authorization)

Update ProjectDeployment

Send a request to this endpoint to update one or more ProjectDeployment. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.project_deployment import ProjectDeployment
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
    api_instance = openapi_client.ProjectDeploymentApi(api_client)
    project_deployment = [openapi_client.ProjectDeployment()] # List[ProjectDeployment] | A list of ProjectDeployment objects
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ProjectDeployment
        api_response = api_instance.update_project_deployment(project_deployment, authorization=authorization)
        print("The response of ProjectDeploymentApi->update_project_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDeploymentApi->update_project_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_deployment** | [**List[ProjectDeployment]**](ProjectDeployment.md)| A list of ProjectDeployment objects | 
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

