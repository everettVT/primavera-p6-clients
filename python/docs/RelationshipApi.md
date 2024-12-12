# openapi_client.RelationshipApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_relationship**](RelationshipApi.md#create_relationship) | **POST** /relationship | Create Relationship
[**delete_relationship**](RelationshipApi.md#delete_relationship) | **DELETE** /relationship | Delete Relationship
[**get_relationship**](RelationshipApi.md#get_relationship) | **GET** /relationship | Read Relationship
[**get_relationship_field_length**](RelationshipApi.md#get_relationship_field_length) | **GET** /relationship/getFieldLength/{fieldName} | View Relationship Field Length
[**get_relationship_fields**](RelationshipApi.md#get_relationship_fields) | **GET** /relationship/fields | View Relationship fields
[**update_relationship**](RelationshipApi.md#update_relationship) | **PUT** /relationship | Update Relationship


# **create_relationship**
> str create_relationship(relationship, authorization=authorization)

Create Relationship

Send a request to this endpoint to create one or more Relationship. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.relationship import Relationship
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
    api_instance = openapi_client.RelationshipApi(api_client)
    relationship = [openapi_client.Relationship()] # List[Relationship] | A Relationship of project objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create Relationship
        api_response = api_instance.create_relationship(relationship, authorization=authorization)
        print("The response of RelationshipApi->create_relationship:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationshipApi->create_relationship: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relationship** | [**List[Relationship]**](Relationship.md)| A Relationship of project objects. | 
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

# **delete_relationship**
> bool delete_relationship(object_id, authorization=authorization)

Delete Relationship

Send a request to this endpoint to delete one or more Relationship. An application object will be created for each JSON object provided in the request body

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
    api_instance = openapi_client.RelationshipApi(api_client)
    object_id = '1,2,3' # str | Relationship to delete
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete Relationship
        api_response = api_instance.delete_relationship(object_id, authorization=authorization)
        print("The response of RelationshipApi->delete_relationship:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationshipApi->delete_relationship: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Relationship to delete | 
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

# **get_relationship**
> List[Relationship] get_relationship(fields, filter=filter, order_by=order_by, lag_project_id=lag_project_id, authorization=authorization)

Read Relationship

Reads Relationship objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.relationship import Relationship
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
    api_instance = openapi_client.RelationshipApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    lag_project_id = '1234' # str | LagProjectId should be passed while trying to load Driving field (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read Relationship
        api_response = api_instance.get_relationship(fields, filter=filter, order_by=order_by, lag_project_id=lag_project_id, authorization=authorization)
        print("The response of RelationshipApi->get_relationship:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationshipApi->get_relationship: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **lag_project_id** | **str**| LagProjectId should be passed while trying to load Driving field | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[Relationship]**](Relationship.md)

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

# **get_relationship_field_length**
> str get_relationship_field_length(field_name, authorization=authorization)

View Relationship Field Length

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
    api_instance = openapi_client.RelationshipApi(api_client)
    field_name = 'field_name_example' # str | One or more system-generated identifiers of relationship.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View Relationship Field Length
        api_response = api_instance.get_relationship_field_length(field_name, authorization=authorization)
        print("The response of RelationshipApi->get_relationship_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationshipApi->get_relationship_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| One or more system-generated identifiers of relationship. | 
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

# **get_relationship_fields**
> str get_relationship_fields()

View Relationship fields

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
    api_instance = openapi_client.RelationshipApi(api_client)

    try:
        # View Relationship fields
        api_response = api_instance.get_relationship_fields()
        print("The response of RelationshipApi->get_relationship_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationshipApi->get_relationship_fields: %s\n" % e)
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

# **update_relationship**
> bool update_relationship(relationship, authorization=authorization)

Update Relationship

Send a request to this endpoint to update one or more Relationship. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.relationship import Relationship
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
    api_instance = openapi_client.RelationshipApi(api_client)
    relationship = [openapi_client.Relationship()] # List[Relationship] | A Relationship of project objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update Relationship
        api_response = api_instance.update_relationship(relationship, authorization=authorization)
        print("The response of RelationshipApi->update_relationship:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationshipApi->update_relationship: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relationship** | [**List[Relationship]**](Relationship.md)| A Relationship of project objects. | 
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

