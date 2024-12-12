# openapi_client.UserLicenseApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_license**](UserLicenseApi.md#create_user_license) | **POST** /userLicense | Create UserLicense
[**delete_user_license**](UserLicenseApi.md#delete_user_license) | **DELETE** /userLicense | Delete UserLicense
[**get_user_license**](UserLicenseApi.md#get_user_license) | **GET** /userLicense | Read UserLicense
[**get_user_license_field_length**](UserLicenseApi.md#get_user_license_field_length) | **GET** /userLicense/getFieldLength/{fieldName} | View UserLicense Field Length
[**get_user_license_fields**](UserLicenseApi.md#get_user_license_fields) | **GET** /userLicense/fields | View UserLicense fields


# **create_user_license**
> str create_user_license(user_license, authorization=authorization)

Create UserLicense

Send a request to this endpoint to create one or more UserLicense. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.user_license import UserLicense
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
    api_instance = openapi_client.UserLicenseApi(api_client)
    user_license = [openapi_client.UserLicense()] # List[UserLicense] | A list of UserLicense objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create UserLicense
        api_response = api_instance.create_user_license(user_license, authorization=authorization)
        print("The response of UserLicenseApi->create_user_license:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLicenseApi->create_user_license: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_license** | [**List[UserLicense]**](UserLicense.md)| A list of UserLicense objects. | 
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
**201** | UserLicense Created. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_license**
> bool delete_user_license(authorization=authorization, object_id=object_id)

Delete UserLicense

Send a request to this endpoint to delete one or more UserLicense. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.UserLicenseApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of UserLicense. (optional)

    try:
        # Delete UserLicense
        api_response = api_instance.delete_user_license(authorization=authorization, object_id=object_id)
        print("The response of UserLicenseApi->delete_user_license:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLicenseApi->delete_user_license: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| One or more system-generated identifiers of UserLicense. | [optional] 

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

# **get_user_license**
> List[UserLicense] get_user_license(fields, filter=filter, order_by=order_by, authorization=authorization)

Read UserLicense

Reads UserLicense objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.user_license import UserLicense
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
    api_instance = openapi_client.UserLicenseApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read UserLicense
        api_response = api_instance.get_user_license(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of UserLicenseApi->get_user_license:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLicenseApi->get_user_license: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[UserLicense]**](UserLicense.md)

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

# **get_user_license_field_length**
> str get_user_license_field_length(field_name, authorization=authorization)

View UserLicense Field Length

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
    api_instance = openapi_client.UserLicenseApi(api_client)
    field_name = 'field_name_example' # str | A UserLicense field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View UserLicense Field Length
        api_response = api_instance.get_user_license_field_length(field_name, authorization=authorization)
        print("The response of UserLicenseApi->get_user_license_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLicenseApi->get_user_license_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| A UserLicense field. | 
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

# **get_user_license_fields**
> str get_user_license_fields()

View UserLicense fields

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
    api_instance = openapi_client.UserLicenseApi(api_client)

    try:
        # View UserLicense fields
        api_response = api_instance.get_user_license_fields()
        print("The response of UserLicenseApi->get_user_license_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLicenseApi->get_user_license_fields: %s\n" % e)
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

