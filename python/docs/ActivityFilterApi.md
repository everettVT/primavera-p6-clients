# openapi_client.ActivityFilterApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_activity_filters**](ActivityFilterApi.md#create_activity_filters) | **POST** /activityFilter | Create ActivityFilters
[**delete_activity_filters**](ActivityFilterApi.md#delete_activity_filters) | **DELETE** /activityFilter | Deletes ActivityFilters
[**get_activity_filter_field_length**](ActivityFilterApi.md#get_activity_filter_field_length) | **GET** /activityFilter/getFieldLength/{fieldName} | View ActivityFilter Field Length
[**get_activity_filter_fields**](ActivityFilterApi.md#get_activity_filter_fields) | **GET** /activityFilter/fields | View ActivityFilter fields
[**get_activity_filters**](ActivityFilterApi.md#get_activity_filters) | **GET** /activityFilter | Read ActivityFilters
[**update_activity_filters**](ActivityFilterApi.md#update_activity_filters) | **PUT** /activityFilter | Update ActivityFilters


# **create_activity_filters**
> str create_activity_filters(activity_filter, authorization=authorization)

Create ActivityFilters

Send a request to this endpoint to create one or more activityFilter. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.activity_filter import ActivityFilter
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
    api_instance = openapi_client.ActivityFilterApi(api_client)
    activity_filter = [openapi_client.ActivityFilter()] # List[ActivityFilter] | A list of activityFilter objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ActivityFilters
        api_response = api_instance.create_activity_filters(activity_filter, authorization=authorization)
        print("The response of ActivityFilterApi->create_activity_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityFilterApi->create_activity_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_filter** | [**List[ActivityFilter]**](ActivityFilter.md)| A list of activityFilter objects. | 
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

# **delete_activity_filters**
> bool delete_activity_filters(authorization=authorization, object_id=object_id)

Deletes ActivityFilters

Send a request to this endpoint to delete one or more activityFilter. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.ActivityFilterApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of activityFilter. (optional)

    try:
        # Deletes ActivityFilters
        api_response = api_instance.delete_activity_filters(authorization=authorization, object_id=object_id)
        print("The response of ActivityFilterApi->delete_activity_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityFilterApi->delete_activity_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| One or more system-generated identifiers of activityFilter. | [optional] 

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

# **get_activity_filter_field_length**
> str get_activity_filter_field_length(field_name, authorization=authorization)

View ActivityFilter Field Length

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
    api_instance = openapi_client.ActivityFilterApi(api_client)
    field_name = 'field_name_example' # str | An activityFilter field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ActivityFilter Field Length
        api_response = api_instance.get_activity_filter_field_length(field_name, authorization=authorization)
        print("The response of ActivityFilterApi->get_activity_filter_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityFilterApi->get_activity_filter_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An activityFilter field. | 
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

# **get_activity_filter_fields**
> str get_activity_filter_fields()

View ActivityFilter fields

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
    api_instance = openapi_client.ActivityFilterApi(api_client)

    try:
        # View ActivityFilter fields
        api_response = api_instance.get_activity_filter_fields()
        print("The response of ActivityFilterApi->get_activity_filter_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityFilterApi->get_activity_filter_fields: %s\n" % e)
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

# **get_activity_filters**
> List[ActivityFilter] get_activity_filters(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ActivityFilters

Reads Activity objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.activity_filter import ActivityFilter
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
    api_instance = openapi_client.ActivityFilterApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ActivityFilters
        api_response = api_instance.get_activity_filters(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ActivityFilterApi->get_activity_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityFilterApi->get_activity_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ActivityFilter]**](ActivityFilter.md)

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

# **update_activity_filters**
> bool update_activity_filters(activity_filter, authorization=authorization)

Update ActivityFilters

Send a request to this endpoint to update one or more activityFilter. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.activity_filter import ActivityFilter
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
    api_instance = openapi_client.ActivityFilterApi(api_client)
    activity_filter = [openapi_client.ActivityFilter()] # List[ActivityFilter] | A list of activityFilter objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ActivityFilters
        api_response = api_instance.update_activity_filters(activity_filter, authorization=authorization)
        print("The response of ActivityFilterApi->update_activity_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityFilterApi->update_activity_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_filter** | [**List[ActivityFilter]**](ActivityFilter.md)| A list of activityFilter objects. | 
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

