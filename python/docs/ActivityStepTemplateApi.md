# openapi_client.ActivityStepTemplateApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_activity_step_template**](ActivityStepTemplateApi.md#create_activity_step_template) | **POST** /activityStepTemplate | Create ActivityStepTemplates
[**delete_activity_step_template**](ActivityStepTemplateApi.md#delete_activity_step_template) | **DELETE** /activityStepTemplate | Delete ActivityStepTemplates
[**get_activity_step_template_field_length**](ActivityStepTemplateApi.md#get_activity_step_template_field_length) | **GET** /activityStepTemplate/getFieldLength/{fieldName} | View ActivityStepTemplate Field Length
[**get_activity_step_template_fields**](ActivityStepTemplateApi.md#get_activity_step_template_fields) | **GET** /activityStepTemplate/fields | View ActivityStepTemplate fields
[**get_activity_step_templates**](ActivityStepTemplateApi.md#get_activity_step_templates) | **GET** /activityStepTemplate | Read ActivityStepTemplates
[**update_activity_step_template**](ActivityStepTemplateApi.md#update_activity_step_template) | **PUT** /activityStepTemplate | Update ActivityStepTemplates


# **create_activity_step_template**
> str create_activity_step_template(activity_step_template, authorization=authorization)

Create ActivityStepTemplates

Send a request to this endpoint to create one or more activityStepTemplate. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.activity_step_template import ActivityStepTemplate
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
    api_instance = openapi_client.ActivityStepTemplateApi(api_client)
    activity_step_template = [openapi_client.ActivityStepTemplate()] # List[ActivityStepTemplate] | A list of activityStepTemplate objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ActivityStepTemplates
        api_response = api_instance.create_activity_step_template(activity_step_template, authorization=authorization)
        print("The response of ActivityStepTemplateApi->create_activity_step_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityStepTemplateApi->create_activity_step_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_step_template** | [**List[ActivityStepTemplate]**](ActivityStepTemplate.md)| A list of activityStepTemplate objects. | 
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

# **delete_activity_step_template**
> bool delete_activity_step_template(authorization=authorization, object_id=object_id)

Delete ActivityStepTemplates

Send a request to this endpoint to delete one or more activityStepTemplate. Objects with ID values that match the values provided in the request body will be deleted.

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
    api_instance = openapi_client.ActivityStepTemplateApi(api_client)
    authorization = 'authorization_example' # str | OAuth token (optional)
    object_id = 'object_id_example' # str | One or more system-generated identifiers of activityStepTemplate. (optional)

    try:
        # Delete ActivityStepTemplates
        api_response = api_instance.delete_activity_step_template(authorization=authorization, object_id=object_id)
        print("The response of ActivityStepTemplateApi->delete_activity_step_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityStepTemplateApi->delete_activity_step_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth token | [optional] 
 **object_id** | **str**| One or more system-generated identifiers of activityStepTemplate. | [optional] 

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

# **get_activity_step_template_field_length**
> str get_activity_step_template_field_length(field_name, authorization=authorization)

View ActivityStepTemplate Field Length

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
    api_instance = openapi_client.ActivityStepTemplateApi(api_client)
    field_name = 'field_name_example' # str | An activityStepTemplate field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ActivityStepTemplate Field Length
        api_response = api_instance.get_activity_step_template_field_length(field_name, authorization=authorization)
        print("The response of ActivityStepTemplateApi->get_activity_step_template_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityStepTemplateApi->get_activity_step_template_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An activityStepTemplate field. | 
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

# **get_activity_step_template_fields**
> str get_activity_step_template_fields()

View ActivityStepTemplate fields

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
    api_instance = openapi_client.ActivityStepTemplateApi(api_client)

    try:
        # View ActivityStepTemplate fields
        api_response = api_instance.get_activity_step_template_fields()
        print("The response of ActivityStepTemplateApi->get_activity_step_template_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityStepTemplateApi->get_activity_step_template_fields: %s\n" % e)
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

# **get_activity_step_templates**
> List[ActivityStepTemplate] get_activity_step_templates(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ActivityStepTemplates

Reads ActivityStepTemplate objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.activity_step_template import ActivityStepTemplate
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
    api_instance = openapi_client.ActivityStepTemplateApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ActivityStepTemplates
        api_response = api_instance.get_activity_step_templates(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ActivityStepTemplateApi->get_activity_step_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityStepTemplateApi->get_activity_step_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ActivityStepTemplate]**](ActivityStepTemplate.md)

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

# **update_activity_step_template**
> bool update_activity_step_template(activity_step_template, authorization=authorization)

Update ActivityStepTemplates

Send a request to this endpoint to update one or more activityStepTemplate. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.activity_step_template import ActivityStepTemplate
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
    api_instance = openapi_client.ActivityStepTemplateApi(api_client)
    activity_step_template = [openapi_client.ActivityStepTemplate()] # List[ActivityStepTemplate] | A list of activityStepTemplate objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ActivityStepTemplates
        api_response = api_instance.update_activity_step_template(activity_step_template, authorization=authorization)
        print("The response of ActivityStepTemplateApi->update_activity_step_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityStepTemplateApi->update_activity_step_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_step_template** | [**List[ActivityStepTemplate]**](ActivityStepTemplate.md)| A list of activityStepTemplate objects. | 
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

