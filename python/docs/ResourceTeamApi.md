# openapi_client.ResourceTeamApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_resource_team**](ResourceTeamApi.md#create_resource_team) | **POST** /resourceTeam | Create ResourceTeam
[**delete_resource_team**](ResourceTeamApi.md#delete_resource_team) | **DELETE** /resourceTeam | Delete ResourceTeam
[**get_resource_team**](ResourceTeamApi.md#get_resource_team) | **GET** /resourceTeam | Read ResourceTeam
[**get_resource_team_field_length**](ResourceTeamApi.md#get_resource_team_field_length) | **GET** /resourceTeam/getFieldLength/{fieldName} | View ResourceTeam Field Length
[**get_resource_team_fields**](ResourceTeamApi.md#get_resource_team_fields) | **GET** /resourceTeam/fields | View ResourceTeam fields
[**update_resource_team**](ResourceTeamApi.md#update_resource_team) | **PUT** /resourceTeam | Update ResourceTeam


# **create_resource_team**
> str create_resource_team(resource_team, authorization=authorization)

Create ResourceTeam

Send a request to this endpoint to create one or more ResourceTeam. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.resource_team import ResourceTeam
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
    api_instance = openapi_client.ResourceTeamApi(api_client)
    resource_team = [openapi_client.ResourceTeam()] # List[ResourceTeam] | A list of ResourceTeam objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ResourceTeam
        api_response = api_instance.create_resource_team(resource_team, authorization=authorization)
        print("The response of ResourceTeamApi->create_resource_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceTeamApi->create_resource_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_team** | [**List[ResourceTeam]**](ResourceTeam.md)| A list of ResourceTeam objects. | 
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

# **delete_resource_team**
> bool delete_resource_team(object_id, authorization=authorization)

Delete ResourceTeam

Send a request to this endpoint to delete one or more ResourceTeam. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.ResourceTeamApi(api_client)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of resourceTeam.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete ResourceTeam
        api_response = api_instance.delete_resource_team(object_id, authorization=authorization)
        print("The response of ResourceTeamApi->delete_resource_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceTeamApi->delete_resource_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| One or more system-generated identifiers of resourceTeam. | 
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

# **get_resource_team**
> List[ResourceTeam] get_resource_team(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ResourceTeam

Reads ResourceTeam objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.resource_team import ResourceTeam
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
    api_instance = openapi_client.ResourceTeamApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ResourceTeam
        api_response = api_instance.get_resource_team(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ResourceTeamApi->get_resource_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceTeamApi->get_resource_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ResourceTeam]**](ResourceTeam.md)

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

# **get_resource_team_field_length**
> str get_resource_team_field_length(field_name, authorization=authorization)

View ResourceTeam Field Length

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
    api_instance = openapi_client.ResourceTeamApi(api_client)
    field_name = 'field_name_example' # str | A ResourceTeam field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ResourceTeam Field Length
        api_response = api_instance.get_resource_team_field_length(field_name, authorization=authorization)
        print("The response of ResourceTeamApi->get_resource_team_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceTeamApi->get_resource_team_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| A ResourceTeam field. | 
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

# **get_resource_team_fields**
> str get_resource_team_fields()

View ResourceTeam fields

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
    api_instance = openapi_client.ResourceTeamApi(api_client)

    try:
        # View ResourceTeam fields
        api_response = api_instance.get_resource_team_fields()
        print("The response of ResourceTeamApi->get_resource_team_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceTeamApi->get_resource_team_fields: %s\n" % e)
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

# **update_resource_team**
> bool update_resource_team(resource_team, authorization=authorization)

Update ResourceTeam

Send a request to this endpoint to update one or more ResourceTeam. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.resource_team import ResourceTeam
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
    api_instance = openapi_client.ResourceTeamApi(api_client)
    resource_team = [openapi_client.ResourceTeam()] # List[ResourceTeam] | A list of ResourceTeam objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ResourceTeam
        api_response = api_instance.update_resource_team(resource_team, authorization=authorization)
        print("The response of ResourceTeamApi->update_resource_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceTeamApi->update_resource_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_team** | [**List[ResourceTeam]**](ResourceTeam.md)| A list of ResourceTeam objects. | 
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

