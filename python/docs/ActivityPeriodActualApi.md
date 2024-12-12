# openapi_client.ActivityPeriodActualApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_activity_period_actuals**](ActivityPeriodActualApi.md#create_activity_period_actuals) | **POST** /activityPeriodActual | Create ActivityPeriodActuals
[**delete_activity_period_actuals**](ActivityPeriodActualApi.md#delete_activity_period_actuals) | **DELETE** /activityPeriodActual | Delete ActivityPeriodActuals
[**get_activity_period_actuals**](ActivityPeriodActualApi.md#get_activity_period_actuals) | **GET** /activityPeriodActual | Reads ActivityPeriodActuals.
[**get_activity_period_actuals_field_length**](ActivityPeriodActualApi.md#get_activity_period_actuals_field_length) | **GET** /activityPeriodActual/getFieldLength/{fieldName} | View ActivityPeriodActuals Field Length
[**get_activity_period_actuals_fields**](ActivityPeriodActualApi.md#get_activity_period_actuals_fields) | **GET** /activityPeriodActual/fields | View ActivityPeriodActuals fields
[**update_activity_period_actuals**](ActivityPeriodActualApi.md#update_activity_period_actuals) | **PUT** /activityPeriodActual | Update ActivityPeriodActuals


# **create_activity_period_actuals**
> List[CreateActivityPeriodActualResponse] create_activity_period_actuals(activity_period_actual, authorization=authorization)

Create ActivityPeriodActuals

Send a request to this endpoint to create one or more ActivityPeriodActuals. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.activity_period_actual import ActivityPeriodActual
from openapi_client.models.create_activity_period_actual_response import CreateActivityPeriodActualResponse
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
    api_instance = openapi_client.ActivityPeriodActualApi(api_client)
    activity_period_actual = [openapi_client.ActivityPeriodActual()] # List[ActivityPeriodActual] | A list of activityPeriodActuals objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ActivityPeriodActuals
        api_response = api_instance.create_activity_period_actuals(activity_period_actual, authorization=authorization)
        print("The response of ActivityPeriodActualApi->create_activity_period_actuals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityPeriodActualApi->create_activity_period_actuals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_period_actual** | [**List[ActivityPeriodActual]**](ActivityPeriodActual.md)| A list of activityPeriodActuals objects. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[CreateActivityPeriodActualResponse]**](CreateActivityPeriodActualResponse.md)

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

# **delete_activity_period_actuals**
> bool delete_activity_period_actuals(activity_period_actual, authorization=authorization)

Delete ActivityPeriodActuals

Send a request to this endpoint to delete one or more activityPeriodActual. Objects with ID values that match the values provided in the request body will be deleted.

### Example


```python
import openapi_client
from openapi_client.models.activity_period_actual import ActivityPeriodActual
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
    api_instance = openapi_client.ActivityPeriodActualApi(api_client)
    activity_period_actual = [openapi_client.ActivityPeriodActual()] # List[ActivityPeriodActual] | <p>A list of activityPeriodActuals objects.<p><p>Required fields: You must supply both the ActivityObjectId and FinancialPeriodObjectId fields when you use the Delete ActivityPeriodActuals operation. All other fields are optional.</p>
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete ActivityPeriodActuals
        api_response = api_instance.delete_activity_period_actuals(activity_period_actual, authorization=authorization)
        print("The response of ActivityPeriodActualApi->delete_activity_period_actuals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityPeriodActualApi->delete_activity_period_actuals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_period_actual** | [**List[ActivityPeriodActual]**](ActivityPeriodActual.md)| &lt;p&gt;A list of activityPeriodActuals objects.&lt;p&gt;&lt;p&gt;Required fields: You must supply both the ActivityObjectId and FinancialPeriodObjectId fields when you use the Delete ActivityPeriodActuals operation. All other fields are optional.&lt;/p&gt; | 
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

# **get_activity_period_actuals**
> List[ActivityPeriodActual] get_activity_period_actuals(fields, filter=filter, order_by=order_by, authorization=authorization)

Reads ActivityPeriodActuals.

Reads ActivityPeriodActual objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.activity_period_actual import ActivityPeriodActual
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
    api_instance = openapi_client.ActivityPeriodActualApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Reads ActivityPeriodActuals.
        api_response = api_instance.get_activity_period_actuals(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ActivityPeriodActualApi->get_activity_period_actuals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityPeriodActualApi->get_activity_period_actuals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ActivityPeriodActual]**](ActivityPeriodActual.md)

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

# **get_activity_period_actuals_field_length**
> str get_activity_period_actuals_field_length(field_name, authorization=authorization)

View ActivityPeriodActuals Field Length

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
    api_instance = openapi_client.ActivityPeriodActualApi(api_client)
    field_name = 'field_name_example' # str | An activityPeriodActual field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ActivityPeriodActuals Field Length
        api_response = api_instance.get_activity_period_actuals_field_length(field_name, authorization=authorization)
        print("The response of ActivityPeriodActualApi->get_activity_period_actuals_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityPeriodActualApi->get_activity_period_actuals_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An activityPeriodActual field. | 
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

# **get_activity_period_actuals_fields**
> str get_activity_period_actuals_fields()

View ActivityPeriodActuals fields

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
    api_instance = openapi_client.ActivityPeriodActualApi(api_client)

    try:
        # View ActivityPeriodActuals fields
        api_response = api_instance.get_activity_period_actuals_fields()
        print("The response of ActivityPeriodActualApi->get_activity_period_actuals_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityPeriodActualApi->get_activity_period_actuals_fields: %s\n" % e)
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

# **update_activity_period_actuals**
> List[CreateActivityPeriodActualResponse] update_activity_period_actuals(activity_period_actual, authorization=authorization)

Update ActivityPeriodActuals

Send a request to this endpoint to update one or more ActivityPeriodActuals. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.activity_period_actual import ActivityPeriodActual
from openapi_client.models.create_activity_period_actual_response import CreateActivityPeriodActualResponse
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
    api_instance = openapi_client.ActivityPeriodActualApi(api_client)
    activity_period_actual = [openapi_client.ActivityPeriodActual()] # List[ActivityPeriodActual] | <p>A list of activityPeriodActuals objects.<p><p>Required fields: You must supply both the ActivityObjectId and FinancialPeriodObjectId fields when you use the Update ActivityPeriodActuals operation. All other fields are optional.</p>
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ActivityPeriodActuals
        api_response = api_instance.update_activity_period_actuals(activity_period_actual, authorization=authorization)
        print("The response of ActivityPeriodActualApi->update_activity_period_actuals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityPeriodActualApi->update_activity_period_actuals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_period_actual** | [**List[ActivityPeriodActual]**](ActivityPeriodActual.md)| &lt;p&gt;A list of activityPeriodActuals objects.&lt;p&gt;&lt;p&gt;Required fields: You must supply both the ActivityObjectId and FinancialPeriodObjectId fields when you use the Update ActivityPeriodActuals operation. All other fields are optional.&lt;/p&gt; | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[CreateActivityPeriodActualResponse]**](CreateActivityPeriodActualResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Input. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

