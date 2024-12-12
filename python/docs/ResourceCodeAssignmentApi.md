# openapi_client.ResourceCodeAssignmentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_resource_code_assignment**](ResourceCodeAssignmentApi.md#create_resource_code_assignment) | **POST** /resourceCodeAssignment | Create ResourceCodeAssignment
[**delete_resource_code_assignment**](ResourceCodeAssignmentApi.md#delete_resource_code_assignment) | **DELETE** /resourceCodeAssignment | Delete ResourceCodeAssignment
[**get_resource_code_assignment**](ResourceCodeAssignmentApi.md#get_resource_code_assignment) | **GET** /resourceCodeAssignment | Read ResourceCodeAssignment
[**get_resource_code_assignment_field_length**](ResourceCodeAssignmentApi.md#get_resource_code_assignment_field_length) | **GET** /resourceCodeAssignment/getFieldLength/{fieldName} | View ResourceCodeAssignment Field Length
[**get_resource_code_assignment_fields**](ResourceCodeAssignmentApi.md#get_resource_code_assignment_fields) | **GET** /resourceCodeAssignment/fields | View ResourceCodeAssignment fields
[**update_resource_code_assignment**](ResourceCodeAssignmentApi.md#update_resource_code_assignment) | **PUT** /resourceCodeAssignment | Update ResourceCodeAssignment


# **create_resource_code_assignment**
> CreateResourceCodeAssignmentsResponse create_resource_code_assignment(resource_code_assignment, authorization=authorization)

Create ResourceCodeAssignment

Send a request to this endpoint to create one or more ResourceCodeAssignment. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.create_resource_code_assignments_response import CreateResourceCodeAssignmentsResponse
from openapi_client.models.resource_code_assignment import ResourceCodeAssignment
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
    api_instance = openapi_client.ResourceCodeAssignmentApi(api_client)
    resource_code_assignment = [openapi_client.ResourceCodeAssignment()] # List[ResourceCodeAssignment] | A list of ResourceCodeAssignment objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ResourceCodeAssignment
        api_response = api_instance.create_resource_code_assignment(resource_code_assignment, authorization=authorization)
        print("The response of ResourceCodeAssignmentApi->create_resource_code_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceCodeAssignmentApi->create_resource_code_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_code_assignment** | [**List[ResourceCodeAssignment]**](ResourceCodeAssignment.md)| A list of ResourceCodeAssignment objects. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**CreateResourceCodeAssignmentsResponse**](CreateResourceCodeAssignmentsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ResourceCodeAssignment Created. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resource_code_assignment**
> bool delete_resource_code_assignment(resource_code_assignment, authorization=authorization)

Delete ResourceCodeAssignment

Send a request to this endpoint to delete one or more ResourceCodeAssignment. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.resource_code_assignment import ResourceCodeAssignment
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
    api_instance = openapi_client.ResourceCodeAssignmentApi(api_client)
    resource_code_assignment = [openapi_client.ResourceCodeAssignment()] # List[ResourceCodeAssignment] | <p>A list of ResourceCodeAssignment objects.<p><p>Required fields: You must supply both the ResourceCodeTypeObjectId and ResourceObjectId fields when you use the Delete ResourceAssignmentUpdate operation. All other fields are optional.</p>
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete ResourceCodeAssignment
        api_response = api_instance.delete_resource_code_assignment(resource_code_assignment, authorization=authorization)
        print("The response of ResourceCodeAssignmentApi->delete_resource_code_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceCodeAssignmentApi->delete_resource_code_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_code_assignment** | [**List[ResourceCodeAssignment]**](ResourceCodeAssignment.md)| &lt;p&gt;A list of ResourceCodeAssignment objects.&lt;p&gt;&lt;p&gt;Required fields: You must supply both the ResourceCodeTypeObjectId and ResourceObjectId fields when you use the Delete ResourceAssignmentUpdate operation. All other fields are optional.&lt;/p&gt; | 
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

# **get_resource_code_assignment**
> List[ResourceCodeAssignment] get_resource_code_assignment(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ResourceCodeAssignment

Reads ResourceCodeAssignment objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.resource_code_assignment import ResourceCodeAssignment
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
    api_instance = openapi_client.ResourceCodeAssignmentApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ResourceCodeAssignment
        api_response = api_instance.get_resource_code_assignment(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ResourceCodeAssignmentApi->get_resource_code_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceCodeAssignmentApi->get_resource_code_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ResourceCodeAssignment]**](ResourceCodeAssignment.md)

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

# **get_resource_code_assignment_field_length**
> str get_resource_code_assignment_field_length(field_name, authorization=authorization)

View ResourceCodeAssignment Field Length

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
    api_instance = openapi_client.ResourceCodeAssignmentApi(api_client)
    field_name = 'field_name_example' # str | An ResourceCodeAssignment field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ResourceCodeAssignment Field Length
        api_response = api_instance.get_resource_code_assignment_field_length(field_name, authorization=authorization)
        print("The response of ResourceCodeAssignmentApi->get_resource_code_assignment_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceCodeAssignmentApi->get_resource_code_assignment_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An ResourceCodeAssignment field. | 
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

# **get_resource_code_assignment_fields**
> str get_resource_code_assignment_fields()

View ResourceCodeAssignment fields

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
    api_instance = openapi_client.ResourceCodeAssignmentApi(api_client)

    try:
        # View ResourceCodeAssignment fields
        api_response = api_instance.get_resource_code_assignment_fields()
        print("The response of ResourceCodeAssignmentApi->get_resource_code_assignment_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceCodeAssignmentApi->get_resource_code_assignment_fields: %s\n" % e)
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

# **update_resource_code_assignment**
> bool update_resource_code_assignment(resource_code_assignment, authorization=authorization)

Update ResourceCodeAssignment

Send a request to this endpoint to update one or more ResourceCodeAssignment. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.resource_code_assignment import ResourceCodeAssignment
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
    api_instance = openapi_client.ResourceCodeAssignmentApi(api_client)
    resource_code_assignment = [openapi_client.ResourceCodeAssignment()] # List[ResourceCodeAssignment] | <p>A list of ResourceCodeAssignment objects.<p><p>Required fields: You must supply both the ResourceObjectId and ResourceCodeTypeObjectId fields when you use the Update ResourceCodeAssignment operation. All other fields are optional.</p>
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ResourceCodeAssignment
        api_response = api_instance.update_resource_code_assignment(resource_code_assignment, authorization=authorization)
        print("The response of ResourceCodeAssignmentApi->update_resource_code_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceCodeAssignmentApi->update_resource_code_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_code_assignment** | [**List[ResourceCodeAssignment]**](ResourceCodeAssignment.md)| &lt;p&gt;A list of ResourceCodeAssignment objects.&lt;p&gt;&lt;p&gt;Required fields: You must supply both the ResourceObjectId and ResourceCodeTypeObjectId fields when you use the Update ResourceCodeAssignment operation. All other fields are optional.&lt;/p&gt; | 
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

