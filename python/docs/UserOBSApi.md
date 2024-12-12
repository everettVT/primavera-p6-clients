# openapi_client.UserOBSApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_obs**](UserOBSApi.md#create_user_obs) | **POST** /userOBS | Create UserOBS
[**delete_user_obs**](UserOBSApi.md#delete_user_obs) | **DELETE** /userOBS | Delete UserOBS
[**get_user_obs**](UserOBSApi.md#get_user_obs) | **GET** /userOBS | Read UserOBS
[**get_user_obs_field_length**](UserOBSApi.md#get_user_obs_field_length) | **GET** /userOBS/getFieldLength/{fieldName} | View UserOBS Field Length
[**get_user_obs_fields**](UserOBSApi.md#get_user_obs_fields) | **GET** /userOBS/fields | View UserOBS fields
[**update_user_obs**](UserOBSApi.md#update_user_obs) | **PUT** /userOBS | Update UserOBS


# **create_user_obs**
> CreateUserOBSResponse create_user_obs(user_obs, authorization=authorization)

Create UserOBS

Send a request to this endpoint to create one or more UserOBS. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.create_user_obs_response import CreateUserOBSResponse
from openapi_client.models.user_obs import UserOBS
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
    api_instance = openapi_client.UserOBSApi(api_client)
    user_obs = [openapi_client.UserOBS()] # List[UserOBS] | A list of UserOBS objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create UserOBS
        api_response = api_instance.create_user_obs(user_obs, authorization=authorization)
        print("The response of UserOBSApi->create_user_obs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserOBSApi->create_user_obs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_obs** | [**List[UserOBS]**](UserOBS.md)| A list of UserOBS objects. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**CreateUserOBSResponse**](CreateUserOBSResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | UserOBS Created. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_obs**
> bool delete_user_obs(user_obs, authorization=authorization)

Delete UserOBS

Send a request to this endpoint to delete one or more UserOBS. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.user_obs import UserOBS
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
    api_instance = openapi_client.UserOBSApi(api_client)
    user_obs = [openapi_client.UserOBS()] # List[UserOBS] | <p>A list of UserOBS objects.<p><p>Required fields: You must supply both the OBSObjectId and UserObjectId fields when you use the Delete UserOBS operation. All other fields are optional.</p>
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete UserOBS
        api_response = api_instance.delete_user_obs(user_obs, authorization=authorization)
        print("The response of UserOBSApi->delete_user_obs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserOBSApi->delete_user_obs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_obs** | [**List[UserOBS]**](UserOBS.md)| &lt;p&gt;A list of UserOBS objects.&lt;p&gt;&lt;p&gt;Required fields: You must supply both the OBSObjectId and UserObjectId fields when you use the Delete UserOBS operation. All other fields are optional.&lt;/p&gt; | 
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

# **get_user_obs**
> List[UserOBS] get_user_obs(fields, filter=filter, order_by=order_by, authorization=authorization)

Read UserOBS

Reads UserOBS objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.user_obs import UserOBS
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
    api_instance = openapi_client.UserOBSApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read UserOBS
        api_response = api_instance.get_user_obs(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of UserOBSApi->get_user_obs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserOBSApi->get_user_obs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[UserOBS]**](UserOBS.md)

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

# **get_user_obs_field_length**
> str get_user_obs_field_length(field_name, authorization=authorization)

View UserOBS Field Length

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
    api_instance = openapi_client.UserOBSApi(api_client)
    field_name = 'field_name_example' # str | Field to retun length
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View UserOBS Field Length
        api_response = api_instance.get_user_obs_field_length(field_name, authorization=authorization)
        print("The response of UserOBSApi->get_user_obs_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserOBSApi->get_user_obs_field_length: %s\n" % e)
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

# **get_user_obs_fields**
> str get_user_obs_fields()

View UserOBS fields

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
    api_instance = openapi_client.UserOBSApi(api_client)

    try:
        # View UserOBS fields
        api_response = api_instance.get_user_obs_fields()
        print("The response of UserOBSApi->get_user_obs_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserOBSApi->get_user_obs_fields: %s\n" % e)
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

# **update_user_obs**
> bool update_user_obs(user_obs, authorization=authorization)

Update UserOBS

Send a request to this endpoint to update one or more UserOBS. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.user_obs import UserOBS
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
    api_instance = openapi_client.UserOBSApi(api_client)
    user_obs = [openapi_client.UserOBS()] # List[UserOBS] | A list of UserOBS objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update UserOBS
        api_response = api_instance.update_user_obs(user_obs, authorization=authorization)
        print("The response of UserOBSApi->update_user_obs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserOBSApi->update_user_obs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_obs** | [**List[UserOBS]**](UserOBS.md)| A list of UserOBS objects. | 
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

