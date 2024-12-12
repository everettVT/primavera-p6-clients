# openapi_client.ActivityCommentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_activity_comment**](ActivityCommentApi.md#create_activity_comment) | **POST** /activityComment | Create ActivityComments
[**get_activity_comment_field_length**](ActivityCommentApi.md#get_activity_comment_field_length) | **GET** /activityComment/getFieldLength/{fieldName} | View ActivityComment Field Length
[**get_activity_comment_fields**](ActivityCommentApi.md#get_activity_comment_fields) | **GET** /activityComment/fields | View ActivityComment fields
[**get_activity_comments**](ActivityCommentApi.md#get_activity_comments) | **GET** /activityComment | Read ActivityComments
[**put_activity_comment**](ActivityCommentApi.md#put_activity_comment) | **PUT** /activityComment | Update ActivityComments


# **create_activity_comment**
> str create_activity_comment(activity_comment, authorization=authorization)

Create ActivityComments

Send a request to this endpoint to create one or more activityComment. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.activity_comment import ActivityComment
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
    api_instance = openapi_client.ActivityCommentApi(api_client)
    activity_comment = [openapi_client.ActivityComment()] # List[ActivityComment] | A list of activityComment objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ActivityComments
        api_response = api_instance.create_activity_comment(activity_comment, authorization=authorization)
        print("The response of ActivityCommentApi->create_activity_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityCommentApi->create_activity_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_comment** | [**List[ActivityComment]**](ActivityComment.md)| A list of activityComment objects. | 
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

# **get_activity_comment_field_length**
> str get_activity_comment_field_length(field_name, authorization=authorization)

View ActivityComment Field Length

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
    api_instance = openapi_client.ActivityCommentApi(api_client)
    field_name = 'field_name_example' # str | An activityComment field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ActivityComment Field Length
        api_response = api_instance.get_activity_comment_field_length(field_name, authorization=authorization)
        print("The response of ActivityCommentApi->get_activity_comment_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityCommentApi->get_activity_comment_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An activityComment field. | 
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

# **get_activity_comment_fields**
> str get_activity_comment_fields()

View ActivityComment fields

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
    api_instance = openapi_client.ActivityCommentApi(api_client)

    try:
        # View ActivityComment fields
        api_response = api_instance.get_activity_comment_fields()
        print("The response of ActivityCommentApi->get_activity_comment_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityCommentApi->get_activity_comment_fields: %s\n" % e)
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

# **get_activity_comments**
> List[ActivityComment] get_activity_comments(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ActivityComments

Reads ActivityComment objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.activity_comment import ActivityComment
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
    api_instance = openapi_client.ActivityCommentApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ActivityComments
        api_response = api_instance.get_activity_comments(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ActivityCommentApi->get_activity_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityCommentApi->get_activity_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ActivityComment]**](ActivityComment.md)

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

# **put_activity_comment**
> bool put_activity_comment(activity_comment, authorization=authorization)

Update ActivityComments

Send a request to this endpoint to update one or more activityComment. For each JSON object provided in the request body, an application object with a matching ID value will be updated to reflect the JSON contents.

### Example


```python
import openapi_client
from openapi_client.models.activity_comment import ActivityComment
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
    api_instance = openapi_client.ActivityCommentApi(api_client)
    activity_comment = [openapi_client.ActivityComment()] # List[ActivityComment] | A list of activityComment objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ActivityComments
        api_response = api_instance.put_activity_comment(activity_comment, authorization=authorization)
        print("The response of ActivityCommentApi->put_activity_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityCommentApi->put_activity_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_comment** | [**List[ActivityComment]**](ActivityComment.md)| A list of activityComment objects. | 
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

