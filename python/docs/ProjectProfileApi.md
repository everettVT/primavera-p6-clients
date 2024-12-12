# openapi_client.ProjectProfileApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_profile**](ProjectProfileApi.md#create_project_profile) | **POST** /projectProfile | Create ProjectProfile
[**delete_project_profile**](ProjectProfileApi.md#delete_project_profile) | **DELETE** /projectProfile | Delete ProjectProfile
[**get_project_profile**](ProjectProfileApi.md#get_project_profile) | **GET** /projectProfile | Read ProjectProfile
[**get_project_profile_field_length**](ProjectProfileApi.md#get_project_profile_field_length) | **GET** /projectProfile/getFieldLength/{fieldName} | View ProjectProfile Field Length
[**get_project_profile_fields**](ProjectProfileApi.md#get_project_profile_fields) | **GET** /projectProfile/fields | View ProjectProfile fields
[**update_project_profile**](ProjectProfileApi.md#update_project_profile) | **PUT** /projectProfile | Update ProjectProfile


# **create_project_profile**
> str create_project_profile(project_profile, authorization=authorization)

Create ProjectProfile

Send a request to this endpoint to create one or more ProjectProfile. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.project_profile import ProjectProfile
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
    api_instance = openapi_client.ProjectProfileApi(api_client)
    project_profile = [openapi_client.ProjectProfile()] # List[ProjectProfile] | A list of projectProfile objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ProjectProfile
        api_response = api_instance.create_project_profile(project_profile, authorization=authorization)
        print("The response of ProjectProfileApi->create_project_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectProfileApi->create_project_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_profile** | [**List[ProjectProfile]**](ProjectProfile.md)| A list of projectProfile objects. | 
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

# **delete_project_profile**
> bool delete_project_profile(object_id, authorization=authorization)

Delete ProjectProfile

Send a request to this endpoint to delete one or more ProjectProfile. An application object will be created for each JSON object provided in the request body

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
    api_instance = openapi_client.ProjectProfileApi(api_client)
    object_id = '1,2,3' # str | One or more system-generated identifiers of projectprofile.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete ProjectProfile
        api_response = api_instance.delete_project_profile(object_id, authorization=authorization)
        print("The response of ProjectProfileApi->delete_project_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectProfileApi->delete_project_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| One or more system-generated identifiers of projectprofile. | 
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

# **get_project_profile**
> List[ProjectProfile] get_project_profile(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ProjectProfile

Reads ProjectProfile objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.project_profile import ProjectProfile
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
    api_instance = openapi_client.ProjectProfileApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ProjectProfile
        api_response = api_instance.get_project_profile(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ProjectProfileApi->get_project_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectProfileApi->get_project_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ProjectProfile]**](ProjectProfile.md)

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

# **get_project_profile_field_length**
> str get_project_profile_field_length(field_name, authorization=authorization)

View ProjectProfile Field Length

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
    api_instance = openapi_client.ProjectProfileApi(api_client)
    field_name = 'field_name_example' # str | Field to retun length
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ProjectProfile Field Length
        api_response = api_instance.get_project_profile_field_length(field_name, authorization=authorization)
        print("The response of ProjectProfileApi->get_project_profile_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectProfileApi->get_project_profile_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| Field to retun length | 
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

# **get_project_profile_fields**
> str get_project_profile_fields()

View ProjectProfile fields

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
    api_instance = openapi_client.ProjectProfileApi(api_client)

    try:
        # View ProjectProfile fields
        api_response = api_instance.get_project_profile_fields()
        print("The response of ProjectProfileApi->get_project_profile_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectProfileApi->get_project_profile_fields: %s\n" % e)
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

# **update_project_profile**
> bool update_project_profile(project_profile, authorization=authorization)

Update ProjectProfile

Send a request to this endpoint to update one or more ProjectProfile. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.project_profile import ProjectProfile
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
    api_instance = openapi_client.ProjectProfileApi(api_client)
    project_profile = [openapi_client.ProjectProfile()] # List[ProjectProfile] | A list of projectProfile objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ProjectProfile
        api_response = api_instance.update_project_profile(project_profile, authorization=authorization)
        print("The response of ProjectProfileApi->update_project_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectProfileApi->update_project_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_profile** | [**List[ProjectProfile]**](ProjectProfile.md)| A list of projectProfile objects. | 
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

