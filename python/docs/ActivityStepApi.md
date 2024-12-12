# openapi_client.ActivityStepApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_activity_step**](ActivityStepApi.md#create_activity_step) | **POST** /activityStep | Create ActivitySteps
[**delete_activity_step**](ActivityStepApi.md#delete_activity_step) | **DELETE** /activityStep | Delete ActivitySteps
[**get_activity_step_field_length**](ActivityStepApi.md#get_activity_step_field_length) | **GET** /activityStep/getFieldLength/{fieldName} | View ActivityStep Field Length
[**get_activity_step_fields**](ActivityStepApi.md#get_activity_step_fields) | **GET** /activityStep/fields | View ActivityStep fields
[**get_activity_steps**](ActivityStepApi.md#get_activity_steps) | **GET** /activityStep | Read ActivitySteps
[**update_activity_step**](ActivityStepApi.md#update_activity_step) | **PUT** /activityStep | Update ActivitySteps


# **create_activity_step**
> str create_activity_step(activity_step, authorization=authorization)

Create ActivitySteps

Send a request to this endpoint to create one or more activityStep. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.activity_step import ActivityStep
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
    api_instance = openapi_client.ActivityStepApi(api_client)
    activity_step = [openapi_client.ActivityStep()] # List[ActivityStep] | A list of activityStep objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ActivitySteps
        api_response = api_instance.create_activity_step(activity_step, authorization=authorization)
        print("The response of ActivityStepApi->create_activity_step:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityStepApi->create_activity_step: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_step** | [**List[ActivityStep]**](ActivityStep.md)| A list of activityStep objects. | 
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

# **delete_activity_step**
> bool delete_activity_step(authorization=authorization, object_id=object_id)

Delete ActivitySteps

Send a request to this endpoint to delete one or more activityStep. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.ActivityStepApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | ActivityStep to delete (optional)

    try:
        # Delete ActivitySteps
        api_response = api_instance.delete_activity_step(authorization=authorization, object_id=object_id)
        print("The response of ActivityStepApi->delete_activity_step:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityStepApi->delete_activity_step: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| ActivityStep to delete | [optional] 

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

# **get_activity_step_field_length**
> str get_activity_step_field_length(field_name, authorization=authorization)

View ActivityStep Field Length

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
    api_instance = openapi_client.ActivityStepApi(api_client)
    field_name = 'field_name_example' # str | An activityStep field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ActivityStep Field Length
        api_response = api_instance.get_activity_step_field_length(field_name, authorization=authorization)
        print("The response of ActivityStepApi->get_activity_step_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityStepApi->get_activity_step_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An activityStep field. | 
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

# **get_activity_step_fields**
> str get_activity_step_fields()

View ActivityStep fields

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
    api_instance = openapi_client.ActivityStepApi(api_client)

    try:
        # View ActivityStep fields
        api_response = api_instance.get_activity_step_fields()
        print("The response of ActivityStepApi->get_activity_step_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityStepApi->get_activity_step_fields: %s\n" % e)
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

# **get_activity_steps**
> List[ActivityStep] get_activity_steps(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ActivitySteps

Reads ActivityStep objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.activity_step import ActivityStep
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
    api_instance = openapi_client.ActivityStepApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ActivitySteps
        api_response = api_instance.get_activity_steps(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ActivityStepApi->get_activity_steps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityStepApi->get_activity_steps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ActivityStep]**](ActivityStep.md)

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

# **update_activity_step**
> bool update_activity_step(activity_step, authorization=authorization)

Update ActivitySteps

Send a request to this endpoint to update one or more activityStep. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.activity_step import ActivityStep
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
    api_instance = openapi_client.ActivityStepApi(api_client)
    activity_step = [openapi_client.ActivityStep()] # List[ActivityStep] | A list of activityStep objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ActivitySteps
        api_response = api_instance.update_activity_step(activity_step, authorization=authorization)
        print("The response of ActivityStepApi->update_activity_step:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityStepApi->update_activity_step: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_step** | [**List[ActivityStep]**](ActivityStep.md)| A list of activityStep objects. | 
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

