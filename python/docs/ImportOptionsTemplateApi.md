# openapi_client.ImportOptionsTemplateApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_import_options_template**](ImportOptionsTemplateApi.md#get_import_options_template) | **GET** /importOptionsTemplate | Read ImportOptionsTemplate
[**get_import_options_template_field_length**](ImportOptionsTemplateApi.md#get_import_options_template_field_length) | **GET** /importOptionsTemplate/getFieldLength/{fieldName} | View ImportOptionsTemplate Field Length
[**get_import_options_template_fields**](ImportOptionsTemplateApi.md#get_import_options_template_fields) | **GET** /importOptionsTemplate/fields | View ImportOptionsTemplate fields


# **get_import_options_template**
> List[ImportOptionsTemplate] get_import_options_template(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ImportOptionsTemplate

Reads ImportOptionsTemplate objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.import_options_template import ImportOptionsTemplate
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
    api_instance = openapi_client.ImportOptionsTemplateApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ImportOptionsTemplate
        api_response = api_instance.get_import_options_template(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ImportOptionsTemplateApi->get_import_options_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportOptionsTemplateApi->get_import_options_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ImportOptionsTemplate]**](ImportOptionsTemplate.md)

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

# **get_import_options_template_field_length**
> str get_import_options_template_field_length(field_name, authorization=authorization)

View ImportOptionsTemplate Field Length

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
    api_instance = openapi_client.ImportOptionsTemplateApi(api_client)
    field_name = 'field_name_example' # str | An ImportOptionsTemplate field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ImportOptionsTemplate Field Length
        api_response = api_instance.get_import_options_template_field_length(field_name, authorization=authorization)
        print("The response of ImportOptionsTemplateApi->get_import_options_template_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportOptionsTemplateApi->get_import_options_template_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An ImportOptionsTemplate field. | 
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

# **get_import_options_template_fields**
> str get_import_options_template_fields()

View ImportOptionsTemplate fields

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
    api_instance = openapi_client.ImportOptionsTemplateApi(api_client)

    try:
        # View ImportOptionsTemplate fields
        api_response = api_instance.get_import_options_template_fields()
        print("The response of ImportOptionsTemplateApi->get_import_options_template_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportOptionsTemplateApi->get_import_options_template_fields: %s\n" % e)
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

