# openapi_client.ResourceAssignmentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_resource_assignment**](ResourceAssignmentApi.md#create_resource_assignment) | **POST** /resourceAssignment | Create ResourceAssignments
[**delete_resource_assignment**](ResourceAssignmentApi.md#delete_resource_assignment) | **DELETE** /resourceAssignment | Delete ResourceAssignments
[**get_resource_assignment**](ResourceAssignmentApi.md#get_resource_assignment) | **GET** /resourceAssignment | Read ResourceAssignments
[**get_resource_assignment_field_length**](ResourceAssignmentApi.md#get_resource_assignment_field_length) | **GET** /resourceAssignment/getFieldLength/{fieldName} | View ResourceAssignment Field Length
[**get_resource_assignment_fields**](ResourceAssignmentApi.md#get_resource_assignment_fields) | **GET** /resourceAssignment/fields | View ResourceAssignment fields
[**update_resource_assignment**](ResourceAssignmentApi.md#update_resource_assignment) | **PUT** /resourceAssignment | Update ResourceAssignments


# **create_resource_assignment**
> str create_resource_assignment(resource_assignment, authorization=authorization)

Create ResourceAssignments

Send a request to this endpoint to create one or more resourceAssignment. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.resource_assignment import ResourceAssignment
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
    api_instance = openapi_client.ResourceAssignmentApi(api_client)
    resource_assignment = [openapi_client.ResourceAssignment()] # List[ResourceAssignment] | A list of resourceAssignment objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ResourceAssignments
        api_response = api_instance.create_resource_assignment(resource_assignment, authorization=authorization)
        print("The response of ResourceAssignmentApi->create_resource_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceAssignmentApi->create_resource_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_assignment** | [**List[ResourceAssignment]**](ResourceAssignment.md)| A list of resourceAssignment objects. | 
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

# **delete_resource_assignment**
> bool delete_resource_assignment(authorization=authorization, object_id=object_id)

Delete ResourceAssignments

Send a request to this endpoint to delete one or more resourceAssignment. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.ResourceAssignmentApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of resourceAssignment. (optional)

    try:
        # Delete ResourceAssignments
        api_response = api_instance.delete_resource_assignment(authorization=authorization, object_id=object_id)
        print("The response of ResourceAssignmentApi->delete_resource_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceAssignmentApi->delete_resource_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| One or more system-generated identifiers of resourceAssignment. | [optional] 

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

# **get_resource_assignment**
> List[ResourceAssignment] get_resource_assignment(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ResourceAssignments

Reads ResourceAssignment objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.resource_assignment import ResourceAssignment
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
    api_instance = openapi_client.ResourceAssignmentApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ResourceAssignments
        api_response = api_instance.get_resource_assignment(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ResourceAssignmentApi->get_resource_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceAssignmentApi->get_resource_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ResourceAssignment]**](ResourceAssignment.md)

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

# **get_resource_assignment_field_length**
> str get_resource_assignment_field_length(field_name, authorization=authorization)

View ResourceAssignment Field Length

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
    api_instance = openapi_client.ResourceAssignmentApi(api_client)
    field_name = 'field_name_example' # str | A resourceAssignment field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ResourceAssignment Field Length
        api_response = api_instance.get_resource_assignment_field_length(field_name, authorization=authorization)
        print("The response of ResourceAssignmentApi->get_resource_assignment_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceAssignmentApi->get_resource_assignment_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| A resourceAssignment field. | 
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

# **get_resource_assignment_fields**
> str get_resource_assignment_fields()

View ResourceAssignment fields

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
    api_instance = openapi_client.ResourceAssignmentApi(api_client)

    try:
        # View ResourceAssignment fields
        api_response = api_instance.get_resource_assignment_fields()
        print("The response of ResourceAssignmentApi->get_resource_assignment_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceAssignmentApi->get_resource_assignment_fields: %s\n" % e)
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

# **update_resource_assignment**
> bool update_resource_assignment(resource_assignment, authorization=authorization)

Update ResourceAssignments

Send a request to this endpoint to update one or more resourceAssignment. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.resource_assignment import ResourceAssignment
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
    api_instance = openapi_client.ResourceAssignmentApi(api_client)
    resource_assignment = [openapi_client.ResourceAssignment()] # List[ResourceAssignment] | A list of resourceAssignment objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ResourceAssignments
        api_response = api_instance.update_resource_assignment(resource_assignment, authorization=authorization)
        print("The response of ResourceAssignmentApi->update_resource_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceAssignmentApi->update_resource_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_assignment** | [**List[ResourceAssignment]**](ResourceAssignment.md)| A list of resourceAssignment objects. | 
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

