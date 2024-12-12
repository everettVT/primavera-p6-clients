# openapi_client.ProjectResourceQuantityApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_resource_quantity**](ProjectResourceQuantityApi.md#create_project_resource_quantity) | **POST** /projectResourceQuantity | Create ProjectResourceQuantity
[**delete_project_resource_quantity**](ProjectResourceQuantityApi.md#delete_project_resource_quantity) | **DELETE** /projectResourceQuantity | Delete ProjectResourceQuantity
[**get_project_resource_quantity**](ProjectResourceQuantityApi.md#get_project_resource_quantity) | **GET** /projectResourceQuantity | Reads ProjectResourceQuantity
[**get_project_resource_quantity_fields**](ProjectResourceQuantityApi.md#get_project_resource_quantity_fields) | **GET** /projectResourceQuantity/fields | View ProjectResourceQuantity fields
[**get_project_resource_quantity_length**](ProjectResourceQuantityApi.md#get_project_resource_quantity_length) | **GET** /projectResourceQuantity/getFieldLength/{fieldName} | View ProjectResourceQuantity Field Length
[**update_project_resource_quantity**](ProjectResourceQuantityApi.md#update_project_resource_quantity) | **PUT** /projectResourceQuantity | Update ProjectResourceQuantity


# **create_project_resource_quantity**
> List[CreateProjectResourceQuantityResponse] create_project_resource_quantity(project_resource_quantity, authorization=authorization)

Create ProjectResourceQuantity

Send a request to this endpoint to create one or more ProjectResourceQuantity. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.create_project_resource_quantity_response import CreateProjectResourceQuantityResponse
from openapi_client.models.project_resource_quantity import ProjectResourceQuantity
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
    api_instance = openapi_client.ProjectResourceQuantityApi(api_client)
    project_resource_quantity = [openapi_client.ProjectResourceQuantity()] # List[ProjectResourceQuantity] | A list of projectresourcequantity objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ProjectResourceQuantity
        api_response = api_instance.create_project_resource_quantity(project_resource_quantity, authorization=authorization)
        print("The response of ProjectResourceQuantityApi->create_project_resource_quantity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectResourceQuantityApi->create_project_resource_quantity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_resource_quantity** | [**List[ProjectResourceQuantity]**](ProjectResourceQuantity.md)| A list of projectresourcequantity objects. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[CreateProjectResourceQuantityResponse]**](CreateProjectResourceQuantityResponse.md)

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

# **delete_project_resource_quantity**
> bool delete_project_resource_quantity(project_resource_quantity, authorization=authorization)

Delete ProjectResourceQuantity

Send a request to this endpoint to delete one or more ProjectResourceQuantity. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.project_resource_quantity import ProjectResourceQuantity
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
    api_instance = openapi_client.ProjectResourceQuantityApi(api_client)
    project_resource_quantity = [openapi_client.ProjectResourceQuantity()] # List[ProjectResourceQuantity] | <p>A list of projectResourceQuantity objects.<p><p>Required fields: You must supply both the ProjectResourceObjectId, WeekStartDate and Quantity fields when you use the Delete ProjectResourceQuantity operation. All other fields are optional.</p>
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete ProjectResourceQuantity
        api_response = api_instance.delete_project_resource_quantity(project_resource_quantity, authorization=authorization)
        print("The response of ProjectResourceQuantityApi->delete_project_resource_quantity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectResourceQuantityApi->delete_project_resource_quantity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_resource_quantity** | [**List[ProjectResourceQuantity]**](ProjectResourceQuantity.md)| &lt;p&gt;A list of projectResourceQuantity objects.&lt;p&gt;&lt;p&gt;Required fields: You must supply both the ProjectResourceObjectId, WeekStartDate and Quantity fields when you use the Delete ProjectResourceQuantity operation. All other fields are optional.&lt;/p&gt; | 
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

# **get_project_resource_quantity**
> List[ProjectResourceQuantity] get_project_resource_quantity(fields, filter=filter, order_by=order_by, authorization=authorization)

Reads ProjectResourceQuantity

Reads ProjectResourceQuantity objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.project_resource_quantity import ProjectResourceQuantity
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
    api_instance = openapi_client.ProjectResourceQuantityApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Reads ProjectResourceQuantity
        api_response = api_instance.get_project_resource_quantity(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ProjectResourceQuantityApi->get_project_resource_quantity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectResourceQuantityApi->get_project_resource_quantity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ProjectResourceQuantity]**](ProjectResourceQuantity.md)

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

# **get_project_resource_quantity_fields**
> str get_project_resource_quantity_fields()

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
    api_instance = openapi_client.ProjectResourceQuantityApi(api_client)

    try:
        # View ProjectResourceQuantity fields
        api_response = api_instance.get_project_resource_quantity_fields()
        print("The response of ProjectResourceQuantityApi->get_project_resource_quantity_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectResourceQuantityApi->get_project_resource_quantity_fields: %s\n" % e)
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

# **get_project_resource_quantity_length**
> str get_project_resource_quantity_length(field_name, authorization=authorization)

View ProjectResourceQuantity Field Length

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
    api_instance = openapi_client.ProjectResourceQuantityApi(api_client)
    field_name = 'field_name_example' # str | An projectresourcequantity field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ProjectResourceQuantity Field Length
        api_response = api_instance.get_project_resource_quantity_length(field_name, authorization=authorization)
        print("The response of ProjectResourceQuantityApi->get_project_resource_quantity_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectResourceQuantityApi->get_project_resource_quantity_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An projectresourcequantity field. | 
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

# **update_project_resource_quantity**
> str update_project_resource_quantity(project_resource_quantity, authorization=authorization)

Update ProjectResourceQuantity

Send a request to this endpoint to update one or more ProjectResourceQuantity. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.project_resource_quantity import ProjectResourceQuantity
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
    api_instance = openapi_client.ProjectResourceQuantityApi(api_client)
    project_resource_quantity = [openapi_client.ProjectResourceQuantity()] # List[ProjectResourceQuantity] | <p>A list of projectResourceQuantity objects.<p><p>Required fields: You must supply both the ProjectResourceObjectId, WeekStartDate and Quantity fields when you use the Update ProjectResourceQuantity operation. All other fields are optional.</p>
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ProjectResourceQuantity
        api_response = api_instance.update_project_resource_quantity(project_resource_quantity, authorization=authorization)
        print("The response of ProjectResourceQuantityApi->update_project_resource_quantity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectResourceQuantityApi->update_project_resource_quantity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_resource_quantity** | [**List[ProjectResourceQuantity]**](ProjectResourceQuantity.md)| &lt;p&gt;A list of projectResourceQuantity objects.&lt;p&gt;&lt;p&gt;Required fields: You must supply both the ProjectResourceObjectId, WeekStartDate and Quantity fields when you use the Update ProjectResourceQuantity operation. All other fields are optional.&lt;/p&gt; | 
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

