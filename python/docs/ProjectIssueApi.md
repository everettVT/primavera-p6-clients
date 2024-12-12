# openapi_client.ProjectIssueApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_issue**](ProjectIssueApi.md#create_project_issue) | **POST** /projectIssue | Create ProjectIssue
[**delete_project_issue**](ProjectIssueApi.md#delete_project_issue) | **DELETE** /projectIssue | Delete ProjectIssue
[**get_project_issue**](ProjectIssueApi.md#get_project_issue) | **GET** /projectIssue | Reads ProjectIssue
[**get_project_issue_field_length**](ProjectIssueApi.md#get_project_issue_field_length) | **GET** /projectIssue/getFieldLength/{fieldName} | View ProjectIssue Field Length
[**get_project_issue_fields**](ProjectIssueApi.md#get_project_issue_fields) | **GET** /projectIssue/fields | View Project fields
[**update_project_issue**](ProjectIssueApi.md#update_project_issue) | **PUT** /projectIssue | Update ProjectIssue


# **create_project_issue**
> str create_project_issue(project_issue, authorization=authorization)

Create ProjectIssue

Send a request to this endpoint to create one or more ProjectIssue. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.project_issue import ProjectIssue
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
    api_instance = openapi_client.ProjectIssueApi(api_client)
    project_issue = [openapi_client.ProjectIssue()] # List[ProjectIssue] | A list of projectissue objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ProjectIssue
        api_response = api_instance.create_project_issue(project_issue, authorization=authorization)
        print("The response of ProjectIssueApi->create_project_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectIssueApi->create_project_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_issue** | [**List[ProjectIssue]**](ProjectIssue.md)| A list of projectissue objects. | 
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

# **delete_project_issue**
> bool delete_project_issue(object_id, authorization=authorization)

Delete ProjectIssue

Send a request to this endpoint to delete one or more ProjectIssue. An application object will be created for each JSON object provided in the request body

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
    api_instance = openapi_client.ProjectIssueApi(api_client)
    object_id = '1,2,3' # str | One or more system-generated identifiers of projectissue.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete ProjectIssue
        api_response = api_instance.delete_project_issue(object_id, authorization=authorization)
        print("The response of ProjectIssueApi->delete_project_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectIssueApi->delete_project_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| One or more system-generated identifiers of projectissue. | 
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

# **get_project_issue**
> List[ProjectIssue] get_project_issue(fields, filter=filter, order_by=order_by, authorization=authorization)

Reads ProjectIssue

Reads ProjectIssue objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.project_issue import ProjectIssue
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
    api_instance = openapi_client.ProjectIssueApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Reads ProjectIssue
        api_response = api_instance.get_project_issue(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ProjectIssueApi->get_project_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectIssueApi->get_project_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ProjectIssue]**](ProjectIssue.md)

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

# **get_project_issue_field_length**
> str get_project_issue_field_length(field_name, field_name2)

View ProjectIssue Field Length

Returns length of variable character fields for a BO.

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
    api_instance = openapi_client.ProjectIssueApi(api_client)
    field_name = 'field_name_example' # str | OAuth token
    field_name2 = 'field_name_example' # str | An projectissue field.

    try:
        # View ProjectIssue Field Length
        api_response = api_instance.get_project_issue_field_length(field_name, field_name2)
        print("The response of ProjectIssueApi->get_project_issue_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectIssueApi->get_project_issue_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| OAuth token | 
 **field_name2** | **str**| An projectissue field. | 

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

# **get_project_issue_fields**
> str get_project_issue_fields()

View Project fields

Returns length of variable character fields for a BO.

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
    api_instance = openapi_client.ProjectIssueApi(api_client)

    try:
        # View Project fields
        api_response = api_instance.get_project_issue_fields()
        print("The response of ProjectIssueApi->get_project_issue_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectIssueApi->get_project_issue_fields: %s\n" % e)
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

# **update_project_issue**
> bool update_project_issue(project_issue, authorization=authorization)

Update ProjectIssue

Send a request to this endpoint to update one or more ProjectIssue. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.project_issue import ProjectIssue
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
    api_instance = openapi_client.ProjectIssueApi(api_client)
    project_issue = [openapi_client.ProjectIssue()] # List[ProjectIssue] | A list of projectissue objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ProjectIssue
        api_response = api_instance.update_project_issue(project_issue, authorization=authorization)
        print("The response of ProjectIssueApi->update_project_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectIssueApi->update_project_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_issue** | [**List[ProjectIssue]**](ProjectIssue.md)| A list of projectissue objects. | 
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

