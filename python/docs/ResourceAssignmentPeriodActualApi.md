# openapi_client.ResourceAssignmentPeriodActualApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_resource_assignment_period_actual**](ResourceAssignmentPeriodActualApi.md#create_resource_assignment_period_actual) | **POST** /resourceAssignmentPeriodActual | Create ResourceAssignmentPeriodActual
[**delete_resource_assignment_period_actual**](ResourceAssignmentPeriodActualApi.md#delete_resource_assignment_period_actual) | **DELETE** /resourceAssignmentPeriodActual | Delete ResourceAssignmentPeriodActual
[**get_resource_assignment_period_actual**](ResourceAssignmentPeriodActualApi.md#get_resource_assignment_period_actual) | **GET** /resourceAssignmentPeriodActual | Read ResourceAssignmentPeriodActual
[**get_resource_assignment_period_actual_field_length**](ResourceAssignmentPeriodActualApi.md#get_resource_assignment_period_actual_field_length) | **GET** /resourceAssignmentPeriodActual/getFieldLength/{fieldName} | View ResourceAssignmentPeriodActual Field Length
[**get_resource_assignment_period_actual_fields**](ResourceAssignmentPeriodActualApi.md#get_resource_assignment_period_actual_fields) | **GET** /resourceAssignmentPeriodActual/fields | View ResourceAssignmentPeriodActual fields
[**update_resource_assignment_period_actual**](ResourceAssignmentPeriodActualApi.md#update_resource_assignment_period_actual) | **PUT** /resourceAssignmentPeriodActual | Update ResourceAssignmentPeriodActual


# **create_resource_assignment_period_actual**
> List[CreateResourceAssignmentPeriodActualsResponse] create_resource_assignment_period_actual(resource_assignment_period_actual, authorization=authorization)

Create ResourceAssignmentPeriodActual

Send a request to this endpoint to create one or more ResourceAssignmentPeriodActual. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.create_resource_assignment_period_actuals_response import CreateResourceAssignmentPeriodActualsResponse
from openapi_client.models.resource_assignment_period_actual import ResourceAssignmentPeriodActual
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
    api_instance = openapi_client.ResourceAssignmentPeriodActualApi(api_client)
    resource_assignment_period_actual = [openapi_client.ResourceAssignmentPeriodActual()] # List[ResourceAssignmentPeriodActual] | A list of ResourceAssignmentPeriodActual objects.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Create ResourceAssignmentPeriodActual
        api_response = api_instance.create_resource_assignment_period_actual(resource_assignment_period_actual, authorization=authorization)
        print("The response of ResourceAssignmentPeriodActualApi->create_resource_assignment_period_actual:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceAssignmentPeriodActualApi->create_resource_assignment_period_actual: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_assignment_period_actual** | [**List[ResourceAssignmentPeriodActual]**](ResourceAssignmentPeriodActual.md)| A list of ResourceAssignmentPeriodActual objects. | 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[CreateResourceAssignmentPeriodActualsResponse]**](CreateResourceAssignmentPeriodActualsResponse.md)

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

# **delete_resource_assignment_period_actual**
> bool delete_resource_assignment_period_actual(resource_assignment_period_actual, authorization=authorization)

Delete ResourceAssignmentPeriodActual

Send a request to this endpoint to delete one or more ResourceAssignmentPeriodActual. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.resource_assignment_period_actual import ResourceAssignmentPeriodActual
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
    api_instance = openapi_client.ResourceAssignmentPeriodActualApi(api_client)
    resource_assignment_period_actual = [openapi_client.ResourceAssignmentPeriodActual()] # List[ResourceAssignmentPeriodActual] | <p>A list of ResourceAssignmentPeriodActual objects.<p><p>Required fields: You must supply both the ResourceAssignmentObjectId, ActualUnits and FinancialPeriodObjectId fields when you use the Delete ResourceAssignmentPeriodActual operation. All other fields are optional.</p>
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Delete ResourceAssignmentPeriodActual
        api_response = api_instance.delete_resource_assignment_period_actual(resource_assignment_period_actual, authorization=authorization)
        print("The response of ResourceAssignmentPeriodActualApi->delete_resource_assignment_period_actual:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceAssignmentPeriodActualApi->delete_resource_assignment_period_actual: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_assignment_period_actual** | [**List[ResourceAssignmentPeriodActual]**](ResourceAssignmentPeriodActual.md)| &lt;p&gt;A list of ResourceAssignmentPeriodActual objects.&lt;p&gt;&lt;p&gt;Required fields: You must supply both the ResourceAssignmentObjectId, ActualUnits and FinancialPeriodObjectId fields when you use the Delete ResourceAssignmentPeriodActual operation. All other fields are optional.&lt;/p&gt; | 
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

# **get_resource_assignment_period_actual**
> List[ResourceAssignmentPeriodActual] get_resource_assignment_period_actual(fields, filter=filter, order_by=order_by, authorization=authorization)

Read ResourceAssignmentPeriodActual

Reads ResourceAssignmentPeriodActual objects from the database.

### Example


```python
import openapi_client
from openapi_client.models.resource_assignment_period_actual import ResourceAssignmentPeriodActual
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
    api_instance = openapi_client.ResourceAssignmentPeriodActualApi(api_client)
    fields = 'Name,ObjectId' # str | Fields to load
    filter = 'ObjectId IN(1,2) :and: CreateDate:gte:\'2021-04-20\' :and: LastUpdateDate:lt:\'2022-04-20\' :and: Name :like: \'abc%\'' # str | Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: (optional)
    order_by = 'ObjectId desc' # str | OrderBy condition (optional)
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Read ResourceAssignmentPeriodActual
        api_response = api_instance.get_resource_assignment_period_actual(fields, filter=filter, order_by=order_by, authorization=authorization)
        print("The response of ResourceAssignmentPeriodActualApi->get_resource_assignment_period_actual:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceAssignmentPeriodActualApi->get_resource_assignment_period_actual: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to load | 
 **filter** | **str**| Supported Filter Operators -  :gt:, :lt:, :eq:, :gte:, :lte:, :and:, :or: | [optional] 
 **order_by** | **str**| OrderBy condition | [optional] 
 **authorization** | **str**| OAuth token | [optional] 

### Return type

[**List[ResourceAssignmentPeriodActual]**](ResourceAssignmentPeriodActual.md)

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

# **get_resource_assignment_period_actual_field_length**
> str get_resource_assignment_period_actual_field_length(field_name, authorization=authorization)

View ResourceAssignmentPeriodActual Field Length

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
    api_instance = openapi_client.ResourceAssignmentPeriodActualApi(api_client)
    field_name = 'field_name_example' # str | An ResourceAssignmentPeriodActual field.
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # View ResourceAssignmentPeriodActual Field Length
        api_response = api_instance.get_resource_assignment_period_actual_field_length(field_name, authorization=authorization)
        print("The response of ResourceAssignmentPeriodActualApi->get_resource_assignment_period_actual_field_length:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceAssignmentPeriodActualApi->get_resource_assignment_period_actual_field_length: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| An ResourceAssignmentPeriodActual field. | 
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

# **get_resource_assignment_period_actual_fields**
> str get_resource_assignment_period_actual_fields()

View ResourceAssignmentPeriodActual fields

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
    api_instance = openapi_client.ResourceAssignmentPeriodActualApi(api_client)

    try:
        # View ResourceAssignmentPeriodActual fields
        api_response = api_instance.get_resource_assignment_period_actual_fields()
        print("The response of ResourceAssignmentPeriodActualApi->get_resource_assignment_period_actual_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceAssignmentPeriodActualApi->get_resource_assignment_period_actual_fields: %s\n" % e)
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

# **update_resource_assignment_period_actual**
> bool update_resource_assignment_period_actual(resource_assignment_period_actual, authorization=authorization)

Update ResourceAssignmentPeriodActual

Send a request to this endpoint to update one or more ResourceAssignmentPeriodActual. An application object will be created for each JSON object provided in the request body

### Example


```python
import openapi_client
from openapi_client.models.resource_assignment_period_actual import ResourceAssignmentPeriodActual
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
    api_instance = openapi_client.ResourceAssignmentPeriodActualApi(api_client)
    resource_assignment_period_actual = [openapi_client.ResourceAssignmentPeriodActual()] # List[ResourceAssignmentPeriodActual] | <p>A list of ResourceAssignmentPeriodActual objects.<p><p>Required fields: You must supply both the ResourceAssignmentObjectId, ActualUnits and FinancialPeriodObjectId fields when you use the Update ResourceAssignmentPeriodActual operation. All other fields are optional.</p>
    authorization = 'authorization_example' # str | OAuth token (optional)

    try:
        # Update ResourceAssignmentPeriodActual
        api_response = api_instance.update_resource_assignment_period_actual(resource_assignment_period_actual, authorization=authorization)
        print("The response of ResourceAssignmentPeriodActualApi->update_resource_assignment_period_actual:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceAssignmentPeriodActualApi->update_resource_assignment_period_actual: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_assignment_period_actual** | [**List[ResourceAssignmentPeriodActual]**](ResourceAssignmentPeriodActual.md)| &lt;p&gt;A list of ResourceAssignmentPeriodActual objects.&lt;p&gt;&lt;p&gt;Required fields: You must supply both the ResourceAssignmentObjectId, ActualUnits and FinancialPeriodObjectId fields when you use the Update ResourceAssignmentPeriodActual operation. All other fields are optional.&lt;/p&gt; | 
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

