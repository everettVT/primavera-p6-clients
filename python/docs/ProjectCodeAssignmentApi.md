# openapi_client.ProjectCodeAssignmentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_code_assignment**](ProjectCodeAssignmentApi.md#create_project_code_assignment) | **POST** /projectCodeAssignment | Create ProjectCodeAssignment
[**delete_project_code_assignment**](ProjectCodeAssignmentApi.md#delete_project_code_assignment) | **DELETE** /projectCodeAssignment | Delete Project Code Assignment
[**get_project_code_assignment**](ProjectCodeAssignmentApi.md#get_project_code_assignment) | **GET** /projectCodeAssignment | Read ProjectCodeAssignment
[**get_project_code_assignment_field_length**](ProjectCodeAssignmentApi.md#get_project_code_assignment_field_length) | **GET** /projectCodeAssignment/getFieldLength/{fieldName} | View ProjectCodeAssignment Field Length
[**get_project_code_assignment_fields**](ProjectCodeAssignmentApi.md#get_project_code_assignment_fields) | **GET** /projectCodeAssignment/fields | View ProjectCodeAssignment Field
[**updateproject_code_assignment**](ProjectCodeAssignmentApi.md#updateproject_code_assignment) | **PUT** /projectCodeAssignment | Update ProjectCodeAssignment


# **create_project_code_assignment**
> List[CreateProjectCodeAssignmentsResponse] create_project_code_assignment(project_code_assignment, authorization=authorization)

Create ProjectCodeAssignment

Send a request to this endpoint to create one or more ProjectCodeAssignment. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.create_project_code_assignments_response import CreateProjectCodeAssignmentsResponse
from openapi_client.models.project_code_assignment import ProjectCodeAssignment
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
    api_instance = openapi_client.ProjectCodeAssignmentApi(api_client)
    project_code_assignment = [openapi_client.ProjectCodeAssignment()] # List[ProjectCodeAssignment] | A list of projectcodeassignment objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ProjectCodeAssignment
        api_response = api_instance.create_project_code_assignment(project_code_assignment, authorization=authorization)
        print("The response of ProjectCodeAssignmentApi->create_project_code_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectCodeAssignmentApi->create_project_code_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_code_assignment** | [**List[ProjectCodeAssignment]**](ProjectCodeAssignment.md)| A list of projectcodeassignment objects. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[CreateProjectCodeAssignmentsResponse]**](CreateProjectCodeAssignmentsResponse.md)

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

# **delete_project_code_assignment**
> bool delete_project_code_assignment(project_code_assignment, authorization=authorization)

Delete Project Code Assignment

Send a request to this endpoint to delete one or more ProjectCodeAssignment. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.project_code_assignment import ProjectCodeAssignment
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
    api_instance = openapi_client.ProjectCodeAssignmentApi(api_client)
    project_code_assignment = [openapi_client.ProjectCodeAssignment()] # List[ProjectCodeAssignment] | <p>A list of projectcodeassignment objects.<p><p>Required fields: You must supply both the ProjectCodeObjectId and ProjectObjectId fields when you use the Delete projectcodeassignment operation. All other fields are optional.</p>
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete Project Code Assignment
        api_response = api_instance.delete_project_code_assignment(project_code_assignment, authorization=authorization)
        print("The response of ProjectCodeAssignmentApi->delete_project_code_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectCodeAssignmentApi->delete_project_code_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_code_assignment** | [**List[ProjectCodeAssignment]**](ProjectCodeAssignment.md)| &lt;p&gt;A list of projectcodeassignment objects.&lt;p&gt;&lt;p&gt;Required fields: You must supply both the ProjectCodeObjectId and ProjectObjectId fields when you use the Delete projectcodeassignment operation. All other fields are optional.&lt;/p&gt; | 
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

# **get_project_code_assignment**
> List[ProjectCodeAssignment] get_project_code_assignment(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ProjectCodeAssignment

Reads ProjectCodeAssignment objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.project_code_assignment import ProjectCodeAssignment
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
    api_instance = openapi_client.ProjectCodeAssignmentApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ProjectCodeAssignment
        api_response = api_instance.get_project_code_assignment(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ProjectCodeAssignmentApi->get_project_code_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectCodeAssignmentApi->get_project_code_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ProjectCodeAssignment]**](ProjectCodeAssignment.md)

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

# **get_project_code_assignment_field_length**
> str get_project_code_assignment_field_length(field_name, authorization=authorization)

View ProjectCodeAssignment Field Length

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
    api_instance = openapi_client.ProjectCodeAssignmentApi(api_client)
    field_name = 'field_name_example' # str | An projectcodeassignment field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ProjectCodeAssignment Field Length
        api_response = api_instance.get_project_code_assignment_field_length(field_name, authorization=authorization)
        print("The response of ProjectCodeAssignmentApi->get_project_code_assignment_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectCodeAssignmentApi->get_project_code_assignment_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An projectcodeassignment field. | 
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

# **get_project_code_assignment_fields**
> str get_project_code_assignment_fields()

View ProjectCodeAssignment Field

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
    api_instance = openapi_client.ProjectCodeAssignmentApi(api_client)

    try:
        # View ProjectCodeAssignment Field
        api_response = api_instance.get_project_code_assignment_fields()
        print("The response of ProjectCodeAssignmentApi->get_project_code_assignment_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectCodeAssignmentApi->get_project_code_assignment_fields: %s\n" % e)
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

# **updateproject_code_assignment**
> bool updateproject_code_assignment(project_code_assignment, authorization=authorization)

Update ProjectCodeAssignment

Send a request to this endpoint to update one or more ProjectCodeAssignment. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.project_code_assignment import ProjectCodeAssignment
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
    api_instance = openapi_client.ProjectCodeAssignmentApi(api_client)
    project_code_assignment = [openapi_client.ProjectCodeAssignment()] # List[ProjectCodeAssignment] | <p>A list of projectcodeassignment objects.<p><p>Required fields: You must supply both the ProjectCodeObjectId and ProjectObjectId fields when you use the Update projectcodeassignment operation. All other fields are optional.</p>
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ProjectCodeAssignment
        api_response = api_instance.updateproject_code_assignment(project_code_assignment, authorization=authorization)
        print("The response of ProjectCodeAssignmentApi->updateproject_code_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectCodeAssignmentApi->updateproject_code_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_code_assignment** | [**List[ProjectCodeAssignment]**](ProjectCodeAssignment.md)| &lt;p&gt;A list of projectcodeassignment objects.&lt;p&gt;&lt;p&gt;Required fields: You must supply both the ProjectCodeObjectId and ProjectObjectId fields when you use the Update projectcodeassignment operation. All other fields are optional.&lt;/p&gt; | 
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

