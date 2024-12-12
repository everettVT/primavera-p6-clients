# openapi_client.ActivityStepTemplateItemApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_activity_step_template_item**](ActivityStepTemplateItemApi.md#create_activity_step_template_item) | **POST** /activityStepTemplateItem | Create ActivityStepTemplateItems
[**delete_activity_step_template_item**](ActivityStepTemplateItemApi.md#delete_activity_step_template_item) | **DELETE** /activityStepTemplateItem | Delete ActivityStepTemplateItems
[**get_activity_step_template_item_field_length**](ActivityStepTemplateItemApi.md#get_activity_step_template_item_field_length) | **GET** /activityStepTemplateItem/getFieldLength/{fieldName} | View ActivityStepTemplateItem Field Length
[**get_activity_step_template_item_fields**](ActivityStepTemplateItemApi.md#get_activity_step_template_item_fields) | **GET** /activityStepTemplateItem/fields | View ActivityStepTemplateItem fields
[**get_activity_step_template_items**](ActivityStepTemplateItemApi.md#get_activity_step_template_items) | **GET** /activityStepTemplateItem | Read ActivityStepTemplateItems
[**update_activity_step_template_item**](ActivityStepTemplateItemApi.md#update_activity_step_template_item) | **PUT** /activityStepTemplateItem | Update ActivityStepTemplateItems


# **create_activity_step_template_item**
> str create_activity_step_template_item(activity_step_template_item, authorization=authorization)

Create ActivityStepTemplateItems

Send a request to this endpoint to create one or more activityStepTemplateItem. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.activity_step_template_item import ActivityStepTemplateItem
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
    api_instance = openapi_client.ActivityStepTemplateItemApi(api_client)
    activity_step_template_item = [openapi_client.ActivityStepTemplateItem()] # List[ActivityStepTemplateItem] | A list of activityStepTemplateItem objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ActivityStepTemplateItems
        api_response = api_instance.create_activity_step_template_item(activity_step_template_item, authorization=authorization)
        print("The response of ActivityStepTemplateItemApi->create_activity_step_template_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityStepTemplateItemApi->create_activity_step_template_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_step_template_item** | [**List[ActivityStepTemplateItem]**](ActivityStepTemplateItem.md)| A list of activityStepTemplateItem objects. | 
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

# **delete_activity_step_template_item**
> bool delete_activity_step_template_item(authorization=authorization, object_id=object_id)

Delete ActivityStepTemplateItems

Send a request to this endpoint to delete one or more activityStepTemplateItem. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.ActivityStepTemplateItemApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of activityStepTemplateItem. (optional)

    try:
        # Delete ActivityStepTemplateItems
        api_response = api_instance.delete_activity_step_template_item(authorization=authorization, object_id=object_id)
        print("The response of ActivityStepTemplateItemApi->delete_activity_step_template_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityStepTemplateItemApi->delete_activity_step_template_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| One or more system-generated identifiers of activityStepTemplateItem. | [optional] 

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

# **get_activity_step_template_item_field_length**
> str get_activity_step_template_item_field_length(field_name, authorization=authorization)

View ActivityStepTemplateItem Field Length

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
    api_instance = openapi_client.ActivityStepTemplateItemApi(api_client)
    field_name = 'field_name_example' # str | An ActivityStepTemplateItem field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ActivityStepTemplateItem Field Length
        api_response = api_instance.get_activity_step_template_item_field_length(field_name, authorization=authorization)
        print("The response of ActivityStepTemplateItemApi->get_activity_step_template_item_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityStepTemplateItemApi->get_activity_step_template_item_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An ActivityStepTemplateItem field. | 
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

# **get_activity_step_template_item_fields**
> str get_activity_step_template_item_fields()

View ActivityStepTemplateItem fields

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
    api_instance = openapi_client.ActivityStepTemplateItemApi(api_client)

    try:
        # View ActivityStepTemplateItem fields
        api_response = api_instance.get_activity_step_template_item_fields()
        print("The response of ActivityStepTemplateItemApi->get_activity_step_template_item_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityStepTemplateItemApi->get_activity_step_template_item_fields: %s\n" % e)
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

# **get_activity_step_template_items**
> List[ActivityStepTemplateItem] get_activity_step_template_items(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ActivityStepTemplateItems

Reads ActivityStepTemplateItem objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.activity_step_template_item import ActivityStepTemplateItem
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
    api_instance = openapi_client.ActivityStepTemplateItemApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ActivityStepTemplateItems
        api_response = api_instance.get_activity_step_template_items(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ActivityStepTemplateItemApi->get_activity_step_template_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityStepTemplateItemApi->get_activity_step_template_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ActivityStepTemplateItem]**](ActivityStepTemplateItem.md)

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

# **update_activity_step_template_item**
> bool update_activity_step_template_item(activity_step_template_item, authorization=authorization)

Update ActivityStepTemplateItems

Send a request to this endpoint to update one or more activityStepTemplateItem. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.activity_step_template_item import ActivityStepTemplateItem
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
    api_instance = openapi_client.ActivityStepTemplateItemApi(api_client)
    activity_step_template_item = [openapi_client.ActivityStepTemplateItem()] # List[ActivityStepTemplateItem] | A list of activityStepTemplateItem objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ActivityStepTemplateItems
        api_response = api_instance.update_activity_step_template_item(activity_step_template_item, authorization=authorization)
        print("The response of ActivityStepTemplateItemApi->update_activity_step_template_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityStepTemplateItemApi->update_activity_step_template_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_step_template_item** | [**List[ActivityStepTemplateItem]**](ActivityStepTemplateItem.md)| A list of activityStepTemplateItem objects. | 
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

