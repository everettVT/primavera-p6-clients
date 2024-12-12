# openapi_client.ActivityRiskApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_activity_risk**](ActivityRiskApi.md#create_activity_risk) | **POST** /activityRisk | Create ActivityRisk
[**delete_activity_risk**](ActivityRiskApi.md#delete_activity_risk) | **DELETE** /activityRisk | Delete ActivityRisk
[**get_activity_risk_field_length**](ActivityRiskApi.md#get_activity_risk_field_length) | **GET** /activityRisk/getFieldLength/{fieldName} | View ActivityRisk Field Length
[**get_activity_risk_fields**](ActivityRiskApi.md#get_activity_risk_fields) | **GET** /activityRisk/fields | View ActivityRisk fields
[**get_activity_risks**](ActivityRiskApi.md#get_activity_risks) | **GET** /activityRisk | Reads ActivityRisks.


# **create_activity_risk**
> List[CreateActivityRiskResponse] create_activity_risk(activity_risk, authorization=authorization)

Create ActivityRisk

Send a request to this endpoint to create one or more activityRisk. An application object will be created for each JSON object provided in the request body.

### Example


```python
import openapi_client
from openapi_client.models.activity_risk import ActivityRisk
from openapi_client.models.create_activity_risk_response import CreateActivityRiskResponse
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
    api_instance = openapi_client.ActivityRiskApi(api_client)
    activity_risk = [openapi_client.ActivityRisk()] # List[ActivityRisk] | A list of ActivityRisk objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ActivityRisk
        api_response = api_instance.create_activity_risk(activity_risk, authorization=authorization)
        print("The response of ActivityRiskApi->create_activity_risk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityRiskApi->create_activity_risk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_risk** | [**List[ActivityRisk]**](ActivityRisk.md)| A list of ActivityRisk objects. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[CreateActivityRiskResponse]**](CreateActivityRiskResponse.md)

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

# **delete_activity_risk**
> bool delete_activity_risk(activity_risk, authorization=authorization)

Delete ActivityRisk

Send a request to this endpoint to delete one or more activityRisk. Objects with ID values that match the values provided in the request body will be deleted.

### Example


```python
import openapi_client
from openapi_client.models.activity_risk import ActivityRisk
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
    api_instance = openapi_client.ActivityRiskApi(api_client)
    activity_risk = [openapi_client.ActivityRisk()] # List[ActivityRisk] | <p>A list of ActivityRisk objects.<p><p>Required fields: You must supply both the ActivityObjectId and RiskObjectId fields when you use the Delete ActivityRisk operation. All other fields are optional.</p>
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete ActivityRisk
        api_response = api_instance.delete_activity_risk(activity_risk, authorization=authorization)
        print("The response of ActivityRiskApi->delete_activity_risk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityRiskApi->delete_activity_risk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_risk** | [**List[ActivityRisk]**](ActivityRisk.md)| &lt;p&gt;A list of ActivityRisk objects.&lt;p&gt;&lt;p&gt;Required fields: You must supply both the ActivityObjectId and RiskObjectId fields when you use the Delete ActivityRisk operation. All other fields are optional.&lt;/p&gt; | 
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

# **get_activity_risk_field_length**
> str get_activity_risk_field_length(field_name, authorization=authorization)

View ActivityRisk Field Length

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
    api_instance = openapi_client.ActivityRiskApi(api_client)
    field_name = 'field_name_example' # str | An activityRisk field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ActivityRisk Field Length
        api_response = api_instance.get_activity_risk_field_length(field_name, authorization=authorization)
        print("The response of ActivityRiskApi->get_activity_risk_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityRiskApi->get_activity_risk_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An activityRisk field. | 
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

# **get_activity_risk_fields**
> str get_activity_risk_fields()

View ActivityRisk fields

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
    api_instance = openapi_client.ActivityRiskApi(api_client)

    try:
        # View ActivityRisk fields
        api_response = api_instance.get_activity_risk_fields()
        print("The response of ActivityRiskApi->get_activity_risk_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityRiskApi->get_activity_risk_fields: %s\n" % e)
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

# **get_activity_risks**
> List[ActivityRisk] get_activity_risks(fields, filter=filter, order_by=order_by, authorization=authorization)

Reads ActivityRisks.

Reads ActivityRisks objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.activity_risk import ActivityRisk
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
    api_instance = openapi_client.ActivityRiskApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Reads ActivityRisks.
        api_response = api_instance.get_activity_risks(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ActivityRiskApi->get_activity_risks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityRiskApi->get_activity_risks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ActivityRisk]**](ActivityRisk.md)

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

