# openapi_client.ResourceAssignmentUpdateApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_resource_assignment_update**](ResourceAssignmentUpdateApi.md#create_resource_assignment_update) | **POST** /resourceAssignmentUpdate | Create ResourceAssignmentUpdate
[**delete_resource_assignment_update**](ResourceAssignmentUpdateApi.md#delete_resource_assignment_update) | **DELETE** /resourceAssignmentUpdate | Delete ResourceAssignmentUpdate
[**get_resource_assignment_update**](ResourceAssignmentUpdateApi.md#get_resource_assignment_update) | **GET** /resourceAssignmentUpdate | Read ResourceAssignmentUpdate
[**get_resource_assignment_update_field_length**](ResourceAssignmentUpdateApi.md#get_resource_assignment_update_field_length) | **GET** /resourceAssignmentUpdate/getFieldLength/{fieldName} | View ResourceAssignmentUpdate Field Length
[**get_resource_assignment_update_fields**](ResourceAssignmentUpdateApi.md#get_resource_assignment_update_fields) | **GET** /resourceAssignmentUpdate/fields | View ResourceAssignmentUpdate fields
[**update_resource_assignment_update**](ResourceAssignmentUpdateApi.md#update_resource_assignment_update) | **PUT** /resourceAssignmentUpdate | Update ResourceAssignmentUpdate


# **create_resource_assignment_update**
> List[CreateResourceAssignmentUpdateResponse] create_resource_assignment_update(resource_assignment_update, authorization=authorization)

Create ResourceAssignmentUpdate

Send a request to this endpoint to create one or more ResourceAssignmentUpdate. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.create_resource_assignment_update_response import CreateResourceAssignmentUpdateResponse
from openapi_client.models.resource_assignment_update import ResourceAssignmentUpdate
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
    api_instance = openapi_client.ResourceAssignmentUpdateApi(api_client)
    resource_assignment_update = [openapi_client.ResourceAssignmentUpdate()] # List[ResourceAssignmentUpdate] | A list of ResourceAssignmentUpdate objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ResourceAssignmentUpdate
        api_response = api_instance.create_resource_assignment_update(resource_assignment_update, authorization=authorization)
        print("The response of ResourceAssignmentUpdateApi->create_resource_assignment_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceAssignmentUpdateApi->create_resource_assignment_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_assignment_update** | [**List[ResourceAssignmentUpdate]**](ResourceAssignmentUpdate.md)| A list of ResourceAssignmentUpdate objects. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[CreateResourceAssignmentUpdateResponse]**](CreateResourceAssignmentUpdateResponse.md)

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

# **delete_resource_assignment_update**
> bool delete_resource_assignment_update(resource_assignment_update, authorization=authorization)

Delete ResourceAssignmentUpdate

Send a request to this endpoint to delete one or more ResourceAssignmentUpdate. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.resource_assignment_update import ResourceAssignmentUpdate
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
    api_instance = openapi_client.ResourceAssignmentUpdateApi(api_client)
    resource_assignment_update = [openapi_client.ResourceAssignmentUpdate()] # List[ResourceAssignmentUpdate] | <p>A list of ResourceAssignmentUpdate objects.<p><p>Required fields: You must supply both the ResourceAssignmentObjectId and ChangeSetObjectId fields when you use the Delete ResourceAssignmentUpdate operation. All other fields are optional.</p>
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete ResourceAssignmentUpdate
        api_response = api_instance.delete_resource_assignment_update(resource_assignment_update, authorization=authorization)
        print("The response of ResourceAssignmentUpdateApi->delete_resource_assignment_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceAssignmentUpdateApi->delete_resource_assignment_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_assignment_update** | [**List[ResourceAssignmentUpdate]**](ResourceAssignmentUpdate.md)| &lt;p&gt;A list of ResourceAssignmentUpdate objects.&lt;p&gt;&lt;p&gt;Required fields: You must supply both the ResourceAssignmentObjectId and ChangeSetObjectId fields when you use the Delete ResourceAssignmentUpdate operation. All other fields are optional.&lt;/p&gt; | 
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

# **get_resource_assignment_update**
> List[ResourceAssignmentUpdate] get_resource_assignment_update(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ResourceAssignmentUpdate

Reads ResourceAssignmentUpdate objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.resource_assignment_update import ResourceAssignmentUpdate
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
    api_instance = openapi_client.ResourceAssignmentUpdateApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ResourceAssignmentUpdate
        api_response = api_instance.get_resource_assignment_update(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ResourceAssignmentUpdateApi->get_resource_assignment_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceAssignmentUpdateApi->get_resource_assignment_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ResourceAssignmentUpdate]**](ResourceAssignmentUpdate.md)

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

# **get_resource_assignment_update_field_length**
> str get_resource_assignment_update_field_length(field_name, authorization=authorization)

View ResourceAssignmentUpdate Field Length

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
    api_instance = openapi_client.ResourceAssignmentUpdateApi(api_client)
    field_name = 'field_name_example' # str | An ResourceAssignmentUpdate field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ResourceAssignmentUpdate Field Length
        api_response = api_instance.get_resource_assignment_update_field_length(field_name, authorization=authorization)
        print("The response of ResourceAssignmentUpdateApi->get_resource_assignment_update_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceAssignmentUpdateApi->get_resource_assignment_update_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An ResourceAssignmentUpdate field. | 
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

# **get_resource_assignment_update_fields**
> str get_resource_assignment_update_fields()

View ResourceAssignmentUpdate fields

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
    api_instance = openapi_client.ResourceAssignmentUpdateApi(api_client)

    try:
        # View ResourceAssignmentUpdate fields
        api_response = api_instance.get_resource_assignment_update_fields()
        print("The response of ResourceAssignmentUpdateApi->get_resource_assignment_update_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceAssignmentUpdateApi->get_resource_assignment_update_fields: %s\n" % e)
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

# **update_resource_assignment_update**
> bool update_resource_assignment_update(resource_assignment_update, authorization=authorization)

Update ResourceAssignmentUpdate

Send a request to this endpoint to update one or more ResourceAssignmentUpdate. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.resource_assignment_update import ResourceAssignmentUpdate
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
    api_instance = openapi_client.ResourceAssignmentUpdateApi(api_client)
    resource_assignment_update = [openapi_client.ResourceAssignmentUpdate()] # List[ResourceAssignmentUpdate] | <p>A list of ResourceAssignmentUpdate objects.<p><p>Required fields: You must supply both the ResourceAssignmentObjectId and ChangeSetObjectId fields when you use the Update ResourceAssignmentUpdate operation. All other fields are optional.</p>
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ResourceAssignmentUpdate
        api_response = api_instance.update_resource_assignment_update(resource_assignment_update, authorization=authorization)
        print("The response of ResourceAssignmentUpdateApi->update_resource_assignment_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceAssignmentUpdateApi->update_resource_assignment_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_assignment_update** | [**List[ResourceAssignmentUpdate]**](ResourceAssignmentUpdate.md)| &lt;p&gt;A list of ResourceAssignmentUpdate objects.&lt;p&gt;&lt;p&gt;Required fields: You must supply both the ResourceAssignmentObjectId and ChangeSetObjectId fields when you use the Update ResourceAssignmentUpdate operation. All other fields are optional.&lt;/p&gt; | 
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

