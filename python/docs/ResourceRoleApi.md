# openapi_client.ResourceRoleApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_resource_role**](ResourceRoleApi.md#create_resource_role) | **POST** /resourceRole | Create ResourceRole
[**delete_resource_role**](ResourceRoleApi.md#delete_resource_role) | **DELETE** /resourceRole | Delete ResourceRole
[**get_resource_role**](ResourceRoleApi.md#get_resource_role) | **GET** /resourceRole | Read ResourceRole
[**get_resource_role_field_length**](ResourceRoleApi.md#get_resource_role_field_length) | **GET** /resourceRole/getFieldLength/{fieldName} | View ResourceRole Field Length
[**get_resource_role_fields**](ResourceRoleApi.md#get_resource_role_fields) | **GET** /resourceRole/fields | View ResourceRole fields
[**update_resource_role**](ResourceRoleApi.md#update_resource_role) | **PUT** /resourceRole | Update ResourceRole


# **create_resource_role**
> CreateResourceRoleResponse create_resource_role(resource_role, authorization=authorization)

Create ResourceRole

Send a request to this endpoint to create one or more ResourceRole. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.create_resource_role_response import CreateResourceRoleResponse
from openapi_client.models.resource_role import ResourceRole
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
    api_instance = openapi_client.ResourceRoleApi(api_client)
    resource_role = [openapi_client.ResourceRole()] # List[ResourceRole] | A list of ResourceRole objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ResourceRole
        api_response = api_instance.create_resource_role(resource_role, authorization=authorization)
        print("The response of ResourceRoleApi->create_resource_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceRoleApi->create_resource_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_role** | [**List[ResourceRole]**](ResourceRole.md)| A list of ResourceRole objects. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**CreateResourceRoleResponse**](CreateResourceRoleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource Role Created. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resource_role**
> bool delete_resource_role(resource_role, authorization=authorization)

Delete ResourceRole

Send a request to this endpoint to delete one or more ResourceRole. Objects with ID values that match the values provided in the request body will be deleted.

### Example


```python
import openapi_client
from openapi_client.models.resource_role import ResourceRole
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
    api_instance = openapi_client.ResourceRoleApi(api_client)
    resource_role = [openapi_client.ResourceRole()] # List[ResourceRole] | <p>A list of ResourceRole objects.<p><p>Required fields: You must supply both the RoleObjectId and ResourceObjectId fields when you use the Delete ResourceAccess operation. All other fields are optional.</p>
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete ResourceRole
        api_response = api_instance.delete_resource_role(resource_role, authorization=authorization)
        print("The response of ResourceRoleApi->delete_resource_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceRoleApi->delete_resource_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_role** | [**List[ResourceRole]**](ResourceRole.md)| &lt;p&gt;A list of ResourceRole objects.&lt;p&gt;&lt;p&gt;Required fields: You must supply both the RoleObjectId and ResourceObjectId fields when you use the Delete ResourceAccess operation. All other fields are optional.&lt;/p&gt; | 
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

# **get_resource_role**
> List[ResourceRole] get_resource_role(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ResourceRole

Reads ResourceRole objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.resource_role import ResourceRole
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
    api_instance = openapi_client.ResourceRoleApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ResourceRole
        api_response = api_instance.get_resource_role(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ResourceRoleApi->get_resource_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceRoleApi->get_resource_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ResourceRole]**](ResourceRole.md)

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

# **get_resource_role_field_length**
> str get_resource_role_field_length(field_name, authorization=authorization)

View ResourceRole Field Length

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
    api_instance = openapi_client.ResourceRoleApi(api_client)
    field_name = 'field_name_example' # str | A ResourceRole field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ResourceRole Field Length
        api_response = api_instance.get_resource_role_field_length(field_name, authorization=authorization)
        print("The response of ResourceRoleApi->get_resource_role_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceRoleApi->get_resource_role_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| A ResourceRole field. | 
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

# **get_resource_role_fields**
> str get_resource_role_fields()

View ResourceRole fields

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
    api_instance = openapi_client.ResourceRoleApi(api_client)

    try:
        # View ResourceRole fields
        api_response = api_instance.get_resource_role_fields()
        print("The response of ResourceRoleApi->get_resource_role_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceRoleApi->get_resource_role_fields: %s\n" % e)
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

# **update_resource_role**
> bool update_resource_role(resource_role, authorization=authorization)

Update ResourceRole

Send a request to this endpoint to update one or more ResourceRole. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.resource_role import ResourceRole
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
    api_instance = openapi_client.ResourceRoleApi(api_client)
    resource_role = [openapi_client.ResourceRole()] # List[ResourceRole] | A list of ResourceRole objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ResourceRole
        api_response = api_instance.update_resource_role(resource_role, authorization=authorization)
        print("The response of ResourceRoleApi->update_resource_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceRoleApi->update_resource_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_role** | [**List[ResourceRole]**](ResourceRole.md)| A list of ResourceRole objects. | 
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

