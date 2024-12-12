# openapi_client.ProjectThresholdApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_threshold**](ProjectThresholdApi.md#create_project_threshold) | **POST** /projectThreshold | Create ProjectThreshold
[**delete_project_threshold**](ProjectThresholdApi.md#delete_project_threshold) | **DELETE** /projectThreshold | Delete ProjectThreshold
[**get_project_threshold**](ProjectThresholdApi.md#get_project_threshold) | **GET** /projectThreshold | Read ProjectThreshold
[**get_project_threshold_field_length**](ProjectThresholdApi.md#get_project_threshold_field_length) | **GET** /projectThreshold/getFieldLength/{fieldName} | View Project Field Length
[**get_project_threshold_fields**](ProjectThresholdApi.md#get_project_threshold_fields) | **GET** /projectThreshold/fields | View Project fields
[**update_project_threshold**](ProjectThresholdApi.md#update_project_threshold) | **PUT** /projectThreshold | Update ProjectThreshold


# **create_project_threshold**
> str create_project_threshold(project_threshold, authorization=authorization)

Create ProjectThreshold

Send a request to this endpoint to create one or more ProjectThreshold. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.project_threshold import ProjectThreshold
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
    api_instance = openapi_client.ProjectThresholdApi(api_client)
    project_threshold = [openapi_client.ProjectThreshold()] # List[ProjectThreshold] | A list of projectthreshold objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ProjectThreshold
        api_response = api_instance.create_project_threshold(project_threshold, authorization=authorization)
        print("The response of ProjectThresholdApi->create_project_threshold:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectThresholdApi->create_project_threshold: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_threshold** | [**List[ProjectThreshold]**](ProjectThreshold.md)| A list of projectthreshold objects. | 
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

# **delete_project_threshold**
> bool delete_project_threshold(object_id, authorization=authorization)

Delete ProjectThreshold

Send a request to this endpoint to delete one or more ProjectThreshold. An application object will be created for each JSON object provided in the request body

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
    api_instance = openapi_client.ProjectThresholdApi(api_client)
    object_id = '1,2,3' # str | One or more system-generated identifiers of projectthreshold.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete ProjectThreshold
        api_response = api_instance.delete_project_threshold(object_id, authorization=authorization)
        print("The response of ProjectThresholdApi->delete_project_threshold:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectThresholdApi->delete_project_threshold: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| One or more system-generated identifiers of projectthreshold. | 
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

# **get_project_threshold**
> List[ProjectThreshold] get_project_threshold(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ProjectThreshold

Reads Project objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.project_threshold import ProjectThreshold
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
    api_instance = openapi_client.ProjectThresholdApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ProjectThreshold
        api_response = api_instance.get_project_threshold(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ProjectThresholdApi->get_project_threshold:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectThresholdApi->get_project_threshold: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ProjectThreshold]**](ProjectThreshold.md)

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

# **get_project_threshold_field_length**
> str get_project_threshold_field_length(field_name, authorization=authorization)

View Project Field Length

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
    api_instance = openapi_client.ProjectThresholdApi(api_client)
    field_name = 'field_name_example' # str | An projectthreshold field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View Project Field Length
        api_response = api_instance.get_project_threshold_field_length(field_name, authorization=authorization)
        print("The response of ProjectThresholdApi->get_project_threshold_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectThresholdApi->get_project_threshold_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An projectthreshold field. | 
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

# **get_project_threshold_fields**
> str get_project_threshold_fields()

View Project fields

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
    api_instance = openapi_client.ProjectThresholdApi(api_client)

    try:
        # View Project fields
        api_response = api_instance.get_project_threshold_fields()
        print("The response of ProjectThresholdApi->get_project_threshold_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectThresholdApi->get_project_threshold_fields: %s\n" % e)
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

# **update_project_threshold**
> bool update_project_threshold(project_threshold, authorization=authorization)

Update ProjectThreshold

Send a request to this endpoint to update one or more ProjectThreshold. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.project_threshold import ProjectThreshold
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
    api_instance = openapi_client.ProjectThresholdApi(api_client)
    project_threshold = [openapi_client.ProjectThreshold()] # List[ProjectThreshold] | A list of projectthreshold objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ProjectThreshold
        api_response = api_instance.update_project_threshold(project_threshold, authorization=authorization)
        print("The response of ProjectThresholdApi->update_project_threshold:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectThresholdApi->update_project_threshold: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_threshold** | [**List[ProjectThreshold]**](ProjectThreshold.md)| A list of projectthreshold objects. | 
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

