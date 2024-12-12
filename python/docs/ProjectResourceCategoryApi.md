# openapi_client.ProjectResourceCategoryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_resource_category**](ProjectResourceCategoryApi.md#create_project_resource_category) | **POST** /projectResourceCategory | Create ProjectResourceCategory
[**delete_project_resource_category**](ProjectResourceCategoryApi.md#delete_project_resource_category) | **DELETE** /projectResourceCategory | Delete ProjectResourceCategory
[**get_project_resource_category**](ProjectResourceCategoryApi.md#get_project_resource_category) | **GET** /projectResourceCategory | Read ProjectResourceCategory
[**get_project_resource_category_field_length**](ProjectResourceCategoryApi.md#get_project_resource_category_field_length) | **GET** /projectResourceCategory/getFieldLength/{fieldName} | View ProjectResourceCategory Field Length
[**get_project_resource_category_fields**](ProjectResourceCategoryApi.md#get_project_resource_category_fields) | **GET** /projectResourceCategory/fields | View projectresourcecategory fields
[**update_project_resource_category**](ProjectResourceCategoryApi.md#update_project_resource_category) | **PUT** /projectResourceCategory | Update ProjectResourceCategory


# **create_project_resource_category**
> str create_project_resource_category(project_resource_category, authorization=authorization)

Create ProjectResourceCategory

Send a request to this endpoint to create one or more ProjectResourceCategory. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.project_resource_category import ProjectResourceCategory
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
    api_instance = openapi_client.ProjectResourceCategoryApi(api_client)
    project_resource_category = [openapi_client.ProjectResourceCategory()] # List[ProjectResourceCategory] | A list of projectresourcecategory objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ProjectResourceCategory
        api_response = api_instance.create_project_resource_category(project_resource_category, authorization=authorization)
        print("The response of ProjectResourceCategoryApi->create_project_resource_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectResourceCategoryApi->create_project_resource_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_resource_category** | [**List[ProjectResourceCategory]**](ProjectResourceCategory.md)| A list of projectresourcecategory objects. | 
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

# **delete_project_resource_category**
> bool delete_project_resource_category(object_id, authorization=authorization)

Delete ProjectResourceCategory

Send a request to this endpoint to delete one or more ProjectResourceCategory. An application object will be created for each JSON object provided in the request body

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
    api_instance = openapi_client.ProjectResourceCategoryApi(api_client)
    object_id = '1,2,3' # str | A list of projectresourcecategory objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete ProjectResourceCategory
        api_response = api_instance.delete_project_resource_category(object_id, authorization=authorization)
        print("The response of ProjectResourceCategoryApi->delete_project_resource_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectResourceCategoryApi->delete_project_resource_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| A list of projectresourcecategory objects. | 
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

# **get_project_resource_category**
> List[ProjectResourceCategory] get_project_resource_category(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ProjectResourceCategory

Reads ProjectResourceCategory objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.project_resource_category import ProjectResourceCategory
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
    api_instance = openapi_client.ProjectResourceCategoryApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ProjectResourceCategory
        api_response = api_instance.get_project_resource_category(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ProjectResourceCategoryApi->get_project_resource_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectResourceCategoryApi->get_project_resource_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ProjectResourceCategory]**](ProjectResourceCategory.md)

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

# **get_project_resource_category_field_length**
> str get_project_resource_category_field_length(field_name, authorization=authorization)

View ProjectResourceCategory Field Length

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
    api_instance = openapi_client.ProjectResourceCategoryApi(api_client)
    field_name = 'field_name_example' # str | An project field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ProjectResourceCategory Field Length
        api_response = api_instance.get_project_resource_category_field_length(field_name, authorization=authorization)
        print("The response of ProjectResourceCategoryApi->get_project_resource_category_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectResourceCategoryApi->get_project_resource_category_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An project field. | 
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

# **get_project_resource_category_fields**
> str get_project_resource_category_fields()

View projectresourcecategory fields

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
    api_instance = openapi_client.ProjectResourceCategoryApi(api_client)

    try:
        # View projectresourcecategory fields
        api_response = api_instance.get_project_resource_category_fields()
        print("The response of ProjectResourceCategoryApi->get_project_resource_category_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectResourceCategoryApi->get_project_resource_category_fields: %s\n" % e)
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

# **update_project_resource_category**
> bool update_project_resource_category(project_resource_category, authorization=authorization)

Update ProjectResourceCategory

Send a request to this endpoint to update one or more ProjectResourceCategory. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.project_resource_category import ProjectResourceCategory
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
    api_instance = openapi_client.ProjectResourceCategoryApi(api_client)
    project_resource_category = [openapi_client.ProjectResourceCategory()] # List[ProjectResourceCategory] | A list of projectresourcecategory objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ProjectResourceCategory
        api_response = api_instance.update_project_resource_category(project_resource_category, authorization=authorization)
        print("The response of ProjectResourceCategoryApi->update_project_resource_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectResourceCategoryApi->update_project_resource_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_resource_category** | [**List[ProjectResourceCategory]**](ProjectResourceCategory.md)| A list of projectresourcecategory objects. | 
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

