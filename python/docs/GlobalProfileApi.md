# openapi_client.GlobalProfileApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_global_profile**](GlobalProfileApi.md#create_global_profile) | **POST** /globalProfile | Create GlobalProfiles
[**delete_global_profile**](GlobalProfileApi.md#delete_global_profile) | **DELETE** /globalProfile | Delete GlobalProfiles
[**get_global_profile**](GlobalProfileApi.md#get_global_profile) | **GET** /globalProfile | Read GlobalProfile
[**get_global_profile_field_length**](GlobalProfileApi.md#get_global_profile_field_length) | **GET** /globalProfile/getFieldLength/{fieldName} | View GlobalProfile Field Length
[**get_global_profile_fields**](GlobalProfileApi.md#get_global_profile_fields) | **GET** /globalProfile/fields | View GlobalProfile fields
[**update_global_profile**](GlobalProfileApi.md#update_global_profile) | **PUT** /globalProfile | Update GlobalProfile


# **create_global_profile**
> str create_global_profile(global_profile, authorization=authorization)

Create GlobalProfiles

Send a request to this endpoint to create one or more globalProfile. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.global_profile import GlobalProfile
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
    api_instance = openapi_client.GlobalProfileApi(api_client)
    global_profile = [openapi_client.GlobalProfile()] # List[GlobalProfile] | A list of user objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create GlobalProfiles
        api_response = api_instance.create_global_profile(global_profile, authorization=authorization)
        print("The response of GlobalProfileApi->create_global_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalProfileApi->create_global_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **global_profile** | [**List[GlobalProfile]**](GlobalProfile.md)| A list of user objects. | 
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

# **delete_global_profile**
> bool delete_global_profile(object_id, authorization=authorization)

Delete GlobalProfiles

Send a request to this endpoint to delete one or more globalProfile. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.GlobalProfileApi(api_client)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of globalProfile.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete GlobalProfiles
        api_response = api_instance.delete_global_profile(object_id, authorization=authorization)
        print("The response of GlobalProfileApi->delete_global_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalProfileApi->delete_global_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| One or more system-generated identifiers of globalProfile. | 
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

# **get_global_profile**
> List[GlobalProfile] get_global_profile(fields, filter=filter, order_by=order_by, authorization=authorization)

Read GlobalProfile

Reads GlobalProfile objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.global_profile import GlobalProfile
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
    api_instance = openapi_client.GlobalProfileApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read GlobalProfile
        api_response = api_instance.get_global_profile(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of GlobalProfileApi->get_global_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalProfileApi->get_global_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[GlobalProfile]**](GlobalProfile.md)

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

# **get_global_profile_field_length**
> str get_global_profile_field_length(field_name, authorization=authorization)

View GlobalProfile Field Length

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
    api_instance = openapi_client.GlobalProfileApi(api_client)
    field_name = 'field_name_example' # str | A GlobalProfile field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View GlobalProfile Field Length
        api_response = api_instance.get_global_profile_field_length(field_name, authorization=authorization)
        print("The response of GlobalProfileApi->get_global_profile_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalProfileApi->get_global_profile_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| A GlobalProfile field. | 
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

# **get_global_profile_fields**
> str get_global_profile_fields()

View GlobalProfile fields

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
    api_instance = openapi_client.GlobalProfileApi(api_client)

    try:
        # View GlobalProfile fields
        api_response = api_instance.get_global_profile_fields()
        print("The response of GlobalProfileApi->get_global_profile_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalProfileApi->get_global_profile_fields: %s\n" % e)
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

# **update_global_profile**
> bool update_global_profile(global_profile, authorization=authorization)

Update GlobalProfile

Send a request to this endpoint to update one or more GlobalProfile. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.global_profile import GlobalProfile
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
    api_instance = openapi_client.GlobalProfileApi(api_client)
    global_profile = [openapi_client.GlobalProfile()] # List[GlobalProfile] | A list of GlobalPreferences objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update GlobalProfile
        api_response = api_instance.update_global_profile(global_profile, authorization=authorization)
        print("The response of GlobalProfileApi->update_global_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalProfileApi->update_global_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **global_profile** | [**List[GlobalProfile]**](GlobalProfile.md)| A list of GlobalPreferences objects. | 
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

