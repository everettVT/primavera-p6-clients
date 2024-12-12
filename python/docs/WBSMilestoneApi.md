# openapi_client.WBSMilestoneApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_wbs_milestone**](WBSMilestoneApi.md#create_wbs_milestone) | **POST** /wbsMilestone | Create WBSMilestone
[**delete_wbs_milestone**](WBSMilestoneApi.md#delete_wbs_milestone) | **DELETE** /wbsMilestone | Delete WBSMilestone
[**get_wbs_milestone**](WBSMilestoneApi.md#get_wbs_milestone) | **GET** /wbsMilestone | Read WBSMilestone
[**get_wbs_milestone_field_length**](WBSMilestoneApi.md#get_wbs_milestone_field_length) | **GET** /wbsMilestone/getFieldLength/{fieldName} | View Project Field Length
[**get_wbs_milestone_fields**](WBSMilestoneApi.md#get_wbs_milestone_fields) | **GET** /wbsMilestone/fields | View Project fields
[**update_wbs_milestone**](WBSMilestoneApi.md#update_wbs_milestone) | **PUT** /wbsMilestone | Update WBSMilestone


# **create_wbs_milestone**
> str create_wbs_milestone(wbs_milestone, authorization=authorization)

Create WBSMilestone

Send a request to this endpoint to create one or more WBSMilestone. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.wbs_milestone import WBSMilestone
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
    api_instance = openapi_client.WBSMilestoneApi(api_client)
    wbs_milestone = [openapi_client.WBSMilestone()] # List[WBSMilestone] | A list of WBSMilestone objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create WBSMilestone
        api_response = api_instance.create_wbs_milestone(wbs_milestone, authorization=authorization)
        print("The response of WBSMilestoneApi->create_wbs_milestone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WBSMilestoneApi->create_wbs_milestone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wbs_milestone** | [**List[WBSMilestone]**](WBSMilestone.md)| A list of WBSMilestone objects. | 
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

# **delete_wbs_milestone**
> bool delete_wbs_milestone(object_id, authorization=authorization)

Delete WBSMilestone

Send a request to this endpoint to delete one or more WBSMilestone. An application object will be created for each JSON object provided in the request body

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
    api_instance = openapi_client.WBSMilestoneApi(api_client)
    object_id = '1,2,3' # str | One or more system-generated identifiers of WBSMilestone.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete WBSMilestone
        api_response = api_instance.delete_wbs_milestone(object_id, authorization=authorization)
        print("The response of WBSMilestoneApi->delete_wbs_milestone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WBSMilestoneApi->delete_wbs_milestone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| One or more system-generated identifiers of WBSMilestone. | 
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

# **get_wbs_milestone**
> List[WBSMilestone] get_wbs_milestone(fields, filter=filter, order_by=order_by, authorization=authorization)

Read WBSMilestone

Reads WBSMilestone objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.wbs_milestone import WBSMilestone
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
    api_instance = openapi_client.WBSMilestoneApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read WBSMilestone
        api_response = api_instance.get_wbs_milestone(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of WBSMilestoneApi->get_wbs_milestone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WBSMilestoneApi->get_wbs_milestone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[WBSMilestone]**](WBSMilestone.md)

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

# **get_wbs_milestone_field_length**
> str get_wbs_milestone_field_length(field_name, authorization=authorization)

View Project Field Length

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
    api_instance = openapi_client.WBSMilestoneApi(api_client)
    field_name = 'field_name_example' # str | An project field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View Project Field Length
        api_response = api_instance.get_wbs_milestone_field_length(field_name, authorization=authorization)
        print("The response of WBSMilestoneApi->get_wbs_milestone_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WBSMilestoneApi->get_wbs_milestone_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An project field. | 
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

# **get_wbs_milestone_fields**
> str get_wbs_milestone_fields()

View Project fields

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
    api_instance = openapi_client.WBSMilestoneApi(api_client)

    try:
        # View Project fields
        api_response = api_instance.get_wbs_milestone_fields()
        print("The response of WBSMilestoneApi->get_wbs_milestone_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WBSMilestoneApi->get_wbs_milestone_fields: %s\n" % e)
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

# **update_wbs_milestone**
> bool update_wbs_milestone(wbs_milestone, authorization=authorization)

Update WBSMilestone

Send a request to this endpoint to update one or more WBSMilestone. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.wbs_milestone import WBSMilestone
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
    api_instance = openapi_client.WBSMilestoneApi(api_client)
    wbs_milestone = [openapi_client.WBSMilestone()] # List[WBSMilestone] | A list of WBSMilestone objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update WBSMilestone
        api_response = api_instance.update_wbs_milestone(wbs_milestone, authorization=authorization)
        print("The response of WBSMilestoneApi->update_wbs_milestone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WBSMilestoneApi->update_wbs_milestone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wbs_milestone** | [**List[WBSMilestone]**](WBSMilestone.md)| A list of WBSMilestone objects. | 
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

