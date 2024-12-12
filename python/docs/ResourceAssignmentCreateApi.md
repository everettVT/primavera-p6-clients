# openapi_client.ResourceAssignmentCreateApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_resource_assignment_create**](ResourceAssignmentCreateApi.md#create_resource_assignment_create) | **POST** /resourceAssignmentCreate | Create ResourceAssignmentCreate
[**delete_resource_assignment_create**](ResourceAssignmentCreateApi.md#delete_resource_assignment_create) | **DELETE** /resourceAssignmentCreate | Delete ResourceAssignmentCreate
[**get_resource_assignment_create**](ResourceAssignmentCreateApi.md#get_resource_assignment_create) | **GET** /resourceAssignmentCreate | Read ResourceAssignmentCreate
[**get_resource_assignment_create_field_length**](ResourceAssignmentCreateApi.md#get_resource_assignment_create_field_length) | **GET** /resourceAssignmentCreate/getFieldLength/{fieldName} | View ResourceAssignmentCreate Field Length
[**get_resource_assignment_create_fields**](ResourceAssignmentCreateApi.md#get_resource_assignment_create_fields) | **GET** /resourceAssignmentCreate/fields | View ResourceAssignmentCreate fields
[**update_resource_assignment_create**](ResourceAssignmentCreateApi.md#update_resource_assignment_create) | **PUT** /resourceAssignmentCreate | Update ResourceAssignmentCreate


# **create_resource_assignment_create**
> str create_resource_assignment_create(resource_assignment_create, authorization=authorization)

Create ResourceAssignmentCreate

Send a request to this endpoint to create one or more ResourceAssignmentCreate. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.resource_assignment_create import ResourceAssignmentCreate
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
    api_instance = openapi_client.ResourceAssignmentCreateApi(api_client)
    resource_assignment_create = [openapi_client.ResourceAssignmentCreate()] # List[ResourceAssignmentCreate] | A list of ResourceAssignmentCreate objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ResourceAssignmentCreate
        api_response = api_instance.create_resource_assignment_create(resource_assignment_create, authorization=authorization)
        print("The response of ResourceAssignmentCreateApi->create_resource_assignment_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceAssignmentCreateApi->create_resource_assignment_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_assignment_create** | [**List[ResourceAssignmentCreate]**](ResourceAssignmentCreate.md)| A list of ResourceAssignmentCreate objects. | 
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

# **delete_resource_assignment_create**
> bool delete_resource_assignment_create(object_id, authorization=authorization)

Delete ResourceAssignmentCreate

Send a request to this endpoint to delete one or more ResourceAssignmentCreate. An application object will be created for each JSON object provided in the request body

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
    api_instance = openapi_client.ResourceAssignmentCreateApi(api_client)
    object_id = '1,2,3' # str | One or more system-generated identifiers of ResourceAssignmentCreate.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete ResourceAssignmentCreate
        api_response = api_instance.delete_resource_assignment_create(object_id, authorization=authorization)
        print("The response of ResourceAssignmentCreateApi->delete_resource_assignment_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceAssignmentCreateApi->delete_resource_assignment_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| One or more system-generated identifiers of ResourceAssignmentCreate. | 
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

# **get_resource_assignment_create**
> List[ResourceAssignmentCreate] get_resource_assignment_create(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ResourceAssignmentCreate

Reads ResourceAssignmentCreate objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.resource_assignment_create import ResourceAssignmentCreate
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
    api_instance = openapi_client.ResourceAssignmentCreateApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ResourceAssignmentCreate
        api_response = api_instance.get_resource_assignment_create(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ResourceAssignmentCreateApi->get_resource_assignment_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceAssignmentCreateApi->get_resource_assignment_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ResourceAssignmentCreate]**](ResourceAssignmentCreate.md)

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

# **get_resource_assignment_create_field_length**
> str get_resource_assignment_create_field_length(field_name, authorization=authorization)

View ResourceAssignmentCreate Field Length

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
    api_instance = openapi_client.ResourceAssignmentCreateApi(api_client)
    field_name = 'field_name_example' # str | An ResourceAssignmentCreate field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ResourceAssignmentCreate Field Length
        api_response = api_instance.get_resource_assignment_create_field_length(field_name, authorization=authorization)
        print("The response of ResourceAssignmentCreateApi->get_resource_assignment_create_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceAssignmentCreateApi->get_resource_assignment_create_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An ResourceAssignmentCreate field. | 
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

# **get_resource_assignment_create_fields**
> str get_resource_assignment_create_fields()

View ResourceAssignmentCreate fields

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
    api_instance = openapi_client.ResourceAssignmentCreateApi(api_client)

    try:
        # View ResourceAssignmentCreate fields
        api_response = api_instance.get_resource_assignment_create_fields()
        print("The response of ResourceAssignmentCreateApi->get_resource_assignment_create_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceAssignmentCreateApi->get_resource_assignment_create_fields: %s\n" % e)
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

# **update_resource_assignment_create**
> bool update_resource_assignment_create(resource_assignment_create, authorization=authorization)

Update ResourceAssignmentCreate

Send a request to this endpoint to update one or more ResourceAssignmentCreate. An application object will be created for each JSON object provided in the request body. ResourceAssignmentCreateObjectId is mandatory field

### Example


```python
import openapi_client
from openapi_client.models.resource_assignment_create import ResourceAssignmentCreate
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
    api_instance = openapi_client.ResourceAssignmentCreateApi(api_client)
    resource_assignment_create = [openapi_client.ResourceAssignmentCreate()] # List[ResourceAssignmentCreate] | A list of ResourceAssignmentCreate objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ResourceAssignmentCreate
        api_response = api_instance.update_resource_assignment_create(resource_assignment_create, authorization=authorization)
        print("The response of ResourceAssignmentCreateApi->update_resource_assignment_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceAssignmentCreateApi->update_resource_assignment_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_assignment_create** | [**List[ResourceAssignmentCreate]**](ResourceAssignmentCreate.md)| A list of ResourceAssignmentCreate objects. | 
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

