# openapi_client.ActivityOwnerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_activity_owners**](ActivityOwnerApi.md#create_activity_owners) | **POST** /activityOwner | Create ActivityOwners
[**delete_activity_owners**](ActivityOwnerApi.md#delete_activity_owners) | **DELETE** /activityOwner | Delete ActivityOwners
[**get_activity_owners**](ActivityOwnerApi.md#get_activity_owners) | **GET** /activityOwner | Read ActivityOwners
[**get_activity_owners_field_length**](ActivityOwnerApi.md#get_activity_owners_field_length) | **GET** /activityOwner/getFieldLength/{fieldName} | View ActivityOwner Field Length
[**get_activity_owners_fields**](ActivityOwnerApi.md#get_activity_owners_fields) | **GET** /activityOwner/fields | View ActivityOwner fields
[**update_activity_owners**](ActivityOwnerApi.md#update_activity_owners) | **PUT** /activityOwner | Update ActivityOwners


# **create_activity_owners**
> str create_activity_owners(activity_owner, authorization=authorization)

Create ActivityOwners

Send a request to this endpoint to create one or more activityOwner. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.activity_owner import ActivityOwner
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
    api_instance = openapi_client.ActivityOwnerApi(api_client)
    activity_owner = [openapi_client.ActivityOwner()] # List[ActivityOwner] | A list of activityOwner objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ActivityOwners
        api_response = api_instance.create_activity_owners(activity_owner, authorization=authorization)
        print("The response of ActivityOwnerApi->create_activity_owners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityOwnerApi->create_activity_owners: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_owner** | [**List[ActivityOwner]**](ActivityOwner.md)| A list of activityOwner objects. | 
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

# **delete_activity_owners**
> bool delete_activity_owners(authorization=authorization, object_id=object_id)

Delete ActivityOwners

Send a request to this endpoint to delete one or more activityOwner. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.ActivityOwnerApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of activityOwner. (optional)

    try:
        # Delete ActivityOwners
        api_response = api_instance.delete_activity_owners(authorization=authorization, object_id=object_id)
        print("The response of ActivityOwnerApi->delete_activity_owners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityOwnerApi->delete_activity_owners: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| One or more system-generated identifiers of activityOwner. | [optional] 

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

# **get_activity_owners**
> List[ActivityOwner] get_activity_owners(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ActivityOwners

Reads ActivityOwner objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.activity_owner import ActivityOwner
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
    api_instance = openapi_client.ActivityOwnerApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ActivityOwners
        api_response = api_instance.get_activity_owners(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ActivityOwnerApi->get_activity_owners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityOwnerApi->get_activity_owners: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ActivityOwner]**](ActivityOwner.md)

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

# **get_activity_owners_field_length**
> str get_activity_owners_field_length(field_name, authorization=authorization)

View ActivityOwner Field Length

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
    api_instance = openapi_client.ActivityOwnerApi(api_client)
    field_name = 'field_name_example' # str | An activityOwner field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ActivityOwner Field Length
        api_response = api_instance.get_activity_owners_field_length(field_name, authorization=authorization)
        print("The response of ActivityOwnerApi->get_activity_owners_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityOwnerApi->get_activity_owners_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An activityOwner field. | 
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

# **get_activity_owners_fields**
> str get_activity_owners_fields()

View ActivityOwner fields

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
    api_instance = openapi_client.ActivityOwnerApi(api_client)

    try:
        # View ActivityOwner fields
        api_response = api_instance.get_activity_owners_fields()
        print("The response of ActivityOwnerApi->get_activity_owners_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityOwnerApi->get_activity_owners_fields: %s\n" % e)
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

# **update_activity_owners**
> bool update_activity_owners(activity_owner, authorization=authorization)

Update ActivityOwners

Send a request to this endpoint to update one or more activityOwner. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.activity_owner import ActivityOwner
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
    api_instance = openapi_client.ActivityOwnerApi(api_client)
    activity_owner = [openapi_client.ActivityOwner()] # List[ActivityOwner] | A list of activityOwner objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ActivityOwners
        api_response = api_instance.update_activity_owners(activity_owner, authorization=authorization)
        print("The response of ActivityOwnerApi->update_activity_owners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityOwnerApi->update_activity_owners: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_owner** | [**List[ActivityOwner]**](ActivityOwner.md)| A list of activityOwner objects. | 
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

