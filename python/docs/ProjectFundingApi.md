# openapi_client.ProjectFundingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_funding**](ProjectFundingApi.md#create_project_funding) | **POST** /projectFunding | Creates ProjectFunding
[**delete_project_funding**](ProjectFundingApi.md#delete_project_funding) | **DELETE** /projectFunding | Delete ProjectFunding
[**get_project_funding**](ProjectFundingApi.md#get_project_funding) | **GET** /projectFunding | Read ProjectFunding
[**get_project_funding_field_length**](ProjectFundingApi.md#get_project_funding_field_length) | **GET** /projectFunding/getFieldLength/{fieldName} | View ProjectFunding Field Length
[**get_project_funding_fields**](ProjectFundingApi.md#get_project_funding_fields) | **GET** /projectFunding/fields | View ProjectFunding fields
[**update_project_funding**](ProjectFundingApi.md#update_project_funding) | **PUT** /projectFunding | Update ProjectFunding


# **create_project_funding**
> str create_project_funding(project_funding, authorization=authorization)

Creates ProjectFunding

Send a request to this endpoint to create one or more ProjectFunding. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.project_funding import ProjectFunding
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
    api_instance = openapi_client.ProjectFundingApi(api_client)
    project_funding = [openapi_client.ProjectFunding()] # List[ProjectFunding] | A list of projectfunding objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Creates ProjectFunding
        api_response = api_instance.create_project_funding(project_funding, authorization=authorization)
        print("The response of ProjectFundingApi->create_project_funding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectFundingApi->create_project_funding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_funding** | [**List[ProjectFunding]**](ProjectFunding.md)| A list of projectfunding objects. | 
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

# **delete_project_funding**
> bool delete_project_funding(object_id, authorization=authorization)

Delete ProjectFunding

Send a request to this endpoint to delete one or more ProjectFunding. An application object will be created for each JSON object provided in the request body

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
    api_instance = openapi_client.ProjectFundingApi(api_client)
    object_id = '1,2,3' # str | One or more system-generated identifiers of projectfunding.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete ProjectFunding
        api_response = api_instance.delete_project_funding(object_id, authorization=authorization)
        print("The response of ProjectFundingApi->delete_project_funding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectFundingApi->delete_project_funding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| One or more system-generated identifiers of projectfunding. | 
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

# **get_project_funding**
> List[ProjectFunding] get_project_funding(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ProjectFunding

Reads ProjectFunding objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.project_funding import ProjectFunding
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
    api_instance = openapi_client.ProjectFundingApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ProjectFunding
        api_response = api_instance.get_project_funding(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ProjectFundingApi->get_project_funding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectFundingApi->get_project_funding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ProjectFunding]**](ProjectFunding.md)

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

# **get_project_funding_field_length**
> str get_project_funding_field_length(field_name, authorization=authorization)

View ProjectFunding Field Length

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
    api_instance = openapi_client.ProjectFundingApi(api_client)
    field_name = 'field_name_example' # str | An projectfunding field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ProjectFunding Field Length
        api_response = api_instance.get_project_funding_field_length(field_name, authorization=authorization)
        print("The response of ProjectFundingApi->get_project_funding_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectFundingApi->get_project_funding_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An projectfunding field. | 
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

# **get_project_funding_fields**
> str get_project_funding_fields()

View ProjectFunding fields

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
    api_instance = openapi_client.ProjectFundingApi(api_client)

    try:
        # View ProjectFunding fields
        api_response = api_instance.get_project_funding_fields()
        print("The response of ProjectFundingApi->get_project_funding_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectFundingApi->get_project_funding_fields: %s\n" % e)
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

# **update_project_funding**
> bool update_project_funding(project_funding, authorization=authorization)

Update ProjectFunding

Send a request to this endpoint to update one or more ProjectFunding. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.project_funding import ProjectFunding
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
    api_instance = openapi_client.ProjectFundingApi(api_client)
    project_funding = [openapi_client.ProjectFunding()] # List[ProjectFunding] | A list of projectfunding objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ProjectFunding
        api_response = api_instance.update_project_funding(project_funding, authorization=authorization)
        print("The response of ProjectFundingApi->update_project_funding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectFundingApi->update_project_funding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_funding** | [**List[ProjectFunding]**](ProjectFunding.md)| A list of projectfunding objects. | 
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

