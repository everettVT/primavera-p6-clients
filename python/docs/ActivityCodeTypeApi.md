# openapi_client.ActivityCodeTypeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_activity_code_type**](ActivityCodeTypeApi.md#create_activity_code_type) | **POST** /activityCodeType | Create ActivitiyCodeTypes
[**delete_activity_code_type**](ActivityCodeTypeApi.md#delete_activity_code_type) | **DELETE** /activityCodeType | Delete ActivitiyCodeTypes
[**get_activity_code_type_field_length**](ActivityCodeTypeApi.md#get_activity_code_type_field_length) | **GET** /activityCodeType/getFieldLength/{fieldName} | View ActivitiyCodeType Field Length
[**get_activity_code_type_fields**](ActivityCodeTypeApi.md#get_activity_code_type_fields) | **GET** /activityCodeType/fields | View ActivitiyCodeType fields
[**get_activity_code_types**](ActivityCodeTypeApi.md#get_activity_code_types) | **GET** /activityCodeType | Read ActivityCodeTypes
[**update_activity_code_type**](ActivityCodeTypeApi.md#update_activity_code_type) | **PUT** /activityCodeType | Update ActivitiyCodeTypes


# **create_activity_code_type**
> str create_activity_code_type(activity_code_type, authorization=authorization)

Create ActivitiyCodeTypes

Send a request to this endpoint to create one or more activityCodeType. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.activity_code_type import ActivityCodeType
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
    api_instance = openapi_client.ActivityCodeTypeApi(api_client)
    activity_code_type = [openapi_client.ActivityCodeType()] # List[ActivityCodeType] | A list of activityCodeType objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ActivitiyCodeTypes
        api_response = api_instance.create_activity_code_type(activity_code_type, authorization=authorization)
        print("The response of ActivityCodeTypeApi->create_activity_code_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityCodeTypeApi->create_activity_code_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_code_type** | [**List[ActivityCodeType]**](ActivityCodeType.md)| A list of activityCodeType objects. | 
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

# **delete_activity_code_type**
> bool delete_activity_code_type(authorization=authorization, object_id=object_id)

Delete ActivitiyCodeTypes

Send a request to this endpoint to delete one or more activityCodeType. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.ActivityCodeTypeApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of activityCodeType. (optional)

    try:
        # Delete ActivitiyCodeTypes
        api_response = api_instance.delete_activity_code_type(authorization=authorization, object_id=object_id)
        print("The response of ActivityCodeTypeApi->delete_activity_code_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityCodeTypeApi->delete_activity_code_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| One or more system-generated identifiers of activityCodeType. | [optional] 

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

# **get_activity_code_type_field_length**
> str get_activity_code_type_field_length(field_name, authorization=authorization)

View ActivitiyCodeType Field Length

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
    api_instance = openapi_client.ActivityCodeTypeApi(api_client)
    field_name = 'field_name_example' # str | An activityCodeType field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ActivitiyCodeType Field Length
        api_response = api_instance.get_activity_code_type_field_length(field_name, authorization=authorization)
        print("The response of ActivityCodeTypeApi->get_activity_code_type_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityCodeTypeApi->get_activity_code_type_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An activityCodeType field. | 
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

# **get_activity_code_type_fields**
> str get_activity_code_type_fields()

View ActivitiyCodeType fields

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
    api_instance = openapi_client.ActivityCodeTypeApi(api_client)

    try:
        # View ActivitiyCodeType fields
        api_response = api_instance.get_activity_code_type_fields()
        print("The response of ActivityCodeTypeApi->get_activity_code_type_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityCodeTypeApi->get_activity_code_type_fields: %s\n" % e)
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

# **get_activity_code_types**
> List[ActivityCodeType] get_activity_code_types(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ActivityCodeTypes

Reads ActivityCodeType objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.activity_code_type import ActivityCodeType
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
    api_instance = openapi_client.ActivityCodeTypeApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ActivityCodeTypes
        api_response = api_instance.get_activity_code_types(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ActivityCodeTypeApi->get_activity_code_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityCodeTypeApi->get_activity_code_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ActivityCodeType]**](ActivityCodeType.md)

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

# **update_activity_code_type**
> bool update_activity_code_type(activity_code_type, authorization=authorization)

Update ActivitiyCodeTypes

Send a request to this endpoint to update one or more activityCodeType. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.activity_code_type import ActivityCodeType
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
    api_instance = openapi_client.ActivityCodeTypeApi(api_client)
    activity_code_type = [openapi_client.ActivityCodeType()] # List[ActivityCodeType] | A list of activityCodeType objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ActivitiyCodeTypes
        api_response = api_instance.update_activity_code_type(activity_code_type, authorization=authorization)
        print("The response of ActivityCodeTypeApi->update_activity_code_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityCodeTypeApi->update_activity_code_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_code_type** | [**List[ActivityCodeType]**](ActivityCodeType.md)| A list of activityCodeType objects. | 
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

